# Álvaro Domingo Cordón — Portafolio

**CV y portafolio web de Álvaro Domingo Cordón, Data Analyst Junior.**

[![Web](https://img.shields.io/badge/Web-en%20vivo-2ea44f?style=flat-square)](https://alvarodc093-pixel.github.io/alvarodc093.github.io/) ![HTML](https://img.shields.io/badge/HTML-CSS%20%2B%20JS-E34F26?style=flat-square&logo=html5&logoColor=white) ![GitHub Pages](https://img.shields.io/badge/GitHub%20Pages-deploy-222222?style=flat-square&logo=github&logoColor=white)

![Portada del portafolio](docs/img/portada.png)

## En resumen

- **Qué es:** una sola página con perfil, experiencia, formación, habilidades y proyectos, cada uno con su demo y su repositorio.
- **Detalles:** español e inglés, modo oscuro y CV en PDF (español e inglés) generado desde código.

## Contenido

- Perfil, experiencia, formación, habilidades e idiomas.
- Proyectos destacados, cada uno con su demo y su repositorio, y una lista de los demás repositorios públicos que se carga desde la API de GitHub.
- CV en PDF de una página en español e inglés. El botón de descarga da el del idioma activo.

## Detalles técnicos

- Un único `index.html` con HTML, CSS y JavaScript sin dependencias ni build.
- Español e inglés, modo oscuro (respeta la preferencia del sistema) y ambas preferencias guardadas en el navegador.
- Navegación fija con la sección activa resaltada, enlace para saltar al contenido, soporte de teclado y de `prefers-reduced-motion`.
- Metadatos para buscadores y redes sociales (Open Graph y datos estructurados `Person`).
- Página 404 propia y una pequeña terminal oculta en el pie (`>_`).

## Estructura

```text
├── index.html               # Toda la web
├── 404.html                 # Página de error
├── profile.jpg              # Foto
├── CV_Alvaro_Domingo.pdf    # CV en español
├── CV_Alvaro_Domingo_EN.pdf # CV en inglés
└── cv/generar_cv.py         # genera los dos PDF (una columna, legible por los ATS)
```

Para actualizar el CV: editar los datos en `cv/generar_cv.py` y ejecutar `python cv/generar_cv.py` (usa Microsoft Edge para imprimir el PDF).

GitHub Pages publica la rama `main` tal cual.

## Contacto

[LinkedIn](https://www.linkedin.com/in/alvaro-domingo/) · [GitHub](https://github.com/alvarodc093-pixel) · alvarodc093@gmail.com
