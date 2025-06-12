# Clinical Guidelines for Variant Interpretation

This document outlines key clinical guidelines and standards used in variant interpretation and how they relate to computational prediction tools.

## ACMG/AMP Guidelines

### Overview
- **Full Name**: American College of Medical Genetics and Genomics / Association for Molecular Pathology
- **Publication**: Richards et al. (2015) Genetics in Medicine
- **Purpose**: Standardized framework for variant classification

### Classification Categories
1. **Pathogenic (P)**
2. **Likely Pathogenic (LP)**
3. **Variant of Uncertain Significance (VUS)**
4. **Likely Benign (LB)**
5. **Benign (B)**

### Evidence Types
- **Population Data**: Allele frequency thresholds
- **Computational Data**: In silico prediction tools
- **Functional Data**: Experimental validation
- **Segregation Data**: Family studies
- **De novo Data**: Parent-offspring trios

## ClinGen Guidelines

### ClinGen Calibration
- **Purpose**: Calibrating computational tools for clinical use
- **Process**: Establishing tool-specific thresholds
- **Tools Evaluated**: REVEL, BayesDel, MPC, PrimateAI

### Sequence Variant Interpretation Working Groups
- Gene-specific guidelines for variant interpretation
- Expert panel recommendations
- Tool-specific calibrations

## International Guidelines

### EuroGentest
- **Region**: European guidelines
- **Focus**: Laboratory standards and variant classification
- **URL**: https://www.eurogentest.org/

### HGVS Nomenclature
- **Purpose**: Standardized variant description
- **URL**: https://varnomen.hgvs.org/
- **Importance**: Consistent variant reporting

## Regulatory Frameworks

### FDA Guidance
- **Document**: "Use of Public Human Genetic Variant Databases"
- **Scope**: Regulatory considerations for genetic testing
- **Impact**: Requirements for clinical-grade tools

### CAP/CLIA Standards
- **Scope**: Laboratory quality standards
- **Relevance**: Requirements for clinical implementation

## Implementation Considerations

### For Tool Developers
1. **ACMG Compliance**: Ensure outputs align with ACMG categories
2. **Clinical Calibration**: Provide clinically-calibrated thresholds
3. **Evidence Integration**: Support multiple evidence types
4. **Uncertainty Handling**: Appropriate handling of VUS

### For Clinical Users
1. **Guideline Adherence**: Follow established interpretation frameworks
2. **Tool Limitations**: Understand computational tool boundaries
3. **Expert Review**: Combine computational with clinical expertise
4. **Documentation**: Maintain evidence trail for decisions

## Best Practices

1. **Multi-tool Approach**: Use multiple computational predictors
2. **Clinical Context**: Consider patient phenotype and family history
3. **Literature Review**: Check recent publications for gene/variant
4. **Expert Consultation**: Engage clinical geneticists for complex cases
5. **Regular Updates**: Stay current with guideline revisions

## Resources

- [ClinGen](https://clinicalgenome.org/)
- [ACMG Practice Guidelines](https://www.acmg.net/ACMG/Medical-Genetics-Practice-Resources/Practice-Guidelines.aspx)
- [ClinVar Submission Guidelines](https://www.ncbi.nlm.nih.gov/clinvar/docs/submission_guidelines/)
- [HGVS Variant Nomenclature](https://varnomen.hgvs.org/)