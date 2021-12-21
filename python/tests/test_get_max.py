from attr import validate
from trees.trees import BinaryTree, Node
import pytest

def test_find_tree_max(sample_tree):
    assert sample_tree.get_max_value() == 15

def test_find_tree_max_just_root(just_root_tree):
    assert just_root_tree.get_max_value() == 7

def test_max_empty():
    tree = BinaryTree()
    with pytest.raises(ValueError) as e:
        tree.get_max_value()

    assert str(e.value) == "Cannot perform operation on empty tree!"


@pytest.fixture
def sample_tree():
    tree = BinaryTree()
    tree.root = Node(3, Node(4, Node(7), Node(11)), Node(9, Node(15), Node(3)))
    return tree

@pytest.fixture
def just_root_tree():
    tree = BinaryTree()
    tree.root = Node(7)
    return tree
