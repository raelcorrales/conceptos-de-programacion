# **Sorted Sets en Python** 🔢📊

## **📖 Descripción**  
Un **Sorted Set** (o conjunto ordenado) es una estructura de datos que combina las propiedades de un conjunto (sin elementos duplicados) y una lista ordenada. En un Sorted Set, los elementos están almacenados en orden, pero a diferencia de una lista, no puedes tener duplicados. Es una estructura muy útil cuando necesitas mantener elementos únicos con un orden determinado.

En Python, los **Sorted Sets** se pueden implementar utilizando bibliotecas externas como `sortedcontainers` o `redis-py`, que permiten mantener un conjunto ordenado de elementos de manera eficiente.

---

## **📌 Contenido**  
1. ¿Qué es un Sorted Set?  
2. ¿Por qué usar un Sorted Set?  
3. Implementación en Python utilizando `sortedcontainers`  
4. Operaciones básicas en Sorted Sets  
5. Ejemplos prácticos  
6. Recursos adicionales

---

## **📍 1. ¿Qué es un Sorted Set?**  
Un **Sorted Set** es una colección de elementos que tiene dos características principales:

1. **Elementos únicos**: No se permiten duplicados.
2. **Ordenado**: Los elementos están siempre ordenados según un criterio específico. Generalmente, el orden se basa en los valores de los elementos, y este orden se puede ascendente o descendente.

En términos generales, un Sorted Set puede considerarse como un conjunto que garantiza el orden de los elementos. Esto lo hace muy útil para situaciones en las que se necesita acceso rápido a los elementos de un conjunto en un orden determinado, como en sistemas de clasificación o almacenamiento de puntuaciones.

---

## **📍 2. ¿Por qué usar un Sorted Set?**  
Algunas ventajas de los **Sorted Sets** son:

1. **Búsqueda eficiente**: Puedes acceder a los elementos de manera rápida, en tiempo logarítmico, gracias a su estructura interna.
2. **Orden automático**: No necesitas preocuparte por ordenar manualmente los elementos, ya que el conjunto mantiene el orden por sí mismo.
3. **Sin duplicados**: Similar a los conjuntos (`set`), no se permiten elementos duplicados, lo que asegura la unicidad de los valores.
4. **Operaciones rápidas**: Muchas operaciones como inserciones, eliminaciones y búsquedas se realizan de manera eficiente.

Algunas aplicaciones comunes de los **Sorted Sets** incluyen:
- Implementación de sistemas de puntuaciones (por ejemplo, tablas de clasificación).
- Mantener un conjunto de elementos ordenados, como fechas o valores numéricos.
- Sistemas de caché donde se necesita acceder a los elementos más recientes o más importantes.

---

## **📍 3. Implementación en Python utilizando `sortedcontainers`**  
En Python, uno de los paquetes más utilizados para trabajar con **Sorted Sets** es `sortedcontainers`. Esta librería proporciona una estructura llamada `SortedSet` que mantiene los elementos ordenados y permite realizar operaciones de manera eficiente.

### 📌 **Instalación**  
Para instalar `sortedcontainers`, puedes utilizar `pip`:

```bash
pip install sortedcontainers
```

---

## **📍 4. Operaciones básicas en Sorted Sets**  

La clase `SortedSet` de la librería `sortedcontainers` proporciona una variedad de operaciones para trabajar con conjuntos ordenados. Algunas de las operaciones más comunes incluyen:

1. **Crear un Sorted Set**  
   Puedes crear un `SortedSet` de manera similar a un conjunto normal, pero con la diferencia de que los elementos estarán ordenados.

   ```python
   from sortedcontainers import SortedSet

   # Crear un Sorted Set vacío
   sset = SortedSet()

   # Crear un Sorted Set con elementos iniciales
   sset = SortedSet([5, 3, 7, 1])
   print(sset)  # Salida: SortedSet([1, 3, 5, 7])
   ```

2. **Agregar elementos**  
   Puedes agregar elementos a un `SortedSet` utilizando el método `add()`.

   ```python
   sset.add(4)
   print(sset)  # Salida: SortedSet([1, 3, 4, 5, 7])
   ```

3. **Eliminar elementos**  
   Para eliminar un elemento de un `SortedSet`, puedes usar `remove()`.

   ```python
   sset.remove(3)
   print(sset)  # Salida: SortedSet([1, 4, 5, 7])
   ```

4. **Buscar elementos**  
   Puedes verificar si un elemento está presente en el conjunto utilizando el operador `in`.

   ```python
   print(4 in sset)  # Salida: True
   print(10 in sset)  # Salida: False
   ```

5. **Acceder al primer o último elemento**  
   Para acceder al primer o último elemento del `SortedSet`, puedes usar el índice:

   ```python
   print(sset[0])  # Primer elemento: 1
   print(sset[-1])  # Último elemento: 7
   ```

6. **Recorrer un SortedSet**  
   Puedes iterar sobre los elementos de un `SortedSet` de manera similar a cómo iteras sobre una lista.

   ```python
   for elem in sset:
       print(elem)
   ```

7. **Obtener el tamaño del SortedSet**  
   Puedes obtener el tamaño de un `SortedSet` utilizando `len()`.

   ```python
   print(len(sset))  # Salida: 4
   ```

8. **Encontrar el rango de un SortedSet**  
   Puedes obtener un rango de elementos entre dos valores usando el operador de corte (`:`).

   ```python
   print(sset[1:3])  # Salida: SortedSet([4, 5])
   ```

---

## **📍 5. Ejemplos prácticos**  

### 📌 **Ejemplo 1: Implementación de una tabla de clasificación**  
Supón que estás implementando una tabla de clasificación para un juego y quieres mantener las puntuaciones de los jugadores en orden descendente.

```python
from sortedcontainers import SortedSet

# Crear el conjunto ordenado
tabla_clasificacion = SortedSet()

# Agregar puntuaciones
tabla_clasificacion.add(500)
tabla_clasificacion.add(700)
tabla_clasificacion.add(600)
tabla_clasificacion.add(800)

# Ver la tabla
print(tabla_clasificacion)  # Salida: SortedSet([500, 600, 700, 800])

# Obtener la puntuación más alta (el último elemento)
print(tabla_clasificacion[-1])  # Salida: 800
```

### 📌 **Ejemplo 2: Mantener un conjunto de elementos únicos y ordenados**  
Otro ejemplo práctico es cuando necesitas mantener un conjunto de elementos únicos, pero también necesitas acceder a ellos en orden.

```python
from sortedcontainers import SortedSet

# Crear un conjunto ordenado
numeros = SortedSet([5, 3, 8, 6, 2])

# Agregar más elementos
numeros.add(4)
numeros.add(7)

# Eliminar un elemento
numeros.remove(3)

# Ver el conjunto ordenado
print(numeros)  # Salida: SortedSet([2, 4, 5, 6, 7, 8])
```

---

## **📍 6. Recursos adicionales**  
- [Documentación oficial de `sortedcontainers`](https://sortedcontainers.readthedocs.io/en/latest/)  
- [Introducción a los Sorted Sets - Geeks for Geeks](https://www.geeksforgeeks.org/redis-sorted-sets/)  
- [Tutorial sobre Sorted Sets con `sortedcontainers` - Real Python](https://realpython.com/python-sorted-containers/)

---

## **📌 Contribuciones**  
Si tienes sugerencias o mejoras para esta sección, **haz un fork del repositorio y envía un pull request**.

---

## **📜 Licencia**  
Este proyecto está bajo la licencia **MIT**, lo que significa que puedes usarlo libremente.
