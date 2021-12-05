from linked_list.linked_list import LinkedList, Node


def test_import():
    assert LinkedList


def test_linked_list_instantiation():
    assert LinkedList()


def test_node_instantiation():
    breakfast = Node('spam')
    assert breakfast.value == 'spam'
    assert breakfast.next is None
