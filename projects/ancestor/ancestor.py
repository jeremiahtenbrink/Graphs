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
        self.furthest = 0
        self.furthest_nodes = []

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
        queue.enqueue(node)

        while queue.size() > 0:
            node = queue.dequeue()
            parents = node.get_parents()

            for parent in parents:
                if not parent.visited:
                    parent.visited = True
                    queue.enqueue(parent)
                    parent.weight = node.weight + 1
                    if self.furthest < parent.weight:
                        self.furthest_nodes = [parent]
                        self.furthest = parent.weight
                    elif self.furthest == parent.weight:
                        self.furthest_nodes.append(parent)

        if self.furthest == 0:
            return -1

        smallest = None
        for node in self.furthest_nodes:
            if smallest is None or node.value < smallest.value:
                smallest = node
        return smallest.value

    def dfs(self, start):
        stack = Stack()
        start_node = self.get_node(start)
        stack.push(start_node)

        while stack.size() > 0:
            node = stack.pop()
            if not node.visited:
                node.visited = True
                parents = node.get_parents()
                for each in parents:
                    stack.push(each)
                    each.weight = node.weight + 1
                    if self.furthest < each.weight:
                        self.furthest = each.weight
                        self.furthest_nodes = [each]
                    elif self.furthest == each.weight:
                        self.furthest_nodes.append(each)
        if self.furthest == 0:
            return -1
        smallest = None
        for node in self.furthest_nodes:
            if smallest is None or smallest.value > node.value:
                smallest = node

        return smallest.value


def earliest_ancestor(ancestors, starting_node):
    graph = Graph(ancestors)
    return graph.dfs(starting_node)
