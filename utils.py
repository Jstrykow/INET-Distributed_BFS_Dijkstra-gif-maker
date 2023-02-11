# https://towardsdatascience.com/basics-of-gifs-with-pythons-matplotlib-54dd544b6f30
# https://networkx.org/documentation/stable/reference/classes/graph.html


import matplotlib.pyplot as plt
import imageio.v2 as imageio # gifs
import networkx as nx
import os
import globals


ColorLegend = {'No used': 1,'ACK': 2, 'No-ACK': 4, 'Tree': 3}

# dodac zmiane nazwy 
def define_graph(nodes, edges):
    # undirected graph
    G = nx.Graph()
    G.add_nodes_from(nodes)
    G.add_edges_from(edges)
    return G

def draw_graph(G : nx.Graph(), blue_nodes, green_nodes, orange_nodes, orange_edges, red_edges, green_edges):
    pos = nx.spring_layout(G, seed=globals.SEED)  # positions for all nodes - seed for reproducibility
   
    # nodes
    nx.draw_networkx_nodes(G, pos,nodelist=blue_nodes, node_color="tab:blue", node_size=700)
    nx.draw_networkx_nodes(G, pos,nodelist=green_nodes, node_color="tab:green", node_size=700)
    nx.draw_networkx_nodes(G, pos,nodelist=orange_nodes, node_color="tab:orange", node_size=700)
    
    # edges
    nx.draw_networkx_edges(G, pos, edgelist=G.edges(data=True), width=4)
    nx.draw_networkx_edges(G, pos, edgelist=green_edges, edge_color="green", width=4)
    nx.draw_networkx_edges(G, pos, edgelist=orange_edges, edge_color="orange", label="ACK", width=4)
    nx.draw_networkx_edges(G, pos, edgelist=red_edges, edge_color="red", label="NACK", width=4)
    nx.draw_networkx_labels(G, pos, font_size=20, font_color="whitesmoke", font_family="sans-serif")
    # show
    ax = plt.gca()
    ax.margins(0.08)
    plt.axis("off")
    #plt.tight_layout()   
    plt.title("Distributed BFS: Dijkstra Flavor", weight="bold", size='x-large')
    plt.text(0.9, 0.9, 'ACK', horizontalalignment='center', verticalalignment='center', transform=ax.transAxes, c="orange", animated=True, size='x-large', weight="bold")
    plt.text(0.9, 0.85, 'No-ACK', horizontalalignment='center', verticalalignment='center', transform=ax.transAxes, c="red", animated=True, size='x-large', weight="bold")
    plt.text(0.9, 0.80, 'In-Tree', horizontalalignment='center', verticalalignment='center', transform=ax.transAxes, c="green", animated=True, size='x-large', weight="bold")
    plt.text(0.9, 0.75, 'No-use', horizontalalignment='center', verticalalignment='center', transform=ax.transAxes, c="black", animated=True, size='x-large', weight="bold")
    #plt.show()
    # set name of file
    filename = f'{globals.DIRECTORY +  str(len(os.listdir(globals.DIRECTORY)))}.png'
    plt.draw()
    
    plt.savefig(filename)
    plt.close()
    #make_gif(filenames=filenames)
    # save frame
    # build gif

def make_gif():
    with imageio.get_writer('Distributed_BFS_Dijkstra.gif', mode='I',  fps=1) as writer:
        fi = []
        for f in os.listdir(globals.DIRECTORY):
            fi.append(f)
        for f in fi:
            image = imageio.imread(globals.DIRECTORY + f)
            writer.append_data(image)
    

def clear_folder(d):
    for f in os.listdir(d):
        if not f.endswith(".png"):
            continue
        os.remove(os.path.join(d, f))
    