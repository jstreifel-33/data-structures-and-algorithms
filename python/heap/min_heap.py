# Implement a min-heap using a list.

# Important relationships:
# Parent Idx: (idx - 1) // 2
# Left Child Idx: 2 * idx + 1
# Right Child Idx: 2 * idx + 2


class min_heap_list:
    def __init__(self):
        self.h = []

    # retrieve parent, child indices
    def get_parent(self, idx):
        return (idx - 1) // 2

    def get_left_child(self, idx):
        return 2 * idx + 1

    def get_right_child(self, idx):
        return 2 * idx + 2

    # check for parent, children
    def has_parent(self, idx):
        return self.get_parent(idx) >= 0

    def has_left_child(self, idx):
        return self.get_left_child(idx) < len(self.h)

    def has_right_child(self, idx):
        return self.get_right_child(idx) < len(self.h)

    # swap two values in heap
    def swap(self, idx, idx_2):
        self.h[idx], self.h[idx_2] = self.h[idx_2], self.h[idx]

    # maintain min-heap structure
    def heapify_up(self):
        idx = len(self.h) - 1
        while self.has_parent(idx):
            parent = self.get_parent(idx)
            if self.h[idx] < self.h[parent]:
                self.swap(idx, parent)
                idx = parent
                continue
            break

    def heapify_down(self):
        idx = 0
        while self.has_left_child(idx):
            child = self.get_left_child(idx)

            if self.has_right_child:
                right = self.get_right_child
                if self.h[right] < self.h[child]:
                    child = right

            if self.h[child] < self.h[idx]:
                self.swap(idx, child)
                idx = child
                continue
            break

    # peek, add and remove values
    def peek(self):
        return self.h[0]

    def pop(self):
        min_val = self.h[0]

        self.h[0] = self.h.pop()
        self.heapify_down()

        return min_val

    def add(self, val):
        self.h += [val]
        self.heapify_up()
