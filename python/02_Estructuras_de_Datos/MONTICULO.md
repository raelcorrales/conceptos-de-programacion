# **Montículos en Python** 🏔️💻

## **📖 Descripción**  
Un **montículo** (o **heap**) es una estructura de datos que satisface la propiedad de **orden parcial**: en un **montículo máximo**, el valor de cada nodo es mayor o igual al de sus hijos, mientras que en un **montículo mínimo**, el valor de cada nodo es menor o igual al de sus hijos. Es una estructura de árbol binario completa que se utiliza principalmente para implementar **colas de prioridad**.

Los montículos son útiles cuando necesitas una manera eficiente de obtener el elemento máximo (o mínimo) en un conjunto de datos, sin necesidad de ordenar todo el conjunto.

---

## **📌 Contenido**  
1. ¿Qué es un montículo?  
2. Tipos de montículos  
3. Creación de montículos en Python  
4. Operaciones básicas en montículos  
5. Implementación en Python utilizando la biblioteca `heapq`  
6. Ejemplos prácticos  
7. Recursos adicionales

---

## **📍 1. ¿Qué es un montículo?**  
Un **montículo** es una estructura de árbol binario donde el valor de un nodo es comparado con los valores de sus hijos. Dependiendo de si es un **montículo máximo** o **mínimo**, la propiedad de orden puede variar:

- **Montículo máximo**: El valor del nodo padre es siempre mayor o igual que el de sus hijos.
- **Montículo mínimo**: El valor del nodo padre es siempre menor o igual que el de sus hijos.

El árbol está **completo**, es decir, todos los niveles están completamente llenos, excepto posiblemente el último, que debe ser llenado de izquierda a derecha.

---

## **📍 2. Tipos de montículos**  
1. **Montículo máximo**  
   En un montículo máximo, el valor máximo siempre está en la raíz, y sus subárboles también cumplen la misma propiedad de montículo.

2. **Montículo mínimo**  
   En un montículo mínimo, el valor mínimo siempre está en la raíz, y sus subárboles también cumplen la propiedad de montículo mínimo.

---

## **📍 3. Creación de montículos en Python**  
Python tiene una librería estándar llamada **`heapq`** que proporciona funciones para trabajar con montículos. A pesar de que `heapq` implementa un **montículo mínimo**, se puede usar para crear montículos máximos invirtiendo los valores al insertarlos.

### 📌 **Crear un montículo mínimo**  
Para crear un montículo mínimo en Python, simplemente usa la librería `heapq`:

```python
import heapq

# Crear un montículo vacío
monticulo = []
heapq.heappush(monticulo, 5)  # Insertar el valor 5
heapq.heappush(monticulo, 1)  # Insertar el valor 1
heapq.heappush(monticulo, 3)  # Insertar el valor 3

print(monticulo)  # Salida: [1, 5, 3] (raíz = 1)
```

### 📌 **Crear un montículo máximo**  
Puedes crear un montículo máximo invirtiendo los valores:

```python
import heapq

# Crear un montículo vacío
monticulo_max = []
heapq.heappush(monticulo_max, -5)  # Insertar el valor 5 (invertido)
heapq.heappush(monticulo_max, -1)  # Insertar el valor 1 (invertido)
heapq.heappush(monticulo_max, -3)  # Insertar el valor 3 (invertido)

# Convertir los valores de nuevo a positivos para ver el montículo máximo
monticulo_max = [-x for x in monticulo_max]
print(monticulo_max)  # Salida: [5, 3, 1] (raíz = 5)
```

---

## **📍 4. Operaciones básicas en montículos**  
Las operaciones principales en un montículo incluyen:

1. **Insertar un elemento** (`heappush` o `heappushpop`)  
   Añade un nuevo elemento al montículo.

2. **Eliminar el elemento raíz** (`heappop`)  
   Elimina el elemento raíz, que será el mínimo en un montículo mínimo y el máximo en un montículo máximo.

3. **Obtener el elemento raíz** (`heap[0]`)  
   Para obtener el valor máximo o mínimo sin eliminarlo.

