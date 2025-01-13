# **📌 Guía de BigQuery para Data Engineers**

## **1️⃣ Arquitectura de BigQuery**
### **🔹 Conceptos Clave**
- **Data Warehouse Serverless**: BigQuery no requiere administración de infraestructura.
- **Escalabilidad y Elasticidad**: Se adapta automáticamente a la carga de trabajo.
- **Columnares y Sin Índices**: Utiliza un formato columnar optimizado para análisis.
- **Procesamiento Distribuido**: Divide las consultas en tareas paralelas.
- **Costo Basado en Uso**: Se cobra por almacenamiento y procesamiento de consultas.

### **🔹 Componentes de BigQuery**  
- **Storage**: Maneja datos en formato **Capacitor** (columnar, optimizado para análisis).  
- **Compute (Dremel Engine)**: Motor de consulta que ejecuta SQL en paralelo.  
- **Metadata Store**: Administra esquemas, permisos y metadatos.  
- **Networking**: Comunicación entre BigQuery y otros servicios de GCP.  

### **🔹 Diferencias con Bases de Datos Relacionales**  
| **Característica** | **BigQuery** | **PostgreSQL/MySQL** |
|--------------------|-------------|---------------------|
| Modelo de Datos | Columnar | Filas y Columnas |
| Indexación | No hay índices | Índices tradicionales |
| Escalabilidad | Automática | Manual (sharding, particiones) |
| Tipos de Workloads | OLAP (Consultas Analíticas) | OLTP (Transaccional) |

---

## **2️⃣ Optimización de Costos en BigQuery**  
BigQuery cobra por **almacenamiento** y **procesamiento de consultas**. Aquí algunas estrategias para optimizar costos:  

### **🔹 Optimización de Costos de Almacenamiento**  
✔ **Elimina tablas no utilizadas** o archívalas en almacenamiento de baja frecuencia.  
✔ Usa **tablas particionadas** para mejorar la consulta y reducir el costo de escaneo.  
✔ Comprime datos antes de cargarlos (parquet, avro) en lugar de CSV o JSON.  

### **🔹 Optimización de Costos de Consultas**  
✔ **Usa SELECT con columnas específicas** en lugar de `SELECT *`.  
✔ **Filtra con WHERE y particionamiento** para evitar escanear toda la tabla.  
✔ **Limita el uso de JOINs complejos**, usa preprocesamiento en ETL si es posible.  
✔ **Aprovecha materialized views y tablas agregadas** para evitar recalcular datos.  

### **🔹 Control de Costos con Cuotas y Monitoreo**  
✔ **Configura presupuestos y alertas** en GCP Billing.  
✔ **Habilita cuotas en BigQuery** para evitar consultas costosas.  
✔ Usa **INFORMATION_SCHEMA.JOBS_BY_PROJECT** para analizar el consumo de consultas.  

---

## **3️⃣ Optimización de Rendimiento en BigQuery**  
BigQuery ejecuta consultas en paralelo, pero hay varias estrategias para mejorar la eficiencia:  

### **🔹 Optimización de Consultas**  
✔ **Usar tablas particionadas y clusterizadas** para reducir el escaneo de datos.  
✔ **Minimizar el uso de subconsultas y CTEs** (`WITH`), convertir en tablas materializadas.  
✔ **Optimizar filtros WHERE** para reducir la cantidad de datos procesados.  
✔ **Aprovechar funciones analíticas** (`PARTITION BY`, `LAG`, `LEAD`) en lugar de múltiples JOINs.  

### **🔹 Optimización de Tablas**  
✔ **Convertir datos en formatos eficientes (Parquet, Avro)** en lugar de CSV o JSON.  
✔ **Evitar tablas excesivamente grandes** y dividirlas en particiones.  
✔ **Usar tablas temporales** para reducir carga en consultas recurrentes.  

### **🔹 Indexación y Clustering en BigQuery**  
BigQuery no usa índices tradicionales, pero ofrece **clustering** como una alternativa eficiente para mejorar el rendimiento.  

---

## **4️⃣ Particionamiento en BigQuery**  
### **🔹 ¿Qué es el Particionamiento?**  
BigQuery **divide los datos en segmentos más pequeños**, lo que mejora la eficiencia de las consultas al evitar escanear datos innecesarios.  

### **🔹 Tipos de Particionamiento**  
| **Tipo** | **Ejemplo** | **Casos de Uso** |
|----------|------------|-----------------|
| **Por Fecha (DATE/TIMESTAMP)** | `ORDER_DATE` | Datos históricos, logs, eventos |
| **Por Ingestión (Partitioned by _PARTITIONTIME)** | `_PARTITIONTIME` | Datos de streaming o logs en tiempo real |
| **Por Rango de Números** | `USER_ID BETWEEN 1 y 1000` | Datos categóricos, IDs secuenciales |

### **🔹 Buenas Prácticas para Particionamiento**  
✔ **Usar columnas de tipo DATE/TIMESTAMP** en particionamiento basado en tiempo.  
✔ **Siempre filtrar por la columna de partición** (`WHERE fecha BETWEEN '2023-01-01' AND '2023-12-31'`).  
✔ **Evitar particiones con menos de 10MB de datos**, ya que aumenta la latencia.  

---

## **5️⃣ Clustering en BigQuery**  
### **🔹 ¿Qué es el Clustering?**  
BigQuery organiza los datos en **bloques ordenados** dentro de una partición, lo que reduce el escaneo de datos y mejora el rendimiento de las consultas.  

### **🔹 Ejemplo de Creación de Tabla Clusterizada**  
```sql
CREATE TABLE my_dataset.sales (
  order_id STRING,
  customer_id STRING,
  order_date DATE,
  total_amount FLOAT64
)
PARTITION BY order_date
CLUSTER BY customer_id;
```
**Explicación**:  
✅ **Particionamos por `order_date`** para segmentar los datos por fecha.  
✅ **Clusterizamos por `customer_id`** para mejorar las consultas por cliente.  

### **🔹 Cuándo Usar Clustering**  
✔ **Cuando las consultas suelen filtrar por ciertas columnas** (`customer_id`, `region`, `category`).  
✔ **Cuando hay muchas particiones y se quiere evitar escaneos innecesarios**.  
✔ **Cuando el tamaño de cada partición es grande y queremos mejorar la localización de datos**.  

### **🔹 Cuándo Evitar Clustering**  
❌ **Si la cardinalidad de la columna es baja** (ejemplo: `gender` con solo `M` y `F`).  
❌ **Si los datos no tienen una distribución uniforme** (por ejemplo, si un solo `customer_id` tiene millones de registros).  

---

# **✅ Resumen y Estrategia de Uso en BigQuery**
| **Técnica** | **Beneficio** | **Cuándo Usarla** |
|------------|--------------|------------------|
| **Particionamiento** | Reduce el escaneo de datos | Datos históricos, logs, eventos |
| **Clustering** | Mejora consultas en columnas específicas | Filtros frecuentes en columnas categóricas |
| **Formato de Datos Eficiente (Parquet, Avro)** | Reduce almacenamiento y costo de escaneo | Carga de datos masivos |
| **Materialized Views** | Acelera consultas recurrentes | Dashboards y reportes frecuentes |
| **Optimización de Consultas** | Mejora rendimiento y costos | Uso de `SELECT *`, `JOINs` innecesarios |
