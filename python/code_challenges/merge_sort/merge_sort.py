def merge_sort(num_list):
    n = len(num_list)

    if n > 1:
        mid = n//2
        left = num_list[0:mid]
        right = num_list[mid:n]

        merge_sort(left)
        merge_sort(right)
        merge(left, right, num_list)

def merge(left, right, num_list):
    i = 0
    j = 0
    k = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            num_list[k] = left[i]
            i += 1
        else:
            num_list[k] = right[j]
            j += 1
        k += 1

    if i == len(left):
        for pos in range(k, len(num_list)):
            num_list[pos] = right[j]
            j+=1
    else:
        for pos in range(k, len(num_list)):
            num_list[pos] = left[i]
            i+=1

