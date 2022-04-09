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
