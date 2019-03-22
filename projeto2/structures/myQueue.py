class MyQueue:

    def __init__(self):
        self.queue = []

    def enqueue(self, data):
        return self.queue.insert(0, data)

    def dequeue(self):
        if len(self.queue) > 0:
            return self.queue.pop()

    def size(self):
        return len(self.queue)

    def printQueue(self):
        return self.queue

    def __str__(self):
        return str(self.queue)[1:-1]
