# **📌 Guía de Cloud Storage en Google Cloud**  

## **1️⃣ Introducción a Cloud Storage**  

### **🔹 ¿Qué es Cloud Storage?**  
Cloud Storage es el servicio de almacenamiento de objetos de Google Cloud, diseñado para **almacenamiento escalable, seguro y altamente disponible**.  

✔ **Almacenamiento de objetos** → Similar a Amazon S3, usa "buckets" en lugar de sistemas de archivos tradicionales.  
✔ **Alta disponibilidad** → Replica datos globalmente para garantizar durabilidad.  
✔ **Escalabilidad automática** → Maneja grandes volúmenes de datos sin administración manual.  
✔ **Integración con otros servicios de GCP** → BigQuery, Dataflow, AI/ML, Pub/Sub.  

---

## **2️⃣ Tipos de Clases de Almacenamiento**  

| **Clase** | **Costo ($/GB/mes)** | **Latencia** | **Uso recomendado** |
|-----------|----------------|-----------|----------------|
| **Standard** | Alto | Baja | Datos de acceso frecuente, sitios web, apps |
| **Nearline** | Medio | Media | Backups, datos con acceso 1 vez al mes |
| **Coldline** | Bajo | Alta | Archivos accedidos menos de 1 vez al año |
| **Archive** | Muy bajo | Muy alta | Archivos a largo plazo (5+ años) |

📌 **Estrategia recomendada:**  
- **Standard** → Datos en producción.  
- **Nearline** → Respaldos y logs históricos.  
- **Coldline** → Datos raramente usados.  
- **Archive** → Retención a largo plazo.  

---

## **3️⃣ Creación y Administración de Buckets**  

### **🔹 Crear un Bucket en Cloud Storage**  
```bash
gcloud storage buckets create mi-bucket --location=us-central1 --storage-class=STANDARD
```

### **🔹 Subir un Archivo**  
```bash
gcloud storage cp archivo.txt gs://mi-bucket/
```

### **🔹 Listar Archivos**  
```bash
gcloud storage ls gs://mi-bucket/
```

### **🔹 Descargar un Archivo**  
```bash
gcloud storage cp gs://mi-bucket/archivo.txt .
```

### **🔹 Eliminar un Archivo**  
```bash
gcloud storage rm gs://mi-bucket/archivo.txt
```

---

## **4️⃣ Mejores Prácticas en Cloud Storage**  

✅ **Usar el Storage Class adecuado**  
- No uses **Standard** si los datos se acceden rara vez.  
- Usa **Nearline/Coldline** para reducir costos en backups.  

✅ **Activar Versioning para evitar pérdida de datos**  
```bash
gcloud storage buckets versioning enable gs://mi-bucket/
```

✅ **Usar IAM para controlar acceso**  
```bash
gcloud storage buckets add-iam-policy-binding gs://mi-bucket/ \
  --member=user:juan@example.com --role=roles/storage.objectViewer
```

✅ **Habilitar encriptación de datos**  
- Por defecto, Google Cloud cifra todos los datos.  
- Se pueden usar claves de **Cloud KMS** para mayor control.  

✅ **Optimizar el uso de Cloud CDN**  
- Para mejorar rendimiento, usar **Cloud Storage + Cloud CDN**.  
- Útil para **sitios web estáticos y distribución global de archivos**.  

---

## **5️⃣ Lifecycle Policies (Ciclo de Vida de los Datos)**  
Las **Lifecycle Policies** permiten **mover o eliminar archivos automáticamente** según su antigüedad.  

### **🔹 Ejemplo: Mover archivos a Coldline después de 30 días y eliminarlos tras 1 año**  
```json
{
  "rule": [
    {
      "action": {"type": "SetStorageClass", "storageClass": "COLDLINE"},
      "condition": {"age": 30}
    },
    {
      "action": {"type": "Delete"},
      "condition": {"age": 365}
    }
  ]
}
```

📌 **Aplicar la política a un bucket:**  
```bash
gcloud storage buckets update gs://mi-bucket --lifecycle-file=lifecycle.json
```

✔ **Reduce costos** al mover datos automáticamente.  
✔ **Evita almacenamiento innecesario** de archivos antiguos.  

---

## **6️⃣ Estrategias de Almacenamiento Eficiente**  

✅ **Fragmentar archivos grandes (Sharding)**  
✔ Divide archivos en partes más pequeñas (ej. 100MB).  
✔ Evita cuellos de botella en lectura/escritura.  

✅ **Compresión de archivos**  
✔ Usa **gzip** o **Parquet/Avro** en grandes volúmenes de datos.  
✔ Reduce costos de almacenamiento y mejora rendimiento en BigQuery.  

✅ **Evitar listas innecesarias de objetos**  
✔ No hagas `gsutil ls -r` en buckets con millones de archivos.  
✔ Usa **Cloud Storage Insights** para análisis de uso.  

✅ **Optimizar el uso de Signed URLs para acceso temporal**  
✔ Permite compartir archivos con acceso restringido.  
✔ Ejemplo en Python:  
```python
from google.cloud import storage
import datetime

client = storage.Client()
bucket = client.bucket("mi-bucket")
blob = bucket.blob("archivo.txt")

url = blob.generate_signed_url(
    expiration=datetime.timedelta(hours=1),
    method="GET"
)
print(f"URL de acceso temporal: {url}")
```

---

## **7️⃣ Seguridad en Cloud Storage**  

✅ **Habilitar registros de auditoría con Cloud Logging**  
```bash
gcloud logging sinks create storage-logs \
  --log-filter='resource.type="gcs_bucket"' \
  --destination=bigquery.googleapis.com/projects/mi-proyecto/datasets/logs
```

✅ **Proteger datos sensibles con etiquetas de acceso**  
✔ Usa etiquetas de IAM para restringir acceso a buckets.  
✔ Ejemplo: Prohibir acceso a datos personales fuera de un equipo.  

✅ **Habilitar Retención de Datos**  
✔ Evita eliminación accidental configurando una política de retención:  
```bash
gcloud storage buckets update gs://mi-bucket --retention-period=31536000
```
✔ Esto impide eliminar archivos antes de 1 año.  

---

## **✅ Resumen y Estrategia para Usar Cloud Storage**
| **Funcionalidad** | **Uso** |
|------------------|--------|
| **Storage Classes** | Reducir costos según frecuencia de acceso |
| **Lifecycle Policies** | Automatizar limpieza de archivos |
| **Versioning** | Evitar pérdidas de datos |
| **Compresión (gzip, Parquet)** | Reducir tamaño y mejorar rendimiento |
| **Signed URLs** | Acceso temporal seguro |
| **IAM + Retention Policies** | Protección de datos |
