from utils import draw_graph, define_graph, make_gif, clear_folder
from dijkstra import dijkstra
import globals

#delete *.png 
clear_folder(globals.DIRECTORY)

nodes = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
root_id = 5 # clear folder when changing root
edges = [(1, 2), (1,3), (1,4), (2, 5), (3, 5), (5, 7), (3, 7), (4, 6), (3,6), (2,3), (7,8), (7,9), (5,9), (8,9), (8,6), (4,10)]

G = define_graph(nodes=nodes, edges=edges)

dijkstra(G, root_id=root_id)
make_gif()
