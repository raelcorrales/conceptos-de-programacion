Aquí tienes un tutorial sobre **GitHub Pages**, una herramienta de GitHub que permite crear sitios web estáticos directamente desde repositorios. GitHub Pages es útil para alojar proyectos, portafolios, documentación y sitios personales, todo de forma gratuita y con integración continua desde el repositorio de GitHub.

---

### ¿Qué es GitHub Pages?

**GitHub Pages** convierte los archivos de un repositorio (HTML, CSS, JavaScript, Markdown, etc.) en un sitio web estático. Cada vez que haces un cambio en el repositorio, GitHub Pages actualiza el sitio automáticamente. Los sitios se alojan en GitHub y suelen estar disponibles en una URL de la forma `https://username.github.io/repository-name/`.

GitHub Pages es ideal para:
1. Crear documentación de proyectos.
2. Publicar portafolios y blogs.
3. Crear sitios personales o para organizaciones.

---

### Tipos de Sitios en GitHub Pages

Existen tres tipos de sitios que puedes crear con GitHub Pages:
1. **Sitio de Usuario**: Un sitio web personal para un usuario de GitHub (ejemplo: `https://username.github.io`).
2. **Sitio de Organización**: Similar al sitio de usuario, pero para organizaciones (ejemplo: `https://organization.github.io`).
3. **Sitio de Proyecto**: Asociado a un repositorio específico dentro de una cuenta de usuario o de organización (ejemplo: `https://username.github.io/repository-name/`).

---

### Configuración de GitHub Pages para un Sitio de Proyecto

1. **Crear el Repositorio**:
   - Inicia un nuevo repositorio o elige uno existente en GitHub. Puede ser público o privado.
   - Da un nombre al repositorio, por ejemplo `mi-sitio`.

2. **Crear el Archivo de Inicio (index.html)**:
   - Crea un archivo `index.html` en la raíz del repositorio o en la carpeta designada para el sitio web.
   - Este archivo será la página principal del sitio.

   Ejemplo de `index.html`:
   ```html
   <!DOCTYPE html>
   <html lang="es">
   <head>
       <meta charset="UTF-8">
       <meta name="viewport" content="width=device-width, initial-scale=1.0">
       <title>Mi Proyecto</title>
   </head>
   <body>
       <h1>Bienvenido a Mi Proyecto</h1>
       <p>Este es mi sitio web usando GitHub Pages.</p>
   </body>
   </html>
   ```

3. **Habilitar GitHub Pages**:
   - Ve a `Settings > Pages` en tu repositorio.
   - En la sección "Source", selecciona la rama desde donde deseas publicar el sitio (usualmente `main` o `gh-pages`).
   - Puedes elegir la raíz o una carpeta específica (`/docs`) si tienes organizada la documentación en esa carpeta.
   - Guarda los cambios y GitHub generará la URL del sitio.

4. **Visitar el Sitio**:
   - Una vez habilitado, tu sitio estará disponible en una URL similar a `https://username.github.io/mi-sitio`.

---

### Configuración de GitHub Pages para un Sitio de Usuario u Organización

1. **Crear el Repositorio con un Nombre Específico**:
   - Crea un repositorio llamado `username.github.io`, donde `username` es tu nombre de usuario en GitHub. Este será el sitio raíz para tu cuenta.

2. **Agregar el Archivo `index.html`**:
   - Sube o crea un archivo `index.html` en la raíz del repositorio.
   
3. **Publicar y Visitar el Sitio**:
   - GitHub Pages estará habilitado automáticamente. Visita `https://username.github.io` para ver tu sitio.

---

### Usar Jekyll en GitHub Pages

GitHub Pages es compatible con **Jekyll**, un generador de sitios estáticos que facilita la creación de blogs o sitios de documentación usando Markdown.

1. **Habilitar Jekyll**:
   - Agrega un archivo `_config.yml` en la raíz del repositorio para personalizar el sitio.
   
   Ejemplo de `_config.yml`:
   ```yaml
   title: "Mi sitio en GitHub Pages"
   description: "Este es un sitio de ejemplo usando Jekyll"
   theme: jekyll-theme-cayman
   ```

