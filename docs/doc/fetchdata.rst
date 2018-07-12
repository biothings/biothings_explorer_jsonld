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