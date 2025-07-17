# 🚀 Sistema Completo de Análisis de Ventas

Un sistema integral para consolidar, analizar y visualizar datos de ventas desde múltiples archivos Excel.

## 📋 Características Principales

### 🔧 Consolidación Automática
- ✅ Lectura automática de múltiples archivos Excel (.xlsx, .xls)
- ✅ Consolidación inteligente de datos
- ✅ Validación y limpieza automática
- ✅ Ajuste automático de columnas en Excel
- ✅ Cálculos automáticos (TOTAL_VENTA)

### 📊 Dashboard Interactivo
- 🌐 **Interfaz web moderna** con Bootstrap
- 📱 **Responsive design** - funciona en móviles y tablets
- 🎯 **Filtros dinámicos** por categoría, vendedor y fechas
- 📈 **Gráficos interactivos** con Plotly
- 📋 **Tabla de datos** con búsqueda y ordenamiento
- ⚡ **Actualización en tiempo real**

### 📈 Reportes Gráficos
- 📊 **9 tipos de gráficos** diferentes
- 🎨 **Diseño profesional** listo para presentaciones
- 💾 **Exportación en alta calidad** (PNG, 300 DPI)
- 📋 **Métricas clave** resumidas
- 🎯 **Análisis de tendencias**

## 🛠️ Instalación

### Requisitos
- Python 3.7 o superior
- pip (gestor de paquetes de Python)

### Pasos de Instalación

1. **Clonar o descargar** este proyecto
2. **Navegar** a la carpeta del proyecto
3. **Instalar dependencias** (se hace automáticamente al ejecutar)

```bash
cd "ruta/a/tu/proyecto"
python main.py
```

## 🚀 Uso Rápido

### Opción 1: Script Principal (Recomendado)
```bash
python main.py
```

### Opción 2: Scripts Individuales

**Consolidar datos:**
```bash
python automatizacion.py
```

**Generar reporte gráfico:**
```bash
python reporte_grafico.py
```

**Ejecutar dashboard:**
```bash
python dashboard.py
```

## 📁 Estructura de Archivos

```
📁 Proyecto_Ventas/
├── 📄 main.py                  # Script principal con menú
├── 📄 automatizacion.py        # Consolidación de Excel
├── 📄 dashboard.py             # Dashboard interactivo
├── 📄 reporte_grafico.py       # Reportes estáticos
├── 📄 config.py                # Configuración del sistema
├── 📄 crear_ejemplo.py         # Generador de datos de prueba
├── 📄 README.md                # Este archivo
├── 📊 ventas_ejemplo.xlsx      # Datos de ejemplo
├── 📊 Reporte_Consolidado.xlsx # Resultado consolidado
└── 🖼️ Reporte_Grafico_*.png    # Reportes generados
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
pip install pandas openpyxl matplotlib seaborn plotly dash dash-bootstrap-components
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
- [ ] 🤖 Predicciones con IA
- [ ] 📊 Más tipos de gráficos
- [ ] 🌍 Soporte multi-idioma

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

### 🎯 Optimización
- Carga eficiente de archivos grandes
- Renderizado optimizado de gráficos
- Cache inteligente para mejor rendimiento

---

**¡Disfruta analizando tus datos de ventas! 📊🚀**
