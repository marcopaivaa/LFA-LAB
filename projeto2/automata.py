from structures.myQueue import MyQueue
from structures.myStack import MyStack
from structures.myNode import MyNode


def createAutomata(regex):
    prefix = toPrefix(regex)
    queue = enqueueStringChar(prefix)
    node = automata(queue)
    node.init = True
    return node


def toPrefix(str):
    return "A*B|AB"
    priority = {
        '(': 1,
        ')': 1,
        '+': 1,
        '*': 1,
        '|': 2,
    }
    stack = MyStack()
    posfix = ""

    for x in str:
        if(x == '('):
            stack.push(x)
        elif(x == ')'):
            posfix += stack.pop()
            while priority[x] != priority[stack.peek()]:
                posfix += stack.pop()
            stack.pop()
        elif(x == '|'):
            while stack.peek() is not None and priority[x] <= priority[stack.peek()]:
                posfix += stack.pop()
            stack.push(x)
        else:
            posfix += x

    while stack.empty() is not True:
        posfix += stack.pop()

    return posfix


def enqueueStringChar(str):
    queue = MyQueue()
    for char in list(str):
        queue.enqueue(char)
    return queue


def automata(queue):
    value = queue.dequeue()
    if(value == "|"):
        n = createOr(queue.dequeue(), queue.dequeue())
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
        n.last.addEdge(next, "#")

    return n


def createNode(n1):
    init = MyNode("init")
    end = MyNode("end")
    empty = MyNode("empty")
    value = MyNode("value")

    init.addEdge(empty, '#')
    empty.addEdge(value, n1)
    value.addEdge(end, '#')

    init.last = end

    return init


def createPlus(n1):
    init = MyNode("init")
    end = MyNode("end")
    empty = MyNode("empty")
    value = MyNode("value")

    init.addEdge(empty, '#')
    empty.addEdge(value, n1)
    value.addEdge(empty, '#')
    value.addEdge(end, '#')

    init.last = end

    return init


def createCline(n1):
    init = MyNode("init")
    end = MyNode("end")
    empty = MyNode("empty")
    value = MyNode("value")

    init.addEdge(empty, '#')
    empty.addEdge(end, '#')
    empty.addEdge(value, n1)
    value.addEdge(empty, '#')
    value.addEdge(end, '#')

    init.last = end

    return init


def createOr(n1, n2):
    init = MyNode("init")
    end = MyNode("end")
    empty = MyNode("empty")
    empty2 = MyNode("empty2")
    value = MyNode("value")
    value2 = MyNode("value2")

    init.addEdge(empty, '#')
    init.addEdge(empty2, '#')
    empty.addEdge(value, n1)
    empty2.addEdge(value2, n2)
    value.addEdge(end, '#')
    value2.addEdge(end, '#')

    init.last = end

    return init
