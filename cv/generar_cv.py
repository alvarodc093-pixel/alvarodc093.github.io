"""Genera el CV en PDF (español e inglés) a partir de los datos de este archivo.

Diseño pensado para los ATS (los programas que filtran candidaturas):
una sola columna, texto real (no imágenes), secciones con nombres estándar
y orden lógico de lectura. Se imprime con Microsoft Edge sin ventana.

Uso:  python cv/generar_cv.py
"""

import html
import subprocess
import tempfile
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[1]
EDGE = Path(r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")
GH = "https://github.com/alvarodc093-pixel"

CONTACTO = {
    "telefono": "642 783 118",
    "email": "alvarodc093@gmail.com",
    "linkedin": "linkedin.com/in/alvaro-domingo",
    "github": "github.com/alvarodc093-pixel",
    "web": "alvarodc093-pixel.github.io/alvarodc093.github.io",
}

ES = {
    "archivo": "CV_Alvaro_Domingo.pdf",
    "lang": "es",
    "titulo": "Data Analyst Junior · SQL · Python · Power BI",
    "ubicacion": "Cádiz y Sevilla, España · Remoto o híbrido",
    "secciones": ["Perfil", "Habilidades", "Proyectos", "Experiencia", "Formación", "Idiomas"],
    "perfil": (
        "Data Analyst junior formado en Upgrade Hub. Convierto datos en decisiones de negocio con SQL, Python y "
        "Power BI: análisis con funciones de ventana, dashboards con DAX, A/B testing y segmentación de clientes. "
        "Todos mis proyectos usan datos reales, están probados con tests y se pueden reproducir. Vengo del sector "
        "dental digital (CAD/CAM), de donde traigo precisión, control de calidad y trato con el cliente."
    ),
    "habilidades": [
        ("SQL", "CTEs, funciones de ventana, cohortes, controles de calidad de datos · DuckDB, SQLite"),
        ("Python", "Pandas, NumPy, SciPy, statsmodels, scikit-learn, Matplotlib, Plotly, Streamlit"),
        ("Business Intelligence", "Power BI (modelo en estrella, DAX, Power Query), Excel, Microsoft Fabric"),
        ("Estadística", "A/B testing, intervalos de confianza, bootstrap, enfoque bayesiano, regresión logística, CLV"),
        ("Buenas prácticas", "Git y GitHub, GitHub Actions (CI), pytest, APIs REST, ETL, LLM y RAG"),
    ],
    "proyectos": [
        ("Olist en SQL — análisis de un e-commerce real", "SQL · DuckDB", f"{GH}/Olist-SQL-Analysis", [
            "11 consultas sobre 97.905 pedidos: cohortes, recompra, Pareto de categorías, logística y vendedores; 13 controles de calidad y 20 tests.",
            "Hallazgos: solo el 3 % de los clientes repite y un retraso de más de 7 días baja la nota media de 4,3 a 1,7.",
        ]),
        ("Contoso Retail — dashboard de ventas", "Power BI · DAX · Power Query", f"{GH}/Contoso-Retail-PowerBI", [
            "Informe de 5 páginas sobre 224.000 ventas: modelo en estrella y 28 medidas DAX (año anterior, acumulado, objetivo, clientes nuevos).",
            "Las medidas DAX se validaron contra SQL en los 10 años de datos. 2025: −7,5 % en ventas y 85,7 % del objetivo.",
        ]),
        ("A/B test de una campaña de anuncios", "Python · SciPy · statsmodels", f"{GH}/Marketing-AB-Test", [
            "588.101 usuarios: +43 % de conversión (IC 95 %: +30 % a +58 %) con test z, bootstrap y enfoque bayesiano, ajustado con regresión logística.",
            "Solo el 30 % de las compras se deben a los anuncios y el efecto aparece desde 25 impresiones; CPM máximo rentable.",
        ]),
        ("Segmentación RFM y valor de vida del cliente", "Python · Pandas · SciPy", f"{GH}/Customer-Segmentation-RFM", [
            "10 segmentos con acción para 5.852 clientes; modelos BG/NBD y Gamma-Gamma programados desde cero.",
            "Validado en 6 meses no vistos: compras predichas con un 2 % de error; el top 20 % predicho concentra el 73 % del gasto real.",
        ]),
        ("Steam Launch Radar — previsión de lanzamientos", "Python · scikit-learn · Next.js", f"{GH}/steam-launch-radar", [
            "Estima las reseñas de un juego a 30 días con sus primeros días: 3.019 lanzamientos, validación por fecha y app web.",
        ]),
        ("Solar España — previsión fotovoltaica", "Python · scikit-learn · GitHub Actions", f"{GH}/Energia-Solar", [
            "Previsión diaria con datos de REE y Open-Meteo: 84,5 % de acierto, mejora a 3 modelos de referencia y se reentrena cada semana.",
        ]),
    ],
    "experiencia": [
        ("Analista de datos (proyecto formativo)", "ESTADRIN SEGUR SL · Upgrade Hub · Rota", "2026 — actualidad", [
            "Consultas SQL (JOINs, agregaciones y subconsultas) y limpieza de datos con Python para preparar la información.",
            "Dashboards en Power BI para el seguimiento de KPIs, análisis exploratorio e informes para apoyar decisiones.",
        ]),
        ("Diseñador CAD/CAM", "Sector dental · Sevilla", "may. 2022 — nov. 2022", [
            "Flujo digital de trabajos de clínicas con Exocad: diseño, preparación para fresado e impresión 3D y control de calidad.",
        ]),
        ("Técnico de laboratorio dental", "Digital Dental Box · El Puerto de Santa María", "sep. 2020 — may. 2022", [
            "Fabricación de prótesis en todas sus fases con estándares estrictos de precisión y control de calidad.",
        ]),
        ("Higienista dental", "Clínica Dental Bahía · Cádiz", "dic. 2014 — jul. 2015", []),
    ],
    "formacion": [
        ("Bootcamp de Data Analyst e IA", "Upgrade Hub", "may. 2026 — oct. 2026",
         "Python, SQL, Power BI, Microsoft Fabric, Streamlit, EDA, data storytelling, LLM y RAG."),
        ("Técnico Superior en Prótesis Dentales", "Escuela Esprohident", "2018 — 2020", ""),
        ("Técnico Superior en Higiene Bucodental", "Cesur", "2013 — 2014", ""),
    ],
    "idiomas": "español (nativo), inglés (nativo)",
    "portafolio": "Portafolio con todos los proyectos y demos",
}

EN = {
    "archivo": "CV_Alvaro_Domingo_EN.pdf",
    "lang": "en",
    "titulo": "Junior Data Analyst · SQL · Python · Power BI",
    "ubicacion": "Cádiz & Seville, Spain · Remote or hybrid",
    "secciones": ["Summary", "Skills", "Projects", "Experience", "Education", "Languages"],
    "perfil": (
        "Junior Data Analyst trained at Upgrade Hub. I turn data into business decisions with SQL, Python and "
        "Power BI: window-function analysis, DAX dashboards, A/B testing and customer segmentation. All my projects "
        "use real data, are covered by tests and are reproducible. I come from the digital dental sector (CAD/CAM), "
        "which taught me precision, quality control and client focus."
    ),
    "habilidades": [
        ("SQL", "CTEs, window functions, cohorts, data quality checks · DuckDB, SQLite"),
        ("Python", "Pandas, NumPy, SciPy, statsmodels, scikit-learn, Matplotlib, Plotly, Streamlit"),
        ("Business Intelligence", "Power BI (star schema, DAX, Power Query), Excel, Microsoft Fabric"),
        ("Statistics", "A/B testing, confidence intervals, bootstrap, Bayesian analysis, logistic regression, CLV"),
        ("Engineering practices", "Git and GitHub, GitHub Actions (CI), pytest, REST APIs, ETL, LLMs and RAG"),
    ],
    "proyectos": [
        ("Olist in SQL — real e-commerce analysis", "SQL · DuckDB", f"{GH}/Olist-SQL-Analysis", [
            "11 queries on 97,905 orders: cohorts, repeat purchases, category Pareto, logistics and sellers; 13 data quality checks and 20 tests.",
            "Findings: only 3 % of customers buy again, and deliveries over 7 days late drop the average score from 4.3 to 1.7.",
        ]),
        ("Contoso Retail — sales dashboard", "Power BI · DAX · Power Query", f"{GH}/Contoso-Retail-PowerBI", [
            "5-page report on 224,000 sales: star schema and 28 DAX measures (prior year, YTD, budget, new customers).",
            "DAX measures validated against SQL for all 10 years. 2025: sales −7.5 % and 85.7 % of budget.",
        ]),
        ("A/B test of an ad campaign", "Python · SciPy · statsmodels", f"{GH}/Marketing-AB-Test", [
            "588,101 users: +43 % conversion (95 % CI +30 % to +58 %) with z-test, bootstrap and Bayesian analysis; adjusted for group imbalance with logistic regression.",
            "Only 30 % of purchases are incremental and the effect appears from 25 impressions; break-even CPM calculated.",
        ]),
        ("RFM segmentation and customer lifetime value", "Python · Pandas · SciPy", f"{GH}/Customer-Segmentation-RFM", [
            "10 actionable segments for 5,852 customers; BG/NBD and Gamma-Gamma models implemented from scratch.",
            "Validated on 6 unseen months: purchases within 2 %; the predicted top 20 % captures 73 % of real spend.",
        ]),
        ("Steam Launch Radar — launch forecasting", "Python · scikit-learn · Next.js", f"{GH}/steam-launch-radar", [
            "Predicts a game's 30-day reviews from its first days; 3,019 launches, time-based validation, web app and automated monthly refresh.",
        ]),
        ("Solar Spain — solar power forecasting", "Python · scikit-learn · GitHub Actions", f"{GH}/Energia-Solar", [
            "Daily forecast with REE and Open-Meteo data: 84.5 % accuracy, beats 3 baselines and retrains every week.",
        ]),
    ],
    "experiencia": [
        ("Data Analyst (training project)", "ESTADRIN SEGUR SL · Upgrade Hub · Rota", "2026 — present", [
            "SQL queries (JOINs, aggregations and subqueries) and data cleaning in Python to prepare information.",
            "Power BI dashboards to track KPIs, exploratory analysis and reports to support decisions.",
        ]),
        ("CAD/CAM Designer", "Dental sector · Seville", "May 2022 — Nov 2022", [
            "Digital workflow for clinic orders in Exocad: design, preparation for milling and 3D printing, and quality control.",
        ]),
        ("Dental Laboratory Technician", "Digital Dental Box · El Puerto de Santa María", "Sep 2020 — May 2022", [
            "Manufactured dental prostheses through every stage to strict precision and quality standards.",
        ]),
        ("Dental Hygienist", "Clínica Dental Bahía · Cádiz", "Dec 2014 — Jul 2015", []),
    ],
    "formacion": [
        ("Data Analyst & AI Bootcamp", "Upgrade Hub", "May 2026 — Oct 2026",
         "Python, SQL, Power BI, Microsoft Fabric, Streamlit, EDA, data storytelling, LLMs and RAG."),
        ("Higher Technician in Dental Prosthetics", "Escuela Esprohident", "2018 — 2020", ""),
        ("Higher Technician in Oral Hygiene", "Cesur", "2013 — 2014", ""),
    ],
    "idiomas": "Spanish (native), English (native)",
    "portafolio": "Portfolio with every project and live demos",
}

CSS = """
@page { size: A4; margin: 9mm 13mm 7mm 13mm; }
* { box-sizing: border-box; }
body { font-family: Calibri, 'Segoe UI', Arial, sans-serif; font-size: 9.4pt; line-height: 1.24; color: #111827; margin: 0; }
h1 { font-size: 20pt; margin: 0; letter-spacing: .2px; }
.titulo { font-size: 11pt; color: #1a56db; font-weight: 600; margin: 1px 0 3px; }
.contacto { font-size: 8.8pt; color: #374151; }
.contacto a { color: #374151; text-decoration: none; }
h2 { font-size: 10.5pt; text-transform: uppercase; letter-spacing: .6px; color: #1a56db;
     border-bottom: 1.2px solid #1a56db; padding-bottom: 1px; margin: 7px 0 3px; }
p { margin: 0 0 3px; }
.hab { margin: 0; padding: 0; list-style: none; }
.hab li { margin: 0 0 1px; }
.item { margin: 0 0 4px; page-break-inside: avoid; }
.cab { display: flex; justify-content: space-between; gap: 8px; }
.cab b { font-size: 9.9pt; }
.fecha { color: #4b5563; white-space: nowrap; font-size: 8.8pt; }
.sub { color: #4b5563; font-size: 8.8pt; }
.sub a { color: #1a56db; text-decoration: none; }
ul.b { margin: 1px 0 0; padding-left: 14px; }
ul.b li { margin: 0 0 1px; }
"""


def e(t: str) -> str:
    return html.escape(t)


def construir(d: dict) -> str:
    c = CONTACTO
    s = d["secciones"]
    partes = [f"<!doctype html><html lang='{d['lang']}'><head><meta charset='utf-8'>",
              f"<title>Álvaro Domingo Cordón — CV</title><style>{CSS}</style></head><body>",
              "<h1>Álvaro Domingo Cordón</h1>",
              f"<div class='titulo'>{e(d['titulo'])}</div>",
              f"<div class='contacto'>{e(d['ubicacion'])} · {c['telefono']} · "
              f"<a href='mailto:{c['email']}'>{c['email']}</a><br>"
              f"<a href='https://{c['linkedin']}'>{c['linkedin']}</a> · "
              f"<a href='https://{c['github']}'>{c['github']}</a> · "
              f"<a href='https://{c['web']}/'>{e(d['portafolio'])}: {c['web']}</a></div>",
              f"<h2>{s[0]}</h2><p>{e(d['perfil'])}</p>",
              f"<h2>{s[1]}</h2><ul class='hab'>"]
    partes += [f"<li><b>{e(k)}:</b> {e(v)}</li>" for k, v in d["habilidades"]]
    partes.append(f"<li><b>{s[5]}:</b> {e(d['idiomas'])}</li>")
    partes.append(f"</ul><h2>{s[2]}</h2>")
    for nombre, tec, url, vinetas in d["proyectos"]:
        partes.append(f"<div class='item'><div class='cab'><b>{e(nombre)}</b><span class='fecha'>{e(tec)}</span></div>"
                      f"<div class='sub'><a href='{url}'>{url.replace('https://', '')}</a></div>"
                      "<ul class='b'>" + "".join(f"<li>{e(v)}</li>" for v in vinetas) + "</ul></div>")
    partes.append(f"<h2>{s[3]}</h2>")
    for puesto, empresa, fechas, vinetas in d["experiencia"]:
        lista = ("<ul class='b'>" + "".join(f"<li>{e(v)}</li>" for v in vinetas) + "</ul>") if vinetas else ""
        partes.append(f"<div class='item'><div class='cab'><span><b>{e(puesto)}</b> <span class='sub'>· {e(empresa)}</span></span>"
                      f"<span class='fecha'>{e(fechas)}</span></div>{lista}</div>")
    partes.append(f"<h2>{s[4]}</h2>")
    for titulo, centro, fechas, detalle in d["formacion"]:
        extra = f"<div class='sub'>{e(detalle)}</div>" if detalle else ""
        partes.append(f"<div class='item'><div class='cab'><span><b>{e(titulo)}</b> <span class='sub'>· {e(centro)}</span></span>"
                      f"<span class='fecha'>{e(fechas)}</span></div>{extra}</div>")
    partes.append("</body></html>")
    return "".join(partes)


def imprimir(html_texto: str, destino: Path) -> None:
    with tempfile.TemporaryDirectory() as tmp:
        fuente = Path(tmp) / "cv.html"
        fuente.write_text(html_texto, encoding="utf-8")
        subprocess.run([str(EDGE), "--headless=new", "--disable-gpu", "--no-pdf-header-footer",
                        f"--print-to-pdf={destino}", fuente.as_uri()], check=True,
                       stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)


def main() -> None:
    for datos in (ES, EN):
        destino = RAIZ / datos["archivo"]
        texto = construir(datos)
        (RAIZ / "cv" / (Path(datos["archivo"]).stem + ".html")).write_text(texto, encoding="utf-8")
        imprimir(texto, destino)
        print(f"{destino.name}: {destino.stat().st_size / 1024:.0f} KB")


if __name__ == "__main__":
    main()
