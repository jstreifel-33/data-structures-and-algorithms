from code_challenges.tree_breadth_first.tree_breadth_first import breadth_first
from trees.trees import BinaryTree, Node


def test_breadth_first_traverse(simple_tree):
    actual = breadth_first(simple_tree)
    expected = ["spam", "eggs", "hash"]
    assert actual == expected

def test_breadth_empty_tree():
    tree = BinaryTree()
    actual = breadth_first(tree)
    expected = []
    assert actual == expected

def test_breadth_large_tree(bst_large):
    actual = breadth_first(bst_large)
    expected = [25, 20, 30, 15, 23, 27, 39]
    assert actual == expected

def test_breadth_uneven_tree():
    tree = BinaryTree()
    tree.root = Node("spam")
    tree.root.right = Node("eggs")

    actual = breadth_first(tree)
    expected = ["spam", "eggs"]
    assert actual == expected
