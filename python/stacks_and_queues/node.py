class Node:
    """
    Creates new node object to be used in stacks and queues.
    """
    def __init__(self, value, next=None):
        self.value = value
        self.next = next
