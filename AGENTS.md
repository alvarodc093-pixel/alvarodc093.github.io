# Reglas de este proyecto

## Qué es
Mi CV/portfolio personal como Data Analyst, publicado con GitHub Pages. Público objetivo: recruiters y empresas. Profesional y sobrio.

## Restricciones técnicas (no negociables)
- Todo vive en un único fichero `index.html`: HTML + CSS + JS inline
- Sin frameworks, sin builds, sin npm, sin ficheros externos (salvo imágenes del repo)
- Debe funcionar abriéndolo con doble clic y desplegado desde GitHub Pages tal cual
- Responsive (mobile, tablet, escritorio) y accesible (contraste suficiente, aria, `lang="es"`)
- GitHub Pages despliega automáticamente desde la rama `main` (repo `alvarodc093.github.io`) — no hay gh-pages branch ni Actions workflow

## Estilo
- Texto visible en español; nombres de clases y código en inglés
- Paleta definida en CSS variables (`:root`): `--primary: #1a56db`, `--primary-dark: #1141a0`, `--primary-light: #e8eefb`, `--bg: #f8f9fc`, `--surface: #fff`, `--text: #1a1a2e`, `--text-light: #5a5a7a`, `--border: #e0e5f0`
- Mantén la paleta y tipografía existentes a menos que se pida cambiarlas explícitamente
- Nada de librerías de animación ni efectos aparatosos
- Tipografía: system stack (`-apple-system, BlinkMacSystemFont, "Segoe UI"...`)

## Datos personales
- No inventes datos: usa los que hay en la página (`index.html`)
- NUNCA añadas teléfono, dirección postal ni DNI

## Estructura actual del HTML
Secciones en orden: header (nombre + titular + enlaces rápidos) → perfil profesional → experiencia (timeline con 3 items) → educación (grid de 3 cards) → habilidades (barras animadas con IntersectionObserver, `data-level` en %) → proyectos (grid de 3 cards) → contacto (email, LinkedIn, GitHub) → footer

## Comandos
- No hay sistema de build, test, lint ni typecheck. No hay `package.json`, `requirements.txt` ni ningún gestor de dependencias.
- Para validar: abre `index.html` en navegador. No hay CI/CD más allá del deploy automático de GitHub Pages.

## Al terminar cada cambio
- Resumen en 2-3 líneas de qué se ha tocado y dónde.
