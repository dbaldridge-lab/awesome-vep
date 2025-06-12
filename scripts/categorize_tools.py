#!/usr/bin/env python3
"""
Tool categorization helper for Awesome Variant Effect Predictors.
Helps organize and categorize VEP tools based on their characteristics.
"""

import re
import json
from pathlib import Path
from typing import Dict, List, Set
from collections import defaultdict

# Category definitions
CATEGORIES = {
    'methodology': {
        'sequence_based': [
            'conservation', 'alignment', 'homology', 'evolution', 'phylogenetic',
            'sequence', 'substitution', 'amino acid'
        ],
        'structure_based': [
            'structure', 'structural', '3D', 'protein fold', 'stability',
            'folding', 'PDB', 'crystal', 'AlphaFold'
        ],
        'machine_learning': [
            'SVM', 'random forest', 'logistic regression', 'classifier',
            'supervised', 'ensemble', 'meta'
        ],
        'deep_learning': [
            'neural network', 'deep learning', 'transformer', 'attention',
            'BERT', 'GPT', 'autoencoder', 'CNN', 'RNN', 'LSTM'
        ]
    },
    'variant_type': {
        'snv': [
            'SNV', 'missense', 'nonsense', 'single nucleotide', 'point mutation',
            'substitution'
        ],
        'indel': [
            'indel', 'insertion', 'deletion', 'frameshift', 'in-frame'
        ],
        'structural': [
            'structural variant', 'SV', 'CNV', 'copy number', 'duplication',
            'inversion', 'translocation'
        ],
        'splicing': [
            'splice', 'splicing', 'splice site', 'acceptor', 'donor',
            'branch point', 'exon', 'intron'
        ],
        'regulatory': [
            'regulatory', 'promoter', 'enhancer', 'UTR', 'non-coding',
            'expression', 'transcription', 'TFBS'
        ]
    },
    'application': {
        'clinical': [
            'clinical', 'diagnostic', 'patient', 'disease', 'pathogenic',
            'benign', 'ACMG', 'ClinVar', 'medical'
        ],
        'research': [
            'research', 'experimental', 'laboratory', 'academic', 'study'
        ],
        'pharmacogenomics': [
            'pharmacogenomics', 'drug', 'medication', 'PGx', 'metabolism',
            'dosing', 'adverse'
        ],
        'cancer': [
            'cancer', 'tumor', 'somatic', 'oncogene', 'tumor suppressor',
            'driver', 'passenger'
        ],
        'population': [
            'population', 'ancestry', 'ethnic', 'frequency', 'gnomAD',
            'demographic'
        ]
    }
}

