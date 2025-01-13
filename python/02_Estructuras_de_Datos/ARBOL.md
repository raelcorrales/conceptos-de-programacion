# **Árboles en Python** 🌳💻

## **📖 Descripción**  
Un **Árbol** es una estructura de datos jerárquica que consta de nodos conectados por aristas. Es muy útil para representar datos que tienen una relación jerárquica, como directorios de archivos, estructuras organizacionales, árboles genealógicos, etc.

En un árbol, cada nodo puede tener **nodos hijos** y solo un nodo tiene **nodo padre** (excepto el nodo raíz, que no tiene padre). Los árboles son estructuras fundamentales en informática y se utilizan en diversas aplicaciones, como bases de datos, sistemas de archivos, compiladores, y más.

---

## **📌 Contenido**  
1. ¿Qué es un Árbol?  
2. Tipos de Árboles  
3. Implementación básica de un Árbol en Python  
4. Operaciones básicas en Árboles  
5. Ejemplos prácticos  
6. Recursos adicionales

---

## **📍 1. ¿Qué es un Árbol?**  
Un **Árbol** es una estructura de datos compuesta por nodos conectados entre sí. La idea clave es que los datos están organizados en niveles jerárquicos.

### Elementos de un Árbol:
1. **Raíz (Root)**: El nodo principal que no tiene padre. Es el punto de entrada al árbol.
2. **Nodos (Nodes)**: Los elementos del árbol que contienen datos y referencias a sus nodos hijos.
3. **Hijos (Children)**: Los nodos que están directamente conectados a otro nodo y debajo de él en la jerarquía.
4. **Padre (Parent)**: Un nodo que está conectado a sus nodos hijos.
5. **Hojas (Leaves)**: Los nodos que no tienen hijos.
6. **Altura del árbol (Height)**: La longitud del camino más largo desde la raíz hasta una hoja.
7. **Profundidad del nodo (Depth)**: La longitud del camino desde la raíz hasta el nodo.

---

## **📍 2. Tipos de Árboles**  
Existen varios tipos de árboles, cada uno con características específicas que los hacen adecuados para ciertos problemas. Algunos de los más comunes incluyen:

1. **Árbol Binario**: Un árbol en el que cada nodo tiene como máximo dos hijos (izquierdo y derecho).
2. **Árbol Binario de Búsqueda (BST)**: Un árbol binario en el que los nodos están organizados de tal manera que el valor de cada nodo en el subárbol izquierdo es menor que el valor del nodo raíz y el valor de cada nodo en el subárbol derecho es mayor.
3. **Árbol AVL**: Un árbol binario de búsqueda autoequilibrado en el que las alturas de los subárboles izquierdo y derecho difieren como máximo en 1.
4. **Árbol de Expresiones**: Un árbol usado para representar expresiones matemáticas o lógicas.
5. **Árbol N-ario**: Un árbol en el que cada nodo puede tener más de dos hijos.

---

## **📍 3. Implementación básica de un Árbol en Python**  
A continuación, implementaremos una clase básica para un árbol en Python. Esta implementación tendrá un nodo raíz y permitirá agregar nodos a los hijos.

### **Código de Implementación de Árbol**:

```python
class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.hijos = []

class Arbol:
    def __init__(self, raiz):
        self.raiz = Nodo(raiz)
    
    def agregar_hijo(self, nodo_padre, valor_hijo):
        hijo = Nodo(valor_hijo)
        nodo_padre.hijos.append(hijo)
        return hijo
    
    def imprimir_arbol(self, nodo=None, nivel=0):
        if nodo is None:
            nodo = self.raiz
        print(" " * nivel + str(nodo.valor))
        for hijo in nodo.hijos:
            self.imprimir_arbol(hijo, nivel + 1)
```

### **Explicación**:
- **Nodo**: La clase `Nodo` representa un nodo en el árbol, con un valor y una lista de hijos.
- **Arbol**: La clase `Arbol` representa el árbol y contiene métodos para agregar nodos hijos y para imprimir el árbol de manera jerárquica.

### **Ejemplo de uso**:

```python
# Crear el árbol
arbol = Arbol("Raíz")

# Agregar hijos a la raíz
nodo_izquierdo = arbol.agregar_hijo(arbol.raiz, "Izquierdo")
nodo_derecho = arbol.agregar_hijo(arbol.raiz, "Derecho")

# Agregar hijos a un nodo
arbol.agregar_hijo(nodo_izquierdo, "Izquierdo-Izquierdo")
arbol.agregar_hijo(nodo_izquierdo, "Izquierdo-Derecho")

# Imprimir el árbol
arbol.imprimir_arbol()
```

