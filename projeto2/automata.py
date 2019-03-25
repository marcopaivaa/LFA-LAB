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
        print("Prefixo: "+prefix)
        queue = self.enqueueStringChar(prefix)
        node = self.automata(queue)
        node.init = True
        self.init = node
        return node

    def toPrefix(self, expr):
        # return ".A*B.|AB"
        # return ".*|AB+..CD*E"
        return "*.|AB.CD"
        expression = MyQueue()
        operator = MyStack(len(expr))
        prefixa = ""
        i = 0
        while(i < len(expr)):
            if (expr[i] >= 'A' and expr[i] <= 'Z'):
                prefixa += expr[i]
            elif (expr[i] == '*' or expr[i] == '+'):
                aux = prefixa[-1]
                prefixa = prefixa[:-1]
                prefixa += expr[i]
                prefixa += aux
            elif (expr[i] == '.' or expr[i] == '|'):
                operator.push(expr[i])
            elif (expr[i] == '('):
                if(i > 0 and expr[i-1] != '.' and expr[i-1] != '|'):
                    operator.push('.')
                j = i
                cont = 1
                while(cont >= 1):
                    j = j+1
                    if(expr[j] == '('):
                        cont = cont+1
                    elif(expr[j] == ')'):
                        cont = cont-1
                aux = self.toPrefix(expr[i+1:j])
                i = j
                if(i < len(expr) and (expr[i+1] == '*' or expr[i+1] == '+')):
                    aux = expr[i+1] + aux
                    i = i+1
                prefixa += aux
            i = i+1
        while(not operator.vazia()):
            prefixa = operator.pop() + prefixa
            if(operator.vazia()):
                expression.enqueue(prefixa)
                prefixa = ""
        while(len(prefixa) > 0):
            expression.enqueue(prefixa)
            prefixa = ""
        while (expression.size() > 0):
            prefixa += expression.dequeue()
        return prefixa

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
