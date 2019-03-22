from structures.myEdge import MyEdge


class MyNode:

    def __init__(self, value=None):
        self.value = value
        self.edges = []
        self.parent = None
        self.init = False
        self.end = False
        self.last = None

    def addEdge(self, to, value=None):
        edge = MyEdge(to, value)
        self.edges.append(edge)
