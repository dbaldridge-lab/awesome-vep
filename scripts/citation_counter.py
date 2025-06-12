#!/usr/bin/env python3
"""
Citation counter for Awesome Variant Effect Predictors.
Fetches citation counts from various sources for academic papers.
"""

import re
import json
import time
import requests
from pathlib import Path
from typing import Dict, Optional, Tuple
from urllib.parse import quote

# Configuration
SEMANTIC_SCHOLAR_API = "https://api.semanticscholar.org/v1/paper/{}"
CROSSREF_API = "https://api.crossref.org/works/{}"
USER_AGENT = "awesome-vep-citations/1.0"

# Common VEP tools and their DOIs/identifiers
KNOWN_TOOLS = {
    'SIFT': {
        'doi': '10.1093/nar/gkl423',
        'title': 'Predicting the Effects of Coding Non-Synonymous Variants'
    },
    'PolyPhen-2': {
        'doi': '10.1038/nmeth0410-248',
        'title': 'A method and server for predicting damaging missense mutations'
    },
    'CADD': {
        'doi': '10.1038/ng.2892',
        'title': 'A general framework for estimating the relative pathogenicity'
    },
    'REVEL': {
        'doi': '10.1016/j.ajhg.2016.08.016',
        'title': 'An Ensemble Method for Predicting the Pathogenicity'
    },
    'AlphaMissense': {
        'doi': '10.1126/science.adg7492',
        'title': 'Accurate proteome-wide missense variant effect prediction'
    },
    'EVE': {
        'doi': '10.1038/s41586-021-04043-8',
        'title': 'Disease variant prediction with deep generative models'
    },
    'PrimateAI': {
        'doi': '10.1038/s41588-018-0167-z',
        'title': 'Using deep learning to identify pathogenic variants'
    },
    'SpliceAI': {
        'doi': '10.1016/j.cell.2018.12.015',
        'title': 'A deep learning approach to identify genetic variants'
    },
    'VEST': {
        'doi': '10.1093/bioinformatics/btt685',
        'title': 'VEST 3.0: a resource for the prioritization'
    },
    'MutationTaster': {
        'doi': '10.1038/nmeth0810-575',
        'title': 'MutationTaster evaluates disease-causing potential'
    },
    'PROVEAN': {
        'doi': '10.1371/journal.pone.0046688',
        'title': 'Predicting Functional Effect of Human Missense Mutations'
    },
    'FATHMM': {
        'doi': '10.1093/bioinformatics/bts479',
        'title': 'Predicting the functional, molecular, and phenotypic consequences'
    }
}

