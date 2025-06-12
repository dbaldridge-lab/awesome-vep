# Automation Scripts

This directory contains Python scripts for maintaining the Awesome Variant Effect Predictors repository.

## Scripts

### check_links.py
Validates all URLs in markdown files and reports broken links.

```bash
python scripts/check_links.py
```

Features:
- Concurrent URL checking for performance
- Retry logic for transient failures
- Generates broken links report
- GitHub Actions compatible

### github_stats.py
Fetches and updates GitHub statistics (stars, forks, last commit) for all repositories.

```bash
# Optional: Set GitHub token for higher rate limits
export GITHUB_TOKEN=your_token_here
python scripts/github_stats.py
```

Features:
- Updates shields.io badges automatically
- Generates statistics summary
- Saves detailed stats to JSON

### citation_counter.py
Fetches citation counts from academic sources and updates citation badges.

```bash
python scripts/citation_counter.py
```

Features:
- Semantic Scholar API integration
- Crossref API as fallback
- Updates citation badges in README
- Generates citation report

### categorize_tools.py
Analyzes tool descriptions and suggests categorization improvements.

```bash
python scripts/categorize_tools.py
```

Features:
- Keyword-based categorization
- Identifies uncategorized tools
- Suggests category improvements
- Exports categorization data

## Setup

Install required dependencies:

```bash
pip install -r scripts/requirements.txt
```

## GitHub Actions Integration

The `check_links.py` script is integrated with GitHub Actions through `.github/workflows/link_checker.yml` to run monthly checks.

## Environment Variables

- `GITHUB_TOKEN`: Optional GitHub personal access token for higher API rate limits

## Output Files

Scripts generate the following output files in the repository root:
- `broken_links_report.md`: Report of broken links
- `github_stats.json`: Detailed GitHub statistics
- `citation_counts.json`: Citation data for tools
- `tool_categories.json`: Tool categorization analysis