class ToolCategorizer:
    def __init__(self):
        """Initialize the categorizer."""
        self.tools = {}
        self.categories = defaultdict(lambda: defaultdict(set))
        
    def extract_tools_from_markdown(self, file_path: Path) -> Dict[str, str]:
        """Extract tool names and descriptions from markdown."""
        tools = {}
        
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Pattern to match tool entries
            pattern = re.compile(r'\*\*\[([^\]]+)\]\([^)]+\)\*\* - ([^\n]+)')
            
            matches = pattern.findall(content)
            for tool_name, description in matches:
                tools[tool_name] = description
                
        except Exception as e:
            print(f"Error reading {file_path}: {e}")
        
        return tools
    
    def categorize_tool(self, tool_name: str, description: str) -> Dict[str, List[str]]:
        """Categorize a tool based on its description."""
        tool_categories = defaultdict(list)
        
        # Convert to lowercase for matching
        text = f"{tool_name} {description}".lower()
        
        # Check each category type
        for category_type, subcategories in CATEGORIES.items():
            for subcategory, keywords in subcategories.items():
                # Check if any keyword matches
                for keyword in keywords:
                    if keyword.lower() in text:
                        tool_categories[category_type].append(subcategory)
                        break
        
        return dict(tool_categories)
    
    def analyze_all_tools(self, tools: Dict[str, str]) -> None:
        """Analyze and categorize all tools."""
        for tool_name, description in tools.items():
            categories = self.categorize_tool(tool_name, description)
            self.tools[tool_name] = {
                'description': description,
                'categories': categories
            }
            
            # Update category mappings
            for category_type, subcategories in categories.items():
                for subcategory in subcategories:
                    self.categories[category_type][subcategory].add(tool_name)
    
    def generate_category_report(self) -> None:
        """Generate a report of tool categories."""
        print(f"\n{'='*60}")
        print("Tool Categorization Report")
        print(f"{'='*60}\n")
        
        print(f"Total tools analyzed: {len(self.tools)}\n")
        
        # Report by category type
        for category_type, subcategories in self.categories.items():
            print(f"\n{category_type.upper().replace('_', ' ')}:")
            print("-" * 40)
            
            # Sort by number of tools
            sorted_subcats = sorted(
                subcategories.items(),
                key=lambda x: len(x[1]),
                reverse=True
            )
            
            for subcat, tools in sorted_subcats:
                print(f"  {subcat}: {len(tools)} tools")
                if len(tools) <= 5:
                    print(f"    Tools: {', '.join(sorted(tools))}")
        
        # Find uncategorized tools
        uncategorized = []
        for tool_name, tool_data in self.tools.items():
            if not tool_data['categories']:
                uncategorized.append(tool_name)
        
        if uncategorized:
            print(f"\n\nUNCATEGORIZED TOOLS ({len(uncategorized)}):")
            print("-" * 40)
            for tool in sorted(uncategorized):
                print(f"  - {tool}")
                print(f"    Description: {self.tools[tool]['description'][:80]}...")
    
    def generate_suggestions(self) -> None:
        """Generate suggestions for improving categorization."""
        print(f"\n\n{'='*60}")
        print("Categorization Suggestions")
        print(f"{'='*60}\n")
        
        # Tools with multiple methodology categories
        multi_method = []
        for tool_name, tool_data in self.tools.items():
            methods = tool_data['categories'].get('methodology', [])
            if len(methods) > 1:
                multi_method.append((tool_name, methods))
        
        if multi_method:
            print("Tools with multiple methodologies (consider primary method):")
            for tool, methods in multi_method[:10]:
                print(f"  - {tool}: {', '.join(methods)}")
        
        # Popular tools that might need their own section
        tool_counts = {}
        for tool_name in self.tools:
            # Simple popularity check based on common names
            if tool_name in ['SIFT', 'PolyPhen-2', 'CADD', 'REVEL', 'AlphaMissense']:
                tool_counts[tool_name] = "High"
        
        if tool_counts:
            print("\n\nHighly popular tools (consider 'Popular Tools' section):")
            for tool, status in tool_counts.items():
                print(f"  - {tool}")
    
    def save_categorization(self, output_path: Path) -> None:
        """Save categorization data to JSON."""
        data = {
            'tools': self.tools,
            'categories': {
                cat_type: {
                    subcat: list(tools)
                    for subcat, tools in subcats.items()
                }
                for cat_type, subcats in self.categories.items()
            }
        }
        
        with open(output_path, 'w') as f:
            json.dump(data, f, indent=2)
        
        print(f"\n\nCategorization data saved to: {output_path}")

def main():
    """Main entry point."""
    # Initialize categorizer
    categorizer = ToolCategorizer()
    
    # Find repository root
    script_path = Path(__file__).resolve()
    repo_root = script_path.parent.parent
    
    # Extract tools from README
    readme_path = repo_root / 'README.md'
    if readme_path.exists():
        print("Extracting tools from README.md...")
        tools = categorizer.extract_tools_from_markdown(readme_path)
        print(f"Found {len(tools)} tools")
        
        # Analyze and categorize
        print("\nAnalyzing tool descriptions...")
        categorizer.analyze_all_tools(tools)
        
        # Generate reports
        categorizer.generate_category_report()
        categorizer.generate_suggestions()
        
        # Save results
        output_path = repo_root / 'tool_categories.json'
        categorizer.save_categorization(output_path)
    else:
        print("README.md not found!")

if __name__ == "__main__":
    main()