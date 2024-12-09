# Estructura de datos en Python
## Listas
**Definición:** Colección ordenada y mutable de elementos.
**Sintaxis:**
```python
my_list = [1, 2, 3, 4]
```
**Operaciones:** Append, insert, remove, pop, sort, reverse.

## Tuplas
**Definición:** Colección ordenada e inmutable de elementos.
**Sintaxis:**
```python
my_tuple = (1, 2, 3, 4)
```
**Operaciones:** Indexing, slicing (no modification).

## Diccionarios
**Definición:** Colección de pares clave-valor, desordenada y mutable.
**Sintaxis:**
```python
my_dict = {'key1': 'value1', 'key2': 'value2'}
```
**Operaciones:** Add, update, delete items, keys, values.

## Conjuntos
**Definición:** Colección desordenada de elementos únicos.
**Sintaxis:**
```python
my_set = {1, 2, 3, 4}
```
**Operaciones:** Add, remove, union, intersection, difference.

## Cadenas
**Definición:** Secuencia inmutable de caracteres.
**Sintaxis:**
```python
my_string = "Hello, World!"
```
**Operaciones:** Concatenation, slicing, formatting.

## Arreglos (using array module)
**Definición:** Colección ordenada y mutable de elementos del mismo tipo.
**Sintaxis:**
```python
from array import array
my_array = array('i', [1, 2, 3, 4])
```
**Operaciones:** Append, insert, remove, pop, extend.

## Listas Enlazadas
**Definición:** Secuencia de nodos donde cada nodo apunta al siguiente nodo.
**Sintaxis:**
```python
# Create a Node class to create a node
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Create a LinkedList class
class LinkedList:
    def __init__(self):
        self.head = None
    ...
```

## Pilas
**Definición:** Colección LIFO (Last In, First Out).
**Sintaxis:**
Usar listas con append y pop o collections.deque.
```python
from collections import deque
stack = deque()
stack.append('a')
stack.pop()
```

## Colas
**Definición:** Colección FIFO (First In, First Out).
**Sintaxis:**
Usar collections.deque o queue.Queue.
```python
from collections import deque
queue = deque()
queue.append('a')
queue.popleft()
```

## Montículo
**Definición:** Montículo binario, una estructura especial basada en árboles.
**Sintaxis:**
```python
import heapq
heap = []
heapq.heappush(heap, 1)
heapq.heappop(heap)
```