from linked_list.linked_list import LinkedList, Node


def test_import():
    assert LinkedList


def test_node_instantiation():
    breakfast = Node('spam')
    assert breakfast.value == 'spam'
    assert breakfast.next is None


def test_linked_list_instantiation():
    breakfast = Node('spam')
    meals = LinkedList()
    LinkedList.head = breakfast
    assert meals.head.value == 'spam'


def test_linked_list_instantiation():
    meals = LinkedList()
    meals.insert('sandwich')
    assert meals.head.value == 'sandwich'

