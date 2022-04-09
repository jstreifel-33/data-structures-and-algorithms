# Implement a min-heap using a list.

# Important relationships:
# Parent Idx: (idx - 1) // 2
# Left Child Idx: 2 * idx + 1
# Right Child Idx: 2 * idx + 2


class min_heap_list:
    def __init__(self):
        self.h = []

    def get_parent(self, idx):
        return (idx - 1) // 2

    def get_left_child(self, idx):
        return 2 * idx + 1

    def get_right_child(self, idx):
        return 2 * idx + 2

    def swap(self, idx, idx_2):
        self.h[idx], self.h[idx_2] = self.h[idx_2], self.h[idx]
