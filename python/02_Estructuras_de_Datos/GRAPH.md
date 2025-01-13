# **Grafos en Python** 🌐💻

## **📖 Descripción**  
Un **Grafo** es una estructura de datos no lineal que se utiliza para representar relaciones entre objetos. Un grafo está compuesto por un conjunto de **nodos** (también llamados vértices) y un conjunto de **aristas** (o bordes) que conectan los nodos. Los grafos son muy útiles para representar redes como redes sociales, redes de transporte, mapas, recomendaciones, etc.

En un grafo, las aristas pueden ser **dirigidas** o **no dirigidas** y pueden tener **pesos** que representen algún tipo de costo o distancia entre los nodos.

---

## **📌 Contenido**  
1. ¿Qué es un Grafo?  
2. Tipos de Grafos  
3. Representación de Grafos en Python  
4. Operaciones básicas en Grafos  
5. Ejemplos prácticos  
6. Recursos adicionales

---

## **📍 1. ¿Qué es un Grafo?**  
Un **Grafo** es un conjunto de nodos (vértices) conectados entre sí por aristas (bordes). Los grafos se utilizan para modelar relaciones entre objetos y pueden ser clasificados según las características de las aristas.

### Elementos de un Grafo:
1. **Nodos (Vértices)**: Los puntos en el grafo que representan los objetos o entidades.
2. **Aristas (Bordes)**: Las conexiones entre los nodos, que representan la relación entre ellos.
3. **Grado de un nodo**: Es el número de aristas que están conectadas a un nodo. En un grafo dirigido, se distinguen los grados de entrada y salida.
4. **Peso**: Algunas aristas pueden tener un valor asociado, llamado peso, que puede representar distancia, costo o tiempo.
5. **Conectividad**: Si hay un camino entre cualquier par de nodos, el grafo se considera **conexo**.

---

## **📍 2. Tipos de Grafos**  
Existen varios tipos de grafos, cada uno adecuado para diferentes aplicaciones. Algunos de los más comunes incluyen:

1. **Grafo dirigido (Digrafo)**: Un grafo en el que las aristas tienen dirección, es decir, las conexiones entre los nodos se representan con flechas.
   
   Ejemplo:
   - A → B
   - A → C

2. **Grafo no dirigido**: Un grafo en el que las aristas no tienen dirección, es decir, la conexión entre los nodos es bidireccional.

   Ejemplo:
   - A — B
   - A — C

3. **Grafo ponderado**: Un grafo en el que cada arista tiene un valor asociado, generalmente llamado peso, que puede representar costo, distancia, etc.

4. **Grafo no ponderado**: Un grafo en el que las aristas no tienen un peso o valor asociado.

5. **Grafo conexo**: Un grafo en el que hay un camino entre cada par de nodos.

6. **Grafo completo**: Un grafo en el que cada par de nodos está conectado por una arista.

7. **Grafo cíclico y acíclico**:
   - **Cíclico**: Un grafo que contiene al menos un ciclo (un camino cerrado).
   - **Acíclico**: Un grafo que no contiene ciclos.

---

## **📍 3. Representación de Grafos en Python**  
En Python, los grafos pueden ser representados utilizando varias estructuras de datos, como listas de adyacencia, matrices de adyacencia, o diccionarios. Aquí te mostramos cómo implementar un grafo utilizando un **diccionario de adyacencia**.

### **Código de Implementación de un Grafo en Python**:

```python
class Grafo:
    def __init__(self):
        self.grafo = {}

    def agregar_nodo(self, nodo):
        if nodo not in self.grafo:
            self.grafo[nodo] = []

    def agregar_arista(self, nodo1, nodo2, peso=0):
        if nodo1 not in self.grafo:
            self.agregar_nodo(nodo1)
        if nodo2 not in self.grafo:
            self.agregar_nodo(nodo2)
        self.grafo[nodo1].append((nodo2, peso))
        self.grafo[nodo2].append((nodo1, peso))  # Para grafo no dirigido

    def imprimir_grafo(self):
        for nodo, adyacentes in self.grafo.items():
            print(f"{nodo} -> {adyacentes}")
```

### **Explicación**:
- **grafos**: La clase `Grafo` representa un grafo mediante un diccionario, donde las claves son los nodos y los valores son listas de tuplas que contienen los nodos adyacentes y el peso de las aristas.
- **agregar_nodo**: Este método agrega un nodo al grafo.
- **agregar_arista**: Este método agrega una arista entre dos nodos. Si el grafo es no dirigido, se agrega la arista en ambos sentidos.

### **Ejemplo de uso**:

