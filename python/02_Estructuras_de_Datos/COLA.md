# **Colas en Python** 🍃

## **📖 Descripción**  
Una **cola** en Python es una estructura de datos que sigue el principio de **FIFO** (First In, First Out), lo que significa que el primer elemento agregado es el primero en ser eliminado. Las colas son útiles en situaciones donde los elementos deben procesarse en el mismo orden en que fueron agregados, como en la gestión de tareas, sistemas de impresión y procesos en ejecución.

---

## **📌 Contenido**  
1. ¿Qué es una cola?  
2. Creación de colas  
3. Operaciones básicas con colas  
4. Métodos comunes de colas  
5. Uso de colas en Python  
6. Ejercicios prácticos

---

## **📍 1. ¿Qué es una cola?**  
Una **cola** es una estructura de datos lineal que sigue el principio FIFO. Los elementos se agregan al final (encolado) y se eliminan desde el principio (desencolado). Este tipo de estructura es útil cuando se requiere un orden específico para el procesamiento de datos.

### Características de las colas:
- **FIFO**: El primer elemento en entrar es el primero en salir.
- **Operaciones básicas**: Encolar (agregar), desencolar (eliminar).
- **Uso común**: Gestión de tareas, procesamiento de eventos, etc.

---

## **📍 2. Creación de colas**  
En Python, las colas se pueden implementar de varias maneras, siendo las más comunes el uso de listas o la clase `Queue` del módulo `queue`.

### 📌 **Crear una cola con una lista**  
```python
# Crear una cola con una lista
cola = []
print(cola)  # Salida: []
```

### 📌 **Crear una cola con la clase `Queue`**  
```python
# Importar Queue desde el módulo queue
from queue import Queue

# Crear una cola vacía
cola = Queue(maxsize=5)
print(cola)  # Salida: <queue.Queue object at 0x...>
```

---

## **📍 3. Operaciones básicas con colas**  
Las operaciones principales que puedes realizar con una cola son **encolar** (agregar un elemento) y **desencolar** (eliminar un elemento).

### 📌 **Encolar (agregar un elemento)**  
```python
# Encolar un elemento en la cola
cola.append(1)  # Usando lista
print(cola)  # Salida: [1]

# Encolar usando Queue
cola.put(1)  # Usando la clase Queue
print(cola.queue)  # Salida: deque([1])
```

### 📌 **Desencolar (eliminar el primer elemento)**  
```python
# Desencolar un elemento de la cola
elemento = cola.pop(0)  # Usando lista
print(elemento)  # Salida: 1
print(cola)  # Salida: []

# Desencolar usando Queue
elemento = cola.get()  # Usando la clase Queue
print(elemento)  # Salida: 1
```

### 📌 **Verificar si la cola está vacía**  
```python
# Verificar si la cola está vacía
print(len(cola) == 0)  # Salida: True

# Usando Queue
print(cola.empty())  # Salida: True
```

---

## **📍 4. Métodos comunes de colas**  

### 📌 **`put()`**  
Encola un elemento en la cola (solo para `Queue`).
```python
cola.put(2)
print(cola.queue)  # Salida: deque([2])
```

### 📌 **`get()`**  
Desencola un elemento de la cola (solo para `Queue`).
```python
elemento = cola.get()
print(elemento)  # Salida: 2
```

### 📌 **`empty()`**  
Verifica si la cola está vacía (solo para `Queue`).
```python
print(cola.empty())  # Salida: True
```

### 📌 **`qsize()`**  
Obtiene el tamaño de la cola (solo para `Queue`).
```python
print(cola.qsize())  # Salida: 0
```

---

## **📍 5. Uso de colas en Python**  
Las colas son especialmente útiles en escenarios donde se procesan tareas en orden secuencial, como:

- **Procesamiento de eventos**: Cuando se deben procesar eventos en el orden en que ocurren.
- **Simulación de sistemas**: Modelar procesos que requieren un orden estricto de ejecución.
- **Algoritmos de búsqueda**: Utilizadas en algoritmos como el BFS (Breadth-First Search) para explorar estructuras de grafos.

### 📌 **Ejemplo: Simulación de una cola de atención**  
```python
# Cola de atención
cola = Queue()

# Encolar tareas
cola.put("Tarea 1")
cola.put("Tarea 2")
cola.put("Tarea 3")

# Desencolar tareas
print(cola.get())  # Salida: Tarea 1
print(cola.get())  # Salida: Tarea 2
```

---

## **📍 6. Ejercicios prácticos**  

✅ **Crea una cola, encola tres elementos y luego desencola dos.**  
✅ **Simula un sistema de atención al cliente utilizando una cola y verifica el orden de procesamiento.**  
✅ **Usa una cola para gestionar el procesamiento de tareas en un sistema.**

---

## **📌 Recursos adicionales**  
- [Documentación oficial de Python: Queue](https://docs.python.org/3/library/queue.html)  
- [Tutorial sobre Colas en Python - Real Python](https://realpython.com/python-queues/)

---

## **📌 Contribuciones**  
Si tienes sugerencias o mejoras para esta sección, **haz un fork del repositorio y envía un pull request**.

---

## **📜 Licencia**  
Este proyecto está bajo la licencia **MIT**, lo que significa que puedes usarlo libremente.  
