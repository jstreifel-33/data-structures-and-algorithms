from stacks_and_queues.node import Node

class InvalidOperationError(Exception):
    pass

class Queue:
    def __init__(self) -> None:
        self.front = None

    def enqueue(self, value):
        if self.front is None:
            self.front = Node(value)
        else:
            self.front.next = Node(value)

    def dequeue(self):
        front_val = self.front.value
        self.front = self.front.next
        return front_val

