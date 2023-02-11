# Dijkstra
import networkx as nx
import utils


def dijkstra(G: nx.Graph(), root_id):
    edges = [n for n in G.edges]
    nodes = [n for n in G.nodes]
    oragne_nodes = [root_id]
    orange_edges = []
    orange_nodes = []
    red_edges = []
    BFS = []
    know_edges = []

    know_nodes = [root_id]
    
    #unknow_nodes = [n for n in G.nodes]
    #unknow_nodes.remove(root_id)

    #unknow_edges = edges.copy()
    phase = 1
    current_node = root_id

    # def
    utils.draw_graph(G, blue_nodes=G.nodes, green_nodes=know_nodes, orange_edges=orange_edges, green_edges=BFS,red_edges=red_edges, orange_nodes=orange_nodes)


    # broadcast p
    orange_nodes= [n for n in G.neighbors(root_id)]
    orange_edges= [n for n in G.edges(root_id)]
    nodes_in_phase = {phase: orange_nodes.copy()}
    edges_in_phase = {phase: orange_edges.copy()}
    utils.draw_graph(G, blue_nodes=G.nodes, green_nodes=know_nodes, orange_edges=orange_edges, green_edges=BFS,red_edges=red_edges, orange_nodes=orange_nodes)

    # ack first edges all add to BFS
    BFS = edges_in_phase[phase].copy()
    know_nodes+= orange_nodes
    know_edges+= orange_edges
    #for e in know_edges:
    #   remove_edge(e, unknow_edges)

    #utils.draw_graph(G, blue_nodes=unknow_nodes, green_nodes=know_nodes, orange_edges=orange_edges, green_edges=BFS,red_edges=red_edges, orange_nodes=orange_nodes)

    while len(orange_nodes) != 0:
        know_nodes += orange_nodes
        know_edges += orange_edges
        orange_edges = []
        orange_nodes = []
        red_edges = []
        # draw BFS
        utils.draw_graph(G, blue_nodes=G.nodes, green_nodes=know_nodes, orange_edges=[], green_edges=BFS, red_edges=red_edges, orange_nodes=[])
       
        for current_node in nodes_in_phase[phase]:
            for e in G.edges(current_node):
                if e not in know_edges and (e[1], e[0]) not in know_edges:
                    orange_edges.append(e)
            for n in G.neighbors(current_node):
                if n not in know_nodes:
                    orange_nodes.append(n)
        orange_nodes = list(dict.fromkeys(orange_nodes))
        orange_edges = list(dict.fromkeys(orange_edges))
        nodes_in_phase = {phase+1: orange_nodes}
        edges_in_phase = {phase+1: orange_edges}
        
        #draw sending ACK
        #utils.draw_graph(G, blue_nodes=G.nodes, green_nodes=know_nodes, orange_edges=orange_edges,green_edges=BFS, red_edges=red_edges, orange_nodes=orange_nodes)
        
        for e in orange_edges:
            if e[0] and e[1] in know_nodes:
                red_edges.append(e)
                #remove_edge(e, unknow_edges)
            else:
                BFS.append(e)
                know_nodes.append(e[0])
                know_nodes.append(e[1])
                know_nodes = list(dict.fromkeys(know_nodes))
                #remove_edge(e, unknow_edges)
        #draw sending ACK with red
        utils.draw_graph(G, blue_nodes=G.nodes, green_nodes=know_nodes, orange_edges=orange_edges, green_edges=[], red_edges=red_edges, orange_nodes=orange_nodes)
        
        phase+= 1
    print(edges_in_phase, nodes_in_phase)
    
def remove_edge(edge, edges):
    try:
        if edge in edges:
            edges.remove(edge)
        else:
            edges.remove((edge[1], edge[0]))
        return edges
    except:
        pass

def sort_tuple_list(tuple_list):
    sorted_tuple_list = []
    for n in tuple_list:
        sorted_tuple_list.append(sorted(n))
    return sort_tuple_list