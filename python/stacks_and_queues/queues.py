from stacks_and_queues.node import Node

class InvalidOperationError(Exception):
    pass

class Queue:
    def __init__(self) -> None:
        self.front = None
        self.end = None

    def enqueue(self, value):
        if self.front is None:
            self.front = Node(value)
            self.end = self.front
        else:
            self.end.next = Node(value)
            self.end = self.end.next

    def dequeue(self):
        if self.front:
            front_val = self.front.value
            self.front = self.front.next
            return front_val

        raise InvalidOperationError()

    def peek(self):
        if self.front:
            return self.front.value

        raise InvalidOperationError()

    def is_empty(self):
        if self.front is None:
            return True

        return False
