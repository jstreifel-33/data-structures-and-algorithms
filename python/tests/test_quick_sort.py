from code_challenges.quick_sort.quick_sort import quick_sort


def test_quick_sort_normal():
    test_list = [2, 7, 3, 9, 5]
    quick_sort(test_list)
    assert test_list == [2, 3, 5, 7, 9]


def test_quick_sort_longer():
    test_list = [5, 2, 13, 17, 1, 19, 11, 3, 10, 0]
    quick_sort(test_list)
    assert test_list == [0, 1, 2, 3, 5, 10, 11, 13, 17, 19]


def test_quick_sort_dupes():
    test_list = [1, 3, 1, 5, 1, 3, 5]
    quick_sort(test_list)
    assert test_list == [1, 1, 1, 3, 3, 5, 5]


def test_quick_sort_negative():
    test_list = [6, 3, -1, 19, -22]
    quick_sort(test_list)
    assert test_list == [-22, -1, 3, 6, 19]


def test_quick_sort_nearly_sorted():
    test_list = [2, 4, 8, 19, 11]
    quick_sort(test_list)
    assert test_list == [2, 4, 8, 11, 19]
