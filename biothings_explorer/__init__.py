import tabulate
import networkx as nx

from api_call_handler import ApiCallHandler
from visjupyter_helper import find_edge_label

class BioThingsExplorer:
    def __init__(self, loadroadmap=True):
        self.graph_id = 1
        self.apiCallHandler = ApiCallHandler()
        self.registry = self.apiCallHandler.registry
        self.api_map = nx.MultiDiGraph()
        self.temp_G = nx.MultiDiGraph()
        self.graph_id = 0
        if loadroadmap:
            self.construct_api_road_map()

    def show_available_bioentities(self):
        """
        This function displays available IDs in Jupyter Notebook in Tabel format
        The columns of the table includes Preferred Name, URI, description, Identifier Pattern and Type
        Each row represents one bioentity ID in the registry

        Return
        ======
        Table in Jupyter Notebook Cell
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

        Return
        ======
        MultiDiGraph
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

        Return
        ======
        VisJupyter Graph
        """
        if not self.api_map.nodes():
            print('Please call construct_api_road_map function first!')
            return
        self.graph_id += 1
        return draw_graph(self.api_map, graph_id=self.graph_id)

    def path_conversion(self, pathList, relation_filter=None):
        """
        converted path from list to dict
        Example: [1, 2, 3, 4, 5] ==> [{'input': 1, 'endpoint': 2, 'output': 3, relation: '...'},
                                      {'input': 3, 'endpoint': 4, 'output': 5, relation: '...'}]

        Params
        ======
        pathList: (list)
            A list containing one path from start to end
        relation_filter: (str)
            user specified edge label
        """
        pathDict = []
        for i in range(0, len(pathList), 2):
            list2dict = {'input': pathList[i], 'endpoint': pathList[i+1], 
                         'output': pathList[i+2]}
            list2dict.update({'relation': find_edge_label(self.api_map, pathList[i+1], pathList[i+2], relation_filter)})
            path_conversion.append(list2dict)

    def find_path(self, start, end, max_no_api_used=4, intermediate_nodes=[], excluded_nodes=[], relation_filter=None, dictformat=False):
        """
        return paths connecting start and end bio-entity specified

        Params
        ======
        start: (str)
            path start point
        end: (str)
            path end point
        max_no_api_used: (int)
            maximum number of api(s) included in the path
        intermediate_nodes: (list)
            node(s) which the path must contain
        excluded_nodes: (list)
            node(s) which the path must not contain
        
        TODO: include relation_filter
        Return
        ======
        list of paths, each path is a list containing the nodes
        """
        cutoff = max_no_api_used * 2 + 1
        if cutoff < 1:
            print('please specify max_no_api_used with a number >= 1')
            return
        if start not in self.api_map.nodes() or end not in self.api_map.nodes():
            print('the start and end position is not in the api_map')
            return
        visited = [start]
        stack = [self.api_map.successors_iter(start)]
        paths = []
        final_results = []
        while stack:
            children = stack[-1]
            child = next(children, None)
            if child is None:
                stack.pop()
                visited.pop()
            elif len(visited) < cutoff:
                if child == end:
                    new_path = visited + [end]
                    if new_path not in paths:
                        paths.append(visited + [end])
                elif child not in visited:
                    visited.append(child)
                    stack.append(self.api_map.successors_iter(child))
            else: #len(visited) == cutoff:
                if child == end or end in children:
                    new_path = visited + [end]
                    if new_path not in paths:
                        paths.append(visited + [end])
                stack.pop()
                visited.pop()
        for _path in paths:
            # user specify both excluded_nodes and intermediate_nodes
            if excluded_nodes and intermediate_nodes and len(set(excluded_nodes) - set(_path))==len(excluded_nodes) and not set(intermediate_nodes) - set(_path):
                final_results.append(_path)
            # user only specify excluded_nodes
            elif excluded_nodes and len(set(excluded_nodes) - set(_path)) == len(excluded_nodes) and not intermediate_nodes:
                final_results.append(_path)
            # user only specify intermediate nodes
            elif intermediate_nodes and not set(intermediate_nodes) - set(_path) and not excluded_nodes:
                final_results.append(_path)
            # user specify neither excluded_nodes nor intermediate_nodes
            elif not intermediate_nodes and not excluded_nodes:
                final_results.append(_path)
            else:
                continue
        if not dictformat:
            return final_results
        else:
            dict_results = [self.path_conversion(_path, relation_filter) for _path in final_results]
            return dict_results


