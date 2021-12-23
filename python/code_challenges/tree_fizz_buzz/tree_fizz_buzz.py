class KNode():
    def __init__(self, value = None):
        self.value = value
        self.children = []

class KAryTree():
    def __init__(self):
        self.root = None

def fizz_buzz_tree(tree):
    output_tree = KAryTree()

    def fizz_buzz_traversal(root):

        if root.value % 3 == 0 and root.value % 5 == 0:
            new_node = KNode('fizzbuzz')
        elif root.value % 3 == 0:
            new_node = KNode('fizz')
        elif root.value % 5 == 0:
            new_node = KNode('buzz')
        else:
            new_node = KNode(str(root.value))

        new_node.children = [fizz_buzz_traversal(child) for child in root.children]

        return new_node

    if tree.root is not None:
        output_tree.root = fizz_buzz_traversal(tree.root)

    return output_tree


