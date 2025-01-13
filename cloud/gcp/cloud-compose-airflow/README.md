# **📌 Guía de Cloud Composer (Apache Airflow en GCP)**  

## **1️⃣ Introducción a Cloud Composer y Apache Airflow**  

### **🔹 ¿Qué es Cloud Composer?**  
Cloud Composer es un servicio **gestionado** de Apache Airflow en Google Cloud. Permite la **orquestación de flujos de trabajo** para mover, transformar y procesar datos en GCP y otros entornos.  

✔ **Administración gestionada**: Google Cloud gestiona Airflow, reduciendo la sobrecarga operativa.  
✔ **Integración con GCP**: Compatible con BigQuery, Dataflow, GCS, Pub/Sub, Dataproc, etc.  
✔ **Escalabilidad**: Se ejecuta sobre Kubernetes en GKE.  
✔ **Programación y monitoreo**: Permite definir flujos de trabajo en Python y monitorearlos desde una UI web.  

---

## **2️⃣ Arquitectura de Apache Airflow en Cloud Composer**  
Cloud Composer usa **Apache Airflow**, que sigue la siguiente arquitectura:  

1. **DAGs (Directed Acyclic Graphs)** → Flujos de trabajo en Python.  
2. **Scheduler** → Programa la ejecución de tareas según la definición del DAG.  
3. **Executor** → Ejecuta las tareas (Celery, Kubernetes o Local).  
4. **Metastore Database** → Almacena metadatos sobre DAGs y ejecuciones.  
5. **Web Server (UI)** → Interfaz para monitorear DAGs y tareas.  

---

## **3️⃣ Creación de DAGs en Cloud Composer**  
### **🔹 ¿Qué es un DAG?**  
Un **DAG (Directed Acyclic Graph)** es un conjunto de tareas organizadas en una estructura sin ciclos, donde cada nodo es una tarea y las aristas representan dependencias.  

**Ejemplo básico de un DAG en Apache Airflow:**  
```python
from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
from airflow.utils.dates import days_ago

# Definir el DAG
dag = DAG(
    dag_id="mi_primer_dag",
    schedule_interval="@daily",
    start_date=days_ago(1),
    catchup=False
)

# Definir tareas
tarea_1 = DummyOperator(task_id="inicio", dag=dag)
tarea_2 = DummyOperator(task_id="fin", dag=dag)

# Definir flujo de ejecución
tarea_1 >> tarea_2
```

✔ **`dag_id`** → Identificador del DAG.  
✔ **`schedule_interval`** → Frecuencia de ejecución (`@daily`, `@hourly`, `*/5 * * * *`).  
✔ **`start_date`** → Fecha de inicio del DAG.  
✔ **`catchup=False`** → Evita ejecución retroactiva de DAGs pasados.  
✔ **`DummyOperator`** → Representa una tarea sin acción (útil para testing).  

---

## **4️⃣ Dependencias entre Tareas en Airflow**  
Las dependencias entre tareas en Airflow se definen con `>>` (dependencia directa) y `<<` (dependencia inversa).  

### **🔹 Dependencias Simples**  
```python
tarea_1 >> tarea_2  # tarea_2 depende de tarea_1
```

### **🔹 Dependencias Múltiples**  
```python
tarea_1 >> [tarea_2, tarea_3]  # tarea_1 ejecuta tarea_2 y tarea_3 en paralelo
```

### **🔹 Dependencias Encadenadas**  
```python
tarea_1 >> tarea_2 >> tarea_3  # Ejecución secuencial
```

---

## **5️⃣ Tipos de Operadores en Apache Airflow**  
Apache Airflow proporciona múltiples operadores para definir tareas en un DAG:  

