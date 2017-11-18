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
    def get_adjacent(self, v):
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
        pass

    def display(self):
        pass

    def get_edge_weight(self, v1, v2):
        pass

    def get_adjacent(self, v):
        pass

    def add_edge(self, v1, v2, weight=1):
        if v1 > self.numVertices or v2 >= self.numVertices or v1 < 0 or v2 < 0:
            raise ValueError("Vertices %d and %d are out of bounds." % (v1, v2))

        if weight != 1:
            raise ValueError("An adjacent set can't represent weight edges > 1.")

        self.vertex_list[v1].add_edge(v2)
        if self.directed is False:
            self.vertex_list[v2].add_edge(v1)