from linked_list.linked_list import LinkedList
from code_challenges.linked_list_zip.linked_list_zip import linked_list_zip
import pytest

def test_linked_list_zip(zip_list_a, zip_list_1):
    result_list = linked_list_zip(zip_list_a, zip_list_1)
    actual = result_list.to_string()
    expected = '{ a } -> { 1 } -> { b } -> { 2 } -> { c } -> { 3 } -> None'
    assert actual == expected

def test_linked_list_zip_long_first(zip_list_long, zip_list_a):
    result_list = linked_list_zip(zip_list_long, zip_list_a)
    actual = result_list.to_string()
    expected = '{ 1 } -> { a } -> { 2 } -> { b } -> { 3 } -> { c } -> { 4 } -> { 5 } -> None'
    assert actual == expected

def test_linked_list_zip_long_second(zip_list_long, zip_list_a):
    result_list = linked_list_zip(zip_list_a, zip_list_long)
    actual = result_list.to_string()
    expected = '{ a } -> { 1 } -> { b } -> { 2 } -> { c } -> { 3 } -> { 4 } -> { 5 } -> None'
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
    linked_list.insert('5')
    linked_list.insert('4')
    linked_list.insert('3')
    linked_list.insert('2')
    linked_list.insert('1')
    return linked_list
