# Challenge Summary

Write a function called tree_intersection that takes two binary trees as parameters, and returns the numbers shared between the two.

## Whiteboard Process

![tree intersection wb](tree_intersection.jpg)

## Approach & Efficiency

I used depth first traversal on both trees, first placing all values from tree_1 into a hash table, and second comparing the values of tree_2 to the hash table. Any matches found get added to a set, to account for any repetitions. Each unique number found to be shared will only occur in the set once.

Efficiency:

* Time: O(h) where h is the combined height of the two trees, since depth first traversal being used and hash tables have O(1) time efficiency.
* Space: O(N) worst case where N is the number of nodes in the first tree. All values from first tree must be stored in the hash table.

## Solution

`tree_intersection(tree_1, tree_2)` - accepts two binary trees as arguments and returns a set containing all shared values between the two. Will return an empty set in the case of no intersections.
