from structures.myQueue import MyQueue
from structures.myStack import MyStack
from structures.myNode import MyNode

STATE = -1
V_EMPTY = '#'

def createAutomata(regex):
    prefix = toPrefix(regex)
    queue = enqueueStringChar(prefix)
    node = automata(queue)
    node.init = True
    return node

def toPrefix(str):
    return "A*B|AB"

def enqueueStringChar(str):
    queue = MyQueue()
    for char in list(str):
        queue.enqueue(char)
    return queue


def automata(queue):
    value = queue.dequeue()
    if(value == "|"):
        n = createOr(queue.dequeue(),queue.dequeue())
    elif(value == "*"):
        n = createCline(queue.dequeue())
    elif(value == "+"):
        n = createPlus(queue.dequeue())
    else:
        n = createNode(value)

    if(queue.size() == 0):
        n.last.end = True
        return n
    else:
        next = automata(queue)
        n.last.addEdge(next, V_EMPTY)
    
    return n


def createNode(n1):
    init = newNode()
    empty = newNode()
    value = newNode()
    end = newNode()

    init.addEdge(empty,V_EMPTY)
    empty.addEdge(value, n1)
    value.addEdge(end, V_EMPTY)

    init.last = end

    return init

def createPlus(n1):
    init = newNode()
    empty = newNode()
    value = newNode()
    end = newNode()

    init.addEdge(empty,V_EMPTY)
    empty.addEdge(value, n1)
    value.addEdge(empty, V_EMPTY)
    value.addEdge(end, V_EMPTY)

    init.last = end

    return init

def createCline(n1):
    init = newNode()
    empty = newNode()
    value = newNode()
    end = newNode()

    init.addEdge(empty,V_EMPTY)
    empty.addEdge(end, V_EMPTY)
    empty.addEdge(value, n1)
    value.addEdge(empty, V_EMPTY)
    value.addEdge(end, V_EMPTY)
    
    init.last = end

    return init

def createOr(n1, n2):
    init = newNode()
    empty = newNode()
    value = newNode()
    empty2 = newNode()
    value2 = newNode()
    end = newNode()

    init.addEdge(empty,V_EMPTY)
    init.addEdge(empty2,V_EMPTY)
    empty.addEdge(value,n1)
    empty2.addEdge(value2,n2)
    value.addEdge(end,V_EMPTY)
    value2.addEdge(end,V_EMPTY)

    init.last = end

    return init

def newNode():
    global STATE
    STATE += 1
    return MyNode('Q' + str(STATE))