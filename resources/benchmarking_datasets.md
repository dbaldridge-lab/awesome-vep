# Benchmarking Datasets for Variant Effect Predictors

This document provides a curated list of datasets commonly used to benchmark and evaluate variant effect predictors.

## Clinical Datasets

### ClinVar
- **Description**: Database of genomic variation and its clinical significance
- **URL**: https://www.ncbi.nlm.nih.gov/clinvar/
- **Use Case**: Benchmarking clinical variant classification
- **Size**: 2M+ variants with clinical annotations

### HGMD
- **Description**: Human Gene Mutation Database
- **URL**: http://www.hgmd.cf.ac.uk/
- **Use Case**: Disease-causing mutations
- **Access**: Subscription required for full version

## Experimental Datasets

### ProteinGym
- **Description**: Large-scale benchmarking suite for protein fitness prediction
- **URL**: https://proteingym.org/
- **Use Case**: Deep mutational scanning data
- **Size**: 87 experimental datasets

### CAGI Challenges
- **Description**: Critical Assessment of Genome Interpretation
- **URL**: https://genomeinterpretation.org/
- **Use Case**: Community-wide prediction challenges
- **Frequency**: Biennial challenges

## Computational Datasets

### gnomAD
- **Description**: Genome Aggregation Database
- **URL**: https://gnomad.broadinstitute.org/
- **Use Case**: Population frequency data
- **Size**: 140K+ genomes, 125K+ exomes

### dbNSFP
- **Description**: Database of human nonsynonymous SNPs and their functional predictions
- **URL**: https://sites.google.com/site/jpopgen/dbNSFP
- **Use Case**: Precomputed predictions from multiple tools
- **Coverage**: All possible human nonsynonymous variants

## Specialized Datasets

### VariBench
- **Description**: Benchmark for variant effect prediction methods
- **URL**: http://structure.bmc.lu.se/VariBench/
- **Use Case**: Standardized evaluation framework

### MutationAssessor
- **Description**: Functional impact prediction and benchmarking
- **URL**: http://mutationassessor.org/
- **Use Case**: Cancer variant assessment

## Usage Guidelines

1. **Dataset Selection**: Choose datasets appropriate for your tool's scope
2. **Evaluation Metrics**: Use standard metrics (AUC, precision, recall, MCC)
3. **Cross-validation**: Implement proper train/test splits
4. **Comparison**: Compare against established baselines
5. **Reporting**: Follow community standards for performance reporting