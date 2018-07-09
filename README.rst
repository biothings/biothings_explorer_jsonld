# biothings_explorer.py
Python Client for BioThings Explorer

[BioThings Explorer](http://biothings.io/explorer/) is a service to provide central access to multiple biological Application Programming Interfaces (APIs). This repo wraps major functions provided by BioThings Explorer API and make them easily accessible through the Python client.

Intro
=====

[BioThings Explorer](http://biothings.io/explorer/) is a service to provide central access to multiple biological Application Programming Interfaces (APIs). And *biothings_explorer.py* is an easy-to-use Python wrapper for the service.  Currently, the following APIs are available for data access in BioThings Explorer:

    * MyGene.info API - Provide access to gene annotations.
    * MyChem.info API - Provide access to chemical annotations.
    * MyDisease.info API - Provide access to disease annotations.
    * DGIdb API - Database for Drug-Gene interactions.
    * ChEMBL API - Database of bioactive drug-like small molecules.
    * Pharos API - Provide access to gene annotations.
    * Disease Ontology API - Provide standard ontology for human disease.
    * Reactome API - Pathway database which provides intuitive bioinformatics tools for the interpretation and analysis of pathway knowledge.
    * PubChem API - Database of chemical molecules and their activities against biological assays
    * HGNC API - A curated online repository of HGNC-approved gene nomenclature, gene families and associated resources.
    * EBI Ontology API - A repository of bio-medical ontologies.
    * BioLink API - API for linked biological knowledge.


Requirements
============
    python >=2.6 (including python3)

    requests_ (install using "pip install requests")