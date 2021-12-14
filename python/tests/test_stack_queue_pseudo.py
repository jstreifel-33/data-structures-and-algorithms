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
