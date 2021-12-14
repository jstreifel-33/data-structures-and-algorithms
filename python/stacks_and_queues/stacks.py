from stacks_and_queues.node import Node

class InvalidOperationError(Exception):
    pass

class Stack:
    def __init__(self) -> None:
        self.top = None

    def push(self, value):
        self.top = Node(value, self.top)

    def pop(self):
        if self.top:
            top_val = self.top.value
            self.top = self.top.next
            return top_val

        raise InvalidOperationError("Method not allowed on empty collection")

    def is_empty(self):
        if self.top is None:
            return True

        return False

    def peek(self):
        if self.top:
            return self.top.value

        raise InvalidOperationError("Method not allowed on empty collection")
