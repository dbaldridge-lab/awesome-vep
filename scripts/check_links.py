#!/usr/bin/env python3
"""
Link checker for Awesome Variant Effect Predictors repository.
Validates all URLs in markdown files and reports broken links.
"""

import re
import sys
import time
import requests
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor, as_completed
from typing import List, Tuple, Dict

# Configuration
TIMEOUT = 10  # seconds
MAX_WORKERS = 10  # concurrent requests
RETRY_ATTEMPTS = 2
USER_AGENT = "Mozilla/5.0 (compatible; awesome-vep-linkchecker/1.0)"

# Patterns to extract URLs from markdown
URL_PATTERN = re.compile(r'\[([^\]]+)\]\(([^)]+)\)')
SHIELD_IO_PATTERN = re.compile(r'https://img\.shields\.io/.*')
GITHUB_API_PATTERN = re.compile(r'https://api\.github\.com/.*')

def extract_urls_from_file(file_path: Path) -> List[Tuple[str, str, int]]:
    """Extract all URLs from a markdown file."""
    urls = []
    
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            for line_num, line in enumerate(f, 1):
                matches = URL_PATTERN.findall(line)
                for text, url in matches:
                    # Skip shields.io badges (they're dynamically generated)
                    if not SHIELD_IO_PATTERN.match(url):
                        urls.append((url, text, line_num))
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
    
    return urls

def check_url(url: str, retries: int = RETRY_ATTEMPTS) -> Tuple[str, bool, str]:
    """Check if a URL is accessible."""
    headers = {'User-Agent': USER_AGENT}
    
    for attempt in range(retries):
        try:
            # Special handling for GitHub API URLs
            if GITHUB_API_PATTERN.match(url):
                headers['Accept'] = 'application/vnd.github.v3+json'
            
            response = requests.head(url, headers=headers, timeout=TIMEOUT, allow_redirects=True)
            
            # If HEAD request fails, try GET
            if response.status_code >= 400:
                response = requests.get(url, headers=headers, timeout=TIMEOUT, allow_redirects=True, stream=True)
            
            if response.status_code < 400:
                return url, True, f"OK ({response.status_code})"
            else:
                return url, False, f"HTTP {response.status_code}"
                
        except requests.exceptions.Timeout:
            if attempt == retries - 1:
                return url, False, "Timeout"
                
        except requests.exceptions.ConnectionError:
            if attempt == retries - 1:
                return url, False, "Connection Error"
                
        except Exception as e:
            if attempt == retries - 1:
                return url, False, f"Error: {str(e)}"
        
        # Wait before retry
        if attempt < retries - 1:
            time.sleep(2 ** attempt)
    
    return url, False, "Unknown Error"

def check_all_links(base_path: Path) -> Dict[str, List[Tuple[str, str, int, bool, str]]]:
    """Check all links in the repository."""
    results = {}
    all_urls = []
    
    # Find all markdown files
    md_files = list(base_path.glob('**/*.md'))
    
    print(f"Found {len(md_files)} markdown files to check")
    
    # Extract URLs from all files
    for file_path in md_files:
        urls = extract_urls_from_file(file_path)
        if urls:
            results[str(file_path.relative_to(base_path))] = []
            for url, text, line_num in urls:
                all_urls.append((file_path, url, text, line_num))
    
    print(f"Found {len(all_urls)} URLs to check")
    
    # Check URLs concurrently
    unique_urls = list(set(url for _, url, _, _ in all_urls))
    url_status = {}
    
    with ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
        future_to_url = {executor.submit(check_url, url): url for url in unique_urls}
        
        for i, future in enumerate(as_completed(future_to_url), 1):
            url = future_to_url[future]
            try:
                _, is_valid, message = future.result()
                url_status[url] = (is_valid, message)
                
                # Progress indicator
                if i % 10 == 0:
                    print(f"Checked {i}/{len(unique_urls)} unique URLs...")
                    
            except Exception as e:
                url_status[url] = (False, f"Check failed: {e}")
    
    # Compile results by file
    for file_path, url, text, line_num in all_urls:
        is_valid, message = url_status.get(url, (False, "Unknown"))
        rel_path = str(file_path.relative_to(base_path))
        results[rel_path].append((url, text, line_num, is_valid, message))
    
    return results

def generate_report(results: Dict[str, List[Tuple[str, str, int, bool, str]]]) -> bool:
    """Generate a report of broken links."""
    broken_links = []
    total_links = 0
    
    for file_path, links in results.items():
        file_broken = [(url, text, line, msg) for url, text, line, valid, msg in links if not valid]
        total_links += len(links)
        
        if file_broken:
            broken_links.append((file_path, file_broken))
    
    # Summary
    print(f"\n{'='*60}")
    print(f"Link Check Summary")
    print(f"{'='*60}")
    print(f"Total links checked: {total_links}")
    print(f"Broken links found: {sum(len(links) for _, links in broken_links)}")
    
    if broken_links:
        print(f"\n{'='*60}")
        print("Broken Links Details")
        print(f"{'='*60}\n")
        
        for file_path, links in broken_links:
            print(f"File: {file_path}")
            for url, text, line, message in links:
                print(f"  Line {line}: [{text}]({url})")
                print(f"    Status: {message}")
            print()
        
        # Create GitHub issue format
        with open('broken_links_report.md', 'w') as f:
            f.write("# Broken Links Report\n\n")
            f.write(f"Found {sum(len(links) for _, links in broken_links)} broken links.\n\n")
            
            for file_path, links in broken_links:
                f.write(f"## {file_path}\n\n")
                for url, text, line, message in links:
                    f.write(f"- Line {line}: [{text}]({url}) - {message}\n")
                f.write("\n")
        
        print(f"Detailed report saved to: broken_links_report.md")
        return False
    else:
        print("\nAll links are valid! ✅")
        return True

def main():
    """Main entry point."""
    # Determine repository root
    script_path = Path(__file__).resolve()
    repo_root = script_path.parent.parent
    
    print(f"Checking links in: {repo_root}")
    
    # Check all links
    results = check_all_links(repo_root)
    
    # Generate report
    all_valid = generate_report(results)
    
    # Exit with appropriate code
    sys.exit(0 if all_valid else 1)

if __name__ == "__main__":
    main()