# **Pilas en Python** 🧑‍💻📊

## **📖 Descripción**  
Una **pila** en Python es una estructura de datos que sigue el principio **LIFO** (Last In, First Out), lo que significa que el último elemento agregado es el primero en ser eliminado. Las pilas son utilizadas en diversos algoritmos y estructuras de datos, como en la gestión de llamadas a funciones, retroceso en aplicaciones (como en navegadores web), y más.

---

## **📌 Contenido**  
1. ¿Qué es una pila?  
2. Creación de pilas  
3. Operaciones básicas con pilas  
4. Métodos comunes de pilas  
5. Uso de pilas en Python  
6. Ejercicios prácticos  
7. Recursos adicionales

---

## **📍 1. ¿Qué es una pila?**  
Una **pila** es una estructura de datos lineal en la que los elementos se agregan y eliminan de un solo extremo, llamado **tope**. Este tipo de estructura sigue el principio **LIFO**, es decir, el último elemento agregado es el primero en ser eliminado.

### Características de las pilas:
- **LIFO**: El último en entrar es el primero en salir.
- **Operaciones básicas**: Apilar (agregar), desapilar (eliminar).
- **Uso común**: Gestión de funciones, deshacer operaciones, recorrido de árboles, etc.

---

## **📍 2. Creación de pilas**  
En Python, las pilas se pueden implementar de varias maneras, siendo las más comunes el uso de listas o la clase `LifoQueue` del módulo `queue`.

### 📌 **Crear una pila con una lista**  
Una forma rápida de implementar una pila en Python es usar una lista. El último elemento de la lista se considera el **tope** de la pila.

```python
# Crear una pila con una lista
pila = []
print(pila)  # Salida: []
```

### 📌 **Crear una pila con la clase `LifoQueue`**  
Otra forma es utilizar la clase `LifoQueue` del módulo `queue`, que proporciona una implementación de pila segura para hilos.

```python
# Importar LifoQueue desde el módulo queue
from queue import LifoQueue

# Crear una pila vacía
pila = LifoQueue(maxsize=5)
print(pila)  # Salida: <queue.LifoQueue object at 0x...>
```

---

## **📍 3. Operaciones básicas con pilas**  
Las operaciones principales que puedes realizar con una pila son **apilar** (agregar un elemento) y **desapilar** (eliminar un elemento).

### 📌 **Apilar (agregar un elemento)**  
```python
# Apilar un elemento en la pila
pila.append(1)  # Usando lista
print(pila)  # Salida: [1]

# Usando LifoQueue
pila.put(1)  # Usando la clase LifoQueue
print(pila.queue)  # Salida: deque([1])
```

### 📌 **Desapilar (eliminar el último elemento)**  
```python
# Desapilar un elemento de la pila
elemento = pila.pop()  # Usando lista
print(elemento)  # Salida: 1
print(pila)  # Salida: []

# Usando LifoQueue
elemento = pila.get()  # Usando la clase LifoQueue
print(elemento)  # Salida: 1
```

### 📌 **Verificar si la pila está vacía**  
```python
# Verificar si la pila está vacía
print(len(pila) == 0)  # Salida: True

# Usando LifoQueue
print(pila.empty())  # Salida: True
```

---

## **📍 4. Métodos comunes de pilas**  

### 📌 **`put()`**  
Apila un elemento en la pila (solo para `LifoQueue`).
```python
pila.put(2)
print(pila.queue)  # Salida: deque([2])
```

### 📌 **`get()`**  
Desapila un elemento de la pila (solo para `LifoQueue`).
```python
elemento = pila.get()
print(elemento)  # Salida: 2
```

### 📌 **`empty()`**  
Verifica si la pila está vacía (solo para `LifoQueue`).
```python
print(pila.empty())  # Salida: True
```

### 📌 **`qsize()`**  
Obtiene el tamaño de la pila (solo para `LifoQueue`).
```python
print(pila.qsize())  # Salida: 0
```

---

## **📍 5. Uso de pilas en Python**  
Las pilas se utilizan comúnmente en algoritmos que requieren un procesamiento de datos en orden inverso o en la gestión de llamadas a funciones. Algunos ejemplos incluyen:

- **Recursión**: Cada llamada a una función puede ser vista como una operación de apilar. Las pilas se utilizan para mantener el seguimiento de las funciones activas.
- **Navegadores web**: En los navegadores, la pila se usa para gestionar el historial de páginas visitadas (botón de "retroceder").
- **Algoritmos de deshacer/rehacer**: Las pilas son útiles para mantener el estado de una aplicación y revertir acciones previas.

### 📌 **Ejemplo: Simulación de una pila de llamadas**  
```python
# Simular una pila de llamadas
pila = []

# Apilar llamadas
pila.append("Llamada 1")
pila.append("Llamada 2")
pila.append("Llamada 3")

# Desapilar llamadas
print(pila.pop())  # Salida: Llamada 3
print(pila.pop())  # Salida: Llamada 2
```

---

## **📍 6. Ejercicios prácticos**  

✅ **Crea una pila, apila tres elementos y luego desapila dos.**  
✅ **Simula un sistema de retroceso de páginas en un navegador utilizando una pila.**  
✅ **Usa una pila para gestionar un historial de acciones en una aplicación.**

---

## **📌 Recursos adicionales**  
- [Documentación oficial de Python: Queue](https://docs.python.org/3/library/queue.html)  
- [Tutorial sobre Pilas en Python - Real Python](https://realpython.com/python-queues/)

---

## **📌 Contribuciones**  
Si tienes sugerencias o mejoras para esta sección, **haz un fork del repositorio y envía un pull request**.

---

## **📜 Licencia**  
Este proyecto está bajo la licencia **MIT**, lo que significa que puedes usarlo libremente.
