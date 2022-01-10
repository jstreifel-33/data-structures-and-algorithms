def quick_sort(li, left=None, right=None):
    if left is None:
        left = 0
    if right is None:
        right = len(li)-1
    if left < right:
        print(left, right)
        pos = partition(li, left, right)
        print(pos)
        quick_sort(li, left, pos - 1)
        quick_sort(li, pos + 1, right)


def partition(li, left, right):
    pivot = li[right]
    low = left - 1
    for i in range(left,right):
        if li[i] <= pivot:
            low += 1
            swap(li, i, low)
    swap(li, right, low + 1)
    return low + 1


def swap(li, i, low):
    temp = li[i]
    li[i] = li[low]
    li[low] = temp
