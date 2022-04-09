from heap.min_heap import min_heap_list


def test_heap_add():
    heap = min_heap_list()
    heap.add(1)
    assert heap.h == [1]


def test_heap_pop():
    heap = min_heap_list()
    heap.add(1)
    assert heap.pop() == 1
    assert heap.h == []


def test_heap_multi():
    heap = min_heap_list()
    heap.add(1)
    heap.add(2)
    heap.add(3)
    assert heap.pop() == 1
    assert heap.pop() == 2
    assert heap.pop() == 3


def test_heap_unordered():
    heap = min_heap_list()
    heap.add(2)
    heap.add(1)
    heap.add(3)
    assert heap.pop() == 1
    assert heap.pop() == 2
    assert heap.pop() == 3


def test_heap_peek():
    heap = min_heap_list()
    values = [4, 6, 2, 7, 3, 5]

    for value in values:
        heap.add(value)

    assert heap.peek() == 2


def test_same_priority():
    heap = min_heap_list()
    heap.add(2)
    heap.add(3)
    heap.add(2)
    assert heap.peek() == 2
