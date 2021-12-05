class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

class LinkedList:
    """
    Put docstring here
    """

    def __init__(self):
        self.head = None

    def insert(self, value):
        new_node = Node(value, self.head)
        self.head = new_node
