class Node:
    """
    Creates new node object to be used in a linked list object.
    """
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

class LinkedList:
    """
    Initializes a singly linked list object, composed of nodes.
    includes 'insert', 'includes' and 'to_string' methods
    """

    def __init__(self):
        self.head = None

    def insert(self, value):
        """
        Create and insert a new node into a linked list.
        Newly created node is assigned as new head of list.
        """
        self.head = Node(value, self.head)

    def includes(self, value):
        """
        Checks contents of linked list for
        provided value. Return True or False
        """
        check_node = self.head
        while check_node is not None:
            if check_node.value == value:
                return True

            check_node = check_node.next

        return False

    def to_string(self):
        """
        Returns string representation of
        linked list.
        """
        as_string = ""
        check_node = self.head
        while check_node is not None:
            as_string += "{ " +  check_node.value + " } -> "
            check_node = check_node.next

        as_string += "None"
        return as_string
