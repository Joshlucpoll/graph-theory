from objects import Node, Edge, Graph
import random


def prims(graph: Graph) -> list[Edge]:
    nodes = graph.getNodes()

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


def kruskal(graph: Graph):
    edges = graph.getEdges()

    shortestEdge = None
    for edge in edges:
        if shortestEdge == None or edge.weight < shortestEdge.weight:
            shortestEdge = edge

    connectedEdges = [shortestEdge]
