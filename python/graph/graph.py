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
        edge = Edge(end_vert, weight)
        self.adjacency_list[start_vert].append(edge)


class Vertex():
    def __init__(self, value):
        self.value = value


class Edge():
    def __init__(self, end_vert, weight=0):
            self.end_vert = end_vert
            self.weight = weight
