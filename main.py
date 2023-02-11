from utils import draw_graph, define_graph
from dijkstra import dijkstra

nodes = [1, 2, 3, 4, 5, 6, 7, 8, 9]
root_id = 1
blue_nodes = nodes.remove(root_id)
oragne_nodes = [root_id]
yellow_edges = [(1,2)]
red_edges = [(1,3)]

edges = [(1, 2), (1,3), (1,4), (2, 5), (3, 5), (5, 7), (3, 7), (4, 6), (3,6), (2,3), (7,8), (7,9), (5,9), (8,9)]

G = define_graph(
    nodes = nodes, edges=edges
    )

#draw_graph(G,blue_nodes = blue_nodes,oragne_nodes= oragne_nodes, yellow_edges=yellow_edges,red_edges=red_edges)


dijkstra(G, root_id=root_id)

# trzeba przebudowac drow graph bo botrzebujem logiki zniego 

