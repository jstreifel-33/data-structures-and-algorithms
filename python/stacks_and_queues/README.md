# Stacks and Queues

Implementation of stack and queue data structures. A stack is a node-based First In Last Out data structure which can only have data added to and taken from the "top" of the data collection. A queue is a node-based First In First Out data  structure which can have data added to the back and taken from the front of the queue.

## Challenge

Implement a stack and queue class with associated methods for data collection manipulation.

## Approach and Efficiency

Since both data structures require the Node class, I created a Node class in it's own .py file. From there I used the provided tests to guide the development process.

Efficiency of methods is as follows:

* Stack methods
  * `.push(value)` - O(1), all operations are assignment based.
  * `.pop()` - O(1), all operations are assignment based.
  * `.is_empty()` - O(1), single `if` statement and return used.
  * `.peek()` - O(1), all operations are assignment based.
* Queue methods
  * `.enqueue(value)` - O(1), all operations are assignment based.
  * `.dequeue()` - O(1), all operations are assignment based.
  * `.peek()` - O(1), all operations are assignment based.
  * `.is_empty()` - O(1), single `if` statement and return used.

## API

### Stack class

* `Stack()` - used to instantiate a new stack collection.
  * `.push(value)` - adds a node with provided value to the top of the collection.
  * `.pop()` - removes a node from the top of a stack collection and returns its value.
  * `.is_empty()` - used to check if a stack is empty. Returns True if Stack contains no nodes and False otherwise.
  * `.peek()` - checks and returns the value of the top node in a stack. Does not remove top node, and returns an exception if a Queue is empty.

### Queue class

* `Queue()` - used to instantiate a new Queue collection.
  * `.enqueue(value)` - adds a node with provided value to the back of a queue.
  * `.dequeue()` - removes the node at the front of a Queue collection and returns its value.
  * `.peek()` - checks and returns the value of the front node in a stack. Does not remove the front node, and returns an exception if a Queue is empty.
  * `.is_empty()` - used to check if a stack is empty. Returns True if Queue contains no nodes and False otherwise.