```python
# Crear un grafo
grafo = Grafo()

# Agregar nodos
grafo.agregar_nodo("A")
grafo.agregar_nodo("B")
grafo.agregar_nodo("C")

# Agregar aristas (con peso opcional)
grafo.agregar_arista("A", "B", 10)
grafo.agregar_arista("A", "C", 20)
grafo.agregar_arista("B", "C", 30)

# Imprimir el grafo
grafo.imprimir_grafo()
```

**Salida**:
```
A -> [('B', 10), ('C', 20)]
B -> [('A', 10), ('C', 30)]
C -> [('A', 20), ('B', 30)]
```

---

## **📍 4. Operaciones básicas en Grafos**  
Algunas de las operaciones más comunes que puedes realizar con grafos incluyen:

### 1. **Búsqueda en profundidad (DFS)**:  
La búsqueda en profundidad es un algoritmo que recorre un grafo comenzando desde un nodo y explorando tan lejos como sea posible antes de retroceder.

```python
def dfs(self, nodo, visitados=None):
    if visitados is None:
        visitados = set()
    visitados.add(nodo)
    print(nodo, end=" ")
    for vecino, _ in self.grafo[nodo]:
        if vecino not in visitados:
            self.dfs(vecino, visitados)
```

### 2. **Búsqueda en amplitud (BFS)**:  
La búsqueda en amplitud explora el grafo nivel por nivel, comenzando desde el nodo raíz.

```python
from collections import deque

def bfs(self, nodo):
    visitados = set()
    cola = deque([nodo])
    while cola:
        nodo = cola.popleft()
        if nodo not in visitados:
            visitados.add(nodo)
            print(nodo, end=" ")
            for vecino, _ in self.grafo[nodo]:
                if vecino not in visitados:
                    cola.append(vecino)
```

### 3. **Camino más corto (Dijkstra)**:  
El algoritmo de Dijkstra encuentra el camino más corto desde un nodo de inicio a todos los demás nodos en un grafo ponderado.

```python
import heapq

def dijkstra(self, inicio):
    distancias = {nodo: float('inf') for nodo in self.grafo}
    distancias[inicio] = 0
    pq = [(0, inicio)]  # (distancia, nodo)
    
    while pq:
        distancia, nodo = heapq.heappop(pq)
        if distancia > distancias[nodo]:
            continue
        for vecino, peso in self.grafo[nodo]:
            nueva_dist = distancia + peso
            if nueva_dist < distancias[vecino]:
                distancias[vecino] = nueva_dist
                heapq.heappush(pq, (nueva_dist, vecino))
    
    return distancias
```

---

## **📍 5. Ejemplos prácticos**  

### 📌 **Ejemplo 1: Red de Transporte**  
Imagina que deseas representar una red de transporte, donde los nodos son ciudades y las aristas son las rutas entre ellas con su respectiva distancia.

```python
# Crear el grafo de transporte
red_transporte = Grafo()

# Agregar ciudades
red_transporte.agregar_nodo("Ciudad A")
red_transporte.agregar_nodo("Ciudad B")
red_transporte.agregar_nodo("Ciudad C")

# Agregar rutas con distancias
red_transporte.agregar_arista("Ciudad A", "Ciudad B", 100)
red_transporte.agregar_arista("Ciudad B", "Ciudad C", 200)
red_transporte.agregar_arista("Ciudad A", "Ciudad C", 300)

# Imprimir la red de transporte
red_transporte.imprimir_grafo()
```

### 📌 **Ejemplo 2: Red Social**  
Puedes representar una red social como un grafo donde los nodos son usuarios y las aristas representan conexiones de amistad.

```python
# Crear el grafo de red social
red_social = Grafo()

# Agregar usuarios
red_social.agregar_nodo("Usuario 1")
red_social.agregar_nodo("Usuario 2")
red_social.agregar_nodo("Usuario 3")

# Agregar conexiones de amistad
red_social.agregar_arista("Usuario 1", "Usuario 2")
red_social.agregar_arista("Usuario 2", "Usuario 3")

# Imprimir la red social
red_social.imprimir_grafo()
```

---

## **📍 6. Recursos adicionales**  
- [Graph Theory - Geeks for Geeks](https://www.geeksforgeeks.org/graph-data-structure-and-algorithms/)
- [Introducción a los Grafos - Real Python](https://realpython.com/python-graph-library/)
- [Documentación de NetworkX - Python](https://networkx.github.io/)

---

## **📌 Contribuciones**  
Si tienes sugerencias o mejoras para esta sección, **haz un fork del repositorio y envía un pull request**.

---

## **📜 Licencia**  
Este proyecto está bajo la licencia **MIT**, lo que significa que puedes usarlo libremente.
