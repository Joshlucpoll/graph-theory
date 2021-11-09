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


class Graph:
    def __init__(self):
        self.__nodes: dict[str, Node] = {}
        self.__edges: list[Edge] = []

    def getNodes(self) -> list[Node]:
        return self.__nodes.values()

    def getEdges(self) -> list[Edge]:
        return self.__edges

    def generateNodes(self, n: int) -> list[Node]:
        nodes = {}
        for i in range(n):
            nodes[chr(i+65)] = Node(chr(i+65))

        self.__nodes = nodes
        return nodes.values()

    def generateEdges(self, rawEdges: list[list]):
        edges = []
        for rawEdge in rawEdges:
            edges.appends(
                Edge(self.getNodes()[rawEdge[0]], self.getNodes()[rawEdge[1]], rawEdge[2]))

        self.__edges = edges
