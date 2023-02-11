# Dijkstra
import heapq
import networkx as nx


def dijkstra(G: nx.Graph(), root_id):
    edges = G.edges
    blue_nodes = [n for n in G.nodes].remove(root_id)
    oragne_nodes = root_id
    yellow_edges = []
    red_edges = []

    unknow_nodes = [n for n in G.nodes]
    unknow_nodes.remove(root_id)
    phase = 1

    while unknow_nodes:
        # send join

        print(G.neighbors(root_id))
        print([n for n in G.neighbors(root_id)])
        print([n for n in G.edges(root_id)])
        
        unknow_nodes.pop()

        phase += 1



