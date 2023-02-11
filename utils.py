# https://towardsdatascience.com/basics-of-gifs-with-pythons-matplotlib-54dd544b6f30
# https://networkx.org/documentation/stable/reference/classes/graph.html


import matplotlib.pyplot as plt
import imageio.v2 as imageio # gifs
import networkx as nx

# to-do add reading from file
# add algorithms, which would color nodes
# delete or replace img after changing color; maybe a function

# dodac zmiane nazwy 
def define_graph(nodes, edges):
    # undirected graph
    G = nx.Graph()
    G.add_nodes_from(nodes)
    G.add_edges_from(edges)
    return G

def draw_graph(G : nx.Graph(), blue_nodes, green_nodes, orange_nodes, orange_edges, red_edges, green_edges):
    pos = nx.spring_layout(G, seed=100)  # positions for all nodes - seed for reproducibility
   
    # nodes
    nx.draw_networkx_nodes(G, pos,nodelist=blue_nodes, node_color="tab:blue", node_size=700)
    nx.draw_networkx_nodes(G, pos,nodelist=orange_nodes, node_color="tab:orange", node_size=700)
    nx.draw_networkx_nodes(G, pos,nodelist=green_nodes, node_color="tab:green", node_size=700)
     
    # edges
    nx.draw_networkx_edges(G, pos, edgelist=G.edges(data=True), width=4)
    nx.draw_networkx_edges(G, pos, edgelist=green_edges, edge_color="green", width=4)
    nx.draw_networkx_edges(G, pos, edgelist=orange_edges, edge_color="orange", width=4)
    nx.draw_networkx_edges(G, pos, edgelist=red_edges, edge_color="red", width=4)
    nx.draw_networkx_labels(G, pos, font_size=20, font_color="whitesmoke", font_family="sans-serif")
    # edge weight labels
    #edge_labels = nx.get_edge_attributes(G, "weight")
    #nx.draw_networkx_edge_labels(G, pos, edge_labels)

    ax = plt.gca()
    ax.margins(0.08)
    plt.axis("off")
    plt.tight_layout()
    plt.show()



"""
# names of files
filenames = []
directory = "img/"

plt.draw()
plt.savefig("test.png")
plt.close() 
"""
"""
for i, edge in enumerate(edges):
    #print(edge)
    g.add_edge(edge[0], edge[1])
    nx.draw(g,with_labels=True)
    plt.draw()
# set name of file
filename = f'{directory + str(i)}.png'
filenames.append(filename)
# save frame
# build gif
with imageio.get_writer('graph-as-gif.gif', mode='I',  fps=1) as writer:
    for filename in filenames:
        image = imageio.imread(filename)
        writer.append_data(image)
"""