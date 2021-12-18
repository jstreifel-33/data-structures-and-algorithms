import pytest
from code_challenges.stack_queue_brackets.stack_queue_bracket import validate_brackets


def test_passing_string():
    actual = validate_brackets("(){[]}")
    expected = True
    assert actual == expected


def test_failing_string():
    actual = validate_brackets("(){[}]")
    expected = False
    assert actual == expected


def test_passing_string_with_characters():
    actual = validate_brackets("(potato){{cucumber[pear]}}")
    expected = True
    assert actual == expected


def test_failing_string_with_characters():
    actual = validate_brackets("(cat{{hamster[}}])")
    expected = False
    assert actual == expected


def test_first_bracket_close():
    actual = validate_brackets(")[]()")
    expected = False
    assert actual == expected

