#!/usr/bin/env python3
"""
GitHub statistics collector for Awesome Variant Effect Predictors.
Fetches stars, forks, last commit dates, and other metrics for GitHub repositories.
"""

import re
import json
import time
import requests
from pathlib import Path
from datetime import datetime
from typing import Dict, Tuple, Optional
import os

# Configuration
GITHUB_API_URL = "https://api.github.com/repos/{owner}/{repo}"
RATE_LIMIT_URL = "https://api.github.com/rate_limit"
USER_AGENT = "awesome-vep-stats/1.0"

# Patterns
GITHUB_URL_PATTERN = re.compile(r'https://github\.com/([^/]+)/([^/\s]+)')

class GitHubStats:
    def __init__(self, token: Optional[str] = None):
        """Initialize with optional GitHub token for higher rate limits."""
        self.token = token or os.environ.get('GITHUB_TOKEN')
        self.headers = {'User-Agent': USER_AGENT}
        if self.token:
            self.headers['Authorization'] = f'token {self.token}'
        self.stats_cache = {}
        
    def check_rate_limit(self) -> Tuple[int, int]:
        """Check GitHub API rate limit."""
        try:
            response = requests.get(RATE_LIMIT_URL, headers=self.headers)
            if response.status_code == 200:
                data = response.json()
                remaining = data['rate']['remaining']
                reset_time = data['rate']['reset']
                return remaining, reset_time
        except:
            pass
        return -1, -1
    
    def fetch_repo_stats(self, owner: str, repo: str) -> Dict:
        """Fetch statistics for a GitHub repository."""
        # Check cache first
        cache_key = f"{owner}/{repo}"
        if cache_key in self.stats_cache:
            return self.stats_cache[cache_key]
        
        url = GITHUB_API_URL.format(owner=owner, repo=repo.rstrip('/'))
        
        try:
            response = requests.get(url, headers=self.headers, timeout=10)
            
            if response.status_code == 200:
                data = response.json()
                stats = {
                    'stars': data.get('stargazers_count', 0),
                    'forks': data.get('forks_count', 0),
                    'watchers': data.get('watchers_count', 0),
                    'open_issues': data.get('open_issues_count', 0),
                    'last_commit': self._get_last_commit_date(owner, repo),
                    'created_at': data.get('created_at', ''),
                    'updated_at': data.get('updated_at', ''),
                    'language': data.get('language', ''),
                    'license': data.get('license', {}).get('spdx_id', '') if data.get('license') else '',
                    'description': data.get('description', ''),
                    'archived': data.get('archived', False),
                    'topics': data.get('topics', [])
                }
                self.stats_cache[cache_key] = stats
                return stats
            elif response.status_code == 404:
                print(f"Repository not found: {owner}/{repo}")
            elif response.status_code == 403:
                remaining, reset_time = self.check_rate_limit()
                if remaining == 0:
                    reset_dt = datetime.fromtimestamp(reset_time)
                    print(f"Rate limit exceeded. Resets at {reset_dt}")
                else:
                    print(f"Access forbidden for {owner}/{repo}")
            else:
                print(f"Error fetching {owner}/{repo}: HTTP {response.status_code}")
                
        except Exception as e:
            print(f"Error fetching stats for {owner}/{repo}: {e}")
        
        return {}
    
    def _get_last_commit_date(self, owner: str, repo: str) -> str:
        """Get the date of the last commit."""
        url = f"https://api.github.com/repos/{owner}/{repo}/commits"
        
        try:
            response = requests.get(url, headers=self.headers, params={'per_page': 1}, timeout=10)
            if response.status_code == 200:
                commits = response.json()
                if commits:
                    return commits[0]['commit']['committer']['date']
        except:
            pass
        
        return ''
    
    def extract_github_repos(self, file_path: Path) -> Dict[str, Tuple[str, str]]:
        """Extract GitHub repository URLs from a markdown file."""
        repos = {}
        
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
                
                # Find all GitHub URLs
                matches = GITHUB_URL_PATTERN.findall(content)
                for owner, repo in matches:
                    # Clean up repo name
                    repo = repo.rstrip(')')
                    key = f"{owner}/{repo}"
                    repos[key] = (owner, repo)
                    
        except Exception as e:
            print(f"Error reading {file_path}: {e}")
        
        return repos
    
    def update_markdown_badges(self, file_path: Path, stats: Dict[str, Dict]) -> bool:
        """Update GitHub statistics badges in markdown file."""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            updated = False
            
            for repo_key, repo_stats in stats.items():
                if not repo_stats:
                    continue
                
                owner, repo = repo_key.split('/')
                
                # Update or add stars badge
                stars = repo_stats.get('stars', 0)
                stars_badge = f"![GitHub stars](https://img.shields.io/github/stars/{owner}/{repo})"
                
                # Update or add last commit badge
                last_commit_badge = f"![Last commit](https://img.shields.io/github/last-commit/{owner}/{repo})"
                
                # Find the line with this repo and update badges
                pattern = re.compile(rf'\[([^\]]+)\]\(https://github\.com/{owner}/{repo}[^)]*\)[^\n]*')
                
                def replace_func(match):
                    line = match.group(0)
                    # Remove existing badges
                    line = re.sub(r'!\[GitHub stars\]\([^)]+\)', '', line)
                    line = re.sub(r'!\[Last commit\]\([^)]+\)', '', line)
                    # Add new badges
                    return f"{line.rstrip()} {stars_badge} {last_commit_badge}"
                
                new_content, count = pattern.subn(replace_func, content)
                if count > 0:
                    content = new_content
                    updated = True
            
            if updated:
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(content)
                return True
                
        except Exception as e:
            print(f"Error updating {file_path}: {e}")
        
        return False
    
    def generate_stats_report(self, stats: Dict[str, Dict]) -> None:
        """Generate a statistics report."""
        total_repos = len(stats)
        repos_with_stats = sum(1 for s in stats.values() if s)
        
        print(f"\n{'='*60}")
        print("GitHub Statistics Summary")
        print(f"{'='*60}")
        print(f"Total repositories found: {total_repos}")
        print(f"Successfully fetched stats: {repos_with_stats}")
        
        if repos_with_stats > 0:
            # Calculate aggregate statistics
            total_stars = sum(s.get('stars', 0) for s in stats.values() if s)
            total_forks = sum(s.get('forks', 0) for s in stats.values() if s)
            
            print(f"\nAggregate Statistics:")
            print(f"  Total stars: {total_stars:,}")
            print(f"  Total forks: {total_forks:,}")
            
            # Find top repositories
            sorted_by_stars = sorted(
                [(k, v) for k, v in stats.items() if v and v.get('stars', 0) > 0],
                key=lambda x: x[1].get('stars', 0),
                reverse=True
            )
            
            if sorted_by_stars:
                print(f"\nTop 10 Repositories by Stars:")
                for repo, repo_stats in sorted_by_stars[:10]:
                    stars = repo_stats.get('stars', 0)
                    print(f"  {repo}: {stars:,} stars")
            
            # Check for archived/inactive repos
            archived = [(k, v) for k, v in stats.items() if v and v.get('archived', False)]
            if archived:
                print(f"\nArchived Repositories ({len(archived)}):")
                for repo, _ in archived:
                    print(f"  {repo}")
            
            # Save detailed stats to JSON
            with open('github_stats.json', 'w') as f:
                json.dump(stats, f, indent=2)
            print(f"\nDetailed statistics saved to: github_stats.json")

