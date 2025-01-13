# **📌 Guía de Pub/Sub en Google Cloud**  

## **1️⃣ Introducción a Pub/Sub**  

### **🔹 ¿Qué es Pub/Sub?**  
Pub/Sub (**Publish-Subscribe**) es un **servicio de mensajería asíncrono y escalable** de Google Cloud, diseñado para la comunicación entre sistemas distribuidos.  

✔ **Desacopla productores y consumidores** → Permite comunicación asíncrona sin dependencia directa.  
✔ **Alta disponibilidad y escalabilidad** → Gestionado por Google, sin necesidad de administrar infraestructura.  
✔ **Procesamiento en tiempo real** → Compatible con **Dataflow, BigQuery, Cloud Functions, Cloud Run, etc.**  
✔ **Entrega confiable** → Soporta reintentos automáticos y políticas de reintento.  

---

## **2️⃣ Arquitectura de Mensajería en Pub/Sub**  
Pub/Sub sigue un modelo **publish-subscribe**, donde los **productores** (publishers) envían mensajes a un **tópico**, y los **consumidores** (subscribers) reciben esos mensajes a través de **suscripciones**.  

📌 **Componentes principales:**  
1. **Tópico** → Punto central donde los publishers envían mensajes.  
2. **Suscripción** → Canal mediante el cual los suscriptores reciben mensajes.  
3. **Publisher** → Aplicación que publica mensajes en un tópico.  
4. **Subscriber** → Aplicación que recibe mensajes de una suscripción.  
5. **Mensaje** → Unidad de datos transmitida.  

### **🔹 Flujo de Datos en Pub/Sub**  
```plaintext
Publisher → (envía mensaje) → Tópico → (entrega a) → Suscripción → (procesa) → Subscriber
```

📌 **Ejemplo de arquitectura:**  
- Un servicio de pagos publica eventos en un tópico.  
- Dataflow procesa estos eventos en tiempo real.  
- BigQuery almacena los datos para análisis.  

---

## **3️⃣ Creación de un Pub/Sub en Google Cloud**  

### **🔹 Crear un Tópico Pub/Sub**  
```bash
gcloud pubsub topics create mi-topico
```

### **🔹 Crear una Suscripción**  
```bash
gcloud pubsub subscriptions create mi-suscripcion --topic=mi-topico
```

### **🔹 Publicar un Mensaje en un Tópico**  
```bash
gcloud pubsub topics publish mi-topico --message="Hola, Pub/Sub"
```

### **🔹 Leer Mensajes desde una Suscripción**  
```bash
gcloud pubsub subscriptions pull mi-suscripcion --auto-ack
```

---

## **4️⃣ Tipos de Suscripción en Pub/Sub**  

### **🔹 Suscripción PULL**  
✔ **El suscriptor recupera manualmente los mensajes.**  
✔ Útil cuando se necesita control sobre el procesamiento.  
✔ Implementación con la librería de Python:  

```python
from google.cloud import pubsub_v1

subscriber = pubsub_v1.SubscriberClient()
subscription_path = subscriber.subscription_path("mi-proyecto", "mi-suscripcion")

def callback(message):
    print(f"Mensaje recibido: {message.data}")
    message.ack()  # Confirmar recepción

subscriber.subscribe(subscription_path, callback=callback)
print("Escuchando mensajes...")
```

### **🔹 Suscripción PUSH**  
✔ **Pub/Sub envía los mensajes automáticamente a un endpoint HTTP.**  
✔ Útil para integración con microservicios o APIs.  

```bash
gcloud pubsub subscriptions create mi-suscripcion-push \
  --topic=mi-topico \
  --push-endpoint=https://mi-api.com/mensaje
```

---

## **5️⃣ Integración de Pub/Sub con Dataflow (Apache Beam)**  
Pub/Sub se integra con **Dataflow** para procesar eventos en **tiempo real**.  

### **🔹 Ejemplo de un Pipeline en Dataflow con Pub/Sub**  
📌 **Este pipeline lee datos de Pub/Sub y los escribe en BigQuery.**  

```python
import apache_beam as beam
from apache_beam.options.pipeline_options import PipelineOptions

PROJECT_ID = "mi-proyecto"
TOPIC = f"projects/{PROJECT_ID}/topics/mi-topico"
TABLE = f"{PROJECT_ID}:dataset.tabla"

pipeline_options = PipelineOptions(streaming=True, project=PROJECT_ID)

with beam.Pipeline(options=pipeline_options) as p:
    (
        p
        | "Leer desde Pub/Sub" >> beam.io.ReadFromPubSub(topic=TOPIC)
        | "Decodificar" >> beam.Map(lambda x: x.decode("utf-8"))
        | "Transformar en JSON" >> beam.Map(lambda x: {"mensaje": x})
        | "Escribir en BigQuery" >> beam.io.WriteToBigQuery(TABLE)
    )
```

✔ **`ReadFromPubSub(topic=TOPIC)`** → Lee datos en tiempo real desde Pub/Sub.  
✔ **`WriteToBigQuery(TABLE)`** → Inserta los datos en BigQuery.  

---

## **6️⃣ Integración de Pub/Sub con BigQuery (Streaming Directo)**  
📌 **Se puede escribir directamente en BigQuery sin usar Dataflow** con la integración nativa de Pub/Sub.  

### **🔹 Crear una Suscripción con BigQuery como Destino**  
```bash
gcloud pubsub subscriptions create mi-sub-bq \
  --topic=mi-topico \
  --bigquery-table=mi-proyecto:dataset.tabla \
  --use-topic-schema
```

✔ **Esto permite que Pub/Sub inserte datos directamente en BigQuery.**  
✔ **Ideal para casos donde no se necesita transformación en Dataflow.**  

---

## **7️⃣ Estrategias de Optimización y Mejores Prácticas**  

✅ **Minimizar la Latencia**  
- Usa **Dataflow con Pub/Sub** en **modo streaming** para procesamiento en tiempo real.  
- Evita el uso de suscripción **PULL** si se necesita baja latencia.  

✅ **Evitar Pérdida de Mensajes**  
- Usa **ACKs automáticos** en los consumidores para confirmar la recepción.  
- Configura **reintentos** en suscripciones PUSH.  

✅ **Optimizar Costos**  
- Usa **BigQuery Streaming** solo si necesitas datos en **tiempo real**.  
- Usa **Cloud Storage** como buffer antes de enviar datos a BigQuery.  

✅ **Escalabilidad**  
- Configura **Auto-scaling en Dataflow** para manejar picos de carga.  
- Usa múltiples suscripciones para distribuir la carga de procesamiento.  

---

# **✅ Resumen y Estrategia para Usar Pub/Sub**
| **Funcionalidad** | **Uso** |
|------------------|--------|
| **Tópicos y Suscripciones** | Desacoplar sistemas |
| **PULL vs PUSH** | Control manual vs entrega automática |
| **Pub/Sub + Dataflow** | Procesamiento en tiempo real |
| **Pub/Sub + BigQuery** | Análisis de datos en tiempo real |
| **Optimización de costos** | Reducir uso de streaming innecesario |
