from code_challenges.merge_sort.merge_sort import merge_sort


def test_merge_sort_normal_behavior():
    unsorted_list = [3, 6, 2, 9, 7, 0]
    merge_sort(unsorted_list)
    assert unsorted_list == [0, 2, 3, 6, 7, 9]


def test_merge_sort_includes_negative():
    unsorted_list = [3, 7, -4, 11, -22, 2]
    merge_sort(unsorted_list)
    assert unsorted_list == [-22, -4, 2, 3, 7, 11]


def test_merge_sort_odd_list():
    unsorted_list = [3, 6, 2, 9, 7]
    merge_sort(unsorted_list)
    assert unsorted_list == [2, 3, 6, 7, 9]

def test_merge_sort_few_uniques():
    unsorted_list = [2, 6, 2, 7, 6, 7, 2]
    merge_sort(unsorted_list)
    assert unsorted_list == [2, 2, 2, 6, 6, 7, 7]

