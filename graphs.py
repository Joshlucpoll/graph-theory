import random
from objects import Graph
from graphAlgorithms import *

graph = Graph()
graph.generateNodes(6)
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
graph.generateEdges(rawEdges)


MST = prims(graph)

for val in MST:
    print(val.start.id, val.end.id)
