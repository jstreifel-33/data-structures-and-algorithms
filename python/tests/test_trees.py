from trees.trees import BinaryTree, BinarySearchTree, Node


# Feature Tests:
# Can successfully return a collection from a preorder traversal
# Can successfully return a collection from an inorder traversal
# Can successfully return a collection from a postorder traversal

# Can successfully instantiate an empty tree
def test_tree_instance():
    tree = BinaryTree()
    assert tree

# Can successfully instantiate a tree with a single root node
def test_tree_root():
    tree = BinaryTree()
    tree.root = Node("spam")
    assert tree.root.value == "spam"

# Can successfully add a left child and right child to a single root node
def test_tree_left_right():
    tree = BinaryTree()
    tree.root = Node("spam", left=Node("eggs"), right=Node("hash"))
    assert tree.root.value == "spam"
    assert tree.root.left.value == "eggs"
    assert tree.root.right.value == "hash"
