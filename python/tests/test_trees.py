from trees.trees import BinaryTree, BinarySearchTree, Node
import pytest


# Feature Tests:

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

# Can successfully return a collection from a preorder traversal
def test_tree_preorder(simple_tree):
    actual = simple_tree.pre_order_traverse()
    print(actual)
    expected = ["spam", "eggs", "hash"]
    assert actual == expected

# Can successfully return a collection from an inorder traversal
def test_tree_inorder(simple_tree):
    actual = simple_tree.in_order_traverse()
    print(actual)
    expected = ["eggs", "spam", "hash"]
    assert actual == expected

# Can successfully return a collection from a postorder traversal
def test_tree_postorder(simple_tree):
    actual = simple_tree.post_order_traverse()
    print(actual)
    expected = ["eggs", "hash", "spam"]
    assert actual == expected

@pytest.fixture
def simple_tree():
    tree = BinaryTree()
    tree.root = Node("spam", left=Node("eggs"), right=Node("hash"))
    return tree
