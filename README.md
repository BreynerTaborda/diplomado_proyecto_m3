# 📊 Proyecto Final - Diplomado Módulo 3: Análisis de Mercado Inmobiliario en Medellín

## 👥 Autores
- **Breyner Andres Taborda Agudelo**
- **Jhon Sebastian Agudelo Sierra**

## 🎯 Objetivo del Proyecto

Este proyecto final demuestra la capacidad para transformar datos brutos en inteligencia empresarial para la toma de decisiones, utilizando principalmente Power BI como sistema de visualización. El proyecto analiza el mercado inmobiliario de arriendos en Medellín, Colombia, aplicando técnicas completas de ETL, análisis estadístico y visualización de datos.

## 📋 Enunciado del Proyecto

**Objetivos principales:**
- Aplicar técnicas de conexión y transformación (Power Query) en Power BI
- Crear cálculos avanzados (medidas y columnas calculadas)
- Desarrollar dashboards interactivos para visualización de datos
- Responder a preguntas de negocio específicas sobre el mercado inmobiliario

**Requisitos adicionales:**
- Implementar una bodega de datos (PostgreSQL) para almacenar los datos
- Desarrollar procedimientos personalizados de análisis y forecasting utilizando Python
- Generar un informe completo del proceso realizado

## 🏗️ Arquitectura del Proyecto

### 1. 📡 Extracción de Datos (Web Scraping)
**Archivo:** [`web-scraping.py`](web-scraping.py)

- **Fuente:** Sitio web Finca Raíz (fincaraiz.com.co)
- **Alcance:** 50 páginas de resultados de arriendos en Medellín
- **Datos extraídos:**
  - Precio de arriendo
  - Tipo de inmueble (apartamento/casa)
  - Número de habitaciones
  - Número de baños
  - Área en metros cuadrados
  - Ubicación/barrio

- **Tecnologías utilizadas:**
  - `requests` para peticiones HTTP
  - `BeautifulSoup` para parsing HTML
  - `csv` para exportación de datos
  - Manejo de rate limiting con delays aleatorios

### 2. 🗄️ Almacenamiento en Bodega de Datos
**Archivo:** [`migracion_bd.py`](migracion_bd.py)

- **Base de datos:** PostgreSQL
- **Tabla destino:** `inmuebles`
- **Proceso:**
  - Conexión a PostgreSQL usando SQLAlchemy
  - Limpieza automática de tabla existente
  - Migración completa de datos CSV a base de datos
  - Validación de integridad de datos

### 3. 🔍 Análisis y Forecasting con Python
**Archivo:** [`analisis_inmuebles.py`](analisis_inmuebles.py)

- **Librerías utilizadas:**
  - `pandas` y `numpy` para manipulación de datos
  - `matplotlib` y `seaborn` para visualizaciones
  - `warnings` para manejo de advertencias

- **Funcionalidades implementadas:**
  - **Limpieza de datos:** Conversión de formatos, manejo de valores faltantes
  - **Análisis descriptivo:** Estadísticas resumen, distribuciones, correlaciones
  - **Visualizaciones:** Histogramas, box plots, scatter plots, mapas de calor
  - **Análisis por barrio:** Segmentación geográfica de precios
  - **Insights ejecutivos:** Conclusiones y recomendaciones

### 4. 📊 Visualización en Power BI
**Archivo:** [`diplomado_proyecto_m3.pbix`](diplomado_proyecto_m3.pbix)

- **Conexión:** Directa a PostgreSQL
- **Power Query:** Transformaciones avanzadas de datos
- **Medidas DAX:** Cálculos complejos para KPIs
- **Dashboards:** Visualizaciones interactivas del mercado inmobiliario

## 📈 Resultados del Análisis

### Estadísticas Generales
- **Total de inmuebles analizados:** 1,027
- **Rango de precios:** $150,000 - $22,000,000 COP
- **Precio promedio:** $4,026,464 COP
- **Precio mediano:** $3,200,000 COP

### Distribución por Tipo
- **Apartamentos:** 87.0% (894 inmuebles)
- **Casas:** 13.0% (133 inmuebles)

### Barrios Destacados
1. **El Poblado:** 139 inmuebles (precio promedio: $5,673,597)
2. **Laureles:** 72 inmuebles
3. **Centro de Medellín:** 68 inmuebles

## 🛠️ Tecnologías Utilizadas

### Lenguajes de Programación
- **Python 3.x** - Análisis de datos y web scraping
- **SQL** - Consultas a base de datos
- **DAX** - Medidas en Power BI

### Librerías Python
- `requests`, `beautifulsoup4` - Web scraping
- `pandas`, `numpy` - Manipulación de datos
- `matplotlib`, `seaborn` - Visualizaciones
- `sqlalchemy`, `psycopg2` - Conexión a PostgreSQL

### Herramientas
- **PostgreSQL** - Base de datos
- **Power BI Desktop** - Business Intelligence
- **VS Code** - Entorno de desarrollo
- **Git** - Control de versiones

## 🚀 Instalación y Ejecución

### Prerrequisitos
```bash
# Instalar dependencias Python
pip install requests beautifulsoup4 pandas numpy matplotlib seaborn sqlalchemy psycopg2-binary

# PostgreSQL debe estar ejecutándose localmente
# Power BI Desktop instalado
```

### Ejecución del Proyecto
```bash
# 1. Ejecutar web scraping
python web-scraping.py

# 2. Migrar datos a PostgreSQL
python migracion_bd.py

# 3. Ejecutar análisis descriptivo
python analisis_inmuebles.py

# 4. Abrir dashboard en Power BI
# diplomado_proyecto_m3.pbix
```

## 📊 Preguntas de Negocio Respondidas

1. **¿Cuál es la distribución de precios en el mercado de arriendos de Medellín?**
   - Análisis de histogramas y estadísticas descriptivas

2. **¿Cómo varían los precios según el tipo de inmueble y ubicación?**
   - Comparación entre apartamentos y casas por barrio

3. **¿Qué factores influyen más en el precio de arriendo?**
   - Análisis de correlaciones entre variables

4. **¿Cuáles son los barrios más activos y con mejores precios?**
   - Ranking de barrios por volumen y precio promedio

5. **¿Cómo se distribuyen las características de los inmuebles?**
   - Análisis de habitaciones, baños y áreas disponibles

## 🎯 Insights y Conclusiones

### Patrones Observados
- **Dominio de apartamentos:** 87% del mercado son apartamentos
- **Correlación precio-habitaciones:** Relación positiva moderada
- **Variabilidad geográfica:** Precios varían significativamente por barrio
- **Distribución típica:** Mayoría de inmuebles con 2-3 habitaciones y 1-2 baños

### Recomendaciones Estratégicas
1. **Para Inversores:** Enfocarse en El Poblado y Laureles como mercados premium
2. **Para Desarrolladores:** Priorizar apartamentos de 2-3 habitaciones
3. **Para Inquilinos:** Considerar correlación precio-calidad para decisiones informadas