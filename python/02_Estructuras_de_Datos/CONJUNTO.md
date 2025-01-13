# **Conjuntos en Python**

## **📖 Descripción**  
Un **conjunto** en Python es una colección no ordenada de elementos únicos. Los conjuntos son mutables, lo que significa que puedes agregar y eliminar elementos. Sin embargo, no permiten duplicados y no tienen un orden específico, por lo que no se pueden indexar ni ordenar. Son útiles cuando necesitas almacenar elementos únicos y realizar operaciones matemáticas, como la unión, la intersección y la diferencia.

---

## **📌 Contenido**

1. ¿Qué es un conjunto?
2. Creación de conjuntos
3. Operaciones básicas con conjuntos
4. Métodos comunes de conjuntos
5. Conjuntos y operaciones matemáticas
6. Conjuntos de conjunto mutable vs inmutable
7. Ejercicios prácticos

---

## **📍 1. ¿Qué es un conjunto?**  
Un **conjunto** es una colección de elementos no ordenada y sin elementos duplicados. Se utiliza principalmente cuando se requiere verificar la pertenencia a un grupo o realizar operaciones matemáticas con los datos.

### Características de los conjuntos:
- **No ordenados**: Los elementos no tienen un índice.
- **Elementos únicos**: No permiten duplicados.
- **Mutables**: Los elementos pueden agregarse o eliminarse después de la creación.

---

## **📍 2. Creación de conjuntos**  
Los conjuntos se pueden crear utilizando la función `set()` o utilizando llaves `{}`.

### 📌 **Crear un conjunto vacío**  
```python
# Crear un conjunto vacío
mi_conjunto = set()
print(mi_conjunto)  # Salida: set()
```

### 📌 **Crear un conjunto con elementos**  
```python
# Crear un conjunto con algunos elementos
numeros = {1, 2, 3, 4, 5}
print(numeros)  # Salida: {1, 2, 3, 4, 5}
```

### 📌 **Crear un conjunto a partir de una lista (eliminando duplicados)**  
```python
# Crear un conjunto a partir de una lista
mi_lista = [1, 2, 3, 4, 4, 5, 5, 6]
mi_conjunto = set(mi_lista)
print(mi_conjunto)  # Salida: {1, 2, 3, 4, 5, 6}
```

---

## **📍 3. Operaciones básicas con conjuntos**  
Puedes realizar varias operaciones sobre conjuntos como agregar, eliminar o verificar la pertenencia de elementos.

### 📌 **Agregar elementos a un conjunto**  
```python
# Agregar un elemento a un conjunto
numeros.add(6)
print(numeros)  # Salida: {1, 2, 3, 4, 5, 6}
```

### 📌 **Eliminar elementos de un conjunto**  
```python
# Eliminar un elemento de un conjunto
numeros.remove(2)
print(numeros)  # Salida: {1, 3, 4, 5, 6}

# Eliminar un elemento de un conjunto de forma segura (sin error si no existe)
numeros.discard(10)  # No genera error si el elemento no está presente
```

### 📌 **Verificar si un elemento pertenece a un conjunto**  
```python
# Verificar si un elemento está en el conjunto
print(3 in numeros)  # Salida: True
print(10 in numeros)  # Salida: False
```

---

## **📍 4. Métodos comunes de conjuntos**  
Los conjuntos en Python tienen varios métodos útiles para manipular y consultar los datos.

### 📌 **`clear()`**  
Elimina todos los elementos de un conjunto.
```python
numeros.clear()
print(numeros)  # Salida: set()
```

### 📌 **`copy()`**  
Devuelve una copia superficial del conjunto.
```python
numeros = {1, 2, 3}
numeros_copy = numeros.copy()
print(numeros_copy)  # Salida: {1, 2, 3}
```

### 📌 **`union()`**  
Devuelve la unión de dos conjuntos, es decir, todos los elementos de ambos conjuntos.
```python
conjunto1 = {1, 2, 3}
conjunto2 = {3, 4, 5}
union = conjunto1.union(conjunto2)
print(union)  # Salida: {1, 2, 3, 4, 5}
```

### 📌 **`intersection()`**  
Devuelve la intersección de dos conjuntos, es decir, los elementos comunes entre ambos conjuntos.
```python
interseccion = conjunto1.intersection(conjunto2)
print(interseccion)  # Salida: {3}
```

### 📌 **`difference()`**  
Devuelve la diferencia entre dos conjuntos, es decir, los elementos que están en el primer conjunto pero no en el segundo.
```python
diferencia = conjunto1.difference(conjunto2)
print(diferencia)  # Salida: {1, 2}
```

---

## **📍 5. Conjuntos y operaciones matemáticas**  
Los conjuntos en Python son muy útiles para realizar operaciones matemáticas, tales como la unión, la intersección y la diferencia.

### 📌 **Unión de conjuntos**  
La unión de dos conjuntos consiste en combinar todos los elementos de ambos conjuntos sin duplicados.
```python
conjunto1 = {1, 2, 3}
conjunto2 = {3, 4, 5}
union = conjunto1 | conjunto2  # Usando el operador '|'
print(union)  # Salida: {1, 2, 3, 4, 5}
```

### 📌 **Intersección de conjuntos**  
La intersección de dos conjuntos consiste en los elementos que están presentes en ambos conjuntos.
```python
interseccion = conjunto1 & conjunto2  # Usando el operador '&'
print(interseccion)  # Salida: {3}
```

### 📌 **Diferencia de conjuntos**  
La diferencia de conjuntos consiste en los elementos que están en el primer conjunto pero no en el segundo.
```python
diferencia = conjunto1 - conjunto2  # Usando el operador '-'
print(diferencia)  # Salida: {1, 2}
```

### 📌 **Diferencia simétrica**  
La diferencia simétrica consiste en los elementos que están en uno de los conjuntos, pero no en ambos.
```python
diferencia_simetrica = conjunto1 ^ conjunto2  # Usando el operador '^'
print(diferencia_simetrica)  # Salida: {1, 2, 4, 5}
```

---

## **📍 6. Conjuntos: Mutable vs Inmutable**  
En Python, los conjuntos son **mutables**, lo que significa que puedes agregar y eliminar elementos de un conjunto después de su creación. Sin embargo, también existen los **conjuntos inmutables**, llamados **frozensets**, que son similares a los conjuntos pero no pueden modificarse una vez creados.

### 📌 **Crear un conjunto inmutable (`frozenset`)**  
```python
# Crear un frozenset
conjunto_inmutable = frozenset([1, 2, 3])
print(conjunto_inmutable)  # Salida: frozenset({1, 2, 3})
```

---

## **📍 7. Ejercicios prácticos**

✅ **Crear un conjunto con los números del 1 al 5 y agregar el número 6.**  
✅ **Eliminar el número 3 de un conjunto y verificar si se encuentra en el conjunto.**  
✅ **Realizar la unión e intersección de dos conjuntos y mostrar los resultados.**  
✅ **Crear un `frozenset` y tratar de agregar un elemento (debería generar un error).**

---

## **📌 Recursos adicionales**  
- [Documentación oficial de Python: Conjuntos](https://docs.python.org/3/tutorial/datastructures.html#sets)  
- [Tutorial sobre Conjuntos en Python - Real Python](https://realpython.com/python-sets/)

---

## **📌 Contribuciones**  
Si tienes sugerencias o mejoras para esta sección, **haz un fork del repositorio y envía un pull request**.

---

## **📜 Licencia**  
Este proyecto está bajo la licencia **MIT**, lo que significa que puedes usarlo libremente.