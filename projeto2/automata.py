from structures.myQueue import MyQueue
from structures.myStack import MyStack
from structures.myNode import MyNode
import networkx as nx
import matplotlib.pyplot as plt

STATE = -1
V_EMPTY = '#'

class Automata:

    def __init__(self):
        self.nodes = []
        self.init = None
        self.ends = None
        
    def createAutomata(self, regex):
        self.nodes = []
        prefix = self.toPrefix(regex)
        queue = self.enqueueStringChar(prefix)
        node = self.automata(queue)
        node.init = True
        self.init = node
        return node

    def toPrefix(self, str):
        return "A*B|AB"

    def enqueueStringChar(self, str):
        queue = MyQueue()
        for char in list(str):
            queue.enqueue(char)
        return queue


    def automata(self, queue):
        value = queue.dequeue()
        if(value == "|"):
            n = self.createOr(queue.dequeue(),queue.dequeue())
        elif(value == "*"):
            n = self.createCline(queue.dequeue())
        elif(value == "+"):
            n = self.createPlus(queue.dequeue())
        else:
            n = self.createNode(value)

        if(queue.size() == 0):
            n.last.end = True
            self.end = n.last
            return n
        else:
            next = self.automata(queue)
            n.last.addEdge(next, V_EMPTY)
        
        return n


    def createNode(self,n1):
        init = self.newNode()
        empty = self.newNode()
        value = self.newNode()
        end = self.newNode()

        init.addEdge(empty,V_EMPTY)
        empty.addEdge(value, n1)
        value.addEdge(end, V_EMPTY)

        init.last = end

        return init

    def createPlus(self, n1):
        init = self.newNode()
        empty = self.newNode()
        value = self.newNode()
        empty2 = self.newNode()
        end = self.newNode()

        init.addEdge(empty,V_EMPTY)
        empty.addEdge(value, n1)
        value.addEdge(empty2, V_EMPTY)
        empty2.addEdge(empty, V_EMPTY)
        value.addEdge(end, V_EMPTY)

        init.last = end

        return init

    def createCline(self, n1):
        init = self.newNode()
        empty = self.newNode()
        value = self.newNode()
        empty2 = self.newNode()
        end = self.newNode()

        init.addEdge(empty,V_EMPTY)
        empty.addEdge(end, V_EMPTY)
        empty.addEdge(value, n1)
        value.addEdge(empty2, V_EMPTY)
        empty2.addEdge(empty, V_EMPTY)
        value.addEdge(end, V_EMPTY)
        
        init.last = end

        return init

    def createOr(self, n1, n2):
        init = self.newNode()
        empty = self.newNode()
        value = self.newNode()
        empty2 = self.newNode()
        value2 = self.newNode()
        end = self.newNode()

        init.addEdge(empty,V_EMPTY)
        init.addEdge(empty2,V_EMPTY)
        empty.addEdge(value,n1)
        empty2.addEdge(value2,n2)
        value.addEdge(end,V_EMPTY)
        value2.addEdge(end,V_EMPTY)

        init.last = end

        return init

    def newNode(self):
        global STATE
        STATE += 1
        n = MyNode('Q' + str(STATE))
        self.nodes.append(n)
        return n

    def print(self):
        print("\nInitial state: " + str(self.init.value))
        print("Final state: " + str(self.end.value) + "\n")
        for n in self.nodes:
            for e in n.edges:
                print(str(n.value) + " => " + str(e.value) + " -> " + str(e.to.value))
        print("\n")

    def plot(self):
        g = nx.DiGraph()
        edge_labels = dict()
        color_map = []

        for n in self.nodes:
            if(n.init):
                color_map.append('b')
            elif(n.end):
                color_map.append('r')
            else:
                color_map.append('c')
            g.add_node(n.value)

        for n in self.nodes:
            for e in n.edges:
                g.add_edge(n.value,e.to.value)
                edge_labels[(n.value, e.to.value)] = e.value

        pos = nx.shell_layout(g)
        nx.draw(g, pos, with_labels=True, arrows=True, arrowsize=7, node_color=color_map, node_size=400, font_size=10)
        nx.draw_networkx_edge_labels(g,pos,edge_labels=edge_labels)
        plt.show()
