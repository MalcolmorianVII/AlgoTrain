
class Vertex:
    def __init__(self,value,adj_vertices=[]) -> None:
        self.value = value
        self.adj_vertices = adj_vertices
    def add_adj_vertices(self,vertex):
        self.adj_vertices.append(vertex)

def dfs_traverse(vertex,visited_vertices={}):
    # Mark vertex as visited 
    visited_vertices[vertex.value] = True

    # print the vertex value
    print(vertex.value)

    for adj in vertex.adj_vertices:
        if visited_vertices.get(adj.value):
            continue
        dfs_traverse(adj,visited_vertices)
    
alice = Vertex("Alice")
bob = Vertex("Bob")
cynthia = Vertex("Cynthia")

alice.add_adj_vertices(bob)
alice.add_adj_vertices(cynthia)
bob.add_adj_vertices(cynthia)
cynthia.add_adj_vertices(bob)

dfs_traverse(alice)

