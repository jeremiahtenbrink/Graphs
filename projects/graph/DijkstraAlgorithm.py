import sys
import heapq


class Edge(object):

    def __init__(self, weight, start_vertex, target_vertex):
        self.weight = weight
        self.start_vertex = start_vertex
        self.target_vertex = target_vertex


class Node(object):

    def __init__(self, name):
        self.name = name
        self.visited = False
        self.predecessor = None
        self.adjacency_list = []
        self.min_distance = sys.maxsize

    def __cmp__(self, other_vertex):
        return self.cmp(self.min_distance, other_vertex.min_distance)

    def __lt__(self, other):
        self_priority = self.min_distance
        other_priority = other.min_distance
        return self_priority < other_priority


class Algorithm(object):

    def calculate_shortest_path(self, vertex_list, start_vertex):
        q = []
        start_vertex.min_distance = 0
        heapq.heappush(q, start_vertex)

        while len(q) > 0:
            actual_vertex = heapq.heappop(q)

            for edge in actual_vertex.adjacency_list:
                u = edge.start_vertex
                v = edge.target_vertex
                new_distance = u.min_distance + edge.weight

                if new_distance < u.min_distance:
                    v.predecessor = u
                    v.min_distance = new_distance
                    heapq.heappush(q, v)
