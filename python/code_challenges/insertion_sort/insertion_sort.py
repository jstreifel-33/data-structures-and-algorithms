def insertion_sort(num_list):
    for idx in range(1, len(num_list)):
        compare = idx - 1
        num = num_list[idx]

        while compare >= 0 and num < num_list[compare]:
            num_list[compare + 1] = num_list[compare]
            compare = compare - 1

        num_list[compare + 1] = num
