# 🔧 CONFIGURACIÓN DEL SISTEMA DE ANÁLISIS DE VENTAS
# ===================================================

# 📂 CONFIGURACIÓN DE ARCHIVOS
CARPETA_VENTAS = "."  # Carpeta actual por defecto
ARCHIVO_SALIDA = "Reporte_Consolidado.xlsx"
PREFIJO_REPORTE_GRAFICO = "Reporte_Grafico_Ventas"

# 📊 CONFIGURACIÓN DEL DASHBOARD
DASHBOARD_HOST = "localhost"
DASHBOARD_PORT = 8050
DASHBOARD_DEBUG = True

# 🎨 CONFIGURACIÓN DE GRÁFICOS
FIGURA_WIDTH = 20
FIGURA_HEIGHT = 15
DPI_REPORTE = 300
ESTILO_GRAFICO = "seaborn-v0_8"

# 📋 CONFIGURACIÓN DE COLUMNAS ESPERADAS
COLUMNAS_REQUERIDAS = {
    'PRODUCTO': 'Nombre del producto',
    'CANTIDAD': 'Cantidad vendida',
    'PRECIO_UNITARIO': 'Precio por unidad',
    'FECHA': 'Fecha de la venta',
    'CATEGORIA': 'Categoría del producto',
    'VENDEDOR': 'Nombre del vendedor'
}

# 🔢 CONFIGURACIÓN DE CÁLCULOS
COLUMNA_TOTAL_VENTA = 'TOTAL_VENTA'
FORMULA_TOTAL = lambda df: df['PRECIO_UNITARIO'] * df['CANTIDAD']

# 📱 CONFIGURACIÓN DE LA INTERFAZ
TITULO_DASHBOARD = "📊 Dashboard de Ventas"
TEMA_BOOTSTRAP = "BOOTSTRAP"  # Opciones: BOOTSTRAP, CERULEAN, COSMO, FLATLY, etc.

# 🎯 CONFIGURACIÓN DE FILTROS
FILTROS_PREDETERMINADOS = {
    'categoria': 'todas',
    'vendedor': 'todos',
    'fecha_inicio': None,
    'fecha_fin': None
}

# 📈 CONFIGURACIÓN DE MÉTRICAS
METRICAS_PRINCIPALES = [
    'total_ventas',
    'total_productos', 
    'venta_promedio',
    'mejor_vendedor'
]

# 🔍 CONFIGURACIÓN DE TABLA
REGISTROS_POR_PAGINA = 10
ORDENAMIENTO_PREDETERMINADO = 'FECHA'

# ⚠️ CONFIGURACIÓN DE VALIDACIONES
VALIDAR_FECHAS = True
VALIDAR_NUMEROS = True
PERMITIR_VALORES_NULOS = True

# 🎨 COLORES PARA GRÁFICOS
PALETA_COLORES = "husl"  # Opciones: husl, Set3, viridis, etc.
COLOR_PRIMARIO = "#3498db"
COLOR_SECUNDARIO = "#2c3e50"
COLOR_EXITO = "#27ae60"
COLOR_ADVERTENCIA = "#f39c12"

# 🌈 COLORES ESPECÍFICOS PARA GRÁFICOS
COLORES_GRAFICOS = [
    "#3498db",  # Azul principal
    "#e74c3c",  # Rojo
    "#2ecc71",  # Verde
    "#f39c12",  # Naranja
    "#9b59b6",  # Púrpura
    "#1abc9c",  # Turquesa
    "#34495e",  # Gris oscuro
    "#e67e22",  # Naranja oscuro
    "#95a5a6",  # Gris claro
    "#f1c40f"   # Amarillo
]

# 📊 CONFIGURACIÓN DE EXPORTACIÓN
FORMATOS_EXPORTACION = ['xlsx', 'csv', 'png', 'pdf']
INCLUIR_GRAFICOS_EN_EXCEL = True

# 💾 CONFIGURACIÓN DE RESPALDO
CREAR_RESPALDO = True
CARPETA_RESPALDO = "respaldos"
MANTENER_RESPALDOS_DIAS = 30

# 🔄 CONFIGURACIÓN DE ACTUALIZACIÓN
AUTOREFRESH_DASHBOARD = False
INTERVALO_ACTUALIZACION_SEGUNDOS = 60

# 📧 CONFIGURACIÓN DE NOTIFICACIONES (Futuro)
ENVIAR_NOTIFICACIONES = False
EMAIL_DESTINATARIOS = []
WEBHOOK_URL = ""

# 🌐 CONFIGURACIÓN REGIONAL
FORMATO_FECHA = "%d/%m/%Y"
FORMATO_MONEDA = "$"
SEPARADOR_MILES = ","
DECIMALES_MONEDA = 0

# 🎛️ CONFIGURACIÓN AVANZADA
MODO_DEBUG = True
LOG_LEVEL = "INFO"  # DEBUG, INFO, WARNING, ERROR
USAR_CACHE = True
TIMEOUT_OPERACIONES = 30  # segundos
