from trees.trees import BinaryTree, BinarySearchTree, Node
import pytest

#########
# TREES
#########

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
