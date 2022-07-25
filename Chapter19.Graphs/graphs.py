
class Vertex:
    def __init__(self,value,adj_vertices=[]) -> None:
        self.value = value
        self.adj_vertices = adj_vertices
    def add_adj_vertices(self,vertex):
        self.adj_vertices.append(vertex)

alice = Vertex("Alice")
bob = Vertex("Bob")
cynthia = Vertex("Cynthia")

alice.add_adj_vertices(bob)
alice.add_adj_vertices(cynthia)
bob.add_adj_vertices(cynthia)
cynthia.add_adj_vertices(bob)

