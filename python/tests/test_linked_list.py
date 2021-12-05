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
    meals.head = breakfast
    assert meals.head.value == 'spam'


def test_linked_list_insert():
    meals = LinkedList()
    meals.insert('sandwich')
    assert meals.head.value == 'sandwich'

# def test_linked_list_includes():
#     meals = LinkedList()
#     meals.insert('spam')
#     meals.insert('sandwich')
#     assert meals.includes('spam') is True
#     assert meals.includes('kale') is False
