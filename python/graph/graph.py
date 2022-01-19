class Graph():
    def __init__(self):
        self.adjacency_list = {}

    def add_node(self, value):
        vertex = Vertex(value)
        self.adjacency_list[vertex] = []
        return vertex


class Vertex():
    def __init__(self, value):
        self.value = value


class Edge():
    pass
