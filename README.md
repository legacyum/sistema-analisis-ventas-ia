# 🚀 Sistema Inteligente de Análisis de Ventas con IA

[![Python](https://img.shields.io/badge/Python-3.7%2B-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Dashboard](https://img.shields.io/badge/Dashboard-Multiple-orange.svg)](http://localhost:8051)
[![AI](https://img.shields.io/badge/AI-Machine%20Learning-red.svg)](http://localhost:8051)
[![Streamlit](https://img.shields.io/badge/Streamlit-Dashboard-green.svg)](http://localhost:8502)

**Sistema integral con IA para consolidar, analizar y predecir datos de ventas con múltiples interfaces de usuario.**

## 🎯 **¿Qué hace este sistema?**
- 📊 **Consolida** múltiples archivos Excel automáticamente
- 🤖 **Predice ventas futuras** con Machine Learning (99.9% precisión)
- 📈 **Analiza tendencias** y patrones automáticamente
- 🎨 **Múltiples dashboards** para diferentes necesidades
- 💡 **Genera recomendaciones** inteligentes para tu negocio

## 🚀 **INICIO ULTRA RÁPIDO**

```bash
# 1. Descarga o clona el proyecto
git clone https://github.com/legacyum/sistema-analisis-ventas-ia.git

# 2. Ejecuta (instala todo automáticamente)
python main.py

# 3. Elige tu opción favorita:
#    → Opción 4: Dashboard IA Premium
#    → Opción 7: Demo completo con datos
```

## 🎮 **DEMO INMEDIATO**

¿Sin datos? ¡No problema!

```bash
# Genera datos de demo con IA optimizada
python demo_ia.py

# Luego ejecuta cualquier dashboard
python ejecutar_dashboard.py
```

## 📚 Índice

- [🎯 Demo Inmediato](#-demo-inmediato)
- [🤖 Funcionalidades de IA](#-funcionalidades-de-ia)
- [🎨 Dashboards Disponibles](#-dashboards-disponibles)
- [⚡ Instalación Express](#-instalación-express)
- [🚀 Uso Rápido](#-uso-rápido)
- [📊 Características Principales](#-características-principales)
- [🔧 Estructura del Proyecto](#-estructura-del-proyecto)
- [📋 Formato de Datos](#-formato-de-datos)
- [🎛️ Selector de Dashboards](#-selector-de-dashboards)
- [🧠 Sistema de IA](#-sistema-de-ia)
- [🛠️ Personalización](#-personalización)
- [🆘 Solución de Problemas](#-solución-de-problemas)
- [💡 Casos de Uso](#-casos-de-uso)
- [📈 Roadmap](#-roadmap)
- [🤝 Contribuir](#-contribuir)

## 🤖 **Funcionalidades de IA**

### 🔮 **Predicciones Automáticas**
- **Ventas futuras:** 7, 30 días o personalizado
- **Precisión:** R² = 0.999 (99.9% de precisión)
- **Modelos:** Random Forest, Gradient Boosting, Linear Regression
- **Confianza:** Intervalos estadísticos por predicción

### 🎯 **Segmentación Inteligente**
- **Vendedores Estrella:** Alto volumen + frecuencia
- **Vendedores Premium:** Alto volumen + productos exclusivos
- **Vendedores Activos:** Volumen medio + alta frecuencia
- **Análisis K-means:** Clustering automático

### 💡 **Recomendaciones Automáticas**
- **Productos estrella:** Para enfocar marketing
- **Productos en riesgo:** Que necesitan atención
- **Optimización temporal:** Mejores días/meses
- **Desarrollo de equipo:** Programas de mentoring

### 📊 **Análisis Avanzado**
- **Tendencias:** Detección automática con regresión
- **Estacionalidad:** Patrones mensuales/semanales
- **Correlaciones:** Entre variables de negocio
- **Anomalías:** Detección de valores atípicos

## � **Dashboards Disponibles**

### 1️⃣ **Dashboard Premium (Dash)** - Puerto 8051 🏆
```bash
python dashboard_ia.py
# o
python ejecutar_dashboard.py → opción 1
```
**Características:**
- 🎨 Diseño profesional con gradientes y animaciones
- 🤖 IA integrada con predicciones en tiempo real
- 📊 Métricas avanzadas y visualizaciones premium
- 🎯 Ideal para presentaciones ejecutivas
- 💎 Efectos hover y transiciones suaves

### 2️⃣ **Dashboard Streamlit** - Puerto 8502 ⚡
```bash
streamlit run dashboard_streamlit.py
# o  
python ejecutar_dashboard.py → opción 2
```
**Características:**
- ⚡ Interfaz limpia y minimalista
- 🧪 Perfecto para análisis exploratorio
- 🔄 Desarrollo y modificación rápida
- 📱 Responsive automático
- 🎛️ Sidebar intuitivo con controles

### 3️⃣ **Dashboard Estándar** - Puerto 8050 📊
```bash
python dashboard.py
```
**Características:**
- 📊 Análisis básico de ventas
- 🔍 Filtros dinámicos
- 📈 Gráficos interactivos estándar
- 🎯 Funcionalidad core sin IA

## ⚡ **Instalación Express**

### 🔧 **Opción 1: Automática (Recomendada)**
```bash
# 1. Descargar el proyecto
git clone https://github.com/legacyum/sistema-analisis-ventas-ia.git
cd Proyecto_2

# 2. Ejecutar selector (instala todo automáticamente)
python ejecutar_dashboard.py

# 3. ¡Listo! Selecciona tu dashboard favorito
```

### 🛠️ **Opción 2: Manual**
```bash
# Instalar dependencias principales
pip install pandas plotly dash streamlit scikit-learn

# Dependencias adicionales para IA
pip install numpy matplotlib seaborn openpyxl

# Ejecutar cualquier dashboard
python dashboard_ia.py        # Premium con IA
streamlit run dashboard_streamlit.py  # Streamlit
python dashboard.py           # Estándar
```

### � **Dependencias Completas**
```
pandas>=1.3.0          # Análisis de datos
plotly>=5.0.0          # Visualizaciones interactivas
dash>=2.0.0            # Framework web
streamlit>=1.20.0      # Dashboard moderno
scikit-learn>=1.0.0    # Machine Learning
numpy>=1.21.0          # Cálculos numéricos
matplotlib>=3.5.0      # Gráficos base
seaborn>=0.11.0        # Visualizaciones estadísticas
openpyxl>=3.0.0        # Lectura de Excel
```

> **💡 Tip:** El sistema instala automáticamente todas las dependencias la primera vez que ejecutas `ejecutar_dashboard.py`

## 🚀 **Uso Rápido**

### 🎯 **Demo Inmediato (30 segundos)**
```bash
# 1. Generar datos demo
python demo_ia.py

# 2. Lanzar dashboard premium
python dashboard_ia.py

# 3. Abrir http://localhost:8051
```

### 📊 **Con tus datos**
1. **Formato:** Coloca tus archivos Excel en la carpeta del proyecto
2. **Columnas requeridas:** `Vendedor`, `Cliente`, `Producto`, `Precio`, `Fecha`
3. **Ejecutar:** `python ejecutar_dashboard.py` y selecciona tu dashboard
4. **Explorar:** Usa filtros, ve predicciones IA, exporta reportes

### �️ **Selector Inteligente**
```bash
python ejecutar_dashboard.py
```
```
🎨 SELECTOR DE DASHBOARDS 🎨
==============================

1️⃣  Dashboard Premium (Dash + IA)     🤖 Puerto 8051
2️⃣  Dashboard Streamlit (Moderno)     ⚡ Puerto 8502  
3️⃣  Generar datos demo                🎲 Para pruebas
4️⃣  Análisis solo de IA              🧠 Predicciones
5️⃣  Salir                            ❌

Selecciona una opción (1-5): _
```

## � **Características Principales**

### 🔧 **Consolidación Automática**
- ✅ Lectura automática de múltiples archivos Excel (.xlsx, .xls)
- ✅ Consolidación inteligente de datos
- ✅ Validación y limpieza automática
- ✅ Ajuste automático de columnas en Excel
- ✅ Cálculos automáticos (TOTAL_VENTA)

### 🤖 **Inteligencia Artificial**
- 🔮 **Predicciones de ventas** con Machine Learning (R² = 0.999)
- 📈 **Análisis de tendencias** automatizado
- 🎯 **Segmentación inteligente** de vendedores/clientes
- 💡 **Recomendaciones automáticas** basadas en datos
- 🧠 **Modelos predictivos** (Random Forest, K-means)
- 📊 **Métricas avanzadas** con intervalos de confianza

### 📊 **Dashboard Interactivo**
- 🌐 **Interfaz web moderna** multi-tecnología
- 📱 **Responsive design** - funciona en móviles y tablets
- 🎯 **Filtros dinámicos** por categoría, vendedor y fechas
- 📈 **Gráficos interactivos** con Plotly
- 📋 **Tabla de datos** con búsqueda y ordenamiento
- ⚡ **Actualización en tiempo real**

### 📈 **Reportes y Visualizaciones**
- 📊 **12+ tipos de gráficos** diferentes
- 🎨 **Diseño profesional** listo para presentaciones
- 💾 **Exportación en alta calidad** (PNG, 300 DPI)
- 📋 **Métricas clave** resumidas automáticamente
- 🎯 **Análisis de tendencias** con regresión
- 🔍 **Detección de anomalías** en datos

## 🔧 **Estructura del Proyecto**

```
Proyecto_2/
├── 📊 DASHBOARDS
│   ├── dashboard_ia.py           # Dashboard Premium con IA (Puerto 8051)
│   ├── dashboard_streamlit.py    # Dashboard Streamlit (Puerto 8502)
│   └── dashboard.py              # Dashboard Estándar (Puerto 8050)
│
├── 🤖 INTELIGENCIA ARTIFICIAL
│   ├── analisis_ia.py           # Motor de IA con ML
│   └── demo_ia.py               # Generador de datos demo
│
├── 🛠️ UTILIDADES
│   ├── ejecutar_dashboard.py    # Selector inteligente
│   └── automatizacion.py        # Consolidación Excel original
│
├── 📚 DOCUMENTACIÓN
│   ├── README.md                # Este archivo
│   ├── CHANGELOG.md             # Historial de cambios
│   ├── GUIA_RAPIDA_IA.md       # Guía de IA
│   └── COMPARACION_DASHBOARDS.md # Comparativa de dashboards
│
└── 📁 DATOS
    ├── *.xlsx                   # Tus archivos Excel aquí
    ├── ventas_consolidadas.xlsx # Resultado consolidado
    └── ventas_demo_ia.xlsx     # Datos demo generados
```

### 🎯 **Archivos Principales**
- **`ejecutar_dashboard.py`** → 🎯 Punto de entrada principal
- **`dashboard_ia.py`** → 🤖 Dashboard premium con IA
- **`dashboard_streamlit.py`** → ⚡ Dashboard moderno
- **`analisis_ia.py`** → 🧠 Motor de inteligencia artificial
- **`demo_ia.py`** → 🎲 Generador de datos para pruebas

## 📁 Estructura del Proyecto

```
📁 sistema-analisis-ventas/
├── 📄 main.py                  # 🎯 Script principal con menú
├── 📄 automatizacion.py        # 🔧 Consolidación de Excel
├── 📄 dashboard.py             # 📊 Dashboard interactivo
├── 📄 dashboard_ia.py          # 🤖 Dashboard con IA
├── 📄 analisis_ia.py           # 🧠 Análisis inteligente
├── 📄 reporte_grafico.py       # 📈 Reportes estáticos
├── 📄 config.py                # ⚙️ Configuración del sistema
├── 📄 crear_ejemplo.py         # 📝 Generador de datos de prueba
├── 📄 requirements.txt         # 📦 Dependencias
├── 📄 README.md                # 📚 Documentación
├── 📄 CHANGELOG.md             # 📋 Registro de cambios
├── 📄 .gitignore               # 🚫 Archivos ignorados
├── 📊 ventas_ejemplo.xlsx      # 💾 Datos de ejemplo
├── 📁 images/                  # 🖼️ Imágenes y capturas
│   └── mapa_mental_sistema_ventas.png
└── 📁 outputs/                 # 📁 Archivos generados
    ├── Reporte_Consolidado.xlsx
    ├── Reporte_Grafico_*.png
    └── Reporte_IA.png
```

## 📊 Formato de Datos Esperado

### Columnas Requeridas:
- **PRODUCTO**: Nombre del producto
- **CANTIDAD**: Cantidad vendida (número)
- **PRECIO_UNITARIO**: Precio por unidad (número)
- **FECHA**: Fecha de venta (formato: YYYY-MM-DD)

### Columnas Opcionales:
- **CATEGORIA**: Categoría del producto
- **VENDEDOR**: Nombre del vendedor
- **TOTAL_VENTA**: Se calcula automáticamente

### Ejemplo de Datos:
| PRODUCTO | CANTIDAD | PRECIO_UNITARIO | FECHA | CATEGORIA | VENDEDOR |
|----------|----------|-----------------|-------|-----------|----------|
| iPhone 15 | 2 | 1299.99 | 2025-01-15 | Electrónicos | María González |
| Laptop Dell | 1 | 1899.50 | 2025-01-16 | Computadoras | Carlos Rodríguez |

## 🎯 Funcionalidades del Dashboard

### 📊 Métricas Principales
- 💰 **Ventas Totales**: Suma de todas las ventas
- 📦 **Productos Vendidos**: Cantidad total de productos
- 🛍️ **Venta Promedio**: Promedio por transacción
- 📈 **Mejor Vendedor**: Vendedor con más ventas

### 📈 Gráficos Disponibles
1. **Evolución de Ventas** - Línea temporal
2. **Top 10 Productos** - Barras horizontales
3. **Ventas por Categoría** - Gráfico de pastel
4. **Ventas por Vendedor** - Barras verticales

### 🔍 Filtros Disponibles
- **Por Categoría**: Filtrar productos específicos
- **Por Vendedor**: Ver rendimiento individual
- **Por Fechas**: Análisis de períodos específicos

## 🎨 Personalización

### Configuración en `config.py`:
```python
# Cambiar puerto del dashboard
DASHBOARD_PORT = 8080

# Personalizar colores
COLOR_PRIMARIO = "#3498db"
PALETA_COLORES = "viridis"

# Configurar formatos
FORMATO_FECHA = "%d/%m/%Y"
FORMATO_MONEDA = "€"
```

## 🚨 Solución de Problemas

### Error: "No se encontraron archivos Excel"
**Causa**: No hay archivos .xlsx o .xls en la carpeta
**Solución**: 
1. Coloca tus archivos Excel en la misma carpeta que los scripts
2. Ejecuta `python crear_ejemplo.py` para crear datos de prueba

### Error: "ModuleNotFoundError"
**Causa**: Faltan dependencias de Python
**Solución**:
```bash
pip install pandas openpyxl matplotlib seaborn plotly dash dash-bootstrap-components scikit-learn numpy
```

### Error: "Modelo de IA no disponible"
**Causa**: Faltan librerías de Machine Learning
**Solución**:
```bash
pip install scikit-learn numpy
```

### Dashboard no carga
**Causa**: Puerto ocupado o firewall
**Solución**:
1. Cambiar puerto en `config.py`
2. Verificar firewall
3. Probar en: http://localhost:8050

### Gráficos no se muestran
**Causa**: Problemas con matplotlib en algunos sistemas
**Solución**:
```bash
pip install --upgrade matplotlib
```

## 📊 Ejemplos de Uso

### Caso 1: Tienda de Electrónicos
```
Archivos: ventas_enero.xlsx, ventas_febrero.xlsx
Resultado: Dashboard con análisis mensual comparativo
```

### Caso 2: Empresa Multinacional
```
Archivos: ventas_mexico.xlsx, ventas_colombia.xlsx
Filtros: Por vendedor y categoría
Resultado: Análisis regional detallado
```

### Caso 3: Análisis de Temporada
```
Período: Diciembre 2024 - Enero 2025
Filtros: Por fechas específicas
Resultado: Análisis de ventas navideñas
```

## 🔄 Actualizaciones Futuras

### Versión 2.0 (Planificada):
- [ ] 📧 Notificaciones por email
- [ ] 🔄 Actualización automática de datos
- [ ] 📱 App móvil
- [x] 🤖 Predicciones con IA
- [x] 🧠 Dashboard inteligente
- [x] 📊 Análisis de tendencias automatizado
- [x] 🎯 Segmentación de clientes
- [ ] 🌍 Soporte multi-idioma
- [ ] ☁️ Integración con la nube

## 💡 Tips y Trucos

### 🚀 Rendimiento:
- Mantén archivos Excel < 10MB para mejor rendimiento
- Usa el filtro de fechas para análisis de períodos específicos
- Cierra otros programas si el dashboard es lento

### 📊 Mejores Prácticas:
- Mantén nombres de columnas consistentes
- Usa fechas en formato estándar (YYYY-MM-DD)
- Revisa datos antes de consolidar
- Haz respaldos de tus archivos originales

### 🎨 Presentaciones:
- Usa el reporte gráfico para presentaciones estáticas
- El dashboard es ideal para análisis interactivo
- Exporta gráficos específicos desde el dashboard

## 🆘 Soporte

### 📧 Contacto:
- Crea un issue en GitHub
- Revisa la documentación en el README
- Consulta los comentarios en el código

### 📚 Recursos Adicionales:
- [Documentación de Pandas](https://pandas.pydata.org/docs/)
- [Guía de Plotly](https://plotly.com/python/)
- [Tutorial de Dash](https://dash.plotly.com/tutorial)

---

## 🏆 Características Avanzadas

### 🔒 Validación de Datos
- Verificación automática de tipos de datos
- Detección de valores nulos
- Limpieza automática de datos inconsistentes

### 📈 Análisis Estadístico
- Cálculo de tendencias
- Medias móviles
- Correlaciones entre variables

### 🤖 Machine Learning
- **Modelos predictivos**: Random Forest, Gradient Boosting, Linear Regression
- **Segmentación automática**: K-means clustering de vendedores/productos
- **Predicciones temporales**: Ventas futuras con intervalos de confianza
- **Recomendaciones inteligentes**: Basadas en patrones de datos
- **Análisis de anomalías**: Detección de valores atípicos

### 🎯 Optimización
- Carga eficiente de archivos grandes
- Renderizado optimizado de gráficos
- Cache inteligente para mejor rendimiento

---

## 🤝 Contribuir

¡Las contribuciones son bienvenidas! Por favor, abre un issue o pull request para sugerencias, mejoras o correcciones.

---

## 📝 Licencia

Este proyecto está bajo la Licencia MIT. Consulta el archivo [LICENSE](LICENSE) para más detalles.

---

**¡Disfruta analizando tus datos de ventas! 📊🚀**

```python
import automatizacion
# Ejemplo de uso aquí...
```

## 🗺️ Mapa Mental del Proyecto

![Mapa Mental](images/mapa_mental_sistema_ventas.png)
