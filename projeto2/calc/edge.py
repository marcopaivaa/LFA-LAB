from node import *

class Edge:
    def __init__(self, fromNode, toNode):
        self.fromNode = fromNode
        self.toNode = toNode

    def removeEdge(self, edge):
        edges.remove(edge)

    def setName(self, name):
        self.name = name
    
    def addEdge(self, to):
        self.edges.append(to)