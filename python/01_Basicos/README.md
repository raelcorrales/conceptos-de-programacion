### 📌 **Básicos de Python**  

# **Python: Conceptos Básicos**  

## **📖 Descripción**  
Esta sección cubre los **conceptos esenciales de Python**, como variables, tipos de datos, estructuras de control y funciones. Es ideal para quienes buscan consolidar sus conocimientos básicos antes de avanzar a temas más complejos.  

## **📌 Contenido**  
1. Variables y Tipos de Datos  
2. Operadores y Expresiones  
3. Entrada y Salida de Datos  
4. Estructuras de Control  
5. Funciones y Argumentos  
6. Manejo de Errores  
7. Importación de Módulos  
8. Ejercicios Prácticos  

---

## **📍 1. Variables y Tipos de Datos**  
Python es un lenguaje de **tipado dinámico**, lo que significa que no es necesario declarar el tipo de una variable explícitamente.  

```python
# Tipos de datos en Python
nombre = "Juan"       # String
edad = 30            # Integer
altura = 1.75        # Float
es_estudiante = True # Boolean
```

💡 **Verificar tipo de dato:**  
```python
print(type(nombre))  # <class 'str'>
```

---

## **📍 2. Operadores y Expresiones**  
### 🧮 **Operadores Matemáticos**  
```python
a = 10
b = 3

print(a + b)  # Suma
print(a - b)  # Resta
print(a * b)  # Multiplicación
print(a / b)  # División
print(a // b) # División entera
print(a % b)  # Módulo (residuo)
print(a ** b) # Potencia
```

### 🔁 **Operadores Lógicos y Comparación**  
```python
x = 5
y = 10

print(x > y)   # False
print(x < y)   # True
print(x == y)  # False
print(x != y)  # True

print(True and False)  # False
print(True or False)   # True
print(not True)        # False
```

---

## **📍 3. Entrada y Salida de Datos**  
### 🖥️ **Mostrar información en pantalla**  
```python
print("Hola, Python!")
```

### ⌨ **Entrada del usuario**  
```python
nombre = input("¿Cuál es tu nombre? ")
print("Hola, " + nombre + "!")
```

💡 **Convertir datos de entrada**  
```python
edad = int(input("Ingresa tu edad: "))
print("En 10 años tendrás:", edad + 10)
```

---

## **📍 4. Estructuras de Control**  
### ✅ **Condicionales (if-elif-else)**  
```python
edad = 18

if edad >= 18:
    print("Eres mayor de edad")
elif edad >= 13:
    print("Eres adolescente")
else:
    print("Eres menor de edad")
```

### 🔄 **Bucles (for, while)**  
```python
# Bucle for
for i in range(5):
    print("Iteración:", i)

# Bucle while
contador = 0
while contador < 5:
    print("Contador:", contador)
    contador += 1
```

💡 **Interrupción de bucles:**  
```python
for num in range(10):
    if num == 5:
        break  # Sale del bucle
    print(num)
```

---

## **📍 5. Funciones y Argumentos**  
### 📌 **Definir y llamar funciones**  
```python
def saludar(nombre):
    return f"Hola, {nombre}!"

print(saludar("Juan"))
```

### 🔄 **Funciones con valores por defecto**  
```python
def potencia(base, exponente=2):
    return base ** exponente

print(potencia(3))    # 3² = 9
print(potencia(3, 3)) # 3³ = 27
```

---

## **📍 6. Manejo de Errores**  
💡 **Uso de try-except para evitar fallos en el programa**  
```python
try:
    numero = int(input("Ingresa un número: "))
    print("El doble es:", numero * 2)
except ValueError:
    print("Error: Debes ingresar un número válido.")
```

---

## **📍 7. Importación de Módulos**  
Python tiene muchos **módulos estándar** que facilitan tareas comunes.  

```python
import math

print(math.sqrt(16))  # Raíz cuadrada
print(math.pi)        # Valor de π
```

💡 **Importar solo funciones específicas**  
```python
from math import sqrt, pi

print(sqrt(25))
print(pi)
```

---

## **📍 8. Ejercicios Prácticos**  
✅ **Crear un programa que determine si un número es par o impar.**  
✅ **Generar una tabla de multiplicar de un número ingresado por el usuario.**  
✅ **Escribir una función que reciba un string y devuelva su reverso.**  
✅ **Implementar un contador de vocales en una frase dada.**  

---

## **💡 Recursos Adicionales**  
- [Documentación oficial de Python](https://docs.python.org/3/)  
- [Curso interactivo de Python](https://www.w3schools.com/python/)  
- [Ejercicios prácticos](https://www.hackerrank.com/domains/tutorials/10-days-of-python)  

---

## **📌 Contribuciones**  
Si encuentras errores o quieres mejorar esta guía, **haz un fork del repositorio y envía un pull request**.  