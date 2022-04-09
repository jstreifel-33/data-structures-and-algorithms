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


class maxHeapObj:
    def __init__(self, val):
        self.val = val

    def __lt__(self, other):
        return self.val > other.val

    def __eq__(self, other):
        return self.val == other.val

    def __str__(self):
        return str(self.val)


class maxHeap(minHeap):
    def add(self, val):
        heapq.heappush(self.h, maxHeapObj(val))

    def pop(self, val):
        heapq.heappop(self.h, maxHeapObj(val))

    def __getitem__(self, i):
        return self.h[i].val
