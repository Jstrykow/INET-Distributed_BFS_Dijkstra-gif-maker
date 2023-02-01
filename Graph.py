class Node():
    def __init__(self):
        self.edges = []
        # id
        # weight
    def add_edge(self, edge):
        self.edges.append(edge)
  
    def remove_edge(self, edge):
        self.edges.remove(edge)



class Edge():
    def __init__(self):
        self.weight = None
    
    def change_edge_weight(self, weight):
        self.weight = weight


        

edge1 = Edge()
edge1.change_edge_weight(1)

edge2 = Edge()
edge2.change_edge_weight(1)

node1 = Node()
node1.add_edge(edge1)
node1.add_edge(edge2)
print(node1)l
