# Data Structures in Python
## Lists
**Definition:** Ordered, mutable collection of items.
**Syntax:**
```python
my_list = [1, 2, 3, 4]
```
**Operations:** Append, insert, remove, pop, sort, reverse.

## Tuples
**Definition:** Ordered, immutable collection of items.
**Syntax:**
```python
my_tuple = (1, 2, 3, 4)
```
**Operations:** Indexing, slicing (no modification).

## Dictionaries
**Definition:** Collection of key-value pairs, unordered and mutable.
**Syntax:**
```python
my_dict = {'key1': 'value1', 'key2': 'value2'}
```
**Operations:** Add, update, delete items, keys, values.

## Sets
**Definition:** Unordered collection of unique items.
**Syntax:**
```python
my_set = {1, 2, 3, 4}
```
**Operations:** Add, remove, union, intersection, difference.

## Strings
**Definition:** Immutable sequence of characters.
**Syntax:**
```python
my_string = "Hello, World!"
```
**Operations:** Concatenation, slicing, formatting.

## Arrays (using array module)
**Definition:** Ordered, mutable collection of items with the same type.
**Syntax:**
```python
from array import array
my_array = array('i', [1, 2, 3, 4])
```
**Operations:** Append, insert, remove, pop, extend.

## Linked Lists (custom implementation)
**Definition:** Sequence of nodes where each node points to the next node.
**Syntax:** Custom class implementation.

## Stacks (using lists or collections.deque)
**Definition:** LIFO (Last In, First Out) collection.
**Syntax:** Use lists with append() and pop() or collections.deque.
```python
from collections import deque
stack = deque()
stack.append('a')
stack.pop()
```

## Queues (using collections.deque or queue module)
**Definition:** FIFO (First In, First Out) collection.
**Syntax:** Use collections.deque or queue.Queue.
```python
from collections import deque
queue = deque()
queue.append('a')
queue.popleft()
```

## Heaps (using heapq module)
**Definition:** Binary heap, a special tree-based structure.
**Syntax:**
```python
import heapq
heap = []
heapq.heappush(heap, 1)
heapq.heappop(heap)
```