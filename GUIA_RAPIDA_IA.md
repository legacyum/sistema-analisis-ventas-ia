🎯 GUÍA RÁPIDA DE USO - SISTEMA DE IA
=====================================

## 🚀 INICIO RÁPIDO

1. **Ejecutar el sistema:**
   ```bash
   python main.py
   ```

2. **Seleccionar opción 7 para demo completo:**
   - Genera datos optimizados para IA
   - Crea 1000+ registros de prueba
   - Simula patrones reales de ventas

3. **Probar análisis de IA (opción 5):**
   - Entrena modelos automáticamente
   - Genera predicciones de 7 días
   - Segmenta vendedores
   - Crea recomendaciones

4. **Explorar dashboard IA (opción 4):**
   - Abre http://localhost:8051
   - Navega por las 4 pestañas
   - Experimenta con filtros
   - Ve predicciones en tiempo real

## 🤖 FUNCIONALIDADES DE IA DISPONIBLES

### 🔮 Predicciones
- **Ventas futuras:** 7, 30 días o más
- **Confianza:** Intervalos decrecientes
- **Factores:** Temporales, categorías, vendedores

### 🎯 Segmentación
- **Vendedores Estrella:** Alto volumen + frecuencia
- **Vendedores Premium:** Alto volumen + exclusividad
- **Vendedores Activos:** Volumen medio + alta frecuencia
- **Vendedores Nuevos:** Bajo volumen + aprendizaje

### 💡 Recomendaciones
- **Productos estrella:** Para enfocar marketing
- **Productos en riesgo:** Que necesitan atención
- **Optimización temporal:** Mejores días para promociones
- **Desarrollo de equipo:** Programas de mentoring

### 📊 Análisis Avanzado
- **Tendencias:** Automáticas con regresión
- **Estacionalidad:** Patrones mensuales/semanales
- **Correlaciones:** Entre variables
- **Anomalías:** Detección automática

## 🎨 DASHBOARDS DISPONIBLES

### 📊 Dashboard Estándar (puerto 8050)
- Análisis básico de ventas
- Gráficos interactivos
- Filtros por categoría/vendedor
- Tablas dinámicas

### 🤖 Dashboard IA Premium (puerto 8051)
- Todo lo del dashboard estándar
- **PLUS:** Predicciones en tiempo real
- **PLUS:** Análisis de tendencias automatizado
- **PLUS:** Recomendaciones inteligentes
- **PLUS:** Segmentación de vendedores
- **PLUS:** Diseño premium con gradientes

### ⚡ Dashboard Streamlit (puerto 8502) ✨ **NUEVO**
- Interfaz limpia y minimalista
- Desarrollo rápido estilo Streamlit
- Métricas con deltas automáticos
- Sidebar intuitivo con controles
- **PLUS:** Cache automático
- **PLUS:** Todas las funciones de IA

## 📈 TIPOS DE REPORTES

### 🖼️ Reportes Estáticos
- PNG de alta calidad (300 DPI)
- 9 tipos de gráficos
- Listo para presentaciones
- Métricas resumidas

### 🧠 Reportes IA
- Análisis inteligente visual
- Predicciones gráficas
- Segmentación visual
- Tendencias automáticas

## 🔧 CONFIGURACIÓN RÁPIDA

### Cambiar puertos:
```python
# En config.py
DASHBOARD_PORT = 8080  # Dashboard estándar
```

### Personalizar colores:
```python
# En config.py
COLOR_PRIMARIO = "#2c3e50"
COLORES_GRAFICOS = ["#3498db", "#e74c3c", ...]
```

### Ajustar predicciones:
```python
# En analisis_ia.py
predicciones = ia.predecir_ventas_futuras(30)  # 30 días
```

## ⚡ COMANDOS DIRECTOS

```bash
# Selector interactivo de dashboards
python ejecutar_dashboard.py

# Solo análisis IA
python analisis_ia.py

# Dashboard IA Premium (Dash)
python dashboard_ia.py

# Dashboard Simple (Streamlit)
streamlit run dashboard_streamlit.py

# Dashboard estándar
python dashboard.py

# Solo reportes gráficos
python reporte_grafico.py

# Crear datos de prueba
python demo_ia.py
```

## 🎯 CASOS DE USO

### 📊 Análisis Ejecutivo
1. Ejecuta: `python main.py → opción 5`
2. Revisa tendencias y predicciones
3. Implementa recomendaciones

### 📈 Presentaciones
1. Ejecuta: `python main.py → opción 2`
2. Usa PNGs generados
3. Complementa con dashboard en vivo

### 🔍 Análisis Detallado
1. **Opción A:** `python main.py → opción 4` (Dashboard Premium)
2. **Opción B:** `python ejecutar_dashboard.py → opción 2` (Dashboard Streamlit)
3. **Opción C:** `streamlit run dashboard_streamlit.py` (Directo)
4. Explora cada pestaña
5. Aplica filtros específicos

### 🧪 Experimentación
1. **Dashboard Streamlit:** Prototipado rápido
2. **Dashboard Dash:** Presentaciones ejecutivas
3. Ejecuta: `python main.py → opción 7`
4. Genera diferentes escenarios
5. Prueba con tus propios datos

## 💡 TIPS AVANZADOS

### 🚀 Rendimiento
- Archivos < 10MB: Rendimiento óptimo
- Archivos > 10MB: Usar filtros de fecha
- Datasets grandes: Considerar sampling

### 🎯 Precisión
- Más datos = mejores predicciones
- Datos consistentes = mejor segmentación
- Patrones temporales = tendencias más claras

### 🎨 Visualización
- Dashboard IA: Análisis interactivo
- Reportes PNG: Presentaciones formales
- Filtros: Análisis específicos

## 🆘 SOLUCIÓN RÁPIDA DE PROBLEMAS

### Error: "Modelo no entrenado"
```bash
pip install scikit-learn numpy
```

### Puerto ocupado:
```bash
# Cambiar puerto en config.py o
taskkill /f /im python.exe
```

### Datos insuficientes:
```bash
python demo_ia.py  # Genera datos de prueba
```

### Gráficos no cargan:
```bash
pip install --upgrade matplotlib plotly
```

---

**🎉 ¡Tu sistema de IA está listo para analizar ventas como un experto!**

*Desarrollado por Alessandro - Julio 2025*
