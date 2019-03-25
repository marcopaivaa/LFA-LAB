class MyQueue:

    def __init__(self, data = []):
        self.queue = data

    def enqueue(self, data):
        return self.queue.insert(0, data)

    def dequeue(self):
        if len(self.queue) > 0:
            return self.queue.pop()

    def size(self):
        return len(self.queue)

    def printQueue(self):
        return self.queue

    def peek(self):
        return self.queue[0] if len(self.queue) > 0 else None

    def __str__(self):
        return str(self.queue)[1:-1]
