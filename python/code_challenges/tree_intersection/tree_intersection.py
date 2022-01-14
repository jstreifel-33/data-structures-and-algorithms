from hash_table.hash_table import HashTable

def tree_intersection(tree_1, tree_2):
    ht = HashTable()
    intersections = set()

    def ht_traversal(root, ht):
        ht.add(root.value)
        if root.left:
            ht_traversal(root.left, ht)
        if root.right:
            ht_traversal(root.right, ht)

    def intersection_traversal(root, ht, intersections):
        if ht.contains(root.value):
            intersections.add()
        if root.left:
            ht_traversal(root.left, ht, intersections)
        if root.right:
            ht_traversal(root.right, ht, intersections)

        return intersections

    ht_traversal(tree_1.root, ht)

    return intersection_traversal(tree_2.root, ht, intersections)

