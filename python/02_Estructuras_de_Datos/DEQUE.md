# **Deque en Python** 🔄🐍

## **📖 Descripción**  
Un **deque** (pronunciado "deck") es una estructura de datos que significa "double-ended queue" (cola de dos extremos). A diferencia de una lista o arreglo común, un deque permite la inserción y eliminación de elementos desde ambos extremos: **el frente** y **el final**. Esto hace que los deques sean extremadamente útiles en situaciones donde se requiere un acceso rápido desde ambos extremos de la cola.

En Python, los deques están disponibles en el módulo `collections` y se utilizan comúnmente cuando se necesita un rendimiento eficiente al agregar o eliminar elementos desde ambos extremos.

---

## **📌 Contenido**  
1. ¿Qué es un Deque?  
2. Características del Deque  
3. Operaciones básicas en Deque  
4. Métodos útiles de Deque  
5. Ejemplos prácticos  
6. Comparativa con otras estructuras  
7. Recursos adicionales  

---

## **📍 1. ¿Qué es un Deque?**  
Un **deque** es una estructura de datos que permite realizar inserciones y eliminaciones de elementos tanto en el **frente** como en el **final** de la cola de manera eficiente, es decir, con una complejidad de tiempo constante O(1). Esto lo hace muy útil en escenarios donde se necesitan operaciones de este tipo sin preocuparse por la eficiencia.

### Ejemplo visual de un Deque:

```
| 10 | 20 | 30 | 40 | 50 | 60 |
  ^                       ^
 Front                  Rear
```

---

## **📍 2. Características del Deque**  
1. **Acceso en ambos extremos**: Puedes agregar o quitar elementos tanto en el principio como en el final.
2. **Complejidad constante**: Las operaciones de inserción y eliminación son O(1) en ambos extremos.
3. **Mutabilidad**: Los deques son mutables, es decir, puedes modificarlos después de su creación.
4. **Orden de los elementos**: Los elementos en un deque se mantienen en el orden en que se agregan.
5. **Flexibilidad**: Los deques se utilizan en una variedad de situaciones, como colas de prioridad, algoritmos de búsqueda, y más.

---

## **📍 3. Operaciones básicas en Deque**  
Al ser una estructura de datos eficiente y flexible, un deque admite varias operaciones. Las operaciones más comunes son:

### 1. **Agregar elementos**:
- **append()**: Agrega un elemento al final del deque.

```python
from collections import deque

# Crear un deque
mi_deque = deque([10, 20, 30])

# Agregar un elemento al final
mi_deque.append(40)
print(mi_deque)  # Salida: deque([10, 20, 30, 40])
```

- **appendleft()**: Agrega un elemento al principio del deque.

```python
mi_deque.appendleft(5)
print(mi_deque)  # Salida: deque([5, 10, 20, 30, 40])
```

### 2. **Eliminar elementos**:
- **pop()**: Elimina y devuelve el último elemento del deque.

```python
ultimo = mi_deque.pop()
print(ultimo)    # Salida: 40
print(mi_deque)  # Salida: deque([5, 10, 20, 30])
```

- **popleft()**: Elimina y devuelve el primer elemento del deque.

```python
primero = mi_deque.popleft()
print(primero)   # Salida: 5
print(mi_deque)  # Salida: deque([10, 20, 30])
```

### 3. **Acceso a elementos**:
Puedes acceder a los elementos del deque de manera similar a una lista:

```python
# Acceder al primer y último elemento
print(mi_deque[0])  # Salida: 10
print(mi_deque[-1]) # Salida: 30
```

---

## **📍 4. Métodos útiles de Deque**  
El módulo `collections.deque` ofrece varios métodos adicionales para trabajar con deques.

- **extend()**: Extiende el deque agregando todos los elementos de un iterable al final.

```python
mi_deque.extend([40, 50])
print(mi_deque)  # Salida: deque([10, 20, 30, 40, 50])
```

- **extendleft()**: Extiende el deque agregando todos los elementos de un iterable al principio (el orden de los elementos se invierte).

```python
mi_deque.extendleft([5, 0])
print(mi_deque)  # Salida: deque([0, 5, 10, 20, 30, 40, 50])
```

- **rotate()**: Rota los elementos del deque. Si el número es positivo, los elementos se mueven a la derecha. Si es negativo, se mueven a la izquierda.

```python
mi_deque.rotate(1)
print(mi_deque)  # Salida: deque([50, 0, 5, 10, 20, 30, 40])

mi_deque.rotate(-2)
print(mi_deque)  # Salida: deque([10, 20, 30, 40, 50, 0, 5])
```

- **clear()**: Elimina todos los elementos del deque.

```python
mi_deque.clear()
print(mi_deque)  # Salida: deque([])
```

- **count()**: Devuelve el número de veces que un elemento aparece en el deque.

```python
mi_deque = deque([10, 20, 30, 10, 10])
print(mi_deque.count(10))  # Salida: 3
```

---

## **📍 5. Ejemplos prácticos**  

### 📌 **Ejemplo 1: Implementación de una cola con deque**  
Un deque es ideal para implementar una cola donde los elementos se agregan al final y se eliminan desde el principio.

```python
# Crear un deque vacío
cola = deque()

# Agregar elementos a la cola
cola.append("A")
cola.append("B")
cola.append("C")
print(cola)  # Salida: deque(['A', 'B', 'C'])

# Eliminar elementos de la cola
print(cola.popleft())  # Salida: 'A'
print(cola)  # Salida: deque(['B', 'C'])
```

### 📌 **Ejemplo 2: Implementación de una cola de doble extremo**  
Un deque puede ser utilizado como una cola de doble extremo, donde puedes agregar y quitar elementos desde ambos extremos.

```python
# Crear un deque vacío
doble_extremo = deque()

# Agregar elementos a ambos extremos
doble_extremo.append("A")    # Agregar al final
doble_extremo.appendleft("B") # Agregar al principio
print(doble_extremo)  # Salida: deque(['B', 'A'])

# Eliminar elementos de ambos extremos
print(doble_extremo.pop())      # Salida: 'A'
print(doble_extremo.popleft())  # Salida: 'B'
print(doble_extremo)  # Salida: deque([])
```

---

## **📍 6. Comparativa con otras estructuras**  

### **Deque vs Lista**  
- **Listas** en Python permiten acceso eficiente al índice y operaciones de inserción y eliminación solo al final. Sin embargo, insertar o eliminar elementos al principio de una lista es O(n), lo cual es menos eficiente que los deques.
- **Deques** permiten inserciones y eliminaciones eficientes tanto al principio como al final, lo que los hace más adecuados para ciertos algoritmos que requieren acceso a ambos extremos.

### **Deque vs Queue**  
- Ambos son utilizados para implementar colas, pero los deques ofrecen mayor flexibilidad al permitir la inserción y eliminación en ambos extremos, mientras que las colas típicas solo permiten una operación en un extremo.

---

## **📍 7. Recursos adicionales**  
- [Documentación oficial de Python - collections.deque](https://docs.python.org/3/library/collections.html#deque)
- [Deque en Python - Geeks for Geeks](https://www.geeksforgeeks.org/queue-in-python/)
- [Python Deque Methods - W3Schools](https://www.w3schools.com/python/ref_collection_deque.asp)

---

## **📌 Contribuciones**  
Si tienes sugerencias o mejoras para esta sección, **haz un fork del repositorio y envía un pull request**.

---

## **📜 Licencia**  
Este proyecto está bajo la licencia **MIT**, lo que significa que puedes usarlo libremente.