| **Operador** | **Descripción** | **Ejemplo** |
|-------------|----------------|-------------|
| `DummyOperator` | Tarea vacía usada para estructurar DAGs | `DummyOperator(task_id='dummy')` |
| `PythonOperator` | Ejecuta funciones Python | `PythonOperator(task_id='funcion', python_callable=mi_funcion)` |
| `BashOperator` | Ejecuta comandos Bash | `BashOperator(task_id='bash', bash_command='echo "Hola"')` |
| `BigQueryOperator` | Ejecuta consultas en BigQuery | `BigQueryOperator(task_id='consulta', sql='SELECT * FROM tabla')` |
| `DataflowTemplateOperator` | Ejecuta un job de Dataflow | `DataflowTemplateOperator(task_id='dataflow_job', template='gs://ruta/template')` |

**Ejemplo de un DAG con PythonOperator:**  
```python
from airflow.operators.python_operator import PythonOperator

def mi_funcion():
    print("¡Ejecutando tarea en Python!")

tarea_python = PythonOperator(
    task_id="ejecutar_python",
    python_callable=mi_funcion,
    dag=dag
)

tarea_1 >> tarea_python >> tarea_2
```

---

## **6️⃣ Agendamiento y Control de Ejecución en Airflow**  
### **🔹 Intervalos de Ejecución (`schedule_interval`)**  
Airflow permite definir la frecuencia de ejecución de los DAGs con expresiones crontab o keywords:  

| **Expresión** | **Frecuencia** |
|--------------|--------------|
| `@once` | Una sola vez |
| `@hourly` | Cada hora |
| `@daily` | Diario |
| `*/5 * * * *` | Cada 5 minutos |

**Ejemplo de DAG con ejecución cada 5 minutos:**  
```python
dag = DAG(
    dag_id="dag_cada_5_min",
    schedule_interval="*/5 * * * *",
    start_date=days_ago(1),
    catchup=False
)
```

---

## **7️⃣ Ejecución Condicional y Retries en Airflow**  
### **🔹 Configuración de Retries**  
Se pueden definir intentos de reintento (`retries`) y tiempos de espera entre ellos (`retry_delay`).  

```python
from datetime import timedelta

tarea = BashOperator(
    task_id="reintento",
    bash_command="exit 1",  # Simula un fallo
    retries=3,
    retry_delay=timedelta(minutes=5),
    dag=dag
)
```

✔ **`retries=3`** → Reintenta la tarea hasta 3 veces si falla.  
✔ **`retry_delay=timedelta(minutes=5)`** → Espera 5 minutos entre intentos.  

---

## **8️⃣ XComs: Comunicación entre Tareas en Airflow**  
XComs permiten compartir datos entre tareas dentro de un DAG.  

### **🔹 Enviar un Valor con `xcom_push`**  
```python
def enviar_valor(**kwargs):
    kwargs['ti'].xcom_push(key='mensaje', value='Hola desde XCom')

tarea_envio = PythonOperator(
    task_id="enviar",
    python_callable=enviar_valor,
    provide_context=True,
    dag=dag
)
```

### **🔹 Recuperar un Valor con `xcom_pull`**  
```python
def recibir_valor(**kwargs):
    mensaje = kwargs['ti'].xcom_pull(task_ids='enviar', key='mensaje')
    print(f"Mensaje recibido: {mensaje}")

tarea_recibo = PythonOperator(
    task_id="recibir",
    python_callable=recibir_valor,
    provide_context=True,
    dag=dag
)
```

✔ `xcom_push` → Envía datos.  
✔ `xcom_pull` → Recupera datos.  

---

# **✅ Resumen y Estrategia para Usar Cloud Composer**
| **Funcionalidad** | **Uso** |
|------------------|--------|
| **DAGs** | Definir flujos de trabajo |
| **Operadores** | Ejecutar tareas en Python, Bash, SQL, GCP |
| **Dependencias** | Definir orden de ejecución |
| **Schedule Interval** | Programar ejecuciones con crontab |
| **XComs** | Compartir datos entre tareas |
| **Retries** | Manejar fallos y reintentos |