def main():
    """Main entry point."""
    # Initialize stats collector
    stats_collector = GitHubStats()
    
    # Check rate limit
    remaining, reset_time = stats_collector.check_rate_limit()
    if remaining >= 0:
        print(f"GitHub API rate limit: {remaining} requests remaining")
        if remaining < 10:
            print("Warning: Low rate limit. Consider using a GitHub token.")
    
    # Find repository root
    script_path = Path(__file__).resolve()
    repo_root = script_path.parent.parent
    
    # Collect all GitHub repos from markdown files
    all_repos = {}
    md_files = list(repo_root.glob('**/*.md'))
    
    for file_path in md_files:
        repos = stats_collector.extract_github_repos(file_path)
        all_repos.update(repos)
    
    print(f"Found {len(all_repos)} unique GitHub repositories")
    
    # Fetch statistics
    all_stats = {}
    for i, (repo_key, (owner, repo)) in enumerate(all_repos.items(), 1):
        print(f"Fetching stats for {repo_key} ({i}/{len(all_repos)})...")
        stats = stats_collector.fetch_repo_stats(owner, repo)
        all_stats[repo_key] = stats
        
        # Rate limiting
        if i % 10 == 0:
            time.sleep(1)  # Be nice to GitHub
    
    # Update badges in README
    readme_path = repo_root / 'README.md'
    if readme_path.exists():
        if stats_collector.update_markdown_badges(readme_path, all_stats):
            print("\nUpdated GitHub badges in README.md")
    
    # Generate report
    stats_collector.generate_stats_report(all_stats)

if __name__ == "__main__":
    main()