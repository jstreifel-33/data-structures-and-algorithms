class Node:
    """
    Creates new node object to be used in a linked list object.
    """
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

class LinkedList:
    """
    Initialized a singly linked list object, composed of nodes.
    inlcudes 'insert', 'includes' and 'to_string' methods
    """

    def __init__(self):
        self.head = None

    def insert(self, value):
        self.head = Node(value, self.head)
