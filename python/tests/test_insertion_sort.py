from code_challenges.insertion_sort.insertion_sort import insertion_sort


def test_sort_normal():
    test_list = [6, 2, 9, 11, 0, 22, 17]
    insertion_sort(test_list)

    assert test_list == [0, 2, 6, 9, 11, 17, 22]


def test_sort_one_item():
    test_list = [7]
    insertion_sort(test_list)

    assert test_list == [7]


def test_sort_empty_list():
    test_list = []
    insertion_sort(test_list)

    assert test_list == []


def test_sort_already_sorted():
    test_list = [0, 2, 6, 9, 11, 17, 22]
    insertion_sort(test_list)

    assert test_list == [0, 2, 6, 9, 11, 17, 22]
