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

        return _traversal(self.root)

    def in_order_traverse(self):

        def _traversal(root, result = []):
            if root.left:
                _traversal(root.left, result)
            result.append(root.value)
            if root.right:
                _traversal(root.right, result)
            return result

        return _traversal(self.root)

    def post_order_traverse(self):

        def _traversal(root, result = []):
            if root.left:
                _traversal(root.left, result)
            if root.right:
                _traversal(root.right, result)
            result.append(root.value)
            return result

        return _traversal(self.root)


class BinarySearchTree():
    pass