**Salida**:
```
Raíz
 Izquierdo
  Izquierdo-Izquierdo
  Izquierdo-Derecho
 Derecho
```

---

## **📍 4. Operaciones básicas en Árboles**  
Algunas de las operaciones más comunes que puedes realizar en árboles incluyen:

1. **Recorridos en Árboles**: Los recorridos se refieren a la forma en que visitamos los nodos del árbol. Los tres tipos principales son:
   - **Preorden**: Se visita primero el nodo, luego sus hijos (izquierdo y derecho).
   - **Inorden**: Se visita primero el hijo izquierdo, luego el nodo, y finalmente el hijo derecho.
   - **Postorden**: Se visita primero los hijos, luego el nodo.
   - **Nivel por nivel (BFS)**: Se recorren los nodos por niveles.

   **Implementación de Recorridos en Árboles**:

   ```python
   class Arbol:
       # Agregar métodos de recorrido

       def recorrido_preorden(self, nodo=None):
           if nodo is None:
               nodo = self.raiz
           print(nodo.valor, end=" ")
           for hijo in nodo.hijos:
               self.recorrido_preorden(hijo)
       
       def recorrido_inorden(self, nodo=None):
           if nodo is None:
               nodo = self.raiz
           if nodo.hijos:
               self.recorrido_inorden(nodo.hijos[0])  # Solo considerando el primer hijo
           print(nodo.valor, end=" ")
           for hijo in nodo.hijos[1:]:
               self.recorrido_inorden(hijo)

       def recorrido_postorden(self, nodo=None):
           if nodo is None:
               nodo = self.raiz
           for hijo in nodo.hijos:
               self.recorrido_postorden(hijo)
           print(nodo.valor, end=" ")
   
       def recorrido_bfs(self):
           cola = [self.raiz]
           while cola:
               nodo = cola.pop(0)
               print(nodo.valor, end=" ")
               cola.extend(nodo.hijos)
   ```

2. **Buscar un nodo**: Puedes recorrer el árbol en busca de un nodo con un valor específico.
   
   ```python
   def buscar_nodo(self, nodo, valor):
       if nodo.valor == valor:
           return nodo
       for hijo in nodo.hijos:
           resultado = self.buscar_nodo(hijo, valor)
           if resultado:
               return resultado
       return None
   ```

3. **Eliminar un nodo**: Para eliminar un nodo, necesitas modificar las referencias de los nodos padres para que dejen de apuntar al nodo hijo que se desea eliminar.

---

## **📍 5. Ejemplos prácticos**  

### 📌 **Ejemplo 1: Representación de un Árbol Genealógico**  
Puedes usar un árbol para representar un árbol genealógico, donde cada nodo es una persona y los hijos representan los descendientes.

```python
# Crear el árbol genealógico
familia = Arbol("Abuelo")

# Agregar hijos (padres)
padre = familia.agregar_hijo(familia.raiz, "Padre")
madre = familia.agregar_hijo(familia.raiz, "Madre")

# Agregar nietos
familia.agregar_hijo(padre, "Hijo 1")
familia.agregar_hijo(padre, "Hijo 2")
familia.agregar_hijo(madre, "Hija 1")

# Imprimir el árbol genealógico
familia.imprimir_arbol()
```

### 📌 **Ejemplo 2: Sistema de Archivos**  
Puedes representar un sistema de archivos con un árbol, donde cada directorio es un nodo y los archivos son sus hijos.

```python
# Crear el árbol de archivos
sistema_archivos = Arbol("Raíz")

# Agregar directorios
documentos = sistema_archivos.agregar_hijo(sistema_archivos.raiz, "Documentos")
imagenes = sistema_archivos.agregar_hijo(sistema_archivos.raiz, "Imágenes")

# Agregar archivos a directorios
sistema_archivos.agregar_hijo(documentos, "archivo1.txt")
sistema_archivos.agregar_hijo(imagenes, "foto1.png")

# Imprimir el árbol de archivos
sistema_archivos.imprimir_arbol()
```

---

## **📍 6. Recursos adicionales**  
- [Estructuras de Datos en Python - Real Python](https://realpython.com/tutorials/data-structures/)
- [Introducción a los Árboles en Geeks for Geeks](https://www.geeksforgeeks.org/binary-tree-set-1-introduction/)
- [Documentación oficial de Python - Estructuras de Datos](https://docs.python.org/3/tutorial/datastructures.html)

---

## **📌 Contribuciones**  
Si tienes sugerencias o mejoras para esta sección, **haz un fork del repositorio y envía un pull request**.

---

## **📜 Licencia**  
Este proyecto está bajo la licencia **MIT**, lo que significa que puedes usarlo libremente.
