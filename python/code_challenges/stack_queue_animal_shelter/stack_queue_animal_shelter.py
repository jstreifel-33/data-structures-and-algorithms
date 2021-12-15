from stacks_and_queues.node import Node


class Cat(Node):
    def __str__(self):
        return 'cat'


class Dog(Node):
    def __str__(self):
        return 'dog'


class AnimalShelter:
    def __init__(self):
        self.front = None
        self.end = None


    def enqueue(self, animal):
        if self.front is None:
            self.front = animal
            self.end = self.front
        else:
            self.end.next = animal
            self.end = self.end.next


    def dequeue(self, pref):
        searching = True
        self.enqueue(Node('end'))

        while self.front.value != 'end':
            if str(self.front) == pref and searching:
                found_animal = self.front
                searching = False
            else:
                self.enqueue(self.front)

            self.front = self.front.next

        self.front = self.front.next

        if not searching:
            return found_animal
        else:
            return None
