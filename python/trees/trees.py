class Node():
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


class BinaryTree():
    def __init__(self, root=None):
        self.root = root


    def pre_order_traverse(self):

        def _traversal(root, result = []):
            result.append(root.value)
            if root.left:
                _traversal(root.left, result)
            if root.right:
                _traversal(root.right, result)
            return result

        if self.root:
            return _traversal(self.root)
        else:
            raise ValueError("Cannot perform operation on empty tree!")


    def in_order_traverse(self):

        def _traversal(root, result = []):
            if root.left:
                _traversal(root.left, result)
            result.append(root.value)
            if root.right:
                _traversal(root.right, result)
            return result

        if self.root:
            return _traversal(self.root)
        else:
            raise ValueError("Cannot perform operation on empty tree!")


    def post_order_traverse(self):

        def _traversal(root, result = []):
            if root.left:
                _traversal(root.left, result)
            if root.right:
                _traversal(root.right, result)
            result.append(root.value)
            return result

        if self.root:
            return _traversal(self.root)
        else:
            raise ValueError("Cannot perform operation on empty tree!")


    def get_max_value(self):

        def _traversal_max(root, max_value=0):
            if root is None:
                return max_value

            if max_value < root.value:
                max_value = root.value

            left_val = _traversal_max(root.left, max_value)
            if max_value < left_val:
                max_value = left_val

            right_val = _traversal_max(root.right, max_value)
            if max_value < right_val:
                max_value = right_val

            return max_value

        if self.root:
            return _traversal_max(self.root)
        else:
            raise ValueError("Cannot perform operation on empty tree!")

class BinarySearchTree(BinaryTree):
    def add(self, value):

        def _traverse_and_add(root, value):
            if value < root.value:
                if root.left:
                    _traverse_and_add(root.left, value)
                else:
                    root.left = Node(value)
            if value > root.value:
                if root.right:
                    _traverse_and_add(root.right, value)
                else:
                    root.right = Node(value)

        if self.root is None:
            self.root = Node(value)
        else:
            _traverse_and_add(self.root, value)


    def contains(self, query):

        def _traversal_compare(root, query):
            if root.value == query:
                return True
            if root.left and _traversal_compare(root.left, query):
                return True
            if root.right and _traversal_compare(root.right, query):
                return True
            return False

        if self.root:
            return _traversal_compare(self.root, query)
        else:
            return False
