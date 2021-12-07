from linked_list.linked_list import LinkedList, Node
import pytest


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


def test_linked_list_includes():
    meals = LinkedList()
    meals.insert('spam')
    meals.insert('sandwich')
    assert meals.includes('sandwich') is True
    assert meals.includes('spam') is True
    assert meals.includes('kale') is False


def test_linked_list_includes():
    meals = LinkedList()
    meals.insert('sandwich')
    meals.insert('spam')
    actual = meals.to_string()
    expected = "{ spam } -> { sandwich } -> None"
    assert actual == expected

def test_linked_list_append(test_list):
    test_list.append('d')
    actual = test_list.to_string()
    expected = '{ a } -> { b } -> { c } -> { d } -> None'
    actual == expected


@pytest.fixture
def test_list():
    work_list = LinkedList()
    work_list.insert('c')
    work_list.insert('b')
    work_list.insert('a')
    return work_list
