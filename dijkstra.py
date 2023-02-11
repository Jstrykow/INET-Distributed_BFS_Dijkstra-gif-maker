# Dijkstra
import networkx as nx
import utils


def dijkstra(G: nx.Graph(), root_id):
    edges = [n for n in G.edges]
    nodes = [n for n in G.nodes]
    oragne_nodes = [root_id]
    yellow_edges = []
    yellow_nodes = []
    red_edges = []
    BFS = []
    know_edges = []

    know_nodes = [root_id]
    unknow_nodes = [n for n in G.nodes]
    unknow_nodes.remove(root_id)

    unknow_edges = edges.copy()
    phase = 1
    current_node = root_id

    # nodes edges in ith phase
    nodes_in_phase = {1: [n for n in G.neighbors(root_id)]}
    edges_in_phase = {1: [n for n in G.edges(root_id)]}

    # broadcast p
    oragne_nodes = nodes.copy()
    for n in unknow_nodes:
        oragne_nodes.remove(n)
    yellow_edges=edges_in_phase[phase].copy()
    utils.draw_graph( G, blue_nodes=unknow_nodes, oragne_nodes=oragne_nodes, yellow_edges=yellow_edges, green_edges=BFS,red_edges=red_edges)

    # ack first edges all add to BFS
    BFS = edges_in_phase[phase].copy()
    know_edges+=yellow_edges
    for e in yellow_edges:
        unknow_edges = remove_edge(e,unknow_edges)
    yellow_edges = []
    know_nodes+=nodes_in_phase[phase]

    utils.draw_graph( G,blue_nodes=unknow_nodes,oragne_nodes=know_nodes, yellow_edges=yellow_edges,green_edges=BFS,red_edges=red_edges)

    while phase<3:
        print(know_nodes)
        print(know_edges)
        for current_node in nodes_in_phase[phase]:
            for e in G.edges(current_node):
                if e in unknow_edges:
                    yellow_edges.append(e)
            for n in G.neighbors(current_node):
                if n in unknow_nodes:
                    yellow_nodes.append(n)
        yellow_nodes = list(dict.fromkeys(yellow_nodes))
        yellow_edges = list(dict.fromkeys(yellow_edges))
        utils.draw_graph( G,blue_nodes=unknow_nodes,oragne_nodes=know_nodes, yellow_edges=yellow_edges,green_edges=BFS,red_edges=red_edges)
        edges_in_phase = {phase+1: yellow_edges}
        yellow_edges = []

        phase+=1


def remove_edge(edge, edges):
    if edge in edges:
            edges.remove(edge)
    else:
        edges.remove((edge[1], edge[0]))
    return edges