class CitationCounter:
    def __init__(self):
        """Initialize the citation counter."""
        self.headers = {'User-Agent': USER_AGENT}
        self.citation_cache = {}
        
    def get_semantic_scholar_citations(self, doi: str) -> Optional[int]:
        """Get citation count from Semantic Scholar."""
        try:
            # Try DOI first
            url = SEMANTIC_SCHOLAR_API.format(doi)
            response = requests.get(url, headers=self.headers, timeout=10)
            
            if response.status_code == 200:
                data = response.json()
                return data.get('citationCount', 0)
            elif response.status_code == 404:
                # Try with DOI prefix
                url = SEMANTIC_SCHOLAR_API.format(f"DOI:{doi}")
                response = requests.get(url, headers=self.headers, timeout=10)
                if response.status_code == 200:
                    data = response.json()
                    return data.get('citationCount', 0)
        except Exception as e:
            print(f"Error fetching from Semantic Scholar for {doi}: {e}")
        
        return None
    
    def get_crossref_citations(self, doi: str) -> Optional[int]:
        """Get citation count from Crossref."""
        try:
            url = CROSSREF_API.format(doi)
            response = requests.get(url, headers=self.headers, timeout=10)
            
            if response.status_code == 200:
                data = response.json()
                # Crossref doesn't provide direct citation counts
                # but we can get the reference count
                refs = data.get('message', {}).get('reference-count', 0)
                return refs
        except Exception as e:
            print(f"Error fetching from Crossref for {doi}: {e}")
        
        return None
    
    def search_google_scholar(self, title: str) -> Optional[int]:
        """Search Google Scholar for citation count (limited functionality)."""
        # Note: Google Scholar doesn't provide a public API
        # This is a placeholder for manual lookup
        return None
    
    def get_citation_count(self, tool_name: str, doi: Optional[str] = None) -> Tuple[int, str]:
        """Get citation count for a tool."""
        # Check cache first
        cache_key = doi or tool_name
        if cache_key in self.citation_cache:
            return self.citation_cache[cache_key]
        
        # Get DOI if not provided
        if not doi and tool_name in KNOWN_TOOLS:
            doi = KNOWN_TOOLS[tool_name]['doi']
        
        if not doi:
            return 0, "No DOI"
        
        # Try Semantic Scholar first
        count = self.get_semantic_scholar_citations(doi)
        if count is not None:
            self.citation_cache[cache_key] = (count, "Semantic Scholar")
            return count, "Semantic Scholar"
        
        # Try Crossref as backup
        count = self.get_crossref_citations(doi)
        if count is not None:
            self.citation_cache[cache_key] = (count, "Crossref")
            return count, "Crossref"
        
        return 0, "Not found"
    
    def update_citation_badges(self, file_path: Path) -> bool:
        """Update citation badges in markdown file."""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            updated = False
            
            # Find tool entries and update citation badges
            for tool_name, tool_info in KNOWN_TOOLS.items():
                # Search for the tool in the content
                pattern = re.compile(rf'\*\*\[{tool_name}\].*?\*\*[^\n]*', re.IGNORECASE)
                
                matches = pattern.findall(content)
                if matches:
                    count, source = self.get_citation_count(tool_name, tool_info['doi'])
                    
                    if count > 0:
                        # Create citation badge
                        if count >= 10000:
                            badge_text = f"{count//1000}K+"
                        elif count >= 1000:
                            badge_text = f"{count//100*100}+"
                        else:
                            badge_text = str(count)
                        
                        citation_badge = f"![Citations](https://img.shields.io/badge/citations-{badge_text}-brightgreen)"
                        
                        # Update each match
                        for match in matches:
                            # Remove existing citation badge if present
                            clean_match = re.sub(r'!\[Citations\]\([^)]+\)', '', match)
                            # Add new badge
                            new_match = f"{clean_match.rstrip()} {citation_badge}"
                            content = content.replace(match, new_match)
                            updated = True
                            
                            print(f"Updated {tool_name}: {count} citations from {source}")
            
            if updated:
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(content)
                return True
                
        except Exception as e:
            print(f"Error updating {file_path}: {e}")
        
        return False
    
    def generate_citation_report(self) -> None:
        """Generate a citation report."""
        print(f"\n{'='*60}")
        print("Citation Count Report")
        print(f"{'='*60}\n")
        
        # Collect all citations
        citations = []
        for tool_name in KNOWN_TOOLS:
            count, source = self.get_citation_count(tool_name)
            if count > 0:
                citations.append((tool_name, count, source))
        
        # Sort by citation count
        citations.sort(key=lambda x: x[1], reverse=True)
        
        print("Top Tools by Citations:")
        print(f"{'Tool':<20} {'Citations':>10} {'Source':<20}")
        print("-" * 50)
        for tool, count, source in citations:
            print(f"{tool:<20} {count:>10,} {source:<20}")
        
        # Save to JSON
        citation_data = {
            tool: {
                'citations': count,
                'source': source,
                'doi': KNOWN_TOOLS.get(tool, {}).get('doi', '')
            }
            for tool, count, source in citations
        }
        
        with open('citation_counts.json', 'w') as f:
            json.dump(citation_data, f, indent=2)
        
        print(f"\nDetailed citation data saved to: citation_counts.json")

def main():
    """Main entry point."""
    # Initialize citation counter
    counter = CitationCounter()
    
    # Find repository root
    script_path = Path(__file__).resolve()
    repo_root = script_path.parent.parent
    
    print("Fetching citation counts for known VEP tools...")
    
    # Update README with citation badges
    readme_path = repo_root / 'README.md'
    if readme_path.exists():
        if counter.update_citation_badges(readme_path):
            print("\nUpdated citation badges in README.md")
    
    # Generate report
    counter.generate_citation_report()

if __name__ == "__main__":
    main()