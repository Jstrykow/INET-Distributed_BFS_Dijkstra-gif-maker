# https://towardsdatascience.com/basics-of-gifs-with-pythons-matplotlib-54dd544b6f30
# https://networkx.org/documentation/stable/reference/classes/graph.html

import networkx as nx
import matplotlib.pyplot as plt
import imageio # gifs   


# undirected graph
g = nx.Graph()

# to-do add reading from file
nodes = [1, 2, 3, 4, 5]
edges = [(1, 2), (2, 4), (3, 5), (2,3), (4,5), (2,5)]

# add node coloring
# add algorithms, which would color nodes
# delete or replace img after changing color; maybe a function

# names of files
filenames = []
directory = "img/"

g.add_nodes_from([1,2,3,4,5])

#g.add_edges_from(edges)
# in case
# G.add_edges_from(H.edges) collection of edges 

for i, edge in enumerate(edges):
    #print(edge)
    g.add_edge(edge[0], edge[1])
    nx.draw(g,with_labels=True)
    plt.draw()
    
    # set name of file
    filename = f'{directory + str(i)}.png'
    filenames.append(filename)
    # save frame
    plt.savefig(filename)
    plt.close() 

    # build gif
    with imageio.get_writer('graph-as-gif.gif', mode='I',  fps=1) as writer:
        for filename in filenames:
            image = imageio.imread(filename)
            writer.append_data(image)