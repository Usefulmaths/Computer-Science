import sys
sys.path.insert(
    0, '/Users/LiamEloie/Documents/Codes/Computer Science/Arrays and Strings')

from stack import Stack


class Node(object):

    def __init__(self, value):
        self.value = value
        self.edges = []


class Edge(object):

    def __init__(self, value, node_from, node_to):
        self.value = value
        self.node_from = node_from
        self.node_to = node_to

    def __str__(self):
        return "Node from: %s\nNode to: %s" % (self.node_from.value, self.node_to.value)


class Graph(object):

    def __init__(self, nodes=[], edges=[]):
        self.nodes = nodes
        self.edges = edges

    def insert_node(self, value):
        node = Node(value)
        self.nodes.append(node)

    def insert_edge(self, value, node_from_val, node_to_val):
        node_from = None
        node_to = None

        for node in self.nodes:
            if node.value == node_from_val:
                node_from = node

            if node.value == node_to_val:
                node_to = node

        if node_from is None:
            node_from = Node(node_from_val)
            self.nodes.append(node_from)

        if node_to is None:
            node_to = Node(node_to_val)
            self.nodes.append(node_to)

        edge = Edge(value, node_from, node_to)
        node_from.edges.append(edge)
        node_to.edges.append(edge)

        self.edges.append(edge)

    def get_edge_list(self):
        edge_list = []

        for edge in self.edges:
            edge_element = [
                (edge.value, edge.node_from.value, edge.node_to.value)
            ]
            edge_list.append(edge_element)

        return edge_list

    def get_adjacency_list(self):
        adjacency_list = []

        for node in self.nodes:
            node_connections = []
            for edge in node.edges:
                node_to_val = edge.node_to.value
                if node_to_val != node.value:
                    node_connections.append((node_to_val, edge.value))

            if len(node_connections) == 0:
                node_connections = None

            adjacency_list.append(node_connections)

        return adjacency_list

    def get_adjacency_matrix(self):
        number_of_nodes = len(self.nodes)

        connections = []

        for i in range(number_of_nodes):
            connection = [0] * number_of_nodes
            connections.append(connection)

        for edge in self.edges:
            node_to = edge.node_to.value
            node_from = edge.node_from.value

            connections[node_from][node_to] = edge.value
            connections[node_to][node_from] = edge.value

        adjacency_matrix = []

        return adjacency_matrix


if __name__ == '__main__':
    graph = Graph()

    graph.insert_edge(100, 1, 2)
    graph.insert_edge(101, 1, 3)
    graph.insert_edge(102, 1, 4)
    graph.insert_edge(103, 3, 4)

    print(graph.get_edge_list())
    print(graph.get_adjacency_list())
    print(graph.get_adjacency_matrix())

    print(graph.search(3))
