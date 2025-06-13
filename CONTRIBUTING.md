# Contributing to Awesome Variant Effect Predictors

Thank you for your interest in contributing to this curated list! This document provides guidelines for adding new tools, resources, and improvements.

## How to Contribute

### Adding a New Tool

1. **Check if it already exists**: Search the README to ensure the tool isn't already listed
2. **Verify it meets our criteria**: See [Quality Criteria](#quality-criteria) below
3. **Use the proper format**: Follow our [formatting guidelines](#formatting-guidelines)
4. **Submit via pull request**: Fork the repo, make changes, and submit a PR

### Other Contributions

- **Fix broken links**: Update URLs that no longer work
- **Improve descriptions**: Make tool descriptions more accurate or clear
- **Add categories**: Suggest new categories for better organization
- **Update information**: Add missing GitHub stars, last commit dates, etc.
- **Improve documentation**: Enhance the resource files in `/resources/`

## Quality Criteria

### For VEP Tools

#### Essential Criteria (must meet at least 1)
- [ ] **Published research**: Peer-reviewed publication in a reputable journal
- [ ] **Wide adoption**: Used in multiple studies

#### Additional Criteria
- [ ] **Active maintenance**: Commits, releases, or updates within the last 2 years
- [ ] **Open source**: Code available on GitHub or similar platform
- [ ] **Documentation**: Clear usage instructions and documentation
- [ ] **Benchmark performance**: Demonstrated good performance in comparison studies
- [ ] **Clinical relevance**: Applicable to clinical variant interpretation

### For Resources and Databases

- [ ] **Publicly accessible**: Free or widely available resources
- [ ] **Relevant content**: Directly related to variant effect prediction
- [ ] **Quality information**: Authoritative and well-maintained
- [ ] **Active updates**: Regular updates or maintenance

## Formatting Guidelines

### Tool Entry Format

```markdown
- **[Tool Name](URL)** - Brief description highlighting key features, methodology, and use cases. ![GitHub stars](https://img.shields.io/github/stars/username/repo) ![Last commit](https://img.shields.io/github/last-commit/username/repo)
```

### Required Information

- **Tool Name**: Official name of the tool
- **URL**: Link to main website, GitHub repo, or publication
- **Description**: 1-2 sentences describing:
  - What the tool does
  - Key methodology or approach
  - Primary use case or strength
- **Badges**: GitHub stars and last commit (if applicable)

### Optional Information

- **Citation count badge**: `![Citations](https://img.shields.io/badge/citations-XXXX-brightgreen)`
- **License badge**: If relevant for the tool
- **Publication year**: For context on tool age

### Category Placement

Place tools in the most specific appropriate category:

1. **Popular VEP Tools**: Only for the most widely-used tools (1000+ citations)
2. **By Methodology**: Primary technical approach
3. **By Variant Type**: If specialized for specific variant types
4. **Meta-predictors**: Only for ensemble/combination methods
5. **Other categories**: As appropriate

## Submission Process

### Via GitHub Issues

1. Use the "Add a Resource" issue template
2. Fill out all required fields
3. Provide justification for inclusion
4. Wait for review and feedback

### Via Pull Request

1. **Fork** the repository
2. **Create a branch**: `git checkout -b add-tool-name`
3. **Make changes**: Add your tool following the guidelines
4. **Test links**: Ensure all URLs work
5. **Commit**: Use descriptive commit messages
6. **Submit PR**: Provide clear description of changes

## Style Guidelines

### Writing Style

- **Concise**: Keep descriptions brief but informative
- **Objective**: Avoid promotional language
- **Accurate**: Ensure technical details are correct
- **Consistent**: Follow existing description patterns

### Technical Details

- **Methodology**: Briefly mention the core approach
- **Performance**: Include benchmark results if available
- **Limitations**: Note significant limitations if relevant

## What NOT to Include

### Excluded Tools

- **Unmaintained tools**: No updates in 3+ years (unless historically significant)
- **Proprietary tools**: Closed-source commercial tools without free access
- **Duplicate functionality**: Tools that replicate existing functionality without improvement
- **Low-quality tools**: Poor documentation, no validation, or questionable methodology
- **Personal projects**: Unvalidated research projects or homework assignments

### Excluded Content

- **Tool comparisons**: We don't rank tools or make direct comparisons
- **Personal opinions**: Stick to factual descriptions
- **Commercial endorsements**: No promotional content

## Community Guidelines

### Code of Conduct

Please read and follow our [Code of Conduct](CODE_OF_CONDUCT.md).

## Questions?

- **Issues**: Use GitHub issues for questions about specific tools
- **Discussions**: Use GitHub discussions for general questions
- **Email**: Contact maintainers for sensitive matters

Thank you for helping make this resource valuable for the computational biology community!
