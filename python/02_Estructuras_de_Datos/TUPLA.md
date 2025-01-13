# **Tuplas en Python**

## **📖 Descripción**  
Las **tuplas** son un tipo de colección en Python, muy similares a las listas, pero con una diferencia importante: **son inmutables**. Una vez que se crea una tupla, no se puede modificar. Esto las hace útiles cuando se requiere almacenar datos que no deben cambiar. A continuación, exploraremos cómo crear, manipular y trabajar con tuplas en Python.

---

## **📌 Contenido**

1. ¿Qué es una tupla?
2. Creación de tuplas
3. Acceso a elementos en una tupla
4. Modificar tuplas (conceptos y limitaciones)
5. Métodos comunes de tuplas
6. Tuplas anidadas
7. Empaquetado y desempaquetado de tuplas
8. Ejercicios prácticos

---

## **📍 1. ¿Qué es una tupla?**  
Una **tupla** es una colección ordenada de elementos, similar a una lista, pero con la diferencia clave de que es **inmutable**. Esto significa que los elementos de una tupla no se pueden cambiar una vez que ha sido creada. Las tuplas pueden contener diferentes tipos de datos y están definidas utilizando paréntesis `()`.

---

## **📍 2. Creación de tuplas**  
Las tuplas se crean utilizando paréntesis `()`. Puedes definir una tupla con un solo elemento, aunque es necesario agregar una coma para que Python la reconozca como tupla.

### 📌 **Tupla vacía**  
```python
# Crear una tupla vacía
mi_tupla = ()
print(mi_tupla)  # Salida: ()
```

### 📌 **Tupla con elementos**  
```python
# Crear una tupla con varios elementos
colores = ("rojo", "verde", "azul")
print(colores)  # Salida: ('rojo', 'verde', 'azul')
```

### 📌 **Tupla con un solo elemento**  
```python
# Crear una tupla con un solo elemento
tupla_unica = (5,)
print(tupla_unica)  # Salida: (5)
```

---

## **📍 3. Acceso a elementos en una tupla**  
Al igual que las listas, los elementos de una tupla se acceden mediante **índices**. Recuerda que los índices comienzan desde 0.

### 📌 **Acceder a un solo elemento**  
```python
# Acceder al primer elemento de la tupla
colores = ("rojo", "verde", "azul")
print(colores[0])  # Salida: rojo
```

### 📌 **Acceder a elementos desde el final**  
Puedes usar índices negativos para acceder a los elementos desde el final de la tupla. El índice `-1` corresponde al último elemento, `-2` al penúltimo, y así sucesivamente.

```python
# Acceder al último elemento
print(colores[-1])  # Salida: azul

# Acceder al penúltimo elemento
print(colores[-2])  # Salida: verde
```

---

## **📍 4. Modificar tuplas (conceptos y limitaciones)**  
A diferencia de las listas, las tuplas **son inmutables**, lo que significa que no puedes cambiar, agregar ni eliminar elementos después de haber creado una tupla.

### 📌 **Intentar modificar una tupla**  
```python
# Intentar cambiar un elemento de la tupla (esto generará un error)
colores[0] = "amarillo"  # Error: 'tuple' object does not support item assignment
```

Aunque no puedes modificar una tupla directamente, puedes convertirla en una lista, modificar la lista y luego convertirla de nuevo en tupla.

```python
# Convertir una tupla en lista, modificarla y luego volver a tupla
colores = list(colores)
colores[0] = "amarillo"
colores = tuple(colores)
print(colores)  # Salida: ('amarillo', 'verde', 'azul')
```

---

## **📍 5. Métodos comunes de tuplas**  
Aunque las tuplas son inmutables, tienen algunos métodos útiles para interactuar con ellas.

### 📌 **`count()`**  
Devuelve el número de veces que un elemento aparece en la tupla.
```python
numeros = (1, 2, 3, 2, 2, 4)
print(numeros.count(2))  # Salida: 3
```

### 📌 **`index()`**  
Devuelve el índice del primer elemento encontrado que coincide con el valor especificado.
```python
colores = ("rojo", "verde", "azul")
print(colores.index("verde"))  # Salida: 1
```

---

## **📍 6. Tuplas anidadas**  
Al igual que las listas, las tuplas pueden contener otras tuplas o cualquier otro tipo de dato. Esto se conoce como **tuplas anidadas**.

### 📌 **Acceso a elementos en tuplas anidadas**  
```python
matriz = ((1, 2), (3, 4), (5, 6))
print(matriz[1][0])  # Salida: 3
```

---

## **📍 7. Empaquetado y desempaquetado de tuplas**  
El **empaquetado** y **desempaquetado** de tuplas es una técnica que permite asignar varios valores de una tupla a varias variables de forma más eficiente.

### 📌 **Empaquetado**  
```python
# Empaquetar una tupla
tupla = (1, "apple", 3.14)
print(tupla)  # Salida: (1, 'apple', 3.14)
```

### 📌 **Desempaquetado**  
```python
# Desempaquetar una tupla
a, b, c = tupla
print(a)  # Salida: 1
print(b)  # Salida: apple
print(c)  # Salida: 3.14
```

---

## **📍 8. Ejercicios prácticos**

✅ **Crear una tupla con los días de la semana y acceder al tercer día.**  
✅ **Contar cuántas veces aparece el número 5 en una tupla.**  
✅ **Crear una tupla anidada con tres elementos, y acceder al segundo elemento de la segunda tupla.**  
✅ **Desempaquetar una tupla con el nombre y edad de una persona y mostrar los valores.**

---

## **📌 Recursos adicionales**  
- [Documentación oficial de Python: Tuplas](https://docs.python.org/3/tutorial/datastructures.html#tuples-and-sequences)  
- [Tutorial sobre Tuplas en Python - Real Python](https://realpython.com/python-tuples/#creating-a-tuple)

---

## **📌 Contribuciones**  
Si tienes sugerencias o mejoras para esta sección, **haz un fork del repositorio y envía un pull request**.

---

## **📜 Licencia**  
Este proyecto está bajo la licencia **MIT**, lo que significa que puedes usarlo libremente.
