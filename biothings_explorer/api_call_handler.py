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

    
