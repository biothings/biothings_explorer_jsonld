from api_registry_parser import RegistryParser

class ApiCallHandler:
    def __init__(self):
        """
        Handles API calls, including:
        1) Find the right API given input/output type
        2) Preprocessing Input
        3) Make API calls based on given input
        4) Extract Output from API call results
        """
        self.registry = RegistryParser(readmethod='filepath', initialize=True)

    def check_if_exists_multiple_params(self, endpoint_name):
        """
        Some API endpoints takes more than one required input
        e.g. humanbase API ('http://hb.flatironinstitute.org/api') specifies 'tissue'
        and 'geneid' as two required input parameters
        Thus, this function checks whether there exists multiple required parameters
        It returns True when there exists >1 parameters, False if only 1 parameter is required
        
        Params
        ======
        endpoint_name: (str)
            The endpoint name to check
        """
        required_paras = sum([1 for _para in self.registry.endpoint_info[endpoint_name]['get']['parameters'] if _para['required']])
        if required_paras > 1:
            return True
        else:
            return False


    def call_api(self, uri_value, endpoint_name):
        """
        construct requests params/data, based on input type and value
        only handle 'in' value which is body or query
        uri_value is a dict constituting uri:value pairs
        """
        results = {}
        # temp holder for method, should extend this function to handle 'post'
        method = 'get'
        for _para in self.registry.endpoint_info[endpoint_name][method]['parameters']:
            # handle cases where input value is part of the url
            if _para['in'] == 'path':
                endpoint_name = endpoint_name.replace('{' + _para['name'] + '}', str(uri_value[_para['x-valueType'][0]]))
            # handle cases for query
            else:
                # check whether the parameter is required
                if _para['required']:
                    # if the para has a request template, then put value into the placeholder {{input}}
                    if 'x-requestTemplate' in _para:
                        for _template in _para['x-requestTemplate']:
                            if _template['valueType'] == 'default':
                                results[_para['name']] = _template['template'].replace('{{input}}', json.dumps(list(uri_value.values())[0]))
                            elif _template['valueType'] in uri_value.keys():
                                results[_para['name']] = _template['template'].replace('{{input}}', json.dumps(uri_value[_template['valueType']]))
                    else:
                        results[_para['name']] = value
        if requests.get(endpoint_name, params=results).status_code -- 200:
            return requests.get(endpoint_name, params=results)
        else:
            print('This API call returns no results. The URI given is {}, the endpoint given is {}'.format(uri_value, endpoint_name))
            return
