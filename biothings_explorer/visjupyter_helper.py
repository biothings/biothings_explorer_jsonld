import visJS2jupyter.visJS_module
import matplotlib as mpl
import networkx as nx

def draw_graph(G, graph_id=1):
    """
    Given a networkx multiDiGraph, 
    Display it on the jupyter notebook cell block
    using visJS2jupyter

    params
    ======
    G: (networkx MultiDigraph)
        a networkx graph consisting of nodes, edges
    graph_id: (int)
        for displaying multiple graphs in the same jupyter notebook,
        should increase one when a new graph is added
    """
    degree = {}
    for _node in G.nodes():
        degree.update({_node: 1})
    bc = nx.betweenness_centrality(G)
    nx.set_node_attributes(G, name = 'degree', values = degree)
    nx.set_node_attributes(G, name = 'betweenness_centrality', values = bc)
    pos = nx.circular_layout(G)
    nodes_dict = [{"id": n, "color": G.node[n]['color'], "degree": nx.degree(G, n), "x": pos[n][0]*1000, "y": pos[n][0]*1000} for n in G.nodes()]
    edges = []
    for _edge in set(G.edges()):
        labels = G.edge[_edge[0]][_edge[1]].values()
        for _label in labels:
            edges.append((_edge[0], _edge[1], _label['label']))
    node_map = dict(zip(G.nodes(), range(len(G.nodes()))))  # map to indices for source/target in edges
    edges = G.edges(keys=True)
    edges_dict = [{"source": node_map[edges[i][0]], "target": node_map[edges[i][1]],
                  "color": "pink", "id": G.edge[edges[i][0]][edges[i][1]][edges[i][2]]['label']} for i in range(len(edges))]
    return visJS2jupyter.visJS_module.visjs_network(nodes_dict,edges_dict,
                                                      node_size_multiplier=3,
                                                      node_size_transform = '',
                                                      node_color_highlight_border='red',
                                                      node_color_highlight_background='#D3918B',
                                                      node_color_hover_border='blue',
                                                      node_color_hover_background='#8BADD3',
                                                      node_font_size=25,
                                                      edge_arrow_to=True,
                                                      physics_enabled=True,
                                                      edge_color_highlight='#8A324E',
                                                      edge_color_hover='#8BADD3',
                                                      edge_width=3,
                                                      max_velocity=15,
                                                      min_velocity=1,
                                                      edge_smooth_enabled = True)
