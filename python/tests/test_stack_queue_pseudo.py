from stacks_and_queues.stacks import InvalidOperationError
from code_challenges.stack_queue_pseudo.stack_queue_pseudo import PseudoQueue
import pytest

def test_instantiation():
    q = PseudoQueue()
    assert q


def test_single_value():
    q = PseudoQueue()
    q.enqueue('spam')
    actual = q.dequeue()
    expected = 'spam'
    assert actual == expected


def test_many_values():
    q = PseudoQueue()
    q.enqueue('spam')
    q.enqueue('eggs')
    q.enqueue('sparrow')
    assert q.dequeue() == 'spam'
    assert q.dequeue() == 'eggs'
    assert q.dequeue() == 'sparrow'


def test_dequeue_empty_exception():
    q = PseudoQueue()
    with pytest.raises(InvalidOperationError) as e:
        q.dequeue()

    assert str(e.value) == 'Operation cannot be performed on empty collection'


def test_dequeue_out_of_values():
    q = PseudoQueue()
    q.enqueue('spam')
    q.enqueue('eggs')
    q.dequeue()
    q.dequeue()
    with pytest.raises(InvalidOperationError) as e:
        q.dequeue()

    assert str(e.value) == 'Operation cannot be performed on empty collection'
