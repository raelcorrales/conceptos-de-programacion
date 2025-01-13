### 📌 **Introducción a Python**  

# **Python: Fundamentos y Primeros Pasos**  

## **📖 Descripción**  
Este repositorio contiene una introducción a **Python**, abordando desde los fundamentos del lenguaje hasta estructuras de datos y control de flujo. Es ideal para principiantes que desean aprender a programar en Python de manera práctica y sencilla.  

## **📌 Contenido**  
1. **¿Qué es Python?**  
2. Instalación y Configuración  
3. Primer Programa en Python  
4. Tipos de Datos y Variables  
5. Operadores y Expresiones  
6. Control de Flujo (Condiciones y Bucles)  
7. Funciones y Módulos  
8. Manejo de Archivos  
9. Librerías Básicas (math, datetime, os, sys)  
10. Ejercicios Prácticos  

## **📍 1. ¿Qué es Python?**  
Python es un lenguaje de programación **interpretado, de alto nivel y con tipado dinámico**. Su sintaxis sencilla y legible lo convierte en una excelente opción para principiantes y expertos.  

✔ **Fácil de aprender** y leer.  
✔ **Multiparadigma** (programación estructurada, funcional y orientada a objetos).  
✔ **Gran ecosistema de librerías** para desarrollo web, ciencia de datos, IA, etc.  
✔ **Compatible con múltiples plataformas** (Windows, macOS, Linux).  

## **🛠️ 2. Instalación y Configuración**  
🔹 **Windows:** Descarga Python desde [python.org](https://www.python.org/downloads/) y sigue el instalador.  
🔹 **macOS/Linux:** Puedes instalar Python con:  
```bash
sudo apt update && sudo apt install python3  # Ubuntu
brew install python  # macOS con Homebrew
```  
🔹 **Verificar instalación:**  
```bash
python --version
```  

## **🚀 3. Primer Programa en Python**  
Guarda el siguiente código en un archivo llamado `hola_mundo.py` y ejecútalo con `python hola_mundo.py`.  

```python
print("¡Hola, mundo!")
```

## **🔹 4. Tipos de Datos y Variables**  
```python
nombre = "Juan"  # String
edad = 25  # Integer
altura = 1.75  # Float
es_programador = True  # Boolean
```

## **🔹 5. Operadores y Expresiones**  
```python
a = 10
b = 3
print(a + b)  # Suma
print(a - b)  # Resta
print(a * b)  # Multiplicación
print(a / b)  # División
print(a // b) # División entera
print(a % b)  # Módulo
print(a ** b) # Potencia
```

## **🔹 6. Control de Flujo**  
### ✅ Condicionales  
```python
edad = 18
if edad >= 18:
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")
```

### ✅ Bucles  
```python
for i in range(5):
    print(i)

n = 5
while n > 0:
    print(n)
    n -= 1
```

## **🔹 7. Funciones y Módulos**  
```python
def saludar(nombre):
    return f"Hola, {nombre}!"

print(saludar("Juan"))
```

## **🔹 8. Manejo de Archivos**  
```python
with open("archivo.txt", "w") as file:
    file.write("¡Hola desde Python!")

with open("archivo.txt", "r") as file:
    print(file.read())
```

## **🔹 9. Librerías Básicas**  
```python
import math
print(math.sqrt(16))  # Raíz cuadrada

import datetime
print(datetime.datetime.now())  # Fecha y hora actual

import os
print(os.getcwd())  # Ruta del directorio actual
```

## **🎯 10. Ejercicios Prácticos**  
- **Crear un conversor de temperaturas** (°C a °F y viceversa).  
- **Generar una lista de números pares entre 1 y 100**.  
- **Escribir una función que invierta un string**.  
- **Calcular el factorial de un número**.  

---

## **💡 Recursos Adicionales**  
- [Documentación oficial de Python](https://docs.python.org/3/)  
- [Curso de Python en W3Schools](https://www.w3schools.com/python/)  
- [Ejercicios interactivos en Python](https://www.hackerrank.com/domains/tutorials/10-days-of-python)  

---

## **📌 Contribuciones**  
¡Las contribuciones son bienvenidas! Si quieres mejorar esta guía, puedes hacer un **fork** del repositorio y enviar un **pull request**.  