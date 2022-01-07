def merge_sort(unsorted_list):
    n = len(unsorted_list)

    if n > 1:
        mid = n//2
        left = unsorted_list[:mid]
        right = unsorted_list[mid:]

        merge_sort(left)
        merge_sort(right)
        merge(left, right, unsorted_list)

def merge(left, right, unsorted_list):
    i = 0
    j = 0
    k = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[i]:
            unsorted_list[k] = left[i]
            i += 1
        else:
            unsorted_list[k] = right[j]
            j += 1

        k += 1

    if i == len(left):
        unsorted_list = unsorted_list + right
    else:
        unsorted_list = unsorted_list + left
