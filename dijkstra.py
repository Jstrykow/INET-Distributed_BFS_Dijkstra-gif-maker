# Dijkstra
import networkx as nx
import utils


def dijkstra(G: nx.Graph(), root_id):
    edges = G.edges
    nodes = [n for n in G.nodes]
    oragne_nodes = [root_id]
    yellow_edges = []
    red_edges = []

    unknow_nodes = [n for n in G.nodes]
    unknow_nodes.remove(root_id)
    print(unknow_nodes)
    phase = 1
    current_node = root_id

    # nodes edges in ith phase
    nodes_in_phase = {1: [n for n in G.neighbors(root_id)]}
    edges_in_phase = {1: [n for n in G.edges(root_id)]}

    oragne_nodes = nodes.copy()
    for n in unknow_nodes:
        oragne_nodes.remove(n)
        
    #oragne_nodes.remove(unknow_nodes)

    utils.draw_graph(
                G,
                blue_nodes= unknow_nodes,
                oragne_nodes= oragne_nodes,
                yellow_edges=yellow_edges,
                red_edges=red_edges
            )
    while phase<2:
        # send join
        yellow_edges = G.edges(current_node)
        """
        utils.draw_graph(
            G,
            blue_nodes= blue_nodes,
            oragne_nodes= oragne_nodes,
            yellow_edges=yellow_edges,
            red_edges=red_edges
        )
        """
        #print(G.neighbors(root_id))
        #print([n for n in G.neighbors(root_id)])
        #print([n for n in G.edges(root_id)])
        #unknow_nodes.pop()
        phase += 1



