from code_challenges.tree_fizz_buzz.tree_fizz_buzz import KAryTree, KNode, fizz_buzz_tree
import pytest

def test_tree_fizz_buzz_small(small_k_ary):
    output_tree = fizz_buzz_tree(small_k_ary)
    assert output_tree.root.value == '7'
    val_children = [child.value for child in output_tree.root.children]
    assert val_children == ['fizz', 'fizzbuzz', 'buzz']


@pytest.fixture
def small_k_ary():
    tree = KAryTree()
    tree.root = KNode(7)

    children = [KNode(3), KNode(15), KNode(5)]
    for child in children:
        tree.root.children.append(child)

    return tree
