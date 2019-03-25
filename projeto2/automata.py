from structures.myQueue import MyQueue
from structures.myStack import MyStack
from structures.myNode import MyNode
import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

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
        # return ".A*B.|AB"
        # return ".*|AB+..CD*E"
        return "*.|AB.CD"

    def enqueueStringChar(self, str):
        queue = MyQueue()
        for char in list(str):
            queue.enqueue(char)
        return queue

    def automata(self, queue):
        v1 = queue.dequeue()

        if((v1 >= 'a' and v1 <= 'z') or (v1 >= 'A' and v1 <= 'Z')):
            return self.createNode(v1)
        else:
            n1 = self.automata(queue)

        if(v1 == "|" or v1 == "."):
            if(queue.size() == 0):
                return n1
            else:
                n2 = self.automata(queue)
    
        if(v1 == "|"):
            n = self.createOr(n1, n2)
        elif(v1 == "."):
            n = self.createAnd(n1, n2)
        elif(v1 == "*"):
            n = self.createCline(n1)
        elif(v1 == "+"):
            n = self.createPlus(n1)

        if(queue.size() == 0):
            n.last.end = True
            self.end = n.last

        return n

    def createNode(self, v):
        init = self.newNode()
        empty = self.newNode()
        value = self.newNode()
        end = self.newNode()
        init.addEdge(empty, V_EMPTY)
        empty.addEdge(value, v)
        value.addEdge(end, V_EMPTY)
        init.last = end
        return init

    def createCline(self, n1):
        n1.last.addEdge(n1, V_EMPTY)
        n1.addEdge(n1.last, V_EMPTY)
        return n1

    def createPlus(self, n1):
        n1.last.addEdge(n1, V_EMPTY)
        return n1


    def createAnd(self, n1, n2):
        n1.last.addEdge(n2, V_EMPTY)
        n1.last = n2.last
        return n1


    def createOr(self, n1, n2):
        init = self.newNode()
        end = self.newNode()
        init.addEdge(n1,V_EMPTY)
        init.addEdge(n2,V_EMPTY)
        n1.last.addEdge(end,V_EMPTY)
        n2.last.addEdge(end,V_EMPTY)
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
                print(str(n.value) + " => " +
                      str(e.value) + " -> " + str(e.to.value))
        print("\n")

    def plot(self):
        g = nx.DiGraph()
        edge_labels = dict()
        color_map = []

        for n in self.nodes:
            if(n.init):
                color_map.append('y')
            elif(n.end):
                color_map.append('m')
            else:
                color_map.append('c')
            g.add_node(n.value)

        for n in self.nodes:
            for e in n.edges:
                g.add_edge(n.value, e.to.value)
                edge_labels[(n.value, e.to.value)] = e.value

        pos = nx.shell_layout(g)
        nx.draw(g, pos, with_labels=True, arrows=True, arrowsize=7,
                node_color=color_map, node_size=400, font_size=10)
        nx.draw_networkx_edge_labels(g, pos, edge_labels=edge_labels)
        blue = mpatches.Patch(color='y', label='Initial State')
        red = mpatches.Patch(color='m', label='Final State')
        plt.legend(handles=[blue, red])
        plt.show()
