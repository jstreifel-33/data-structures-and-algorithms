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

def test_BST_instance():
    bst = BinarySearchTree()
    assert isinstance(bst, BinaryTree)

def test_BST_add():
    bst = BinarySearchTree()
    #add root
    bst.add(25)
    #add level 1
    bst.add(20)
    bst.add(30)
    actual = bst.in_order_traverse()
    expected = [20, 25, 30]
    assert actual == expected

def test_BST_add_height_2(bst_large):
    actual = bst_large.in_order_traverse()
    expected = [15, 20, 23, 25, 27, 30, 39]
    assert actual == expected

def test_BST_contains_25(bst_large):
    assert bst_large.contains(25)

def test_BST_contains_25(bst_large):
    assert bst_large.contains(15)

def test_BST_contains_25(bst_large):
    assert bst_large.contains(30)

def test_BST_not_contains_47(bst_large):
    assert bst_large.contains(47) is False

# Fixtures
@pytest.fixture
def simple_tree():
    tree = BinaryTree()
    tree.root = Node("spam", left=Node("eggs"), right=Node("hash"))
    return tree

@pytest.fixture
def bst_large():
    bst = BinarySearchTree()
    #add root
    bst.add(25)
    #add level 1
    bst.add(20)
    bst.add(30)
    #add level 2
    bst.add(15)
    bst.add(23)
    bst.add(39)
    bst.add(27)
    return bst
