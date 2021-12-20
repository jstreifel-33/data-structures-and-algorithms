# Trees

Implementation of binary tree and binary search tree.

## Challenge

Implement a binary tree class with associated methods for data collection manipulation. It should include methods for each of the three depth-first traversals: pre-order, in-order, post-order.

Implement a binary search tree as a subclass of the binary tree, with an Add and Contains method.

## Approach and Efficiency

Tree implemented using a root - left - right system. Values are contained within Node instances which point to the left and right following Node. All associated tree methods utilize recursion in some way to accomplish their tasks.

Efficiency of methods is as follows:

* Binary Tree methods:
  * `pre_order_traverse` - O(h) time complexity where h is the height of the tree. O(N) space complexity, where N is the number of nodes within the tree.
  * `in_order_traverse` - O(h) time complexity where h is the height of the tree. O(N) space complexity, where N is the number of nodes within the tree.
  * `post_order_traverse` - O(h) time complexity where h is the height of the tree. O(N) space complexity, where N is the number of nodes within the tree.
* Binary Search Tree methods:
  * `add(value)` - O(logN) time complexity, where N is number of nodes within tree. O(1) space complexity, only one additional object created.
  * `contains(value)` - O(logN) time complexity, where N is number of nodes within tree. O(1) space complexity, no additional assignments used.

## API

### Binary Tree

* `BinaryTree()` - Instantiate a new Binary Tree
  * `.pre_order_traverse()` - returns an array of values from tree arranged pre-order (root -> left -> right). Raises exception when executed on empty tree.
  * `.in_order_traverse()` - returns an array of values from tree arranged in-order (left -> root -> right). Raises exception when executed on empty tree.
  * `.post_order_traverse()` - returns an array of values from tree arranged post-order (left -> right -> root). Raises exception when executed on empty tree.

### Binary Search Tree

* `BinarySearchTree()` - Instantiate a new Binary Search Tree
  * `.add(value)` - traverses tree to find sorted position for given value and creates new leaf within tree.
  * `.contains(value)` - checks to see if provided value is contained within tree. Returns True if value found and False otherwise.
