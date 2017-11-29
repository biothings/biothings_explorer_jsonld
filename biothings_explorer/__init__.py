import tabulate
import networkx as nx

from api_call_handler import ApiCallHandler

class BioThingsExplorer:
    def __init__(self, loadroadmap=True):
        self.graph_id = 1
        self.apiCallHandler = ApiCallHandler()
        self.registry = self.apiCallHandler.registry
        self.api_map = nx.MultiGraph()
        self.temp_G = nx.MultiGraph()
        self.graph_id = 0
        if loadroadmap:
            self.construct_api_road_map()

    def show_available_bioentities(self):
        """
        This function displays available IDs in Jupyter Notebook in Tabel format
        The columns of the table includes Preferred Name, URI, description, Identifier Pattern and Type
        Each row represents one bioentity ID in the registry
        """
        table = [['Preferred Name', 'URI', 'Description', 'Identifier pattern', 'Type']]
        for uri, info in self.api_handler.bioentity_info.items():
            table.append([info['preferred_name'], uri, info['description'], info['identifier_pattern'], info['type']])
        return display(HTML(tabulate.tabulate(table, tablefmt='html')))

    def construct_api_road_map(self):
        """
        This function will add all API, endpoint, input/output info
        as well as the relationship between endpoint and output
        into the networkx MultiGraph.
        """
        # add nodes and edges between api and endpoints
        for _api, _info in self.registry.api_info.items():
            self.api_map.add_node(_api, type='api', color='red')
            for _endpoint in _info['endpoints']:
                self.api_map.add_node(_endpoint, type='endpoint', color='blue')
                self.api_map.add_edge(_endpoint, _api, label='has_endpoint')
        # add endpoint and input/output to the graph
        for _endpoint, _info in self.registry.endpoint_info.items():
            for _input in _info['input']:
                preferred_name = self.registry.bioentity_info[_input]['preferred_name']
                self.api_map.add_node(preferred_name, type='bioentity', color='yellow')
                self.api_map.add_edge(_endpoint, preferred_name, label='has_input')
            for _output in _info['output']:
                preferred_name = self.registry.bioentity_info[_output]['preferred_name']
                self.api_map.add_node(preferred_name, type='bioentity', color='yellow')
                relations = _info['relation'][_output]
                for _relation in relations:
                    self.api_map.add_edge(preferred_name, _endpoint, label=_relation)
        return self.api_map

    def draw_api_road_map(self):
        """
        This function displays the api road map in the jupyter notebook cell block
        """
        if not self.api_map.nodes():
            print('Please call construct_api_road_map function first!')
            return
        return draw_graph(self.api_map, graph_id=self.graph_id = self.graph_id + 1)

