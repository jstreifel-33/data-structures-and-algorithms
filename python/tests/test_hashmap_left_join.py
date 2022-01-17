from code_challenges.hashmap_left_join.hapmap_left_join import left_join

def test_all_match():
    map_1 = {
        'diligent': 'employed',
        'fond': 'enamored',
        'guide': 'usher',
    }
    map_2 = {
        'diligent': 'idle',
        'fond': 'averse',
        'guide': 'follow',
    }

    actual = left_join(map_1, map_2)
    expected = [
        ['diligent', 'employed', 'idle'],
        ['fond', 'enamored', 'averse'],
        ['guide', 'usher', 'follow'],
    ]

    assert actual == expected


def test_some_match():
    map_1 = {
        'diligent': 'employed',
        'fond': 'enamored',
        'guide': 'usher',
    }
    map_2 = {
        'diligent': 'idle',
        'flow': 'jam',
        'guide': 'follow',
    }

    actual = left_join(map_1, map_2)
    expected = [
        ['diligent', 'employed', 'idle'],
        ['fond', 'enamored', None],
        ['guide', 'usher', 'follow'],
    ]

    assert actual == expected


def test_no_match():
    map_1 = {
        'diligent': 'employed',
        'fond': 'enamored',
        'guide': 'usher',
    }
    map_2 = {
        'wrath': 'delight',
        'flow': 'jam',
        'happy': 'sad',
    }

    actual = left_join(map_1, map_2)
    expected = [
        ['diligent', 'employed', None],
        ['fond', 'enamored', None],
        ['guide', 'usher', None],
    ]

    assert actual == expected


def test_empty_left():
    map_1 = {}
    map_2 = {
        'wrath': 'delight',
        'flow': 'jam',
        'happy': 'sad',
    }

    actual = left_join(map_1, map_2)
    expected = []

    assert actual == expected


def test_empty_right():
    map_1 = {
        'diligent': 'employed',
        'fond': 'enamored',
        'guide': 'usher',
    }
    map_2 = {}

    actual = left_join(map_1, map_2)
    expected = [
        ['diligent', 'employed', None],
        ['fond', 'enamored', None],
        ['guide', 'usher', None],
    ]

    assert actual == expected
