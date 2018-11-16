from __future__ import print_function

import requests

class APILocator():
    """Class for locating the right API(s) to use.

    Users could use APILocator to filter for APIs based on input and output prefixes/semantic types.
    .. note::

       `All available semantic types in BioThings Explorer<http://biothings.io/explorer/api/v2/metadata/semantic_types>`_
       `All available prefixes in BioThings Explorer<http://biothings.io/explorer/api/v2/metadata/bioentities>`_
    """
    def locate_apis_by_input_output_semantic_types(self, input_semantic_type, output_semantic_type):
        """Find API to use based on input and output semantic types

        :arg str input_semantic_type: The semantic type of the input, e.g. gene, pathway, chemical.
        :arg str output_semantic_type: The semantic type of the output, e.g. gene, pathway, chemical.
        :returns:  list -- api endpoints which can connect from input semantic type to output semantic type
        """
        response = requests.get('http://biothings.io/explorer/api/v2/knowledgemap?subject.semantic_type={{input}}&object.semantic_type={{output}}'.
                                replace("{{input}}", input_semantic_type).replace("{{output}}", output_semantic_type))

        if response.ok:
            doc = response.json()
            return doc['associations'] if doc else []
        else:
            doc = response.json()
            if 'message' in doc:
                print(doc['message'])
            return []

    def locate_apis_by_input_semantic_type_only(self, input_semantic_type):
        """Find APIs which can take the input_semantic_type

        :arg str input_semantic_type: The semantic type of the input, e.g. gene, pathway, chemical.
        :returns:  list -- api endpoints which can take the input semantic type
        """
        response = requests.get('http://biothings.io/explorer/api/v2/knowledgemap?subject.semantic_type={{input}}'.
                                replace("{{input}}", input_semantic_type))

        if response.ok:
            doc = response.json()
            return doc['associations'] if doc else []
        else:
            doc = response.json()
            if 'message' in doc:
                print(doc['message'])
            return []

    def locate_apis_by_output_semantic_type_only(self, output_semantic_type):
        """Find APIs which can produce the output semantic type

        :arg str output_prefix: The semantic type of the output, e.g. gene, pathway, chemical.
        :returns:  list -- api endpoints which can produce the output prefix
        """
        response = requests.get('http://biothings.io/explorer/api/v2/knowledgemap?object.semantic_type={{output}}'.
                                replace("{{output}}", output_semantic_type))

        if response.ok:
            doc = response.json()
            return doc['associations'] if doc else []
        else:
            doc = response.json()
            if 'message' in doc:
                print(doc['message'])
            return []

    def locate_apis_by_input_output_prefix(self, input_prefix, output_prefix):
        """Find API to use based on input and output prefixes

        :arg str input_prefix: The prefix of the input, e.g. ncbigene, hgnc.symbol.
        :arg str output_prefix: The prefix of the output, e.g. ncbigene, hgnc.symbol.
        :returns:  list -- api endpoints which can connect from input prefix to output prefix
        """
        response = requests.get('http://biothings.io/explorer/api/v2/knowledgemap?subject.prefix={{input}}&object.prefix={{output}}'.
                                replace("{{input}}", input_prefix).replace("{{output}}", output_prefix))

        if response.ok:
            doc = response.json()
            return doc['associations'] if doc else []
        else:
            doc = response.json()
            if 'message' in doc:
                print(doc['message'])
            return []

    def locate_apis_by_input_prefix_only(self, input_prefix):
        """Find APIs which can take the input_prefix

        :arg str input_prefix: The prefix of the input, e.g. ncbigene, hgnc.symbol.
        :returns:  list -- api endpoints which can take the input prefix
        """
        response = requests.get('http://biothings.io/explorer/api/v2/knowledgemap?subject.prefix={{input}}'.
                                replace("{{input}}", input_prefix))

        if response.ok:
            doc = response.json()
            return doc['associations'] if doc else []
        else:
            doc = response.json()
            if 'message' in doc:
                print(doc['message'])
            return []

    def locate_apis_by_output_prefix_only(self, output_prefix):
        """Find APIs which can produce the output_prefix

        :arg str output_prefix: The prefix of the output, e.g. ncbigene, hgnc.symbol.
        :returns:  list -- api endpoints which can produce the output prefix
        """
        response = requests.get('http://biothings.io/explorer/api/v2/knowledgemap?object.prefix={{output}}'.
                                replace("{{output}}", output_prefix))

        if response.ok:
            doc = response.json()
            return doc['associations'] if doc else []
        else:
            doc = response.json()
            if 'message' in doc:
                print(doc['message'])
            return []

    def locate_connected_apis_by_input_output_prefix(self, input_prefix, output_prefix, max_api=3):
        """Find APIs which can be chained together to connect from input prefix to output prefix

        :arg str input_prefix: The prefix of the input, e.g. ncbigene, hgnc.symbol.
        :arg str output_prefix: The prefix of the output, e.g. ncbigene, hgnc.symbol.
        :returns:  list -- api endpoints which can connect from input prefix to output prefix
        """
        response = requests.get('http://biothings.io/explorer/api/v2/findpath?start={{input}}&end={{output}}&max_api={{max_api}}'.
                                replace("{{output}}", output_prefix).replace("{{input}}", input_prefix).replace("{{max_api}}", str(max_api)))
        if response.ok:
            doc = response.json()
            return doc['paths'] if doc else []
        else:
            doc = response.json()
            if 'message' in doc:
                print(doc['message'])
            return []

