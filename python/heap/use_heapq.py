import heapq


class minHeap:
    def __init__(self):
        self.h = []

    def add(self, val):
        heapq.heappush(self.h, val)

    def pop(self, val):
        heapq.heappop(self.h)

    def __getitem__(self, i):
        return self.h[i]

    def __len__(self):
        return len(self.h)
