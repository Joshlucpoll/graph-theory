import random


class Node:
    def __init__(self, id: str):
        self.id: str = id
        self.edges: list["Edge"] = []

    def addEdge(self, edge: "Edge"):
        self.edges.append(edge)


class Edge:
    def __init__(self, start: Node, end: Node, weight: int):
        self.start = start
        self.end = end
        self.weight = weight

        start.addEdge(self)
        end.addEdge(self)

    def findOtherEnd(self, node: Node):
        if node != self.start or node != self.end:
            return 0

        return self.end if node == self.start else self.start


def generateNodes(n: int) -> dict[str, Node]:
    nodes = {}
    for i in range(6):
        nodes[chr(i+65)] = Node(chr(i+65))

    return nodes


def generateEdges(nodes: list[Node], rawEdges: list[list]):
    for rawEdge in rawEdges:
        Edge(nodes[rawEdge[0]], nodes[rawEdge[1]], rawEdge[2])


nodes = generateNodes(6)
rawEdges = [
    ['A', 'B', 20],
    ['A', 'C', 18],
    ['A', 'D', 16],
    ['B', 'C', 15],
    ['B', 'F', 50],
    ['C', 'D', 10],
    ['C', 'E', 20],
    ['C', 'F', 30],
    ['D', 'E', 23],
    ['E', 'F', 25], ]
generateEdges(nodes, rawEdges)


# Edge(nodes[0], nodes[1], 20)
# Edge(nodes[0], nodes[2], 18)
# Edge(nodes[0], nodes[3], 16)

# Edge(nodes[1], nodes[2], 15)
# Edge(nodes[1], nodes[5], 50)

# Edge(nodes[2], nodes[3], 10)
# Edge(nodes[2], nodes[4], 20)
# Edge(nodes[2], nodes[5], 30)

# Edge(nodes[3], nodes[4], 23)

# Edge(nodes[4], nodes[5], 25)


def edgeDiscovery(nodes: list[Node]):
    edges = []
    for node in nodes:
        for edge in node.edges:
            if edge not in edges:
                edges.append(edge)

    return edges


def prims(nodes: list[Node]):
    connectedNodes = []
    connectedNodes.append(random.choice(nodes))
    MST: list[Edge] = []

    while True:
        shortestEdge = None
        for node in connectedNodes:
            for edge in node.edges:
                if edge.start in connectedNodes and edge.end in connectedNodes:
                    continue
                if shortestEdge == None or edge.weight < shortestEdge.weight:
                    shortestEdge = edge

        MST.append(shortestEdge)
        connectedNodes.append(
            shortestEdge.end if shortestEdge.start in connectedNodes else shortestEdge.start)

        if all(elem in connectedNodes for elem in nodes):
            break

    return MST


def kruskal(nodes: list[Node]):
    edges = edgeDiscovery(nodes)

    shortestEdge = None
    for edge in edges:
        if shortestEdge == None or edge.weight < shortestEdge.weight:
            shortestEdge = edge

    connectedEdges = [shortestEdge]


MST = prims(nodes.values)

for val in MST:
    print(val.start.id, val.end.id)
