from stacks_and_queues.stacks import Stack
from stacks_and_queues.stacks import InvalidOperationError


class PseudoQueue:
    def __init__(self) -> None:
        exit = Stack()
        entrance = Stack()

    def enqueue(self, value):
        if self.entrance.is_empty():
            while not self.exit.is_empty():
                self.entrance.push(self.exit.pop())

        self.entrance.push(value)

    def dequeue(self):

        if self.exit.is_empty():
            if self.entrance.is_empty():
                raise InvalidOperationError('Operation cannot be performed on empty collection')

            while not self.entrance.is_empty():
                self.exit.push(self.entrance.pop())

        return exit.pop()