4. **Mantener el montículo** (`heapify`)  
   Convierte una lista en un montículo válido.

---

### 📌 **Insertar un elemento**  
```python
heapq.heappush(monticulo, 2)  # Inserta el valor 2
print(monticulo)  # Salida: [1, 2, 3, 5]
```

### 📌 **Eliminar el elemento raíz**  
```python
min_element = heapq.heappop(monticulo)
print(min_element)  # Salida: 1 (el valor mínimo se elimina)
print(monticulo)  # Salida: [2, 5, 3]
```

### 📌 **Obtener el elemento raíz**  
```python
print(monticulo[0])  # Salida: 2 (raíz = 2 en este caso)
```

### 📌 **Convertir una lista en un montículo**  
```python
lista = [5, 1, 3, 2, 4]
heapq.heapify(lista)
print(lista)  # Salida: [1, 2, 3, 5, 4] (montículo mínimo)
```

---

## **📍 5. Implementación en Python utilizando la biblioteca `heapq`**  
La librería `heapq` permite trabajar con montículos en Python. Es importante recordar que `heapq` implementa un **montículo mínimo** de manera predeterminada.

### 📌 **Funciones principales**  
- **`heapq.heappush(heap, item)`**: Inserta un elemento `item` en el `heap` manteniendo la propiedad de montículo.
- **`heapq.heappop(heap)`**: Elimina y devuelve el elemento mínimo del `heap`.
- **`heapq.heappushpop(heap, item)`**: Inserta un elemento y elimina el mínimo en una sola operación.
- **`heapq.heapify(list)`**: Convierte una lista en un montículo válido.

### 📌 **Ejemplo de uso completo**  
```python
import heapq

# Crear un montículo vacío
monticulo = []

# Insertar elementos
heapq.heappush(monticulo, 10)
heapq.heappush(monticulo, 5)
heapq.heappush(monticulo, 20)

# Obtener el valor mínimo (raíz)
print(monticulo[0])  # Salida: 5

# Eliminar el valor mínimo
print(heapq.heappop(monticulo))  # Salida: 5
print(monticulo)  # Salida: [10, 20]
```

---

## **📍 6. Ejemplos prácticos**  

### 📌 **Montículo para implementar una cola de prioridad**  
Un caso común de uso de montículos es implementar una **cola de prioridad**, donde los elementos con mayor prioridad se procesan primero.

```python
import heapq

# Crear una cola de prioridad
cola_prioridad = []

# Insertar elementos con su prioridad
heapq.heappush(cola_prioridad, (2, 'Tarea 1'))
heapq.heappush(cola_prioridad, (1, 'Tarea 2'))
heapq.heappush(cola_prioridad, (3, 'Tarea 3'))

# Obtener la tarea de mayor prioridad (la que tiene el número más bajo)
print(heapq.heappop(cola_prioridad))  # Salida: (1, 'Tarea 2')
```

### 📌 **Montículo para encontrar los k elementos más grandes**  
Utilizando un montículo mínimo, podemos encontrar los `k` elementos más grandes de una lista.

```python
import heapq

# Lista de números
numeros = [5, 1, 3, 9, 7, 2, 8, 4]

# Encontrar los 3 números más grandes
k = 3
top_k = heapq.nlargest(k, numeros)
print(top_k)  # Salida: [9, 8, 7]
```

---

## **📍 7. Recursos adicionales**  
- [Documentación oficial de `heapq`](https://docs.python.org/3/library/heapq.html)  
- [Tutorial sobre montículos - Geeks for Geeks](https://www.geeksforgeeks.org/heap-queue-or-priority-queue/)  
- [Algoritmos de Montículos - Real Python](https://realpython.com/priority-queues-python/)

---

## **📌 Contribuciones**  
Si tienes sugerencias o mejoras para esta sección, **haz un fork del repositorio y envía un pull request**.

---

## **📜 Licencia**  
Este proyecto está bajo la licencia **MIT**, lo que significa que puedes usarlo libremente.