# biothings_explorer

## Intro
RESTful APIs have been widely used to distribute biological data in a programmatic manner. BioThings Explorer Python Package empowers users to explore the relationship between different biological entities through the vast amount of biological data provided by various API resources. Currently, the following API resources are available for explore:
1. [MyGene.info API](http://mygene.info)
..* UCSC
..* CPDB
..* ExAC
..* Refseq
..* NetAffx
..* Ensembl
..* Entrez
..* Pharmgkb

2. [MyVariant.info API](http://myvariant.info)
..* ExAC
..* CADD
..* ClinVar
..* Cosmic
..* dbSNP
..* dbNSFP
..* EMV
..* EVS
..* GRASP
..* SnpEff
..* geno2mp

3. [Drug and Compound API](http://c.biothings.io)
..* aelous
..* chebi
..* chembl
..* drugbank
..* ginas
..* ndc
..* pharmgkb
..* pubchem
..* sider
..* unii
4. [Reactome API](http://reactome.org/ContentService/)
5. [Lynx API](http://lynx.ci.uchicago.edu/webservices.html)
6. [DGIdb API](http://dgidb.genome.wustl.edu/api)
..* CIViC
..* CancerCommons
..* ChEMBL
..* ClearityFoundationBiomarkers
..* ClearityFoundationClinicalTrial
..* DoCM
..* DrugBank
..* GuideToPharmacologyInteractions
..* MyCancerGenomeMyCancerGenomeClinicalTrial
..* PharmGKB
..* TALC
..* TEND
..* TTD
..* TdgClinicalTrial
7. [openFDA API](https://open.fda.gov/api/)
8. [Pharos API](https://pharos.nih.gov/idg/api)
9. [monarch-initiative API](https://api.monarchinitiative.org/api/)

## Requirements
1. Python >= 2.6 (including python 3)
2. [requests](https://pypi.python.org/pypi/requests) (install using "pip install requests")
3. [pyld](https://pypi.python.org/pypi/PyLD/0.7.2) (install using "pip install PyLD")
4. [biothings_client](https://pypi.python.org/pypi/biothings-client/0.1.1) (install using "pip install biothings_client")
