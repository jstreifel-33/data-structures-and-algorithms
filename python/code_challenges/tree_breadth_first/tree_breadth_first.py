from collections import deque

def breadth_first(tree):
    # Initialize deque for use as queue:
    ### .appendleft() <- add to queue (left side)
    ### .pop() <- remove from queue (right side)
    queue = deque()
