from linked_list.linked_list import LinkedList
from code_challenges.linked_list_zip.linked_list_zip import linked_list_zip
import pytest

def test_linked_list_zip(zip_list_a, zip_list_1):
    result_list = linked_list_zip(zip_list_a, zip_list_1)
    expected = result_list.to_string()
    actual = '{ a } -> { 1 } -> { b } -> { 2 } -> { c } -> { 3 } -> None'
    assert actual == expected


@pytest.fixture
def zip_list_a():
    linked_list = LinkedList()
    linked_list.insert('c')
    linked_list.insert('b')
    linked_list.insert('a')
    return linked_list

@pytest.fixture
def zip_list_1():
    linked_list = LinkedList()
    linked_list.insert('3')
    linked_list.insert('2')
    linked_list.insert('1')
    return linked_list

@pytest.fixture
def zip_list_long():
    linked_list = LinkedList()
    linked_list.append('1')
    linked_list.append('2')
    linked_list.append('3')
    linked_list.append('4')
    linked_list.append('5')
    return linked_list
