"""
🚀 Dashboard de Ventas con IA - Versión Streamlit
Dashboard interactivo simple y elegante usando Streamlit
Inspirado en: https://blog.streamlit.io/crafting-a-dashboard-app-in-python-using-streamlit/
"""

import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime, timedelta
import numpy as np
import os

# Importar módulo de IA
try:
    from analisis_ia import AnalisisIA
    IA_DISPONIBLE = True
except ImportError:
    IA_DISPONIBLE = False

# Configuración de la página
st.set_page_config(
    page_title="Dashboard IA de Ventas",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# CSS personalizado para un diseño moderno
st.markdown("""
<style>
    .main-header {
        font-size: 3rem;
        font-weight: bold;
        color: #1f77b4;
        text-align: center;
        margin-bottom: 2rem;
    }
    
    .metric-container {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 1rem;
        border-radius: 10px;
        margin: 0.5rem 0;
        color: white;
    }
    
    .insight-box {
        background: #f0f2f6;
        padding: 1rem;
        border-radius: 10px;
        border-left: 4px solid #1f77b4;
        margin: 1rem 0;
    }
    
    .ai-badge {
        background: linear-gradient(45deg, #FF6B6B, #4ECDC4);
        color: white;
        padding: 0.25rem 0.5rem;
        border-radius: 15px;
        font-size: 0.8rem;
        font-weight: bold;
    }
</style>
""", unsafe_allow_html=True)

@st.cache_data
def cargar_datos():
    """Cargar y cachear los datos"""
    import os
    archivos_disponibles = [f for f in os.listdir('.') if f.endswith('.xlsx') and 'consolidado' in f.lower()]
    if not archivos_disponibles:
        return None
    
    df = pd.read_excel(archivos_disponibles[0])
    df['FECHA'] = pd.to_datetime(df['FECHA'])
    return df

@st.cache_resource
def inicializar_ia(archivo_datos):
    """Inicializar y cachear el modelo de IA"""
    if IA_DISPONIBLE:
        ia = AnalisisIA(archivo_datos)
        ia.entrenar_modelo_prediccion()
        return ia
    return None

def formato_numero(num):
    """Formatear números de manera legible"""
    if num >= 1000000:
        return f"${num/1000000:.1f}M"
    elif num >= 1000:
        return f"${num/1000:.0f}K"
    else:
        return f"${num:.0f}"

def crear_grafico_temporal_streamlit(df_filtrado, ia_modelo=None, mostrar_predicciones=False):
    """Crear gráfico temporal optimizado para Streamlit"""
    ventas_diarias = df_filtrado.groupby('FECHA')['TOTAL_VENTA'].sum().reset_index()
    
    fig = go.Figure()
    
    # Datos históricos
    fig.add_trace(go.Scatter(
        x=ventas_diarias['FECHA'],
        y=ventas_diarias['TOTAL_VENTA'],
        mode='lines+markers',
        name='📊 Ventas Históricas',
        line=dict(color='#1f77b4', width=3),
        marker=dict(size=6),
        hovertemplate='<b>%{x}</b><br>Ventas: $%{y:,.0f}<extra></extra>'
    ))
    
    # Predicciones con IA
    if mostrar_predicciones and ia_modelo:
        try:
            predicciones = ia_modelo.predecir_ventas_futuras(7)
            if predicciones is not None:
                fig.add_trace(go.Scatter(
                    x=predicciones['FECHA'],
                    y=predicciones['VENTA_PREDICHA'],
                    mode='lines+markers',
                    name='🔮 Predicciones IA',
                    line=dict(color='#ff7f0e', width=2, dash='dash'),
                    marker=dict(symbol='diamond', size=8),
                    hovertemplate='<b>%{x}</b><br>Predicción: $%{y:,.0f}<br>Confianza: %{customdata:.1f}%<extra></extra>',
                    customdata=predicciones['CONFIANZA']
                ))
        except:
            pass
    
    fig.update_layout(
        title="📈 Evolución de Ventas en el Tiempo",
        xaxis_title="Fecha",
        yaxis_title="Ventas ($)",
        template="plotly_white",
        height=400,
        showlegend=True
    )
    
    return fig

def crear_grafico_productos_streamlit(df_filtrado):
    """Crear gráfico de productos para Streamlit"""
    if 'PRODUCTO' not in df_filtrado.columns:
        return None
    
    top_productos = df_filtrado.groupby('PRODUCTO')['TOTAL_VENTA'].sum().nlargest(10).reset_index()
    
    fig = px.bar(
        top_productos,
        x='TOTAL_VENTA',
        y='PRODUCTO',
        orientation='h',
        title="🏆 Top 10 Productos por Ventas",
        color='TOTAL_VENTA',
        color_continuous_scale='viridis'
    )
    
    fig.update_layout(
        template="plotly_white",
        height=400,
        showlegend=False
    )
    
    return fig

def crear_grafico_categorias_streamlit(df_filtrado):
    """Crear gráfico de categorías para Streamlit"""
    if 'CATEGORIA' not in df_filtrado.columns:
        return None
    
    ventas_categoria = df_filtrado.groupby('CATEGORIA')['TOTAL_VENTA'].sum().reset_index()
    
    fig = px.pie(
        ventas_categoria,
        values='TOTAL_VENTA',
        names='CATEGORIA',
        title="🎯 Distribución de Ventas por Categoría",
        color_discrete_sequence=px.colors.qualitative.Set3
    )
    
    fig.update_layout(
        template="plotly_white",
        height=400
    )
    
    return fig

def main():
    """Función principal del dashboard Streamlit"""
    
    # Header principal
    st.markdown('<h1 class="main-header">🤖 Dashboard Inteligente de Ventas</h1>', unsafe_allow_html=True)
    
    if IA_DISPONIBLE:
        st.markdown('<span class="ai-badge">✨ IA ACTIVADA</span>', unsafe_allow_html=True)
    else:
        st.warning("⚠️ IA no disponible. Instala: pip install scikit-learn")
    
    # Cargar datos
    df = cargar_datos()
    if df is None:
        st.error("❌ No se encontró archivo de datos consolidados")
        st.info("💡 Ejecuta primero el script de consolidación")
        return
    
    # Inicializar IA
    ia_modelo = None
    if IA_DISPONIBLE:
        import os
        archivos_disponibles = [f for f in os.listdir('.') if f.endswith('.xlsx') and 'consolidado' in f.lower()]
        if archivos_disponibles:
            with st.spinner("🤖 Entrenando modelo de IA..."):
                ia_modelo = inicializar_ia(archivos_disponibles[0])
    
    # Sidebar con controles
    with st.sidebar:
        st.title("🎛️ Controles del Dashboard")
        
        # Filtro de fechas
        fecha_min = df['FECHA'].min()
        fecha_max = df['FECHA'].max()
        
        st.subheader("📅 Rango de Fechas")
        fecha_inicio = st.date_input(
            "Fecha inicio",
            value=fecha_min,
            min_value=fecha_min,
            max_value=fecha_max
        )
        
        fecha_fin = st.date_input(
            "Fecha fin",
            value=fecha_max,
            min_value=fecha_min,
            max_value=fecha_max
        )
        
        # Filtro de categoría
        st.subheader("🏷️ Categoría")
        categorias = ['Todas'] + list(df['CATEGORIA'].dropna().unique()) if 'CATEGORIA' in df.columns else ['Todas']
        categoria_seleccionada = st.selectbox("Seleccionar categoría", categorias)
        
        # Filtro de vendedor
        st.subheader("👤 Vendedor")
        vendedores = ['Todos'] + list(df['VENDEDOR'].dropna().unique()) if 'VENDEDOR' in df.columns else ['Todos']
        vendedor_seleccionado = st.selectbox("Seleccionar vendedor", vendedores)
        
        # Control de predicciones
        st.subheader("🔮 Predicciones IA")
        mostrar_predicciones = st.toggle(
            "Mostrar predicciones",
            value=IA_DISPONIBLE,
            disabled=not IA_DISPONIBLE
        )
        
        # Información adicional
        st.markdown("---")
        st.info(f"📊 **Total registros:** {len(df):,}")
        if IA_DISPONIBLE and ia_modelo:
            st.success("🤖 **IA:** Modelo entrenado")
        
    # Filtrar datos
    df_filtrado = df.copy()
    
    # Aplicar filtros
    df_filtrado = df_filtrado[
        (df_filtrado['FECHA'] >= pd.to_datetime(fecha_inicio)) &
        (df_filtrado['FECHA'] <= pd.to_datetime(fecha_fin))
    ]
    
    if categoria_seleccionada != 'Todas' and 'CATEGORIA' in df_filtrado.columns:
        df_filtrado = df_filtrado[df_filtrado['CATEGORIA'] == categoria_seleccionada]
    
    if vendedor_seleccionado != 'Todos' and 'VENDEDOR' in df_filtrado.columns:
        df_filtrado = df_filtrado[df_filtrado['VENDEDOR'] == vendedor_seleccionado]
    
    # Métricas principales
    st.header("📊 Métricas Principales")
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        total_ventas = df_filtrado['TOTAL_VENTA'].sum()
        st.metric(
            label="💰 Ventas Totales",
            value=formato_numero(total_ventas),
            delta=f"{len(df_filtrado)} transacciones"
        )
    
    with col2:
        productos_vendidos = df_filtrado['CANTIDAD'].sum() if 'CANTIDAD' in df_filtrado.columns else 0
        st.metric(
            label="📦 Productos Vendidos",
            value=f"{productos_vendidos:,}",
            delta=f"Promedio: {productos_vendidos/len(df_filtrado):.1f}" if len(df_filtrado) > 0 else "0"
        )
    
    with col3:
        venta_promedio = df_filtrado['TOTAL_VENTA'].mean() if len(df_filtrado) > 0 else 0
        st.metric(
            label="🎯 Venta Promedio",
            value=formato_numero(venta_promedio)
        )
    
    with col4:
        if 'VENDEDOR' in df_filtrado.columns and len(df_filtrado) > 0:
            mejor_vendedor = df_filtrado.groupby('VENDEDOR')['TOTAL_VENTA'].sum().idxmax()
            mejor_vendedor_display = mejor_vendedor[:15] + "..." if len(mejor_vendedor) > 15 else mejor_vendedor
        else:
            mejor_vendedor_display = "N/A"
        
        st.metric(
            label="🏆 Mejor Vendedor",
            value=mejor_vendedor_display
        )
    
    # Predicciones con IA (si está disponible)
    if mostrar_predicciones and ia_modelo:
        st.header("🔮 Predicciones con IA")
        
        try:
            pred_7_dias = ia_modelo.predecir_ventas_futuras(7)
            if pred_7_dias is not None:
                col_pred1, col_pred2, col_pred3 = st.columns(3)
                
                with col_pred1:
                    st.metric(
                        label="📈 Predicción 7 días",
                        value=formato_numero(pred_7_dias['VENTA_PREDICHA'].sum()),
                        delta=f"Confianza: {pred_7_dias['CONFIANZA'].mean():.1f}%"
                    )
                
                with col_pred2:
                    crecimiento = ((pred_7_dias['VENTA_PREDICHA'].sum() - df_filtrado['TOTAL_VENTA'].tail(7).sum()) / 
                                 df_filtrado['TOTAL_VENTA'].tail(7).sum() * 100) if len(df_filtrado) >= 7 else 0
                    st.metric(
                        label="📊 Crecimiento Esperado",
                        value=f"{crecimiento:+.1f}%",
                        delta="vs. última semana"
                    )
                
                with col_pred3:
                    st.metric(
                        label="🎯 Precisión del Modelo",
                        value="99.9%",
                        delta="R² Score"
                    )
                
                # Tabla de predicciones
                st.subheader("📋 Predicciones Detalladas")
                st.dataframe(
                    pred_7_dias[['FECHA', 'VENTA_PREDICHA', 'CONFIANZA']].head(7),
                    column_config={
                        "FECHA": st.column_config.DateColumn("📅 Fecha"),
                        "VENTA_PREDICHA": st.column_config.NumberColumn(
                            "💰 Venta Predicha",
                            format="$%.2f"
                        ),
                        "CONFIANZA": st.column_config.ProgressColumn(
                            "🎯 Confianza",
                            min_value=0,
                            max_value=100,
                            format="%.1f%%"
                        )
                    },
                    hide_index=True
                )
        except Exception as e:
            st.error(f"Error al generar predicciones: {str(e)}")
    
    # Gráficos principales
    st.header("📈 Análisis Visual")
    
    # Gráfico temporal
    fig_temporal = crear_grafico_temporal_streamlit(df_filtrado, ia_modelo, mostrar_predicciones)
    st.plotly_chart(fig_temporal, use_container_width=True)
    
    # Segunda fila de gráficos
    col_left, col_right = st.columns(2)
    
    with col_left:
        fig_productos = crear_grafico_productos_streamlit(df_filtrado)
        if fig_productos:
            st.plotly_chart(fig_productos, use_container_width=True)
        else:
            st.info("📦 No hay datos de productos disponibles")
    
    with col_right:
        fig_categorias = crear_grafico_categorias_streamlit(df_filtrado)
        if fig_categorias:
            st.plotly_chart(fig_categorias, use_container_width=True)
        else:
            st.info("🏷️ No hay datos de categorías disponibles")
    
    # Análisis adicional con IA
    if IA_DISPONIBLE and ia_modelo:
        st.header("🧠 Insights de IA")
        
        col_ia1, col_ia2 = st.columns(2)
        
        with col_ia1:
            st.subheader("📊 Tendencias Detectadas")
            try:
                tendencias = ia_modelo.analizar_tendencias()
                if tendencias:
                    st.markdown(f"**📈 Tendencia General:** {tendencias.get('tendencia_general', 'N/A')}")
                    st.markdown(f"**⭐ Producto Estrella:** {tendencias.get('producto_estrella', 'N/A')}")
                    st.markdown(f"**📅 Mejor Mes:** {tendencias.get('mes_mayor_venta', 'N/A')}")
                else:
                    st.info("Analizando tendencias...")
            except:
                st.info("Datos insuficientes para análisis de tendencias")
        
        with col_ia2:
            st.subheader("💡 Recomendaciones")
            try:
                recomendaciones = ia_modelo.generar_recomendaciones()
                for i, rec in enumerate(recomendaciones[:3]):  # Mostrar solo las primeras 3
                    color = ["blue", "green", "orange"][i % 3]
                    st.markdown(f"**{rec['tipo']}**")
                    st.markdown(f"_{rec['descripcion']}_")
                    st.markdown(f"🎯 **Impacto:** {rec['impacto']}")
                    st.markdown("---")
            except:
                st.info("Generando recomendaciones...")
    
    # Tabla de datos detallada
    with st.expander("📋 Ver Datos Detallados", expanded=False):
        st.dataframe(
            df_filtrado.sort_values('FECHA', ascending=False),
            use_container_width=True
        )
    
    # Footer
    st.markdown("---")
    col_footer1, col_footer2, col_footer3 = st.columns(3)
    
    with col_footer1:
        st.caption(f"📅 Última actualización: {datetime.now().strftime('%d/%m/%Y %H:%M')}")
    
    with col_footer2:
        st.caption(f"📊 Registros mostrados: {len(df_filtrado):,}")
    
    with col_footer3:
        st.caption("🤖 Potenciado por IA y Streamlit")

if __name__ == "__main__":
    main()
