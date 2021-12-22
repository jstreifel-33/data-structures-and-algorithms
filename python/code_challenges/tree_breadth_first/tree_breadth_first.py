from collections import deque

def breadth_first(tree):
    """
    Returns a list containing all values within a binary tree as
    encountered using breadth-first (top-down left-right)
    traversal. Returns an empty list if argument is an
    empty tree.
    """
    # Initialize deque for use as queue:
    ### .appendleft() <- add to queue (left side)
    ### .pop() <- remove from queue (right side)
    queue = deque()

    #initialize return list
    traversal_list = []

    if tree.root is None:
        return traversal_list

    queue.appendleft(tree.root)

    while len(queue):
        front = queue.pop()

        traversal_list.append(front.value)

        if front.left is not None:
            queue.appendleft(front.left)
        if front.right is not None:
            queue.appendleft(front.right)


    return traversal_list