class MetaData():
    """Class for accessing meta data information for BioThings Explorer.

    Meta data information includes APIs/Endpoints integrated in BioThings Explorer, prefixes as well as semantic types used in BioThings Explorer.
    """
    def list_all_api_resources(self):
        """List all APIs integrated in BioThings Explorer
        """
        response = requests.get('http://biothings.io/explorer/api/v2/metadata/apis').json()
        return response['api']

    def list_all_endpoints(self):
        """List all API endpoints integrated in BioThings Explorer
        """
        response = requests.get('http://biothings.io/explorer/api/v2/metadata/endpoints').json()
        return response['endpoint']

    def list_all_prefixes(self, group_by_semantic_type=True):
        """List all prefixes used in BioThings Explorer
        """
        response = requests.get('http://biothings.io/explorer/api/v2/metadata/bioentities').json()
        if group_by_semantic_type:
            return response['bioentity']
        else:
            prefixes = []
            for k, v in response['bioentity'].items():
                prefixes += v
            return prefixes

    def list_all_semantic_types(self):
        """List all semantic types used in BioThings Explorer
        """
        response = requests.get('http://biothings.io/explorer/api/v2/metadata/semantic_types').json()
        return response['semantic_types']

    def list_all_predicates(self):
        """List all the predicates used in BioThings Explorer
        """
        response = requests.get('http://biothings.io/explorer/api/v2/knowledgemap').json()
        return list(set([_item['predicate'] for _item in response['associations']]))

def fetch_output(input_prefix, input_value, output_prefix, enable_semantic_search=False):
    """Find APIs which can produce the output_prefix

    :arg str input_prefix: The prefix of the input, e.g. ncbigene, hgnc.symbol.
    :arg str output_prefix: The prefix of the output, e.g. ncbigene, hgnc.symbol.
    :arg str input_value: The actual value of the input
    :arg boolean enable_semantic_search:
    :returns:  list -- api endpoints which can produce the output prefix
    """
    if enable_semantic_search:
        response = requests.get('http://biothings.io/explorer/api/v2/semanticquery?input_prefix={{input}}&output_prefix={{output}}&input_value={{value}}'.
                                replace("{{input}}", input_prefix).replace("{{output}}", output_prefix).replace("{{value}}", input_value))
    else:
        response = requests.get('http://biothings.io/explorer/api/v2/directinput2output?input_prefix={{input}}&output_prefix={{output}}&input_value={{value}}'.
                                replace("{{input}}", input_prefix).replace("{{output}}", output_prefix).replace("{{value}}", input_value))
    if response.ok:
        doc = response.json()
        return doc['data'] if doc else []
    else:
        doc = response.json()
        if 'error message' in doc:
            print(doc['error message'])
        else:
            print("No results could be found for your query!")
        return []
