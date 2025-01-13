# **📌 Guía de Dataflow (Apache Beam) para Data Engineers**  

## **1️⃣ Introducción a Dataflow y Apache Beam**  
### **🔹 ¿Qué es Dataflow?**  
Google Cloud Dataflow es un servicio **serverless** para ejecutar pipelines de procesamiento de datos en tiempo real o en lotes, basado en **Apache Beam**.  

✔ **Serverless**: No requiere gestión de infraestructura.  
✔ **Escalabilidad automática**: Se adapta a la carga de trabajo.  
✔ **Integración con GCP**: Funciona con BigQuery, Pub/Sub, Cloud Storage, etc.  
✔ **Modelo unificado**: Permite el mismo código para batch y streaming.  

### **🔹 ¿Qué es Apache Beam?**  
Apache Beam es un **framework de procesamiento de datos** que permite escribir pipelines de manera agnóstica a la plataforma de ejecución (Dataflow, Spark, Flink, etc.).  

**Arquitectura de Apache Beam:**  
1. **Pipeline** → Representa el flujo de datos.  
2. **PCollection** → Estructura de datos distribuida e inmutable.  
3. **Transformations** → Operaciones aplicadas a los datos (`ParDo`, `GroupByKey`, `Windowing`).  
4. **Runner** → Motor de ejecución (Dataflow, Spark, Flink, DirectRunner).  

---

## **2️⃣ Procesamiento Batch vs Streaming en Dataflow**  
### **🔹 Procesamiento Batch**  
✔ Procesa datos **estáticos** y preexistentes.  
✔ Se ejecuta en intervalos definidos (diario, semanal, etc.).  
✔ Ejemplo: **Cálculo de ventas diarias desde BigQuery**.  

**Ejemplo de Pipeline Batch en Apache Beam (Python)**  
```python
import apache_beam as beam

with beam.Pipeline() as p:
    (p
     | 'Leer Datos' >> beam.io.ReadFromText('gs://mi-bucket/datos.csv')
     | 'Transformar' >> beam.Map(lambda x: x.upper())
     | 'Guardar' >> beam.io.WriteToText('gs://mi-bucket/salida'))
```

### **🔹 Procesamiento Streaming**  
✔ Procesa datos en **tiempo real**.  
✔ Usa ventanas de tiempo (`Fixed`, `Sliding`, `Session`).  
✔ Ejemplo: **Procesamiento de eventos de usuarios en Pub/Sub**.  

**Ejemplo de Pipeline Streaming en Apache Beam (Python)**  
```python
with beam.Pipeline() as p:
    (p
     | 'Leer desde Pub/Sub' >> beam.io.ReadFromPubSub(topic='projects/mi-proyecto/topics/mi-topico')
     | 'Transformar' >> beam.Map(lambda x: x.upper())
     | 'Escribir en BigQuery' >> beam.io.WriteToBigQuery('mi-proyecto:mi_dataset.mi_tabla'))
```

### **🔹 Comparación entre Batch y Streaming**  
| **Aspecto** | **Batch** | **Streaming** |
|------------|---------|------------|
| **Latencia** | Alta | Baja |
| **Tipo de Datos** | Históricos | En tiempo real |
| **Ventanas** | No aplica | `Fixed`, `Sliding`, `Session` |
| **Casos de Uso** | Reportes, ETLs | Análisis en tiempo real, IoT |

---

## **3️⃣ Patrones de Procesamiento de Datos en Dataflow**  
### **🔹 1. Transformaciones Elementales**  
✔ **Map (`ParDo`)** → Aplica una transformación a cada elemento.  
✔ **Filter** → Filtra elementos según una condición.  
✔ **FlatMap** → Expande un elemento en múltiples elementos.  

```python
def convertir_a_mayusculas(elemento):
    return elemento.upper()

p | 'Convertir' >> beam.Map(convertir_a_mayusculas)
```

---

### **🔹 2. Agrupación de Datos**  
✔ **GroupByKey** → Agrupa elementos con la misma clave.  
✔ **CombinePerKey** → Aplica una función de agregación a cada grupo.  

```python
p | 'Agrupar por clave' >> beam.GroupByKey()
```

✔ **Ejemplo: Contar ocurrencias de palabras**  
```python
(p
 | 'Leer Texto' >> beam.io.ReadFromText('gs://mi-bucket/datos.txt')
 | 'Separar Palabras' >> beam.FlatMap(lambda x: x.split())
 | 'Mapear Palabras' >> beam.Map(lambda x: (x, 1))
 | 'Contar' >> beam.CombinePerKey(sum)
 | 'Escribir' >> beam.io.WriteToText('gs://mi-bucket/salida'))
```

---

### **🔹 3. Ventanas en Streaming**  
✔ **Fixed Window** → Intervalos fijos de tiempo (ej. cada 5 min).  
✔ **Sliding Window** → Se superponen en el tiempo (ej. cada 5 min con deslizamiento de 2 min).  
✔ **Session Window** → Basado en períodos de inactividad.  

**Ejemplo de Ventana Fija**  
```python
import apache_beam.transforms.window as window

(p 
 | 'Leer de Pub/Sub' >> beam.io.ReadFromPubSub(topic='projects/mi-proyecto/topics/mi-topico')
 | 'Aplicar Ventana' >> beam.WindowInto(window.FixedWindows(60))  # Ventana de 60 segundos
 | 'Escribir en BigQuery' >> beam.io.WriteToBigQuery('mi-proyecto:mi_dataset.mi_tabla'))
```

---

### **🔹 4. Patrones de Join en Dataflow**  
✔ **CoGroupByKey** → Une dos PCollections por clave común.  
✔ **Side Inputs** → Permite usar una PCollection secundaria como parámetro en una transformación.  

**Ejemplo de CoGroupByKey (Unión de Datos)**  
```python
p1 = p | 'Dataset 1' >> beam.Create([('A', 1), ('B', 2)])
p2 = p | 'Dataset 2' >> beam.Create([('A', 3), ('B', 4)])

(p1, p2) | 'Unir Datos' >> beam.CoGroupByKey()
```

---

### **🔹 5. Manejo de Agua y Retrasos en Streaming**  
✔ **Watermarks** → Controla el tiempo máximo de espera para eventos retrasados.  
✔ **Allowed Lateness** → Define cuánto tiempo aceptar eventos tardíos.  
✔ **Late Data Handling** → Envía eventos tardíos a un destino separado.  

```python
(p 
 | 'Aplicar Ventana' >> beam.WindowInto(window.FixedWindows(60), allowed_lateness=120))
```

---

# **✅ Resumen y Estrategia de Uso en Dataflow**
| **Técnica** | **Beneficio** | **Cuándo Usarla** |
|------------|--------------|------------------|
| **Batch Processing** | Procesa datos históricos | ETLs, Reportes |
| **Streaming Processing** | Responde a eventos en tiempo real | Logs, IoT, Análisis en Vivo |
| **Ventanas (Fixed, Sliding, Session)** | Procesa datos en períodos de tiempo | Casos en tiempo real |
| **GroupByKey, CoGroupByKey** | Agrega datos y combina fuentes | Enriquecimiento de datos |
| **Allowed Lateness** | Maneja eventos tardíos | Datos de sensores o logs |
