class Graph():
    def __init__(self):
        self.adjacency_list = {}

    def add_node(self, value):
        vertex = Vertex(value)
        self.adjacency_list[vertex] = []
        return vertex

    def size(self):
        return len(self.adjacency_list)

    def get_nodes(self):
        return list(self.adjacency_list.keys())

    def add_edge(self, start_vert, end_vert, weight=0):
        if end_vert not in self.adjacency_list.keys():
            raise KeyError("End vertex not in graph")

        edge = Edge(end_vert, weight)
        self.adjacency_list[start_vert].append(edge)

    def get_neighbors(self, vertex):
        return self.adjacency_list[vertex]


class Vertex():
    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return str(self.value)


class Edge():
    def __init__(self, vertex, weight=0):
            self.vertex = vertex
            self.weight = weight

    def __repr__(self):
        return f"({self.vertex}, {self.weight})"
