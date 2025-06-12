# Awesome Variant Effect Predictors [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

> A curated list of tools, resources, and datasets for predicting the functional effects of genetic variants

Variant Effect Predictors (VEPs) are computational tools that assess the potential impact of genetic variants on protein function, disease risk, and phenotypic outcomes. This list focuses on the most reliable, well-maintained, and widely-used tools in the field.

## Contents

- [Popular VEP Tools](#popular-vep-tools)
- [By Methodology](#by-methodology)
  - [Sequence-based Predictors](#sequence-based-predictors)
  - [Structure-based Predictors](#structure-based-predictors)
  - [Machine Learning Methods](#machine-learning-methods)
  - [Deep Learning & Protein Language Models](#deep-learning--protein-language-models)
- [By Variant Type](#by-variant-type)
  - [Single Nucleotide Variants (SNVs)](#single-nucleotide-variants-snvs)
  - [Insertions/Deletions (Indels)](#insertionsdeletions-indels)
  - [Structural Variants](#structural-variants)
  - [Splicing Variants](#splicing-variants)
  - [Regulatory Variants](#regulatory-variants)
- [Meta-predictors & Ensemble Methods](#meta-predictors--ensemble-methods)
- [Annotation Platforms](#annotation-platforms)
- [Databases & Resources](#databases--resources)
- [Benchmarking Tools](#benchmarking-tools)
- [Clinical Applications](#clinical-applications)
- [Specialized Predictors](#specialized-predictors)
  - [Disease-Specific Tools](#disease-specific-tools)
  - [Pharmacogenomics](#pharmacogenomics)
- [Educational Resources](#educational-resources)
- [Web Tools & APIs](#web-tools--apis)
- [Contributing](#contributing)

## Popular VEP Tools

The most widely-used and well-established variant effect predictors:

### Classic Methods

- **[SIFT](http://sift.bii.a-star.edu.sg/)** - Predicts whether amino acid substitutions affect protein function using sequence homology. One of the most cited VEP tools. ![Citations](https://img.shields.io/badge/citations-15000%2B-brightgreen)
- **[PolyPhen-2](http://genetics.bwh.harvard.edu/pph2/)** - Predicts functional effects of human nsSNPs using physical and comparative considerations. Combines sequence, phylogenetic and structural information. ![Citations](https://img.shields.io/badge/citations-12000%2B-brightgreen)
- **[CADD](https://cadd.gs.washington.edu/)** - Combined Annotation Dependent Depletion scores integrating multiple annotations into one metric. Widely used for variant prioritization. ![Citations](https://img.shields.io/badge/citations-5000%2B-brightgreen)

### Modern Deep Learning

- **[AlphaMissense](https://github.com/google-deepmind/alphamissense)** - DeepMind's adaptation of AlphaFold for missense variant effect prediction. Covers 71M possible missense variants. ![GitHub stars](https://img.shields.io/github/stars/google-deepmind/alphamissense) ![Last commit](https://img.shields.io/github/last-commit/google-deepmind/alphamissense)
- **[EVE](https://github.com/OATML-Markslab/EVE)** - Evolutionary model of Variant Effect using unsupervised learning on sequence alignments. Provides uncertainty quantification. ![GitHub stars](https://img.shields.io/github/stars/OATML-Markslab/EVE) ![Last commit](https://img.shields.io/github/last-commit/OATML-Markslab/EVE)
- **[PrimateAI](https://github.com/Illumina/PrimateAI)** - Deep learning tool trained on primate variant data. Particularly effective for benign variant identification. ![GitHub stars](https://img.shields.io/github/stars/Illumina/PrimateAI) ![Last commit](https://img.shields.io/github/last-commit/Illumina/PrimateAI)

### Meta-predictors

- **[REVEL](https://sites.google.com/site/revelgenomics/)** - Ensemble method combining 13 individual predictors. Consistently high performance across benchmarks. Threshold: 0.5. ![Citations](https://img.shields.io/badge/citations-2000%2B-brightgreen)
- **[BayesDel](https://github.com/zengmiao/BayesDel)** - Bayesian framework combining deleteriousness scores. Currently achieves highest balanced accuracy (95.5%). ![GitHub stars](https://img.shields.io/github/stars/zengmiao/BayesDel) ![Last commit](https://img.shields.io/github/last-commit/zengmiao/BayesDel)

## By Methodology

### Sequence-based Predictors

Tools that rely primarily on sequence conservation and alignment:

- **[SIFT](http://sift.bii.a-star.edu.sg/)** - Uses sequence homology and conservation
- **[PROVEAN](http://provean.jcvi.org/)** - Protein Variation Effect Analyzer, supports indels
- **[MutationTaster](http://www.mutationtaster.org/)** - Combines evolutionary conservation with splice-site analysis
- **[PhD-SNP](https://snps.biofold.org/phd-snp/phd-snp.html)** - Support Vector Machine approach using sequence and conservation

### Structure-based Predictors

Tools incorporating protein structure information:

- **[PolyPhen-2](http://genetics.bwh.harvard.edu/pph2/)** - Combines sequence and structural features
- **[SNAP2](https://github.com/Rostlab/SNAP2)** - Neural network using sequence and structure
- **[MutPred2](http://mutpred.mutdb.org/)** - Predicts molecular mechanisms of pathogenicity
- **[FoldX](http://foldxsuite.crg.eu/)** - Protein stability analysis and mutation effects

### Machine Learning Methods

Traditional ML approaches:

- **[FATHMM](http://fathmm.biocompute.org.uk/)** - Hidden Markov Models for functional analysis
- **[LRT](http://www.genetics.wustl.edu/jflab/lrt_query.html)** - Likelihood Ratio Test comparing evolutionary rates
- **[MetaSVM](https://sites.google.com/site/jpopgen/dbNSFP)** - Support Vector Machine ensemble
- **[MetaLR](https://sites.google.com/site/jpopgen/dbNSFP)** - Logistic Regression ensemble

### Deep Learning & Protein Language Models

Modern neural network approaches:

#### AlphaFold-based Methods
- **[AlphaMissense](https://github.com/google-deepmind/alphamissense)** - DeepMind's AlphaFold adaptation for missense variant prediction. Precomputed scores for 71M variants. ![GitHub stars](https://img.shields.io/github/stars/google-deepmind/alphamissense) ![Last commit](https://img.shields.io/github/last-commit/google-deepmind/alphamissense)

#### Protein Language Models
- **[ESM-1v](https://github.com/facebookresearch/esm)** - Meta's evolutionary scale modeling for variant effects. Zero-shot prediction capability. ![GitHub stars](https://img.shields.io/github/stars/facebookresearch/esm) ![Last commit](https://img.shields.io/github/last-commit/facebookresearch/esm)
- **[ProtTrans](https://github.com/agemagician/ProtTrans)** - Transfer learning for protein sequences. Supports variant effect prediction. ![GitHub stars](https://img.shields.io/github/stars/agemagician/ProtTrans) ![Last commit](https://img.shields.io/github/last-commit/agemagician/ProtTrans)
- **[MSA-Transformer](https://github.com/facebookresearch/esm)** - Unsupervised protein language model trained on MSAs. Part of ESM toolkit. 
- **[TAPE](https://github.com/songlab-cal/tape)** - Tasks Assessing Protein Embeddings. Benchmark suite with variant effect models. ![GitHub stars](https://img.shields.io/github/stars/songlab-cal/tape) ![Last commit](https://img.shields.io/github/last-commit/songlab-cal/tape)
- **[ProteinBERT](https://github.com/nadavbra/protein_bert)** - BERT-based model for protein sequences. Includes variant effect fine-tuning. ![GitHub stars](https://img.shields.io/github/stars/nadavbra/protein_bert) ![Last commit](https://img.shields.io/github/last-commit/nadavbra/protein_bert)

#### Generative & Autoregressive Models
- **[EVE](https://github.com/OATML-Markslab/EVE)** - Evolutionary model of variant effect. VAE trained on MSAs. Provides uncertainty estimates. ![GitHub stars](https://img.shields.io/github/stars/OATML-Markslab/EVE) ![Last commit](https://img.shields.io/github/last-commit/OATML-Markslab/EVE)
- **[Tranception](https://github.com/OATML-Markslab/Tranception)** - Autoregressive transformer for protein fitness. Handles insertions and deletions. ![GitHub stars](https://img.shields.io/github/stars/OATML-Markslab/Tranception) ![Last commit](https://img.shields.io/github/last-commit/OATML-Markslab/Tranception)
- **[ProGen](https://github.com/salesforce/progen)** - Protein engineering with large language models. Conditional variant generation. ![GitHub stars](https://img.shields.io/github/stars/salesforce/progen) ![Last commit](https://img.shields.io/github/last-commit/salesforce/progen)

#### Specialized Deep Learning
- **[DeepSequence](https://github.com/debbiemarkslab/DeepSequence)** - Generative model of protein families. Predicts mutation effects. ![GitHub stars](https://img.shields.io/github/stars/debbiemarkslab/DeepSequence) ![Last commit](https://img.shields.io/github/last-commit/debbiemarkslab/DeepSequence)

## By Variant Type

### Single Nucleotide Variants (SNVs)

Most tools focus on missense SNVs:

- **[SIFT](http://sift.bii.a-star.edu.sg/)** - Standard for missense variants
- **[PolyPhen-2](http://genetics.bwh.harvard.edu/pph2/)** - Missense variant specialist
- **[AlphaMissense](https://github.com/google-deepmind/alphamissense)** - Comprehensive missense coverage
- **[CADD](https://cadd.gs.washington.edu/)** - All SNV types including synonymous

### Insertions/Deletions (Indels)

Tools supporting small insertions and deletions:

- **[PROVEAN](http://provean.jcvi.org/)** - Explicitly designed for indels
- **[CADD](https://cadd.gs.washington.edu/)** - Supports indels up to certain size
- **[VEST](http://karchinlab.org/apps/appVest.html)** - Includes indel prediction
- **[MutationTaster](http://www.mutationtaster.org/)** - Comprehensive indel analysis

### Structural Variants

Large-scale genomic rearrangements:

- **[AnnotSV](https://github.com/lgmgeo/AnnotSV)** - Structural variant annotation and ranking
- **[SVFX](https://github.com/KCCG/svfx)** - Structural variant functional annotation
- **[ClassifyCNV](https://github.com/Genotek/ClassifyCNV)** - Copy number variant classification

### Splicing Variants

Tools for splice site and splicing impact prediction:

- **[SpliceAI](https://github.com/Illumina/SpliceAI)** - Deep neural network for splice prediction
- **[MaxEntScan](http://hollywood.mit.edu/burgelab/maxent/Xmaxentscan_scoreseq.html)** - Maximum entropy splice site scoring
- **[SPIDEX](http://tools.genes.toronto.edu/)** - Splicing impact prediction using deep learning
- **[MES](http://hollywood.mit.edu/burgelab/maxent/Xmaxentscan_scoreseq.html)** - Maximum Entropy Score for splice sites

### Regulatory Variants

Non-coding and regulatory region variants:

- **[CADD](https://cadd.gs.washington.edu/)** - Includes non-coding variants
- **[DANN](https://cbcl.ics.uci.edu/public_data/DANN/)** - Deep annotation of genetic variants
- **[FunSeq2](http://funseq2.gersteinlab.org/)** - Functional significance of non-coding variants
- **[GWAVA](https://www.sanger.ac.uk/science/tools/gwava)** - Genome-Wide Annotation of Variants

## Meta-predictors & Ensemble Methods

Tools combining multiple prediction algorithms:

- **[REVEL](https://sites.google.com/site/revelgenomics/)** - Combines 13 tools, excellent clinical performance
- **[BayesDel](https://github.com/zengmiao/BayesDel)** - Bayesian integration, top benchmark performance
- **[MetaSVM](https://sites.google.com/site/jpopgen/dbNSFP)** - Support Vector Machine ensemble
- **[MetaLR](https://sites.google.com/site/jpopgen/dbNSFP)** - Logistic regression ensemble
- **[MPC](https://github.com/quinlan-lab/cse)** - Missense badness, PolyPhen-2, and Constraint score
- **[CardioBoost](https://github.com/ImperialCardioGenetics/CardioBoost)** - Cardiomyopathy-specific ensemble

## Annotation Platforms

Comprehensive variant annotation pipelines:

- **[Ensembl VEP](https://github.com/Ensembl/ensembl-vep)** - Most widely used annotation tool. Integrates 30+ prediction tools. ![GitHub stars](https://img.shields.io/github/stars/Ensembl/ensembl-vep) ![Last commit](https://img.shields.io/github/last-commit/Ensembl/ensembl-vep)
- **[ANNOVAR](https://github.com/WGLab/ANNOVAR)** - Efficient annotation with multiple databases. Command-line focused. ![GitHub stars](https://img.shields.io/github/stars/WGLab/ANNOVAR) ![Last commit](https://img.shields.io/github/last-commit/WGLab/ANNOVAR)
- **[OpenCRAVAT](https://github.com/KarchinLab/open-cravat)** - Modular annotation platform with web interface. 100+ annotation modules. ![GitHub stars](https://img.shields.io/github/stars/KarchinLab/open-cravat) ![Last commit](https://img.shields.io/github/last-commit/KarchinLab/open-cravat)
- **[SnpEff](https://github.com/pcingola/SnpEff)** - Variant annotation and effect prediction tool. ![GitHub stars](https://img.shields.io/github/stars/pcingola/SnpEff) ![Last commit](https://img.shields.io/github/last-commit/pcingola/SnpEff)

## Databases & Resources

Essential databases and precomputed scores:

- **[dbNSFP](https://sites.google.com/site/jpopgen/dbNSFP)** - Database of precomputed scores from 46+ predictors for all possible missense variants
- **[ClinVar](https://www.ncbi.nlm.nih.gov/clinvar/)** - NIH database of genetic variants and clinical significance
- **[gnomAD](https://gnomad.broadinstitute.org/)** - Population frequency data for variant filtering
- **[HGMD](http://www.hgmd.cf.ac.uk/)** - Human Gene Mutation Database (subscription required)
- **[UniProt](https://www.uniprot.org/)** - Protein sequence and functional information
- **[PDB](https://www.rcsb.org/)** - Protein structure database

## Benchmarking Tools

Tools and datasets for evaluating VEP performance:

- **[ProteinGym](https://github.com/OATML-Markslab/ProteinGym)** - Large-scale benchmarking suite with 87 deep mutational scanning datasets. ![GitHub stars](https://img.shields.io/github/stars/OATML-Markslab/ProteinGym) ![Last commit](https://img.shields.io/github/last-commit/OATML-Markslab/ProteinGym)
- **[VariantPrioritizationBenchmark](https://github.com/ZuchnerLab/VariantPrioritizationBenchmark)** - Open benchmark with 52 tools and standardized evaluation. ![GitHub stars](https://img.shields.io/github/stars/ZuchnerLab/VariantPrioritizationBenchmark) ![Last commit](https://img.shields.io/github/last-commit/ZuchnerLab/VariantPrioritizationBenchmark)
- **[CAGI](https://genomeinterpretation.org/)** - Critical Assessment of Genome Interpretation challenges
- **[VariBench](http://structure.bmc.lu.se/VariBench/)** - Benchmark datasets for variant effect prediction

## Clinical Applications

Tools designed for clinical variant interpretation:

- **[InterVar](https://github.com/WGLab/InterVar)** - ACMG/AMP guidelines implementation. ![GitHub stars](https://img.shields.io/github/stars/WGLab/InterVar) ![Last commit](https://img.shields.io/github/last-commit/WGLab/InterVar)
- **[CardioClassifier](https://github.com/ImperialCardioGenetics/CardioClassifier)** - Cardiomyopathy variant classification
- **[SpliceAI-visual](https://github.com/broadinstitute/SpliceAI-visual)** - Clinical splice variant interpretation
- **[Franklin](https://franklin.genoox.com/)** - Clinical variant interpretation platform
- **[AutoPVS1](https://github.com/JiguangPeng/autopvs1)** - Automated ACMG/AMP PVS1 criterion assignment. ![GitHub stars](https://img.shields.io/github/stars/JiguangPeng/autopvs1) ![Last commit](https://img.shields.io/github/last-commit/JiguangPeng/autopvs1)
- **[CharGer](https://github.com/ding-lab/CharGer)** - Clinical interpretation of germline variants in cancer. ![GitHub stars](https://img.shields.io/github/stars/ding-lab/CharGer) ![Last commit](https://img.shields.io/github/last-commit/ding-lab/CharGer)

## Specialized Predictors

### Disease-Specific Tools

#### Cardiovascular
- **[CardioBoost](https://github.com/ImperialCardioGenetics/CardioBoost)** - Gradient boosting for cardiomyopathy variants. ![GitHub stars](https://img.shields.io/github/stars/ImperialCardioGenetics/CardioBoost) ![Last commit](https://img.shields.io/github/last-commit/ImperialCardioGenetics/CardioBoost)

#### Cancer
- **[CHASM](https://github.com/KarchinLab/CHASMplus)** - Cancer driver missense mutation prediction. ![GitHub stars](https://img.shields.io/github/stars/KarchinLab/CHASMplus) ![Last commit](https://img.shields.io/github/last-commit/KarchinLab/CHASMplus)
- **[CanDrA+](http://bioinformatics.mdanderson.org/main/CanDrA)** - Cancer-specific driver annotation. Trained on COSMIC data
- **[FATHMM-cancer](http://fathmm.biocompute.org.uk/cancer.html)** - Functional analysis through hidden Markov models for cancer
- **[CScape](http://cscape.biocompute.org.uk/)** - Cancer driver prediction using coding and non-coding variants

### Pharmacogenomics
- **[PharmGKB](https://www.pharmgkb.org/)** - Pharmacogenomics knowledge resource with variant annotations
- **[CPIC](https://cpicpgx.org/)** - Clinical Pharmacogenetics Implementation Consortium guidelines
- **[Stargazer](https://stargazer.gs.washington.edu/stargazerweb/)** - Calling star alleles from NGS data for pharmacogenes



## Educational Resources

Learning materials and tutorials:

### Tutorials & Courses
- **[Ensembl VEP Tutorial](https://www.ensembl.org/info/docs/tools/vep/index.html)** - Comprehensive VEP usage guide
- **[ANNOVAR Tutorial](https://annovar.openbioinformatics.org/en/latest/user-guide/startup/)** - Step-by-step annotation guide
- **[Variant Interpretation Course](https://www.genome.gov/about-genomics/educational-resources)** - NIH educational materials

### Review Papers
- **"Computational tools for variant effect prediction"** - Comprehensive tool comparison
- **"Clinical variant interpretation guidelines"** - ACMG/AMP framework explanation
- **"Machine learning in variant effect prediction"** - Modern ML approaches review

### Documentation
- [Benchmarking Datasets](resources/benchmarking_datasets.md) - Standard evaluation datasets
- [Clinical Guidelines](resources/clinical_guidelines.md) - ACMG/AMP and other guidelines
- [Comparison Studies](resources/comparison_studies.md) - Key benchmarking papers

## Web Tools & APIs

### Online Prediction Services
- **[PredictSNP](https://loschmidt.chemi.muni.cz/predictsnp/)** - Consensus classifier combining multiple tools. Web interface and API.
- **[MutationAssessor](http://mutationassessor.org/)** - Web service for functional impact of missense variants
- **[Meta-SNP](https://snps.biofold.org/meta-snp/)** - Meta-predictor web service combining 4 methods
- **[PON-P2](http://structure.bmc.lu.se/PON-P2/)** - Pathogenicity of amino acid substitutions predictor

### API Services
- **[myvariant.info](http://myvariant.info/)** - RESTful web service for variant annotation. Aggregates 30+ data sources.
- **[VEP REST API](https://rest.ensembl.org/)** - Ensembl's RESTful service for programmatic VEP access
- **[ExAC API](http://exac.hms.harvard.edu/)** - Programmatic access to population frequency data
- **[ClinGen Allele Registry](http://reg.clinicalgenome.org/)** - API for variant registration and canonical identifiers

### Cloud Platforms
- **[DNAnexus](https://www.dnanexus.com/)** - Cloud platform with integrated VEP tools
- **[Seven Bridges](https://www.sevenbridges.com/)** - Cloud computing platform with variant annotation pipelines
- **[Terra](https://terra.bio/)** - Broad Institute's cloud platform for genomic analysis
- **[Galaxy](https://usegalaxy.org/)** - Web-based platform with VEP tool integrations

## Contributing

We welcome contributions! Please see our [Contributing Guidelines](CONTRIBUTING.md) for details on:

- Adding new tools
- Quality criteria for inclusion
- Submission format requirements
- Review process

## License

[![CC0](https://mirrors.creativecommons.org/presskit/buttons/88x31/svg/cc-zero.svg)](https://creativecommons.org/publicdomain/zero/1.0/)

To the extent possible under law, the contributors have waived all copyright and related rights to this work.