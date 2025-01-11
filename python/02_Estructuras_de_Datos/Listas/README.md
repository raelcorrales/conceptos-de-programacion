# Listas
## Fundamentos
### ¿Qué son las listas en Python?
Son estructuras de datos ordenadas y mutables que permiten almacenar colecciones de elementos.
Ejemplo:
```python
mi_lista = [1, "hola", 3.14]
```

#### Comparación con otros tipos de datos (tuplas, conjuntos).
- **Tuplas:** Inmutables, se utilizan para almacenar datos que no cambiarán.
- **Conjuntos:** Desordenados, no permiten elementos duplicados y se utilizan para realizar operaciones matemáticas de conjuntos.

### Creación de listas:
#### Listas vacías:
```python
lista_vacia = []
```

#### A partir de un iterable:
```python
lista_numeros = list(range(10))
```

#### Listas por comprensión:
```python
cuadrados = [x**2 for x in range(5)]
```

### Acceso a elementos:
#### Indexacion:
```python
primer_elemento = mi_lista[0]
```

#### Slicing:
```python
sublista = mi_lista[2:5]
```

## Modificación de listas
### Añadir elementos:
- **append:** Agrega un elemento al final de la lista.
```python
mi_lista.append(15)
```

- **insert:** Inserta un elemento en una posicion especifica.
```python
mi_lista.insert(0, 16)
```

- **extend:** Agrega los elementos de otra lista a nuestra lista.
```python
otra_lista = [10, 12, 15]
mi_lista.extend(otra_lista)
```

### Eliminar elementos:
#### remove(), pop(), clear().
- **remove():** 
```python
mi_lista.remove()
```

- **pop():** 
```python
mi_lista.pop()
```
- **clear():**
```python
mi_lista.clear()
```

### Operaciones con listas
- **Concatenación de listas:** Usando el operador +.
- **Repetición de listas:** Utilizando el operador *.
- **Longitud de una lista:** Función len().
- **Verificar si un elemento está en una lista:** Operador in.
- **Ordenar listas:** sort(), reverse().
- **Copiar listas:**
	- **Asignación:**
	Al hacer una asignacion de este tipo, ambas variables estarian apuntando al mismo registro, asi que si modificas un variable o la otra, ambas mostraran las mismas modificaciones.
```python
nueva_lista = mi_lista
```
	- **Copia profunda:**
	Al hacer una asignacion usando la funcion de copia profunda, creara un nuevo registro, y si modificas la nueva lista, la anterior no seria afectada.
```python
nueva_lista = mi_lista.copy()
```

### Iteracion sobre listas
- **Bucles for:**
```python
for elemento in mi_lista:
      print(elemento)
```

- **Rangos**
```python
for n in range(0, 5):
      print(mi_lista[n])
```

- **Enumeración:** La funcion enumerate nos sirve para crear un iterador que tendra la enumeracion de cada elemento y el elemento para poder colocarlo en un loop y poder obtener el indice del valor dentro de una iteracion.
```python
for n, elemento in enumerate(mi_lista):
      print(n, elemento)
```

### Listas anidadas
Podemos guardar listas dentro de listas y se manejarian como un valor mas.
```python
matriz = [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]]
matriz[0][1]
```
Esto nos permite acceder el primer valor de nuestra lista matriz y despues acceder al segundo elemento de este valor.
seria lo mismo que hacer:
```python
matriz = [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]]
submatriz = matriz[0]
submatriz[1]
```

### Listas por comprensión
### Funciones y métodos útiles
- **min:** Esta funcion nos permite obtener el menor valor de la lista.
- **max:** Esta funcion nos permite obtener el mayor valor de la lista.
- **sum:**  Esta funcion nos permite obtener la suma de la lista.
- **count:**  Esta funcion nos permite obtener el numero de elementos que existe de cierto valor en la lista.
- **index:** Esta funcion nos permite obtener el indice del primer valor encontrado de la lista.

