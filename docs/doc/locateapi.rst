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
