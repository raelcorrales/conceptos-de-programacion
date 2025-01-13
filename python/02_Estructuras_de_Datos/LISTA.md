# **Listas en Python**

## **📖 Descripción**  
Las **listas** son uno de los tipos de datos más importantes y útiles en Python. Son colecciones ordenadas, mutables y permiten almacenar múltiples elementos de diferentes tipos en una sola estructura. A continuación, aprenderás cómo crear, manipular y trabajar con listas en Python.

---

## **📌 Contenido**

1. ¿Qué es una lista?
2. Creación de listas
3. Acceso a elementos en una lista
4. Modificar listas
5. Métodos comunes de listas
6. Listas anidadas
7. Comprensión de listas
8. Ejercicios prácticos

---

## **📍 1. ¿Qué es una lista?**  
En Python, una **lista** es una colección ordenada de elementos que pueden ser de diferentes tipos, como enteros, cadenas de texto, objetos, etc. Las listas son **mutables**, lo que significa que sus elementos pueden ser modificados después de su creación.

Una lista se define utilizando corchetes `[]`, y los elementos dentro de la lista están separados por comas.

---

## **📍 2. Creación de listas**  
Las listas en Python se crean utilizando los corchetes `[]`, y los elementos se colocan dentro de estos corchetes.

### 📌 **Lista vacía**  
```python
# Crear una lista vacía
mi_lista = []
print(mi_lista)  # Salida: []
```

### 📌 **Lista con elementos**  
```python
# Crear una lista con elementos
frutas = ["manzana", "banana", "cereza"]
print(frutas)  # Salida: ['manzana', 'banana', 'cereza']
```

### 📌 **Lista con diferentes tipos de datos**  
```python
# Crear una lista con diferentes tipos de datos
mi_lista = [1, "hola", 3.14, True]
print(mi_lista)  # Salida: [1, 'hola', 3.14, True]
```

---

## **📍 3. Acceso a elementos en una lista**  
Los elementos de una lista se acceden utilizando **índices**. Los índices en Python comienzan desde 0, por lo que el primer elemento tiene índice 0, el segundo tiene índice 1, y así sucesivamente.

### 📌 **Acceso a un solo elemento**  
```python
# Acceder al primer elemento de la lista
frutas = ["manzana", "banana", "cereza"]
print(frutas[0])  # Salida: manzana
```

### 📌 **Acceso a elementos desde el final**  
Puedes usar índices negativos para acceder a los elementos desde el final de la lista. El índice `-1` corresponde al último elemento, `-2` al penúltimo, y así sucesivamente.

```python
# Acceder al último elemento
print(frutas[-1])  # Salida: cereza

# Acceder al penúltimo elemento
print(frutas[-2])  # Salida: banana
```

---

## **📍 4. Modificar listas**  
Las listas son **mutables**, lo que significa que puedes cambiar sus elementos después de haberlas creado.

### 📌 **Modificar un elemento**  
```python
# Modificar un elemento en la lista
frutas[1] = "naranja"
print(frutas)  # Salida: ['manzana', 'naranja', 'cereza']
```

### 📌 **Agregar elementos a una lista**  
Puedes agregar elementos a una lista utilizando los métodos `append()`, `insert()` y `extend()`.

#### **`append()`** agrega un elemento al final de la lista.
```python
frutas.append("mango")
print(frutas)  # Salida: ['manzana', 'naranja', 'cereza', 'mango']
```

#### **`insert()`** agrega un elemento en una posición específica.
```python
frutas.insert(1, "fresa")
print(frutas)  # Salida: ['manzana', 'fresa', 'naranja', 'cereza', 'mango']
```

#### **`extend()`** agrega todos los elementos de otra lista al final.
```python
frutas2 = ["kiwi", "papaya"]
frutas.extend(frutas2)
print(frutas)  # Salida: ['manzana', 'fresa', 'naranja', 'cereza', 'mango', 'kiwi', 'papaya']
```

### 📌 **Eliminar elementos de una lista**  
Puedes eliminar elementos de una lista utilizando los métodos `remove()`, `pop()` y `del`.

#### **`remove()`** elimina el primer elemento con el valor especificado.
```python
frutas.remove("naranja")
print(frutas)  # Salida: ['manzana', 'fresa', 'cereza', 'mango', 'kiwi', 'papaya']
```

#### **`pop()`** elimina y devuelve el elemento en la posición especificada.
```python
ultimo = frutas.pop()
print(ultimo)  # Salida: papaya
print(frutas)  # Salida: ['manzana', 'fresa', 'cereza', 'mango', 'kiwi']
```

#### **`del`** elimina un elemento en una posición específica o toda la lista.
```python
del frutas[0]  # Elimina el primer elemento
print(frutas)  # Salida: ['fresa', 'cereza', 'mango', 'kiwi']
```

---

## **📍 5. Métodos comunes de listas**  
Las listas tienen una serie de métodos útiles para manipular sus elementos.

### 📌 **`sort()`**  
Ordena los elementos de la lista en orden ascendente (por defecto).
```python
numeros = [5, 2, 9, 1, 5, 6]
numeros.sort()
print(numeros)  # Salida: [1, 2, 5, 5, 6, 9]
```

### 📌 **`reverse()`**  
Invierte el orden de los elementos de la lista.
```python
numeros.reverse()
print(numeros)  # Salida: [9, 6, 5, 5, 2, 1]
```

### 📌 **`len()`**  
Devuelve el número de elementos en la lista.
```python
print(len(frutas))  # Salida: 5
```

---

## **📍 6. Listas anidadas**  
Las listas pueden contener otras listas como elementos. Esto se conoce como **listas anidadas**.

### 📌 **Acceso a elementos en listas anidadas**  
```python
matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(matriz[0][1])  # Salida: 2
```

---

## **📍 7. Comprensión de listas**  
La **comprensión de listas** es una forma concisa de crear listas a partir de otras listas. Puedes agregar condiciones y transformaciones en una sola línea.

### 📌 **Ejemplo básico**  
```python
numeros = [1, 2, 3, 4, 5]
cuadrados = [x**2 for x in numeros]
print(cuadrados)  # Salida: [1, 4, 9, 16, 25]
```

### 📌 **Con condición**  
```python
pares = [x for x in numeros if x % 2 == 0]
print(pares)  # Salida: [2, 4]
```

---

## **📍 8. Ejercicios prácticos**

✅ **Crear una lista de números del 1 al 10 y calcular la suma de todos los elementos.**  
✅ **Escribir un programa que elimine todas las ocurrencias de un elemento específico en una lista.**  
✅ **Crear una lista anidada que contenga 3 listas de 3 números y acceder al elemento central de la lista anidada.**  
✅ **Usar comprensión de listas para obtener una lista con los cuadrados de todos los números impares de una lista.**

---

## **📌 Recursos adicionales**  
- [Documentación oficial de Python: Listas](https://docs.python.org/3/tutorial/datastructures.html#more-on-lists)  
- [Tutorial sobre Listas en Python - Real Python](https://realpython.com/python-lists-tuples/#working-with-lists)

---

## **📌 Contribuciones**  
Si tienes sugerencias o mejoras para esta sección, **haz un fork del repositorio y envía un pull request**.

---

## **📜 Licencia**  
Este proyecto está bajo la licencia **MIT**, lo que significa que puedes usarlo libremente.