# **Matrices en Python** 🧮💻

## **📖 Descripción**  
Una **matriz** es una estructura de datos bidimensional que se representa como una tabla de filas y columnas. Es una extensión de los vectores y es utilizada ampliamente en matemáticas, ciencias computacionales, y en áreas como álgebra lineal, procesamiento de imágenes, y simulaciones científicas.

En Python, las matrices pueden ser representadas utilizando listas de listas o usando bibliotecas especializadas como **NumPy**. Las matrices son útiles para representar datos en forma de tablas y para realizar operaciones como multiplicación, transposición, determinante, y más.

---

## **📌 Contenido**  
1. ¿Qué es una Matriz?  
2. Representación de Matrices en Python  
3. Operaciones básicas en Matrices  
4. Ejemplos prácticos  
5. Recursos adicionales

---

## **📍 1. ¿Qué es una Matriz?**  
Una **matriz** es una estructura de datos rectangular que se organiza en filas y columnas. Cada elemento en una matriz puede ser accedido mediante un par de índices que corresponden a su fila y columna. Las matrices se utilizan principalmente para representar datos numéricos en aplicaciones matemáticas y científicas.

### Elementos de una Matriz:
1. **Filas**: Las filas son las secuencias horizontales de elementos dentro de la matriz.
2. **Columnas**: Las columnas son las secuencias verticales de elementos dentro de la matriz.
3. **Elemento**: Un elemento es un valor dentro de la matriz, y se accede por su posición (fila, columna).
4. **Dimensiones de una matriz**: Una matriz de **m** filas y **n** columnas se dice que tiene dimensiones **m x n**.

### Ejemplo de Matriz 2x3:

```
| 1  2  3 |
| 4  5  6 |
```

Esta matriz tiene 2 filas y 3 columnas.

---

## **📍 2. Representación de Matrices en Python**  
En Python, las matrices pueden ser representadas usando listas de listas. Cada lista interna representa una fila de la matriz. A continuación, se muestra cómo se puede representar y trabajar con matrices en Python.

### **Representación de una matriz como lista de listas**:

```python
# Crear una matriz 2x3 (2 filas, 3 columnas)
matriz = [
    [1, 2, 3],
    [4, 5, 6]
]
```

### **Acceder a los elementos de la matriz**:
Puedes acceder a los elementos de una matriz utilizando índices, donde el primer índice corresponde a la fila y el segundo al valor dentro de la columna.

```python
# Acceder al elemento en la fila 1, columna 2 (índices comienzan en 0)
print(matriz[0][1])  # Salida: 2
```

### **Obtener el número de filas y columnas**:

```python
# Número de filas (longitud de la lista externa)
filas = len(matriz)

# Número de columnas (longitud de la lista interna)
columnas = len(matriz[0])

print("Filas:", filas)       # Salida: 2
print("Columnas:", columnas) # Salida: 3
```

---

## **📍 3. Operaciones básicas en Matrices**  
Al trabajar con matrices, existen varias operaciones matemáticas y computacionales que podemos realizar:

### 1. **Suma de matrices**:  
Para sumar dos matrices, ambas deben tener las mismas dimensiones. La suma de matrices se realiza sumando los elementos correspondientes de ambas matrices.

```python
def suma_matrices(matriz1, matriz2):
    filas = len(matriz1)
    columnas = len(matriz1[0])
    suma = []
    
    for i in range(filas):
        fila_suma = []
        for j in range(columnas):
            fila_suma.append(matriz1[i][j] + matriz2[i][j])
        suma.append(fila_suma)
    
    return suma

# Ejemplo de suma
matriz1 = [[1, 2, 3], [4, 5, 6]]
matriz2 = [[7, 8, 9], [10, 11, 12]]
resultado = suma_matrices(matriz1, matriz2)
print(resultado)  # Salida: [[8, 10, 12], [14, 16, 18]]
```

### 2. **Multiplicación de matrices**:  
La multiplicación de matrices es más compleja y sigue la regla de que el número de columnas de la primera matriz debe ser igual al número de filas de la segunda matriz.

