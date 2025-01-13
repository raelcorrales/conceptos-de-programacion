### 📌 **Funciones y Módulos en Python**  

# **Funciones y Módulos en Python**  

## **📖 Descripción**  
Esta sección cubre cómo **crear y usar funciones** en Python, lo que te permite organizar tu código de manera modular. También aprenderás sobre **módulos** para separar y reutilizar código entre distintos archivos, promoviendo una mejor organización en proyectos más grandes.

## **📌 Contenido**  
1. Funciones  
2. Parámetros y argumentos  
3. Funciones lambda  
4. Retorno de valores  
5. Alcance de las variables  
6. Módulos  
7. Importación de módulos  
8. Ejercicios prácticos  

---

## **📍 1. Funciones**  
Una **función** es un bloque de código reutilizable que realiza una tarea específica. Las funciones permiten estructurar tu programa y evitar la repetición de código.

### 📌 **Definición de funciones**  
```python
# Definir una función simple
def saludar():
    print("¡Hola, Mundo!")

# Llamar a la función
saludar()  # Salida: ¡Hola, Mundo!
```

### 🧩 **Funciones con parámetros**  
```python
# Función con parámetros
def saludar_persona(nombre):
    print(f"¡Hola, {nombre}!")

saludar_persona("Juan")  # Salida: ¡Hola, Juan!
```

---

## **📍 2. Parámetros y argumentos**  
Los **parámetros** son las variables que se definen en la firma de la función, mientras que los **argumentos** son los valores que pasamos a la función cuando la llamamos.

### 📌 **Parámetros por defecto**  
```python
def saludar(nombre="Mundo"):
    print(f"¡Hola, {nombre}!")

saludar()        # Salida: ¡Hola, Mundo!
saludar("Juan")  # Salida: ¡Hola, Juan!
```

### 📌 **Múltiples parámetros**  
```python
def sumar(a, b):
    return a + b

print(sumar(3, 5))  # Salida: 8
```

---

## **📍 3. Funciones lambda**  
Las **funciones lambda** son funciones anónimas que se definen en una sola línea, generalmente para funciones simples y de uso único.

### 📌 **Definición de función lambda**  
```python
# Función lambda que suma dos números
suma = lambda x, y: x + y

print(suma(3, 5))  # Salida: 8
```

---

## **📍 4. Retorno de valores**  
Una **función** puede devolver un valor mediante la palabra clave `return`. El valor retornado se puede almacenar en una variable o utilizar directamente.

### 📌 **Uso de return**  
```python
def multiplicar(a, b):
    return a * b

resultado = multiplicar(4, 3)
print(resultado)  # Salida: 12
```

---

## **📍 5. Alcance de las variables**  
El **alcance** de una variable se refiere a la zona del programa donde se puede acceder a ella. Las variables pueden ser locales o globales.

### 📌 **Variables locales y globales**  
```python
x = 10  # Variable global

def mi_funcion():
    x = 5  # Variable local
    print(f"Valor local de x: {x}")

mi_funcion()       # Salida: Valor local de x: 5
print(f"Valor global de x: {x}")  # Salida: Valor global de x: 10
```

---

## **📍 6. Módulos**  
Un **módulo** es un archivo que contiene definiciones de funciones, clases y variables. Puedes usar módulos para organizar tu código en partes reutilizables.

### 📌 **Creación de un módulo**  
Crea un archivo llamado `mi_modulo.py` con el siguiente contenido:

```python
# mi_modulo.py
def saludar():
    print("¡Hola desde el módulo!")

def despedir():
    print("¡Adiós desde el módulo!")
```

### 📌 **Uso de un módulo**  
```python
# Importar funciones del módulo
import mi_modulo

mi_modulo.saludar()   # Salida: ¡Hola desde el módulo!
mi_modulo.despedir()  # Salida: ¡Adiós desde el módulo!
```

---

## **📍 7. Importación de módulos**  
Puedes importar un módulo completo o solo partes específicas de él.

### 📌 **Importación de módulo completo**  
```python
import math

print(math.sqrt(16))  # Salida: 4.0
```

### 📌 **Importación selectiva de funciones**  
```python
from math import sqrt

print(sqrt(16))  # Salida: 4.0
```

### 📌 **Alias para módulos**  
Puedes asignar un alias a un módulo para hacerlo más fácil de usar.

```python
import numpy as np

arr = np.array([1, 2, 3])
print(arr)  # Salida: [1 2 3]
```

---

## **📍 8. Ejercicios Prácticos**  
✅ **Escribir una función que calcule el área de un círculo dado su radio.**  
✅ **Crear un módulo con funciones para realizar operaciones matemáticas básicas (suma, resta, multiplicación, división).**  
✅ **Escribir una función lambda que calcule el cuadrado de un número.**  
✅ **Crear una función que reciba una lista y devuelva la cantidad de números negativos.**  
✅ **Escribir una función que convierta grados Celsius a Fahrenheit.**

---

## **💡 Recursos Adicionales**  
- [Documentación oficial de Python: Funciones](https://docs.python.org/3/tutorial/controlflow.html#defining-functions)  
- [Tutorial sobre Módulos en Python](https://realpython.com/python-modules-packages/)  

---

## **📌 Contribuciones**  
Si tienes sugerencias o mejoras para esta sección, **haz un fork del repositorio y envía un pull request**.  

---

## **📜 Licencia**  
Este proyecto está bajo la licencia **MIT**, lo que significa que puedes usarlo libremente.  