2. **Crear Páginas en Markdown**:
   - Puedes agregar páginas adicionales en formato Markdown (`.md`), como `about.md`, y Jekyll las convertirá automáticamente en HTML.

3. **Usar Temas de Jekyll**:
   - GitHub Pages ofrece temas prediseñados que puedes aplicar mediante `_config.yml`.

   Ejemplo de cómo seleccionar un tema:
   ```yaml
   theme: jekyll-theme-minimal
   ```

4. **Compilar el Sitio Localmente (Opcional)**:
   - Si quieres ver el sitio en tu máquina antes de publicarlo, puedes instalar Jekyll y ejecutar `jekyll serve` para ver una vista previa local en `http://localhost:4000`.

---

### Personalizar y Configurar el Dominio

1. **Usar un Dominio Personalizado**:
   - En `Settings > Pages`, ve a la sección "Custom domain" y escribe tu dominio personalizado (por ejemplo, `www.mi-sitio.com`).
   - Configura los registros `A` o `CNAME` en tu proveedor de dominio para apuntar a GitHub Pages.

2. **HTTPS en GitHub Pages**:
   - GitHub permite habilitar HTTPS para sitios con dominios personalizados. En `Settings > Pages`, marca la opción **Enforce HTTPS**.

---

### Buenas Prácticas al Usar GitHub Pages

1. **Organizar el Contenido**:
   - Organiza los archivos en carpetas (`assets`, `images`, `css`) para un mejor mantenimiento.
2. **Actualización y Revisión**:
   - Cada vez que subas un cambio al repositorio, GitHub Pages actualizará automáticamente el sitio.
3. **Utiliza un Workflow de CI/CD (Opcional)**:
   - Si necesitas una generación más compleja o agregar pruebas antes de publicar, puedes integrar **GitHub Actions** con GitHub Pages para automatizar el despliegue.

---

### Ejemplo Completo de un Sitio Web en GitHub Pages

1. **Estructura de Archivos**:
   ```
   mi-sitio/
   ├── index.html
   ├── about.md
   ├── assets/
   │   ├── css/
   │   │   └── style.css
   │   └── images/
   │       └── logo.png
   ├── _config.yml
   ```

2. **Archivo `index.html`**:
   ```html
   <!DOCTYPE html>
   <html lang="es">
   <head>
       <meta charset="UTF-8">
       <title>Mi Sitio en GitHub Pages</title>
       <link rel="stylesheet" href="assets/css/style.css">
   </head>
   <body>
       <h1>Bienvenido a Mi Sitio Web</h1>
       <p>Este sitio fue creado usando GitHub Pages.</p>
       <a href="about.html">Sobre mí</a>
   </body>
   </html>
   ```

3. **Página en Markdown (`about.md`)**:
   ```markdown
   ---
   layout: default
   title: Sobre mí
   ---
   # Sobre mí
   ¡Bienvenido a la página "Sobre mí"! Aquí puedes encontrar más información sobre este proyecto.
   ```

4. **Archivo `_config.yml`**:
   ```yaml
   title: "Mi Sitio en GitHub Pages"
   description: "Este es un ejemplo de sitio usando Jekyll en GitHub Pages"
   theme: jekyll-theme-cayman
   ```

---

### Publicar el Sitio

- Una vez que los archivos están en el repositorio y GitHub Pages está habilitado, el sitio será accesible en `https://username.github.io/mi-sitio`.
- Puedes hacer cambios en cualquier momento, y GitHub Pages se encargará de regenerar y actualizar el sitio automáticamente.

### Resumen

Con GitHub Pages, puedes crear y publicar sitios estáticos de manera fácil y gratuita. Es ideal para proyectos de documentación, blogs personales, o portafolios profesionales. Con la integración de Jekyll, es sencillo estructurar el contenido, usar Markdown y aplicar temas preconfigurados.