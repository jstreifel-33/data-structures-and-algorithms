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


class BinarySearchTree():
    pass

