class MyNode:
    def __init__(self):
        self.visited = False
        self.parent = None
        self.name = ""
        self.edges = []

    def removeEdge(self, edge):
        self.edges.remove(edge)

    def setName(self, name):
        self.name = name

    def addEdge(self, to):
        self.edges.append(to)
