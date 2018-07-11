.. biothings_explorer documentation master file, created by
   sphinx-quickstart on Mon Jul  9 15:02:17 2018.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Documentation for BioThings Explorer
====================================

Introduction
------------
`BioThings Explorer <http://biothings.io/explorer>`_ integrates a variety of biomedical API resources and make them available through a central access point. By addressing the data interoperability issue across different APIs through `SmartAPI <http://smart-api.info/>`_ and `JSON-LD <https://json-ld.org/>`_ technologies, BioThings Explorer allows users to perform federated queries across multiple different databases as well as conduct linked biomedical knowledge discovery, e.g. find all **drugs** which interacts with **proteins** produces by **genes** involved in a specific **biological pathway**.

Documentation
-------------

The main documentation of this site could be organized into the following sections.

.. toctree::
   :maxdepth: 2

   doc/metadata

   
Requirements
============
    python >=2.6 (including python3)

    requests (install using "pip install requests")

Installation
=============

Either install from source, like:

.. code-block:: bash
    
    git clone https://github.com/biothings/biothings.api.git
    cd biothings.api
    python setup.py install

or use pip, like:

.. code-block:: bash

    pip install biothings

or directly from our repository, like:

.. code-block:: bash

    pip install git+https://github.com/biothings/biothings.api.git#egg=biothings




How to cite
===========
`Our paper on JSONLD <https://bmcbioinformatics.biomedcentral.com/articles/10.1186/s12859-018-2041-5>`_

Related Links
=============
* `BioThings Explorer Web Interface <http://biothings.io/explorer>`_
* `BioThings Explorer Web Github <https://github.com/biothings/biothings_explorer_web>`_
* `BioThings Explorer Python Client Github <https://github.com/biothings/biothings_explorer>`_
* `SmartAPI <http://smart-api.info/>`_
* `JSON-LD <https://json-ld.org/>`_

