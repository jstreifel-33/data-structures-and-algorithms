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

    def append(self, value):
        current_node = self.head
        while current_node.next is not None:
            current_node = current_node.next
        current_node.next = Node(value)

    def insert_before(self, target, value):
        current_node = self.head
        #check head node, act accordingly if match for target.
        if current_node.value == target:
            self.insert(value)
            return
        #if head node not match, step through for match
        while current_node.next.value != target:
            current_node = current_node.next
        current_node.next = Node(value, current_node.next)

    def insert_after(self, target, value):
        current_node = self.head
        while current_node.value != target:
            current_node = current_node.next
        current_node.next = Node(value, current_node.next)

    def kth_value(self, k):
        current_node = self.head
        found_node = self.head
        dist = 0

        while current_node:
            if dist > k:
                found_node = found_node.next
            current_node = current_node.next
            dist += 1

        if dist > k:
            return found_node.value
        else:
            raise ValueError("Linked list too short for given value!")


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
