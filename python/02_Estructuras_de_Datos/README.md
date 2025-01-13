### 📌 **README: Estructura de Datos en Python**  

# **Estructuras de Datos en Python**  

## **📖 Descripción**  
Esta sección cubre las **estructuras de datos** fundamentales en Python, proporcionándote una comprensión clara de cómo manejar colecciones de datos de manera eficiente. Las estructuras de datos que veremos incluyen **listas**, **tuplas**, **diccionarios** y **conjuntos**, que son esenciales para resolver una variedad de problemas de programación.

## **📌 Contenido**  
1. Listas  
2. Tuplas  
3. Diccionarios  
4. Conjuntos  
5. Métodos comunes y manipulación de estructuras de datos  
6. Ejercicios prácticos  

---

## **📍 1. Listas**  
Una **lista** es una colección ordenada y mutable de elementos. Puedes almacenar elementos de cualquier tipo, y su contenido puede modificarse después de haber sido creada.  

### 📌 **Definición y manipulación**  
```python
# Definición de lista
frutas = ["manzana", "plátano", "cereza"]

# Acceder a elementos
print(frutas[0])  # manzana
print(frutas[-1])  # cereza

# Modificar un elemento
frutas[1] = "naranja"
print(frutas)  # ['manzana', 'naranja', 'cereza']

# Agregar elementos
frutas.append("uva")
print(frutas)  # ['manzana', 'naranja', 'cereza', 'uva']

# Eliminar elementos
frutas.remove("naranja")
print(frutas)  # ['manzana', 'cereza', 'uva']
```

### 🧩 **Métodos comunes**  
```python
# Longitud de la lista
print(len(frutas))

# Contar la cantidad de un elemento
print(frutas.count("uva"))

# Ordenar la lista
frutas.sort()
print(frutas)
```

---

## **📍 2. Tuplas**  
Una **tupla** es una colección ordenada e inmutable. Esto significa que una vez que se crea una tupla, no se puede modificar (no se pueden agregar ni eliminar elementos).  

### 📌 **Definición y manipulación**  
```python
# Definición de tupla
colores = ("rojo", "verde", "azul")

# Acceder a elementos
print(colores[1])  # verde

# Intentar modificar la tupla genera un error
# colores[0] = "morado"  # Error
```

### 🧩 **Métodos comunes**  
```python
# Longitud de la tupla
print(len(colores))

# Buscar un elemento
print(colores.index("verde"))  # 1

# Contar ocurrencias de un elemento
print(colores.count("rojo"))  # 1
```

---

## **📍 3. Diccionarios**  
Un **diccionario** es una colección desordenada de pares clave-valor. Cada valor en un diccionario está asociado a una clave única. Los diccionarios son muy útiles para almacenar datos que necesitan ser accedidos de manera rápida a través de una clave.

### 📌 **Definición y manipulación**  
```python
# Definición de diccionario
persona = {"nombre": "Juan", "edad": 25, "ciudad": "Madrid"}

# Acceder a valores por clave
print(persona["nombre"])  # Juan

# Modificar un valor
persona["edad"] = 26
print(persona)  # {'nombre': 'Juan', 'edad': 26, 'ciudad': 'Madrid'}

# Agregar un nuevo par clave-valor
persona["ocupación"] = "Ingeniero"
print(persona)  # {'nombre': 'Juan', 'edad': 26, 'ciudad': 'Madrid', 'ocupación': 'Ingeniero'}
```

### 🧩 **Métodos comunes**  
```python
# Obtener claves, valores o ambos
print(persona.keys())   # dict_keys(['nombre', 'edad', 'ciudad', 'ocupación'])
print(persona.values()) # dict_values(['Juan', 26, 'Madrid', 'Ingeniero'])
print(persona.items())  # dict_items([('nombre', 'Juan'), ('edad', 26), ('ciudad', 'Madrid'), ('ocupación', 'Ingeniero')])

# Verificar si una clave existe
print("edad" in persona)  # True
```

---

## **📍 4. Conjuntos**  
Un **conjunto** es una colección no ordenada de elementos únicos. Los conjuntos son útiles cuando necesitas almacenar elementos sin duplicados y no te importa el orden de los elementos.  

### 📌 **Definición y manipulación**  
```python
# Definición de conjunto
colores = {"rojo", "verde", "azul"}

# Agregar elementos
colores.add("amarillo")
print(colores)  # {'rojo', 'verde', 'azul', 'amarillo'}

# Eliminar elementos
colores.remove("verde")
print(colores)  # {'rojo', 'azul', 'amarillo'}

# Intentar eliminar un elemento inexistente genera un error
# colores.remove("morado")  # Error
```

### 🧩 **Métodos comunes**  
```python
# Verificar la existencia de un elemento
print("rojo" in colores)  # True

# Operaciones de conjuntos
conjunto1 = {1, 2, 3}
conjunto2 = {3, 4, 5}

# Unión de conjuntos
print(conjunto1 | conjunto2)  # {1, 2, 3, 4, 5}

# Intersección de conjuntos
print(conjunto1 & conjunto2)  # {3}

# Diferencia de conjuntos
print(conjunto1 - conjunto2)  # {1, 2}
```

---

## **📍 5. Métodos comunes y manipulación de estructuras de datos**  
Aquí recopilamos algunos de los métodos más utilizados en listas, tuplas, diccionarios y conjuntos.

### **Listas**  
```python
# Comprobar si un elemento existe en una lista
print(3 in [1, 2, 3])  # True
```

### **Tuplas**  
```python
# Concatenar tuplas
tupla1 = (1, 2)
tupla2 = (3, 4)
print(tupla1 + tupla2)  # (1, 2, 3, 4)
```

### **Diccionarios**  
```python
# Obtener un valor con una clave (sin error si no existe)
print(persona.get("nombre", "Desconocido"))  # Juan
```

### **Conjuntos**  
```python
# Eliminar un elemento sin error si no existe
colores.discard("morado")  # No ocurre error
```

---

## **📍 6. Ejercicios Prácticos**  
✅ **Crear un programa que reciba una lista de nombres y retorne la lista sin duplicados.**  
✅ **Escribir una función que reciba un diccionario y retorne una lista con las claves de los valores mayores a un número dado.**  
✅ **Crear un conjunto de números e implementar operaciones de unión, intersección y diferencia.**  
✅ **Escribir un programa que cuente cuántas veces aparece un elemento en una lista.**

---

## **💡 Recursos Adicionales**  
- [Documentación oficial de Python](https://docs.python.org/3/tutorial/datastructures.html)  
- [Curso interactivo sobre estructuras de datos](https://www.w3schools.com/python/python_lists.asp)  

---

## **📌 Contribuciones**  
Si tienes sugerencias o mejoras para esta sección, **haz un fork del repositorio y envía un pull request**.  

---

## **📜 Licencia**  
Este proyecto está bajo la licencia **MIT**, lo que significa que puedes usarlo libremente.  