from util import Stack, Queue


class Node(object):

    def __init__(self, value):
        self.value = value
        self.parents = []
        self.children = []
        self.visited = False
        self.weight = 0

    def add_parrent(self, parent):
        self.parents.append(parent)

    def add_child(self, child):
        self.children.append(child)

    def get_parents(self):
        return self.parents


class Graph(object):

    def __init__(self, ansestors):
        self.nodes = {}
        self.furthest = None

        for (parent, child) in ansestors:
            self.add_parent_child(parent, child)

    def get_node(self, value):
        node = self.nodes.get(value)
        if not node:
            node = Node(value)
            self.nodes[value] = node
        return node

    def add_parent_child(self, parent, child):
        parent = self.get_node(parent)
        child = self.get_node(child)

        parent.add_child(child)
        child.add_parrent(parent)

    def bfs(self, start):
        queue = Queue()
        node = self.nodes[start]
        self.furthest = node
        queue.enqueue(node)

        while queue.size() > 0:
            node = queue.dequeue()
            parents = node.get_parents()

            for parent in parents:
                if not parent.visited:
                    parent.visited = True
                    queue.enqueue(parent)
                    self.adjust_weight(parent, node.weight)

        return self.return_furthest_node()

    def return_furthest_node(self):
        if self.furthest.weight == 0:
            return -1
        return self.furthest.value

    def adjust_weight(self, node, weight):
        node.weight = weight + 1
        if node.weight > self.furthest.weight:
            self.furthest = node
        elif node.weight == self.furthest.weight and node.value < self.furthest.value:
            self.furthest = node

    def dfs(self, start):
        stack = Stack()
        start_node = self.get_node(start)
        self.furthest = start_node
        stack.push(start_node)

        while stack.size() > 0:
            node = stack.pop()
            if not node.visited:
                node.visited = True
                parents = node.get_parents()
                for each in parents:
                    stack.push(each)
                    self.adjust_weight(each, node.weight)

        return self.return_furthest_node()


def earliest_ancestor(ancestors, starting_node):
    graph = Graph(ancestors)
    return graph.bfs(starting_node)
