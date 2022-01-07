# Algorithm: Merge Sort

The merge sort algorithm is pretty cool. It accomplishes sorting by utilizing the rule that generally, things are easier to sort when there are fewer things to sort. Let's start by taking a look at some pseudocode describing the algorithm:

```
ALGORITHM Mergesort(arr)
    DECLARE n <-- arr.length

    if n > 1
      DECLARE mid <-- n/2
      DECLARE left <-- arr[0...mid]
      DECLARE right <-- arr[mid...n]
      // sort the left side
      Mergesort(left)
      // sort the right side
      Mergesort(right)
      // merge the sorted left and right sides together
      Merge(left, right, arr)

ALGORITHM Merge(left, right, arr)
    DECLARE i <-- 0
    DECLARE j <-- 0
    DECLARE k <-- 0

    while i < left.length && j < right.length
        if left[i] <= right[j]
            arr[k] <-- left[i]
            i <-- i + 1
        else
            arr[k] <-- right[j]
            j <-- j + 1

        k <-- k + 1

    if i = left.length
       set remaining entries in arr to remaining values in right
    else
       set remaining entries in arr to remaining values in left
```

Wow. Very cool. So what is actually happening in this word soup of a code block?

## The Breakdown

The first function defined operates recursively. It receives a list, finds the middle index, and then uses that list to split between a left and right side of the input list. Recursion comes in and continues splitting the left and right sides until no longer possible (our base case being `if length(list > 1)` assures that.)

After all of the splitting is done, the Merge function is called. This receives the left and right sides of a list, as well as the list that was split.

Inside of the merge function, we use a while loop to repeatedly compare the left-most value in the left list to the left-most value in the right list. We place whatever value is smallest (in this case we are sorting low to high) sequentially into the original list, stepping one position further into whatever list had the smaller number that loop.

Once either the left or the right list has been completely stepped through (refer to the while loop conditions) the algorithm proceeds to do a bit of cleanup. We can be assured that whatever is left must be larger than what we have already placed into the original list, and thanks to recursion the leftovers are also sorted. Thanks to this, we can simply add whatever values are left over to the end of the original list and continue on with execution.

But wait, we're in a function call stack thanks to recursion! The merge function cascades back up from the smallest pieces available to gradually larger lists, until we finally compare and merge the original left and right side of our input list! The final result is a list sorted in place, no return necessary.

## The Visual

That was a lot of words, so here is a visual to show the process in action:

![merge_sort](merge_sort.jpg)

## A Note Regarding Efficiency

Thanks to the nature of our recursion, the time complexity of this algorithm is O(nlog(n)). Each call of merge_sort calls two more instances of the function, and the final zip back up the call stack can be very rapid.

The space complexity of the algorithm will scale directly with the size of the input list, leaving us with O(n) in bigO notation.
