from stacks_and_queues.node import Node

class InvalidOperationError(Exception):
    pass

class Stack:
    def __init__(self) -> None:
        self.top = None

    def push(self, value):
        self.top = Node(value, self.top)

    def pop(self):
        top_val = self.top.value
        self.top = self.top.next
        return top_val
