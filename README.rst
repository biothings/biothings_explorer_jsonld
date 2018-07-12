.. biothings_explorer documentation master file, created by
   sphinx-quickstart on Mon Jul  9 15:02:17 2018.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Documentation for BioThings Explorer
====================================

Introduction
------------
`BioThings Explorer <http://biothings.io/explorer>`_ integrates a variety of biomedical API resources and make them available through a central access point. By addressing the data interoperability issue across different APIs through `SmartAPI <http://smart-api.info/>`_ and `JSON-LD <https://json-ld.org/>`_ technologies, BioThings Explorer allows users to perform federated queries across multiple different databases as well as conduct linked biomedical knowledge discovery, e.g. find all **drugs** which interacts with **proteins** produces by **genes** involved in a specific **biological pathway**.

User's Guide
-------------

The main documentation of this site could be organized into the following sections.

.. fetchdata

Locate API Resource
*******************

.. _find_by_semantic_type:

Locate APIs Based on Semantic Types
-----------------------------------

Consider a real use case here: a biologist would like to find information about all **drugs** which might *target* a specific **protein**. You could find all API endpoints which can connect
from gene to drug using the BioThings Explorer pyton client:

.. code-block:: python

    In [1]: from biothings_explorer import APILocator

    In [2]: locator = APILocator()

    In [3]: print(locator.locate_apis_by_input_output_semantic_types(input_semantic_type='gene', output_semantic_type='chemical'))

Here is an example of the output:

.. code-block:: json

    [{
      "endpoint": "https://pharos.nih.gov/idg/api/v1/targets({geneid})", 
      "predicate": "GeneOrGeneProductToChemicalAssociation", 
      "object": {
        "semantic_type": "chemical", 
        "prefix": "pharos.ligand"
        }, 
      "subject": {
        "semantic_type": "gene", 
        "prefix": "pharos.target"
        }
     }, 
     {
      "endpoint": "http://dgidb.genome.wustl.edu/api/v2/interactions.json?genes={genesymbol}", 
      "predicate": "GeneOrGeneProductToChemicalAssociation", 
      "object": {
        "semantic_type": "chemical", 
        "prefix": "chembl.compound"
        }, 
      "subject": {
        "semantic_type": "gene", 
        "prefix": "hgnc.symbol"
        }
     }, 
     {
      "endpoint": "http://MyChem.info/v1/querybydrugtarget", 
      "predicate": "GeneOrGeneProductToChemicalAssociation", 
      "object": {
        "semantic_type": "chemical", 
        "prefix": "inchikey"
        }, 
      "subject": {
        "semantic_type": "gene", 
        "prefix": "uniprot"
        }
    }]

.. hint::

  For how to access all semantic types used in BioThings Explorer, please reference: :ref:`semantic_type`

You could also use BioThings Explorer to find API endpoints which takes **gene** as *input* :

.. code-block:: python

    In [1]: from biothings_explorer import APILocator

    In [2]: locator = APILocator()

    In [3]: print(locator.locate_apis_by_input_semantic_type_only('gene'))

Or find all API endpoints which produce **drug/chemical** as *output*:

.. code-block:: python

    In [1]: from biothings_explorer import APILocator

    In [2]: locator = APILocator()

    In [3]: print(locator.locate_apis_by_output_semantic_type_only('chemical'))

.. _find_by_prefix:

Locate APIs Based on Prefixes
------------------------------

BioThings Explorer also supports finding APIs based on input/output prefixes.

For example, you could find APIs which can *connect* from **hgnc.symbol** to **chembl.compound** through the BioThings Explorer Python client.

.. code-block:: python

    In [1]: from biothings_explorer import APILocator

    In [2]: locator = APILocator()

    In [3]: print(locator.locate_apis_by_input_output_prefix(input_prefix='hgnc.symbol', output_prefix='chembl.compound'))

.. hint::

    For how to access all prefixes used in BioThings Explorer, please reference: :ref:`uri_prefix`

You could also use BioThings Explorer to find API endpoints which takes **uniprot** id as *input* :

.. code-block:: python

    In [1]: from biothings_explorer import APILocator

    In [2]: locator = APILocator()

    In [3]: print(locator.locate_apis_by_input_prefix_only(input_prefix='uniprot'))

Or find all API endpoints which produce **ncbigene** id as *output*:

.. code-block:: python

    In [1]: from biothings_explorer import APILocator

    In [2]: locator = APILocator()

    In [3]: print(locator.locate_apis_by_output_prefix_only(input_prefix='ncbigene'))


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


.. fetchdata

Fetching Data From APIs
***********************

.. _find_single_edge:

Single Edge Query
-----------------

BioThings Explorer makes it simple for users who wants to **query different databases**. All you need to do is to tell BioThings Explorer *what you have* (e.g. hgnc.symbol: CXCR4) and *what you want back* (e.g. chembl.compound). BioThings Explorer will automatically help you **locate the API(s)** which can connect from your *input* to *output* and **fetch the results** for you.

The following code retrieves all *chembl compound IDs* which are related to gene symbol *CXCR4*.

.. code-block:: python

    In [1]: from biothings_explorer_test import fetch_output

    In [2]: data = fetch_output(input_prefix='hgnc.symbol', input_value='CXCR4', output_prefix='chembl.compound')


.. _multi_edge_query:

Multi Edge Query
-----------------

When querying data from multiple different databases, one key obstacle is that databases tend to use different accession numbers. For example, some databases use ncbigene IDs to represent genes while other choose to use hgnc symbols. In this case, an additional ID Conversion step needs to be done in order to fetch the results. 

BioThings Explorer makes it easy for users since it includes functions to automatically find synonyms for common biological IDs (e.g. gene, chemical, disease identifiers). So users no longer needs to perform the ID conversion step themselves.

The following code retrieves all *chembl compound IDs* which are related to gene symbol *CXCR4* and also taking into account all the synonyms of chembl compound IDs.

.. code-block:: python

    In [1]: from biothings_explorer_test import fetch_output

    In [2]: data = fetch_output(input_prefix='hgnc.symbol', input_value='CXCR4', output_prefix='chembl.compound', enable_semantic_search=True)

.. note::

  There might be cases where synonyms could not be found. For example, disease IDs (e.g. DOID, OMIM disease ID) doesn't always have a 1-1 match. 

   
Requirements
============
    1. python >=2.6 (including python3)

    2. requests (install using "pip install requests")

Installation
=============

Either install from source, like:

.. code-block:: bash
    
    git clone https://github.com/biothings/biothings_explorer.git
    cd biothings_explorer
    python setup.py install

or use pip, like:

.. code-block:: bash

    pip install biothings_explorer

or directly from our repository, like:

.. code-block:: bash

    pip install git+https://github.com/biothings/biothings_explorer.git#egg=biothings_explorer


For Developers
---------------


.. toctree::
   :maxdepth: 2

   doc/code

How to cite
===========
`Our paper on JSON-LD <https://bmcbioinformatics.biomedcentral.com/articles/10.1186/s12859-018-2041-5>`_

Related Links
=============
* `BioThings Explorer Web Interface <http://biothings.io/explorer>`_
* `BioThings Explorer Web Github <https://github.com/biothings/biothings_explorer_web>`_
* `BioThings Explorer Python Client Github <https://github.com/biothings/biothings_explorer>`_
* `SmartAPI <http://smart-api.info/>`_
* `JSON-LD <https://json-ld.org/>`_

