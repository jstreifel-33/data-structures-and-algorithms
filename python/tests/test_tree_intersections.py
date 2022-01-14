from code_challenges.tree_intersection.tree_intersection import tree_intersection
from trees.trees import BinarySearchTree

def test_basic_intersections():
    tree_1 = BinarySearchTree()
    for num in [1,2,3,4,5,6]:
        tree_1.add(num)

    tree_2 = BinarySearchTree()
    for num in [4,5,6,7,8,9,10]:
        tree_2.add(num)

    actual = tree_intersection(tree_1, tree_2)
    expected = {4,5,6}

    assert actual == expected


def test_no_intersection():
    tree_1 = BinarySearchTree()
    for num in [1,2,3,4,5]:
        tree_1.add(num)

    tree_2 = BinarySearchTree()
    for num in [6,7,8,9,10]:
        tree_2.add(num)

    actual = tree_intersection(tree_1, tree_2)
    expected = set()

    assert actual == expected


def test_shuffled_trees():
    tree_1 = BinarySearchTree()
    for num in [1,4,2,3,5]:
        tree_1.add(num)

    tree_2 = BinarySearchTree()
    for num in [4,2,1,5,3]:
        tree_2.add(num)

    actual = tree_intersection(tree_1, tree_2)
    expected = {1,2,3,4,5}

    assert actual == expected


def test_negative_numbers():
    tree_1 = BinarySearchTree()
    for num in [-2,4,2,-21,5]:
        tree_1.add(num)

    tree_2 = BinarySearchTree()
    for num in [7,-21,8,9,-2]:
        tree_2.add(num)

    actual = tree_intersection(tree_1, tree_2)
    expected = {-2,-21}

    assert actual == expected
