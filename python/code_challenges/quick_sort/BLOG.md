# Algorithm: Quick Sort

Quick sort is yet another sorting algorithm, that gives merge sort a run for it's money. It uses pivot points within a given list to divide and conquer a list.

As always, let's start by taking a look at some pseudocode:

```pseudo
ALGORITHM QuickSort(arr, left, right)
    if left < right
        // Partition the array by setting the position of the pivot value
        DEFINE position <-- Partition(arr, left, right)
        // Sort the left
        QuickSort(arr, left, position - 1)
        // Sort the right
        QuickSort(arr, position + 1, right)

ALGORITHM Partition(arr, left, right)
    // set a pivot value as a point of reference
    DEFINE pivot <-- arr[right]
    // create a variable to track the largest index of numbers lower than the defined pivot
    DEFINE low <-- left - 1
    for i <- left to right do
        if arr[i] <= pivot
            low++
            Swap(arr, i, low)

     // place the value of the pivot location in the middle.
     // all numbers smaller than the pivot are on the left, larger on the right.
     Swap(arr, right, low + 1)
    // return the pivot index point
     return low + 1

ALGORITHM Swap(arr, i, low)
    DEFINE temp;
    temp <-- arr[i]
    arr[i] <-- arr[low]
    arr[low] <-- temp
```

Make sense? No? Great! Let's break it down.

## The Breakdown

The quick sort algorithm is started by invoking quick_sort(list). In our version, we've set left and right to the first and last values in a list on the first pass.

Next we use partition to grab a pivot value (right value in list) and make repeated comparisons to find where within the list values the pivot value belongs. Other values are placed to either left or right of the pivot. With each pivot swap, we increment low by 1 and use the swap() function to make a quick shuffle of values. After checking each value in the list, we return whatever the value of low is +1. This value is used in our recursion cases, which bloom outward from the low value.

Recursion is used to call quick_sort to the left and right of the pivot value, cascading outward until the list is fully sorted.

Hopefully that helps *sort* things out!
