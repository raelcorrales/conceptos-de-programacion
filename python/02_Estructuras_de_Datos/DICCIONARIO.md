# **Diccionarios en Python**

## **📖 Descripción**  
Un **diccionario** en Python es una colección no ordenada, mutable e indexada de pares clave-valor. Los diccionarios se utilizan para almacenar datos que se pueden asociar con una clave única y permitir un acceso rápido a los valores asociados con estas claves. Son una de las estructuras de datos más poderosas en Python, especialmente útiles cuando se necesita asociar datos relacionados entre sí.

---

## **📌 Contenido**

1. ¿Qué es un diccionario?
2. Creación de diccionarios
3. Acceder, agregar y modificar elementos
4. Eliminar elementos de un diccionario
5. Métodos comunes de diccionarios
6. Diccionarios anidados
7. Ejercicios prácticos

---

## **📍 1. ¿Qué es un diccionario?**  
Un **diccionario** es una colección de elementos donde cada elemento es un par clave-valor. Las claves deben ser únicas y son inmutables (pueden ser de tipo `int`, `str`, `tuple`, entre otros). Los valores pueden ser de cualquier tipo de datos, y un diccionario puede tener diferentes valores asociados a diferentes claves.

### Características de los diccionarios:
- **No ordenados**: Los elementos no tienen un índice numérico.
- **Mutables**: Puedes agregar, eliminar y modificar elementos.
- **Claves únicas**: Las claves no pueden repetirse, pero los valores pueden ser duplicados.
- **Claves inmutables**: Las claves deben ser tipos de datos inmutables como `int`, `str`, `tuple`, etc.

---

## **📍 2. Creación de diccionarios**  
Un diccionario se puede crear utilizando llaves `{}` y separando las claves y los valores con dos puntos `:`. Cada par clave-valor está separado por comas.

### 📌 **Crear un diccionario vacío**  
```python
# Crear un diccionario vacío
mi_diccionario = {}
print(mi_diccionario)  # Salida: {}
```

### 📌 **Crear un diccionario con elementos**  
```python
# Crear un diccionario con algunos elementos
persona = {'nombre': 'Juan', 'edad': 25, 'ciudad': 'Puerto Vallarta'}
print(persona)  # Salida: {'nombre': 'Juan', 'edad': 25, 'ciudad': 'Puerto Vallarta'}
```

---

## **📍 3. Acceder, agregar y modificar elementos**

### 📌 **Acceder a un valor mediante una clave**  
Puedes acceder a un valor de un diccionario utilizando la clave entre corchetes `[]` o el método `get()`.

```python
# Acceder a un valor con corchetes
nombre = persona['nombre']
print(nombre)  # Salida: Juan

# Acceder a un valor con el método get()
edad = persona.get('edad')
print(edad)  # Salida: 25
```

### 📌 **Agregar un nuevo par clave-valor**  
```python
# Agregar un nuevo par clave-valor
persona['correo'] = 'juan@example.com'
print(persona)  # Salida: {'nombre': 'Juan', 'edad': 25, 'ciudad': 'Puerto Vallarta', 'correo': 'juan@example.com'}
```

### 📌 **Modificar el valor de una clave existente**  
```python
# Modificar el valor de una clave existente
persona['edad'] = 26
print(persona)  # Salida: {'nombre': 'Juan', 'edad': 26, 'ciudad': 'Puerto Vallarta', 'correo': 'juan@example.com'}
```

---

## **📍 4. Eliminar elementos de un diccionario**

### 📌 **Eliminar un par clave-valor con `del`**  
```python
# Eliminar un par clave-valor
del persona['correo']
print(persona)  # Salida: {'nombre': 'Juan', 'edad': 26, 'ciudad': 'Puerto Vallarta'}
```

### 📌 **Eliminar un par clave-valor con `pop()`**  
El método `pop()` elimina el elemento con la clave dada y devuelve su valor.
```python
# Eliminar un elemento y obtener su valor
ciudad = persona.pop('ciudad')
print(ciudad)  # Salida: Puerto Vallarta
print(persona)  # Salida: {'nombre': 'Juan', 'edad': 26}
```

### 📌 **Eliminar todos los elementos con `clear()`**  
```python
# Eliminar todos los elementos del diccionario
persona.clear()
print(persona)  # Salida: {}
```

---

## **📍 5. Métodos comunes de diccionarios**

### 📌 **`keys()`**  
Devuelve las claves del diccionario.
```python
# Obtener las claves de un diccionario
claves = persona.keys()
print(claves)  # Salida: dict_keys(['nombre', 'edad'])
```

### 📌 **`values()`**  
Devuelve los valores del diccionario.
```python
# Obtener los valores de un diccionario
valores = persona.values()
print(valores)  # Salida: dict_values(['Juan', 26])
```

### 📌 **`items()`**  
Devuelve los pares clave-valor como tuplas.
```python
# Obtener los pares clave-valor
items = persona.items()
print(items)  # Salida: dict_items([('nombre', 'Juan'), ('edad', 26)])
```

### 📌 **`update()`**  
Permite actualizar un diccionario con otro diccionario o con pares clave-valor.
```python
# Actualizar un diccionario con otro diccionario
persona.update({'ciudad': 'Puerto Vallarta', 'correo': 'juan@example.com'})
print(persona)  # Salida: {'nombre': 'Juan', 'edad': 26, 'ciudad': 'Puerto Vallarta', 'correo': 'juan@example.com'}
```

---

## **📍 6. Diccionarios anidados**  
Es posible tener diccionarios dentro de diccionarios. Esto se conoce como **diccionarios anidados**.

```python
# Diccionario anidado
persona = {
    'nombre': 'Juan',
    'edad': 26,
    'direccion': {
        'calle': 'Avenida Principal',
        'ciudad': 'Puerto Vallarta',
        'pais': 'México'
    }
}

# Acceder a un valor dentro de un diccionario anidado
ciudad = persona['direccion']['ciudad']
print(ciudad)  # Salida: Puerto Vallarta
```

---

## **📍 7. Ejercicios prácticos**

✅ **Crear un diccionario para representar a una persona, que contenga su nombre, edad, ciudad y correo.**  
✅ **Agregar una clave `telefono` al diccionario de la persona y modificar su valor.**  
✅ **Eliminar la clave `correo` del diccionario de la persona.**  
✅ **Usar el método `keys()`, `values()` e `items()` para imprimir las claves, valores y pares clave-valor del diccionario.**  
✅ **Crear un diccionario anidado que represente una empresa con empleados.**

---

## **📌 Recursos adicionales**  
- [Documentación oficial de Python: Diccionarios](https://docs.python.org/3/tutorial/datastructures.html#dictionaries)  
- [Tutorial sobre Diccionarios en Python - Real Python](https://realpython.com/python-dicts/)

---

## **📌 Contribuciones**  
Si tienes sugerencias o mejoras para esta sección, **haz un fork del repositorio y envía un pull request**.

---

## **📜 Licencia**  
Este proyecto está bajo la licencia **MIT**, lo que significa que puedes usarlo libremente.
