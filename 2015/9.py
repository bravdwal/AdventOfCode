import re


class Node:
    def __init__(self, id):
        self.id = id
        self.neighbours = []

    def add_neighbour(self, node):
        self.neighbours.append(node)


class Graph:
    def __init__(self):
        self.nodes = dict()

    def get_or_create_node(self, id):
        if id in self.nodes:
            return self.nodes[id]

        self.nodes[id] = Node(id)
        return self.nodes[id]


def setup(config):
    graph = Graph()

    for line in config:
        m = re.search(r'^(\w+) to (\w+) = (\d+)$', line)
        f, t, d = m.groups()  # from, to, distance
        n1 = graph.get_or_create_node(f)
        n2 = graph.get_or_create_node(t)



with open('files/9.txt', 'r') as f:
    config = f.readlines()
