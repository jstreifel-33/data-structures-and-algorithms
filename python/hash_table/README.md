# Hash Tables

Implementation of hash table data structure. A hash table is essentially just a list of predefined length, usually rather large. Key-value pairs are stored by converting the key string into a numeric value using a hash function. The resulting number is used to index the list and choose where to store the key-value pair.

While generally unlikely, two keys can share the same hash value, which is called a **collision**. To handle this, linked lists can be used within the hash table list to store multiple pieces of information in the same index.

## Challenge

Implement a hash table class, including add, get, contains, and hash methods.

## Approach & Efficiency

For this implementation I used a list with a default length of 1024 for storing information. The hashing algorithm utilizes the ASCII values of characters to calculate a value between 0 and 1023.

Efficiency Analysis:

* `.add()` - O(N) space complexity, since space required for storing added value will directly scale with the size N of the value being stored. O(1) best case time complexity, and O(N) worst case, where N is the number of items currently in the hash table, if all adds are collisions.
* `.get()` - O(1) space complexity, since getting simply involves navigating the data structure and returning the result. O(1) time complexity best case, and O(N) worst case if all adds have been collisions
* `.contains()` - O(1) space complexity, since only navigation of existing values and returning a boolean value. O(1) time complexity best case(miss or only one value in bucket), and O(N) worst case if all adds have been collisions
* `.hash()` - O(1) space complexity, since we are just doing calculations and returning a numeric value, O(N) time complexity due to iterating through key string for calculation.

## API

* `HashTable(size=1024)` - instantiate an empty hash table. All values within table will be `None` by default. Table defaults to size 1024 but can be changed.

  * `HashTable.add(key, value)` - accepts a key string and value as arguments. Add a key-value pair to a hash table. Will chain entries in a linked list in the case of hash collisions.
  * `HashTable.get(key)` - accepts a key string and returns the associated stored value from the hash table. Will return `None` if value not found (not recommended to store keys with value `None` to avoid confusion).
  * `HashTable.contains(key)` - accepts a key string as argument and searches hash table to see if key is contained within. Return boolean.
  * `HashTable.hash(key)` - accepts key string as argument and returns an integer resulting from executing hashing algorithm on string.
