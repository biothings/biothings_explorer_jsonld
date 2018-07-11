.. metadata

Integrated API Resources and Data Types
***************************************

.. _api_resources:

API Resources
-------------

The amount of publically available biomedical data is growing at a tremendous pace. Meanwhile, RESTful APIs has become a popular way for data providers as well as data curators to distribute their data for public access. However, all these APIs and the biological knowledge underneath them are fundamentally unconnected. By solving the interoperability issue across different APIs, BioThings Explorer manages to stitch together individual APIs and build them into a network of linked web services. The following table list current public API resources which has been integrated by BioThings Explorer. 

================    =======================================      ================================================
API                 URL                                          Description
================    =======================================      ================================================
MyGene.info         http://mygene.info                           Gene Annotation Service
MyChem.info         http://mychem.info                           Drug/Chemical Annotation Service
MyDisease.info      http://mydisease.info                        Disease Annotation Service
Reactome            https://reactome.org                         Pathway Analysis Service
DGIdb               http://dgidb.org                             Drug Gene Interaction Database
BioLink             https://api.monarchinitiative.org/api/       Linked Biological Knowledge
Disease Ontology    http://disease-ontology.org/                 Disease Ontology API Service
Pharos              https://pharos.nih.gov/idg/index             Drug Gene Disease Interaction 
EBI OLS             https://www.ebi.ac.uk/ols/index              Ontology Lookup Service
ChEMBL              https://www.ebi.ac.uk/chembl/                Database of Bioactive Drug-Like Small Molecules
PubChem             https://pubchem.ncbi.nlm.nih.gov/            Open Chemistry Database 
Taxonomy            https://t.biothings.io                       Taxonomy Annotation Service
HGNC                https://www.genenames.org/                   Curated online Repo Gene Nomenclature
================    =======================================      ================================================

.. note::

	If you are interested in integrating your own/interested API resource in BioThings Explorer, you could visit `SmartAPI Website <http://smart-api.info/>`_ to create a SmartAPI specification for your API. You could also place an issue at `BioThings Explorer Github Repo <https://github.com/biothings/biothings_explorer/issues>`_ to let us know.

To retrieve all integrated APIs in BioThings Explorer using the pyton client:

.. code-block:: python

    In [1]: from biothings_explorer import MetaData

    In [2]: metadata = MetaData()

    In [3]: print(metadata.list_all_api_resources())

.. _uri_prefix:

URIs and Prefixes
-----------------

Uniform Resource Identifiers (URIs) is a string of characters designed for unambiguous identification of resources. URIs are used in BioThings Explorer to uniquely identify a biological entity. For example, ncbigene ids is represented by http://identifiers.org/ncbigene/ as its unique identifier. Identifiers.org provides stable, persistent and resolvable URIs for the identification of life science data, and is chosen as the default URI repository in the implementation of BioThings Explorer. Meanwhile, there are also cases where existing URIs could not be found in existing URI repos. In this case, we will create a temporary URI for it.
Prefix is essentially a short form of URI. Every URI has its corresponding prefix. Users of BioThings Explorer could use prefixes to navigate through the service. 

To retrieve all prefixes used in BioThings Explorer using the pyton client:

.. code-block:: python

    In [1]: from biothings_explorer import MetaData

    In [2]: metadata = MetaData()

    In [3]: print(metadata.list_all_prefixes())

.. _semantic_type:

Semantic Types
--------------
Every URI/prefix used within BioThings Explorer is associated with a specific semantic type, e.g. gene, variant, chemical, etc. By implementing this feature, users can easily find the right API to use based on the scenario. 

To retrieve all prefixes used in BioThings Explorer using the pyton client:

.. code-block:: python

    In [1]: from biothings_explorer import MetaData

    In [2]: metadata = MetaData()

    In [3]: print(metadata.list_all_semantic_types())

.. _predicate:

Predicates
----------
Predicate specifies the relationship between the input and the output. Users could use predicate to filter the results from BioThings Explorer. For example, the predicate between a drug and a gene/protein could be inhibit, block, agnoize, etc..

To retrieve all predicates used in BioThings Explorer using the pyton client:

.. code-block:: python

    In [1]: from biothings_explorer import MetaData

    In [2]: metadata = MetaData()

    In [3]: print(metadata.list_all_predicates())
