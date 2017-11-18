import abc

import numpy as np

class Graph(abc.ABC):

    def __init__(self, numVertices, directed=False):
        self.numVertices = numVertices
        self.directed = directed

    @abc.abstractmethod
    def add_edge(self, v1, v2, weight):
        pass

    @abc.abstractmethod
    def get_adjacent_vertices(self, v):
        pass

    @abc.abstractmethod
    def get_indegree(self, v):
        pass

    @abc.abstractmethod
    def get_edge_weight(self, v1, v2):
        pass

    @abc.abstractmethod
    def display(self):
        pass


class Node(object):
    def __init__(self, vertex_id):
        self.vertexId = vertex_id
        self.adjacency_set = set()

    def add_edge(self, v):
        if self.vertexId == v:
            raise ValueError("The vertex %d cannot be adjacent to itself." % v)

        self.adjacency_set.add(v)

    def get_adjacent_vertices(self):
        return sorted(self.adjacency_set)


class AdjacencySetGraph(Graph):

    def __init__(self, num_vertices, directed=False):
        super(AdjacencySetGraph, self).__init__(num_vertices, directed)

        self.vertex_list = [Node(i) for i in range(num_vertices)]

    def get_indegree(self, v):
        if v < 0 or v >= self.numVertices:
            raise ValueError("Cannot access vertex %d" % v)

        count = 0

        for vertex in self.vertex_list:
            if v in vertex.get_adjacent_vertices():
                count += 1

        return count

    def display(self):
        for i in range(self.numVertices):
            for vertex in self.get_adjacent_vertices(i):
                print("{0} --> {1}".format(i, vertex))

    def get_edge_weight(self, v1, v2):
        return 1

    def get_adjacent_vertices(self, v):
        return self.vertex_list[v].get_adjacent_vertices()

    def add_edge(self, v1, v2, weight=1):
        if v1 > self.numVertices or v2 >= self.numVertices or v1 < 0 or v2 < 0:
            raise ValueError("Vertices %d and %d are out of bounds." % (v1, v2))

        if weight != 1:
            raise ValueError("An adjacent set can't represent weight edges > 1.")

        self.vertex_list[v1].add_edge(v2)
        if self.directed is False:
            self.vertex_list[v2].add_edge(v1)


class AdjacencyMatrixGraph(Graph):

    def __init__(self, num_vertices, directed=False):
        super(AdjacencyMatrixGraph, self).__init__(num_vertices, directed)

        # row node -> column node
        self.matrix = np.zeros((num_vertices, num_vertices), dtype=int)

    def get_indegree(self, v):
        if v < 0 or v >= self.numVertices:
            raise ValueError("Can't access vertex %d." % v)

        indegrees = 0
        for i in range(self.numVertices):
            if self.matrix[i][v]:
                indegrees += 1

        return indegrees

    def display(self):
        super().display()

    def get_edge_weight(self, v1, v2):
        return self.matrix[v1][v2]

    def get_adjacent_vertices(self, v):
        if v < 0 or v >= self.numVertices:
            raise ValueError("Can't access vertex %d." % v)

        return [i for i in range(self.numVertices) if self.matrix[v][i] != 0]

    def add_edge(self, v1, v2, weight=1):
        if v1 >= self.numVertices or v2 >= self.numVertices or v1 < 0 or v2 < 0:
            raise ValueError("Vertices %d and %d are out of bounds." % (v1, v2))

        if weight < 1:
            raise ValueError("An edge cannot have weight < 1.")

        self.matrix[v1][v2] = weight

        if self.directed is False:
            self.matrix[v2][v1] = weight


g = AdjacencySetGraph(4, True)
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(2, 3)

for i in range(4):
    print("Adjacent to: ", i, g.get_adjacent_vertices(i))

for i in range(4):
     print("Indegree: ", i, g.get_indegree(i))

for i in range(4):
    for j in g.get_adjacent_vertices(i):
       print ("Edge weight: ", i, " ", j, " weight: ", g.get_edge_weight(i, j))

g.display()
