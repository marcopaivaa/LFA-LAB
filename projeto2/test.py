from queue import *
from stack import *
from node import *
from vertex import *
import unittest


class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        automato = createAutomato(regex)
        self.assertTrue(True)


def createAutomato(regex):
    preFix = toPreFix(regex)
    queue = enqueuePreFix(preFix)
    automato = automato(queue)
    automato.init = createInit()
    return automato


def toPreFix(regex):
    return "A*B|AB"


def enqueuePreFix(preFix):
    queue = Queue()
    for char in list(preFix):
        queue.enqueue(char)
    return queue


def automato(queue):
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
        n.end = createEnd()
        return n
    else:
        next = automato(queue)
        n.end = next

    return n
