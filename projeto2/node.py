from edge import *

class Node:
    def __init__(self):
        self.name = ""
        self.edges = []   

    def removeEdge(self, edge):
        edges.remove(edge)

    def setName(self, name):
        self.name = name
    
    def addEdge(self, to):
        self.edges.append(to)