```python
def multiplicacion_matrices(matriz1, matriz2):
    filas_m1 = len(matriz1)
    columnas_m1 = len(matriz1[0])
    filas_m2 = len(matriz2)
    columnas_m2 = len(matriz2[0])
    
    # Verificar si las matrices se pueden multiplicar
    if columnas_m1 != filas_m2:
        raise ValueError("Las matrices no se pueden multiplicar")
    
    # Crear una matriz vacía para el resultado
    resultado = [[0 for _ in range(columnas_m2)] for _ in range(filas_m1)]
    
    # Realizar la multiplicación
    for i in range(filas_m1):
        for j in range(columnas_m2):
            for k in range(columnas_m1):
                resultado[i][j] += matriz1[i][k] * matriz2[k][j]
    
    return resultado

# Ejemplo de multiplicación
matriz1 = [[1, 2], [3, 4]]
matriz2 = [[5, 6], [7, 8]]
resultado = multiplicacion_matrices(matriz1, matriz2)
print(resultado)  # Salida: [[19, 22], [43, 50]]
```

### 3. **Transposición de una matriz**:  
La transposición de una matriz intercambia filas por columnas. Es decir, la fila `i` se convierte en la columna `i`.

```python
def transponer_matriz(matriz):
    filas = len(matriz)
    columnas = len(matriz[0])
    transpuesta = []
    
    for j in range(columnas):
        fila_transpuesta = []
        for i in range(filas):
            fila_transpuesta.append(matriz[i][j])
        transpuesta.append(fila_transpuesta)
    
    return transpuesta

# Ejemplo de transposición
matriz = [[1, 2, 3], [4, 5, 6]]
resultado = transponer_matriz(matriz)
print(resultado)  # Salida: [[1, 4], [2, 5], [3, 6]]
```

### 4. **Determinante de una matriz** (solo para matrices cuadradas):  
El determinante es un valor que se puede calcular solo para matrices cuadradas (el número de filas y columnas debe ser el mismo). En este caso, utilizaremos la regla de Sarrus para matrices 3x3.

```python
def determinante_matriz(matriz):
    if len(matriz) != 3 or len(matriz[0]) != 3:
        raise ValueError("Este método solo es válido para matrices 3x3")
    
    # Regla de Sarrus para matrices 3x3
    det = (matriz[0][0] * matriz[1][1] * matriz[2][2] +
           matriz[0][1] * matriz[1][2] * matriz[2][0] +
           matriz[0][2] * matriz[1][0] * matriz[2][1] -
           matriz[0][2] * matriz[1][1] * matriz[2][0] -
           matriz[0][1] * matriz[1][0] * matriz[2][2] -
           matriz[0][0] * matriz[1][2] * matriz[2][1])
    
    return det

# Ejemplo de determinante
matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
resultado = determinante_matriz(matriz)
print(resultado)  # Salida: 0 (determinante de la matriz)
```

---

## **📍 4. Ejemplos prácticos**  

### 📌 **Ejemplo 1: Crear una matriz identidad**  
Una matriz identidad es una matriz cuadrada en la que los elementos de la diagonal principal son 1 y el resto son 0.

```python
def matriz_identidad(tamano):
    return [[1 if i == j else 0 for j in range(tamano)] for i in range(tamano)]

# Crear una matriz identidad 3x3
matriz = matriz_identidad(3)
print(matriz)
```

**Salida**:
```
[[1, 0, 0], [0, 1, 0], [0, 0, 1]]
```

---

## **📍 5. Recursos adicionales**  
- [Matrices en Python - Geeks for Geeks](https://www.geeksforgeeks.org/python-program-for-matrix-multiplication/)
- [Numpy Documentation](https://numpy.org/doc/stable/reference/generated/numpy.matrix.html)
- [Introduction to Matrices - Khan Academy](https://www.khanacademy.org/math/linear-algebra/matrix-transformations)

---

## **📌 Contribuciones**  
Si tienes sugerencias o mejoras para esta sección, **haz un fork del repositorio y envía un pull request**.

---

## **📜 Licencia**  
Este proyecto está bajo la licencia **MIT**, lo que significa que puedes usarlo libremente.
