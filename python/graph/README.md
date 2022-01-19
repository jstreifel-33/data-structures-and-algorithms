# Hash Tables

Implementation of graph data structure. A graph is a non-linear data structure composed of vertices (also called nodes) connected by relationships called edges.

## Challenge

Implement a graph class, including add_node, size, get_nodes, add_edge, and get_neighbors methods.

## Approach & Efficiency

This implementation utilizes a Graph, Vertex, and Edge class. Vertex and Edge are used to simply store information about the graph structure.

Within the Graph class, vertices are stored in an adjacency list in the form of a Python dictionary. The keys are the vertices of the graph, and the values are lists of associated edges for each vertex.

Efficiency Analysis:

* `add_node(value)` - O(1) time efficiency on account of all operations being assignments. O(N) space efficiency, since the input must be stored in the newly created node.
* `size()` - O(1) time efficiency on account of using `len()`. In Python, `len()` is an O(1) operation is the only method operation under the hood here. O(1) space efficiency, since nothing additional is being stored.
* `get_nodes(value)` - O(N) time efficiency where N is the number of vertices currently in the graph. O(N) space efficiency, since length of returned list will scale directly with number of vertices in graph.
* `add_edge(value)` - O(1) time efficiency, since checking keys of a dictionary is O(1) operation and appending to a list is also O(1) operation. O(1) space efficiency, since the equivalent of 1 list index of space will be added each time the method is called.
* `get_neighbors(value)` - O(1) time and space efficiency, since method simply accesses and returns value from the `adjacency_list` Python dictionary.

## API

* `Graph()` - instantiates a new graph object
  * `.add_node(value)` - Adds a vertex to the graph object, containing the given value. Returns newly created vertex.
  * `.size()` - returns the number of vertices in the graph object.
  * `.get_nodes()` - returns a list containing.
  * `.add_edge(start_vert, end_vert, weight=0)` - creates a new edge, containing end vertex and weight. Adds new edge instance to `adjacency_list` of graph.
  * `.get_neighbors(vertex)` - returns a list containing all edge instances connected to a given vertex.
