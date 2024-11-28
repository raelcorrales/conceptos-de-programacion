Aquí tienes un tutorial sobre **GitHub Actions**, un potente conjunto de herramientas de integración y entrega continua (CI/CD) ofrecido por GitHub. Con GitHub Actions, los desarrolladores pueden automatizar tareas como la ejecución de pruebas, el despliegue de aplicaciones y el análisis de código, integrando estos flujos de trabajo en los repositorios.

---

### Introducción a GitHub Actions

**GitHub Actions** permite crear **Workflows** (flujos de trabajo) personalizados que se ejecutan en respuesta a eventos específicos en tu repositorio, como `push`, `pull_request`, o incluso eventos programados. Puedes configurarlo para que ejecute pruebas, compile y despliegue código, automatice revisiones, y mucho más.

Un flujo de trabajo es una serie de **Jobs** (tareas) que se ejecutan de forma secuencial o en paralelo en un ambiente virtual (Actions runner) configurado según el sistema operativo y el software que necesites.

---

### Conceptos Básicos de GitHub Actions

1. **Workflow**: Un archivo YAML en la carpeta `.github/workflows` que define una serie de tareas a ejecutar cuando ocurre un evento. Por ejemplo, `.github/workflows/ci.yml`.
2. **Event**: Un evento que desencadena la ejecución del Workflow, como `push`, `pull_request`, o `schedule`.
3. **Job**: Cada flujo de trabajo puede estar compuesto por uno o varios **Jobs**. Un Job es una serie de pasos (steps) que se ejecutan en un solo ambiente virtual.
4. **Steps**: Los pasos dentro de un Job, que pueden ser comandos o acciones preconfiguradas.
5. **Actions**: Las acciones son comandos específicos que realizan tareas en un Step. GitHub ofrece un mercado de Actions donde puedes encontrar cientos de acciones útiles.

---

### Crear un Workflow Básico

Para comenzar a trabajar con GitHub Actions, crea un archivo YAML en el directorio `.github/workflows`. Este ejemplo configura un Workflow básico que se ejecuta cuando se hace un `push` o `pull_request` a la rama principal (`main`).

#### Ejemplo: Configurar un Workflow de CI básico para pruebas

1. Crea un archivo `.yml` en el repositorio:
   ```plaintext
   .github/workflows/ci.yml
   ```

2. Agrega el siguiente contenido al archivo YAML para definir el Workflow:

   ```yaml
   name: CI Workflow

   # Especifica los eventos que desencadenarán el flujo de trabajo
   on:
     push:
       branches:
         - main
     pull_request:
       branches:
         - main

   jobs:
     build:
       # Configura el ambiente de ejecución para este Job
       runs-on: ubuntu-latest

       steps:
         # Acción para clonar el repositorio
         - name: Checkout code
           uses: actions/checkout@v2

         # Configura el entorno de Node.js (puedes ajustar la versión)
         - name: Set up Node.js
           uses: actions/setup-node@v2
           with:
             node-version: '16'

         # Instala las dependencias del proyecto
         - name: Install dependencies
           run: npm install

         # Ejecuta las pruebas
         - name: Run tests
           run: npm test
   ```

Este Workflow:
- Se ejecuta en cada `push` y `pull_request` en la rama `main`.
- Clona el repositorio, configura Node.js, instala dependencias y ejecuta las pruebas.

---

### Estructura de un Archivo YAML de GitHub Actions

Para entender mejor, aquí está la estructura típica de un archivo de Workflow:

```yaml
name: Nombre del flujo de trabajo

on: Evento(s) que disparan el Workflow

jobs:
  nombre-del-job:
    runs-on: Ambiente virtual (por ejemplo, `ubuntu-latest`)

    steps:
      - name: Nombre del paso
        uses: acción o comando específico
        with: Parámetros opcionales para la acción
        run: Comando que se ejecutará
```

---

### Personalizar un Workflow: Despliegue Automático

GitHub Actions también se puede configurar para realizar despliegues. En este ejemplo, se configura un flujo de trabajo que realiza un despliegue automático a un servidor mediante **SSH**.

1. **Generar una Clave SSH**: Genera una clave SSH para acceder al servidor remoto y añádela a los **Secrets** del repositorio.
   - Ve a `Settings > Secrets > Actions` y agrega la clave como un Secret, por ejemplo `SSH_KEY`.

2. **Configurar el Archivo de Workflow**:

   ```yaml
   name: Deploy Workflow

   on:
     push:
       branches:
         - main

   jobs:
     deploy:
       runs-on: ubuntu-latest

       steps:
         - name: Checkout code
           uses: actions/checkout@v2

         - name: Run deployment
           env:
             SSH_KEY: ${{ secrets.SSH_KEY }}
           run: |
             mkdir -p ~/.ssh
             echo "$SSH_KEY" > ~/.ssh/id_rsa
             chmod 600 ~/.ssh/id_rsa
             ssh -o StrictHostKeyChecking=no usuario@tu-servidor "cd /ruta/proyecto && git pull origin main && npm install && npm start"
   ```

Este Workflow:
- Se ejecuta en cada `push` a la rama `main`.
- Se conecta al servidor vía SSH y realiza un `git pull`, instala las dependencias y ejecuta la aplicación.

---

### Ejemplo de Uso de Secretos en GitHub Actions

Los Secrets son valores sensibles (como claves de API, contraseñas o claves SSH) que no deben exponerse en el código fuente. En GitHub Actions, puedes agregar secretos desde `Settings > Secrets` del repositorio y luego acceder a ellos en tus Workflows.

```yaml
env:
  API_KEY: ${{ secrets.API_KEY }}
```

---

### Workflows Programados con `cron`

GitHub Actions permite ejecutar flujos de trabajo en un horario programado usando `cron`. Esto es útil para tareas como limpiezas periódicas o generación de reportes.

```yaml
on:
  schedule:
    - cron: "0 0 * * *"  # Ejemplo: todos los días a medianoche
```

---

### GitHub Actions Marketplace

GitHub ofrece un **Marketplace** donde puedes encontrar miles de Actions creadas por la comunidad y por GitHub. Algunas Actions útiles incluyen:

1. **actions/checkout**: Para clonar el repositorio.
2. **actions/setup-node**: Configura Node.js en el ambiente virtual.
3. **codecov/codecov-action**: Sube reportes de cobertura de código a Codecov.
4. **docker/build-push-action**: Construye y publica imágenes Docker.

Explora el Marketplace en [https://github.com/marketplace](https://github.com/marketplace) para encontrar Actions que se adapten a tus necesidades.

---

### Buenas Prácticas para Trabajar con GitHub Actions

1. **Mantén los Workflows simples y específicos**: Separa Workflows en tareas específicas para mayor claridad y facilidad de depuración.
2. **Usa Secrets para valores sensibles**: No incluyas información sensible directamente en los archivos YAML.
3. **Revisa los Logs**: Si ocurre un error, revisa los Logs detallados de cada Step en la interfaz de GitHub.
4. **Reutiliza Actions del Marketplace**: Aprovecha las Actions del Marketplace para ahorrar tiempo en tareas comunes.
5. **Configura Rules para las ramas**: Define reglas de protección para asegurarte de que solo se fusionen cambios que hayan pasado los Workflows de CI.

---

GitHub Actions proporciona una solución robusta y flexible para la automatización de CI/CD, integrándose de forma nativa en GitHub y facilitando el desarrollo colaborativo y automatizado.