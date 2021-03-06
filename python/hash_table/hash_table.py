from linked_list.linked_list import LinkedList

class HashTable:
    def __init__(self, size=1024):
        self.table = [None] * size

    def add(self, key, value):
        info = (key, value)
        hash = self.hash(key)

        if self.table[hash] is None:
            self.table[hash] = LinkedList()

        self.table[hash].insert(info)

    def get(self, key):
        hash = self.hash(key)

        bucket = self.table[hash]

        if bucket:
            node = bucket.head
            while node:
                node_key, node_val = node.value
                if node_key == key:
                    return node_val
                node = node.next

        return None

    def contains(self, key):
        hash = self.hash(key)

        bucket = self.table[hash]

        if bucket:
            node = bucket.head
            while node:
                node_key = node.value[0]
                if node_key == key:
                    return True
                node = node.next

        return False

    def hash(self, key):
        summed = sum([ord(char) for char in key])
        prod = summed * 599
        hash = prod % len(self.table)
        return hash
