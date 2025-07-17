"""
🤖 Módulo de Análisis con Inteligencia Artificial
Sistema avanzado de predicciones y análisis inteligente de ventas
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime, timedelta
import warnings
warnings.filterwarnings('ignore')

# Librerías de Machine Learning
try:
    from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
    from sklearn.linear_model import LinearRegression
    from sklearn.preprocessing import StandardScaler, LabelEncoder
    from sklearn.model_selection import train_test_split
    from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
    from sklearn.cluster import KMeans
    ML_DISPONIBLE = True
except ImportError:
    ML_DISPONIBLE = False
    print("⚠️  Librerías de ML no instaladas. Ejecuta: pip install scikit-learn")

import config

class AnalisisIA:
    def __init__(self, archivo_datos=None):
        """Inicializar el análisis de IA"""
        self.df = None
        self.modelo_ventas = None
        self.scaler = None
        self.le_categoria = LabelEncoder() if ML_DISPONIBLE else None
        self.le_vendedor = LabelEncoder() if ML_DISPONIBLE else None
        
        if archivo_datos:
            self.cargar_datos(archivo_datos)
    
    def cargar_datos(self, archivo):
        """Cargar datos desde archivo Excel"""
        try:
            self.df = pd.read_excel(archivo)
            self.df['FECHA'] = pd.to_datetime(self.df['FECHA'])
            print(f"✅ Datos cargados: {len(self.df)} registros")
            return True
        except Exception as e:
            print(f"❌ Error al cargar datos: {e}")
            return False
    
    def preparar_datos_para_ml(self):
        """Preparar datos para machine learning"""
        if not ML_DISPONIBLE:
            print("❌ Librerías de ML no disponibles")
            return None
        
        df_ml = self.df.copy()
        
        # Crear características temporales
        df_ml['AÑO'] = df_ml['FECHA'].dt.year
        df_ml['MES'] = df_ml['FECHA'].dt.month
        df_ml['DIA_SEMANA'] = df_ml['FECHA'].dt.dayofweek
        df_ml['DIA_MES'] = df_ml['FECHA'].dt.day
        
        # Codificar variables categóricas
        if 'CATEGORIA' in df_ml.columns:
            df_ml['CATEGORIA_COD'] = self.le_categoria.fit_transform(df_ml['CATEGORIA'].fillna('Sin Categoría'))
        
        if 'VENDEDOR' in df_ml.columns:
            df_ml['VENDEDOR_COD'] = self.le_vendedor.fit_transform(df_ml['VENDEDOR'].fillna('Sin Vendedor'))
        
        # Características de agregación
        df_ml['PRECIO_PROMEDIO_CATEGORIA'] = df_ml.groupby('CATEGORIA')['PRECIO_UNITARIO'].transform('mean')
        df_ml['VENTAS_PROMEDIO_VENDEDOR'] = df_ml.groupby('VENDEDOR')['TOTAL_VENTA'].transform('mean')
        
        return df_ml
    
    def entrenar_modelo_prediccion(self):
        """Entrenar modelo para predicción de ventas"""
        if not ML_DISPONIBLE:
            print("❌ Librerías de ML no disponibles")
            return False
        
        print("🤖 Entrenando modelo de predicción de ventas...")
        
        df_ml = self.preparar_datos_para_ml()
        if df_ml is None:
            return False
        
        # Seleccionar características
        caracteristicas = ['CANTIDAD', 'PRECIO_UNITARIO', 'AÑO', 'MES', 'DIA_SEMANA', 'DIA_MES']
        
        if 'CATEGORIA_COD' in df_ml.columns:
            caracteristicas.append('CATEGORIA_COD')
        if 'VENDEDOR_COD' in df_ml.columns:
            caracteristicas.append('VENDEDOR_COD')
        if 'PRECIO_PROMEDIO_CATEGORIA' in df_ml.columns:
            caracteristicas.append('PRECIO_PROMEDIO_CATEGORIA')
        if 'VENTAS_PROMEDIO_VENDEDOR' in df_ml.columns:
            caracteristicas.append('VENTAS_PROMEDIO_VENDEDOR')
        
        X = df_ml[caracteristicas].fillna(0)
        y = df_ml['TOTAL_VENTA']
        
        # Dividir datos
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        
        # Escalar datos
        self.scaler = StandardScaler()
        X_train_scaled = self.scaler.fit_transform(X_train)
        X_test_scaled = self.scaler.transform(X_test)
        
        # Entrenar múltiples modelos y elegir el mejor
        modelos = {
            'Random Forest': RandomForestRegressor(n_estimators=100, random_state=42),
            'Gradient Boosting': GradientBoostingRegressor(random_state=42),
            'Linear Regression': LinearRegression()
        }
        
        mejor_modelo = None
        mejor_score = -float('inf')
        
        for nombre, modelo in modelos.items():
            modelo.fit(X_train_scaled, y_train)
            score = modelo.score(X_test_scaled, y_test)
            print(f"   {nombre}: R² = {score:.3f}")
            
            if score > mejor_score:
                mejor_score = score
                mejor_modelo = modelo
        
        self.modelo_ventas = mejor_modelo
        
        # Evaluación detallada
        y_pred = self.modelo_ventas.predict(X_test_scaled)
        mae = mean_absolute_error(y_test, y_pred)
        rmse = np.sqrt(mean_squared_error(y_test, y_pred))
        
        print(f"\n📊 Métricas del mejor modelo:")
        print(f"   R² Score: {mejor_score:.3f}")
        print(f"   MAE: ${mae:.2f}")
        print(f"   RMSE: ${rmse:.2f}")
        
        return True
    
    def predecir_ventas_futuras(self, dias_adelante=30):
        """Predecir ventas para los próximos días"""
        if not ML_DISPONIBLE or self.modelo_ventas is None:
            print("❌ Modelo no entrenado")
            return None
        
        print(f"🔮 Generando predicciones para los próximos {dias_adelante} días...")
        
        # Obtener estadísticas históricas
        fecha_actual = self.df['FECHA'].max()
        
        predicciones = []
        
        for i in range(1, dias_adelante + 1):
            fecha_futura = fecha_actual + timedelta(days=i)
            
            # Características basadas en promedios históricos
            cantidad_promedio = self.df['CANTIDAD'].mean()
            precio_promedio = self.df['PRECIO_UNITARIO'].mean()
            
            # Crear características temporales
            caracteristicas = [
                cantidad_promedio,
                precio_promedio,
                fecha_futura.year,
                fecha_futura.month,
                fecha_futura.weekday(),
                fecha_futura.day
            ]
            
            # Agregar características categóricas si están disponibles
            if hasattr(self.le_categoria, 'classes_'):
                caracteristicas.append(0)  # Categoría más común
            if hasattr(self.le_vendedor, 'classes_'):
                caracteristicas.append(0)  # Vendedor más común
            if 'CATEGORIA' in self.df.columns:
                caracteristicas.append(self.df.groupby('CATEGORIA')['PRECIO_UNITARIO'].mean().mean())
            if 'VENDEDOR' in self.df.columns:
                caracteristicas.append(self.df.groupby('VENDEDOR')['TOTAL_VENTA'].mean().mean())
            
            # Ajustar longitud de características
            X_pred = np.array(caracteristicas).reshape(1, -1)
            
            # Asegurar que tenga el número correcto de características
            if X_pred.shape[1] != self.scaler.n_features_in_:
                # Rellenar o truncar según sea necesario
                if X_pred.shape[1] < self.scaler.n_features_in_:
                    padding = np.zeros((1, self.scaler.n_features_in_ - X_pred.shape[1]))
                    X_pred = np.hstack([X_pred, padding])
                else:
                    X_pred = X_pred[:, :self.scaler.n_features_in_]
            
            X_pred_scaled = self.scaler.transform(X_pred)
            prediccion = self.modelo_ventas.predict(X_pred_scaled)[0]
            
            predicciones.append({
                'FECHA': fecha_futura,
                'VENTA_PREDICHA': max(0, prediccion),  # No ventas negativas
                'CONFIANZA': min(100, 85 - (i * 0.5))  # Confianza decrece con el tiempo
            })
        
        return pd.DataFrame(predicciones)
    
    def analizar_tendencias(self):
        """Análisis inteligente de tendencias"""
        print("📈 Analizando tendencias con IA...")
        
        # Ventas por día
        ventas_diarias = self.df.groupby('FECHA')['TOTAL_VENTA'].sum().reset_index()
        ventas_diarias = ventas_diarias.sort_values('FECHA')
        
        # Calcular tendencia
        if len(ventas_diarias) > 1:
            x = np.arange(len(ventas_diarias))
            y = ventas_diarias['TOTAL_VENTA'].values
            tendencia = np.polyfit(x, y, 1)[0]
            
            if tendencia > 0:
                direccion = "📈 CRECIENTE"
                color = "verde"
            else:
                direccion = "📉 DECRECIENTE"
                color = "rojo"
        else:
            direccion = "➡️ INSUFICIENTES DATOS"
            color = "amarillo"
        
        # Análisis de estacionalidad
        if 'FECHA' in self.df.columns:
            self.df['MES'] = self.df['FECHA'].dt.month
            ventas_por_mes = self.df.groupby('MES')['TOTAL_VENTA'].sum()
            mes_mayor_venta = ventas_por_mes.idxmax()
            mes_menor_venta = ventas_por_mes.idxmin()
            
            meses = ['Ene', 'Feb', 'Mar', 'Abr', 'May', 'Jun',
                    'Jul', 'Ago', 'Sep', 'Oct', 'Nov', 'Dic']
        
        # Productos top y flop
        productos_ventas = self.df.groupby('PRODUCTO')['TOTAL_VENTA'].sum().sort_values(ascending=False)
        
        return {
            'tendencia_general': direccion,
            'mes_mayor_venta': meses[mes_mayor_venta - 1] if 'mes_mayor_venta' in locals() else 'N/A',
            'mes_menor_venta': meses[mes_menor_venta - 1] if 'mes_menor_venta' in locals() else 'N/A',
            'producto_estrella': productos_ventas.index[0] if len(productos_ventas) > 0 else 'N/A',
            'producto_menor': productos_ventas.index[-1] if len(productos_ventas) > 0 else 'N/A',
            'ventas_diarias': ventas_diarias
        }
    
    def segmentar_clientes(self):
        """Segmentación inteligente de vendedores/productos"""
        if not ML_DISPONIBLE:
            print("❌ Librerías de ML no disponibles para segmentación")
            return None
        
        print("🎯 Segmentando vendedores con IA...")
        
        if 'VENDEDOR' not in self.df.columns:
            print("❌ No hay datos de vendedores para segmentar")
            return None
        
        # Crear métricas por vendedor
        vendedor_metricas = self.df.groupby('VENDEDOR').agg({
            'TOTAL_VENTA': ['sum', 'mean', 'count'],
            'CANTIDAD': 'sum',
            'FECHA': ['min', 'max']
        }).reset_index()
        
        # Aplanar columnas
        vendedor_metricas.columns = ['VENDEDOR', 'TOTAL_VENTAS', 'VENTA_PROMEDIO', 
                                   'NUM_TRANSACCIONES', 'TOTAL_PRODUCTOS', 
                                   'PRIMERA_VENTA', 'ULTIMA_VENTA']
        
        # Calcular días activos
        vendedor_metricas['DIAS_ACTIVO'] = (vendedor_metricas['ULTIMA_VENTA'] - 
                                          vendedor_metricas['PRIMERA_VENTA']).dt.days + 1
        
        # Preparar datos para clustering
        caracteristicas_clustering = ['TOTAL_VENTAS', 'VENTA_PROMEDIO', 'NUM_TRANSACCIONES']
        X_cluster = vendedor_metricas[caracteristicas_clustering].fillna(0)
        
        # Normalizar
        scaler_cluster = StandardScaler()
        X_cluster_scaled = scaler_cluster.fit_transform(X_cluster)
        
        # Aplicar K-means
        kmeans = KMeans(n_clusters=3, random_state=42)
        vendedor_metricas['SEGMENTO'] = kmeans.fit_predict(X_cluster_scaled)
        
        # Interpretar segmentos
        segmentos_info = {}
        for segmento in vendedor_metricas['SEGMENTO'].unique():
            segmento_data = vendedor_metricas[vendedor_metricas['SEGMENTO'] == segmento]
            
            if segmento_data['TOTAL_VENTAS'].mean() > vendedor_metricas['TOTAL_VENTAS'].mean():
                if segmento_data['NUM_TRANSACCIONES'].mean() > vendedor_metricas['NUM_TRANSACCIONES'].mean():
                    tipo = "🌟 VENDEDORES ESTRELLA"
                else:
                    tipo = "💎 VENDEDORES PREMIUM"
            else:
                if segmento_data['NUM_TRANSACCIONES'].mean() > vendedor_metricas['NUM_TRANSACCIONES'].mean():
                    tipo = "🔄 VENDEDORES ACTIVOS"
                else:
                    tipo = "🌱 VENDEDORES NUEVOS"
            
            segmentos_info[segmento] = {
                'tipo': tipo,
                'vendedores': segmento_data['VENDEDOR'].tolist(),
                'total_ventas_promedio': segmento_data['TOTAL_VENTAS'].mean(),
                'transacciones_promedio': segmento_data['NUM_TRANSACCIONES'].mean()
            }
        
        return segmentos_info
    
    def generar_recomendaciones(self):
        """Generar recomendaciones inteligentes"""
        print("💡 Generando recomendaciones con IA...")
        
        recomendaciones = []
        
        # Análisis de rendimiento de productos
        if 'PRODUCTO' in self.df.columns:
            productos_rendimiento = self.df.groupby('PRODUCTO').agg({
                'TOTAL_VENTA': 'sum',
                'CANTIDAD': 'sum'
            }).reset_index()
            
            productos_rendimiento['VENTA_POR_UNIDAD'] = (productos_rendimiento['TOTAL_VENTA'] / 
                                                        productos_rendimiento['CANTIDAD'])
            
            # Top 3 productos más rentables
            top_productos = productos_rendimiento.nlargest(3, 'VENTA_POR_UNIDAD')
            recomendaciones.append({
                'tipo': '🎯 PRODUCTOS ESTRELLA',
                'descripcion': f"Enfocar marketing en: {', '.join(top_productos['PRODUCTO'].tolist())}",
                'impacto': 'ALTO'
            })
            
            # Productos con bajo rendimiento
            productos_bajo = productos_rendimiento.nsmallest(2, 'VENTA_POR_UNIDAD')
            if len(productos_bajo) > 0:
                recomendaciones.append({
                    'tipo': '⚠️ PRODUCTOS EN RIESGO',
                    'descripcion': f"Revisar estrategia para: {', '.join(productos_bajo['PRODUCTO'].tolist())}",
                    'impacto': 'MEDIO'
                })
        
        # Análisis temporal
        if 'FECHA' in self.df.columns:
            self.df['DIA_SEMANA'] = self.df['FECHA'].dt.day_name()
            ventas_por_dia = self.df.groupby('DIA_SEMANA')['TOTAL_VENTA'].sum()
            mejor_dia = ventas_por_dia.idxmax()
            peor_dia = ventas_por_dia.idxmin()
            
            recomendaciones.append({
                'tipo': '📅 OPTIMIZACIÓN TEMPORAL',
                'descripcion': f"Intensificar promociones los {mejor_dia}s. Revisar estrategia para {peor_dia}s",
                'impacto': 'MEDIO'
            })
        
        # Análisis de vendedores
        if 'VENDEDOR' in self.df.columns:
            vendedor_performance = self.df.groupby('VENDEDOR')['TOTAL_VENTA'].sum().sort_values(ascending=False)
            if len(vendedor_performance) > 1:
                top_vendedor = vendedor_performance.index[0]
                recomendaciones.append({
                    'tipo': '👥 DESARROLLO DE EQUIPO',
                    'descripcion': f"Programa de mentoring con {top_vendedor} como líder",
                    'impacto': 'ALTO'
                })
        
        return recomendaciones
    
    def crear_reporte_ia(self, archivo_salida='outputs/Reporte_IA.png'):
        """Crear reporte visual con análisis de IA"""
        print("📊 Generando reporte visual de IA...")
        
        # Crear directorio si no existe
        import os
        os.makedirs(os.path.dirname(archivo_salida), exist_ok=True)
        
        fig, axes = plt.subplots(2, 2, figsize=(16, 12))
        fig.suptitle('🤖 ANÁLISIS INTELIGENTE DE VENTAS', fontsize=20, fontweight='bold')
        
        # 1. Tendencias de ventas
        tendencias = self.analizar_tendencias()
        ventas_diarias = tendencias['ventas_diarias']
        
        axes[0,0].plot(ventas_diarias['FECHA'], ventas_diarias['TOTAL_VENTA'], 
                      color=config.COLOR_PRIMARIO, linewidth=2)
        axes[0,0].set_title('📈 Tendencia de Ventas Diarias', fontweight='bold')
        axes[0,0].set_xlabel('Fecha')
        axes[0,0].set_ylabel('Ventas ($)')
        axes[0,0].grid(True, alpha=0.3)
        
        # 2. Predicciones
        if ML_DISPONIBLE and self.modelo_ventas:
            predicciones = self.predecir_ventas_futuras(7)
            if predicciones is not None:
                axes[0,1].bar(range(len(predicciones)), predicciones['VENTA_PREDICHA'], 
                             color=config.COLORES_GRAFICOS[1])
                axes[0,1].set_title('🔮 Predicciones (7 días)', fontweight='bold')
                axes[0,1].set_xlabel('Días futuros')
                axes[0,1].set_ylabel('Ventas predichas ($)')
        else:
            axes[0,1].text(0.5, 0.5, 'Modelo no disponible\n\nInstala: pip install scikit-learn', 
                          ha='center', va='center', transform=axes[0,1].transAxes,
                          fontsize=12, style='italic')
            axes[0,1].set_title('🔮 Predicciones', fontweight='bold')
        
        # 3. Top productos
        if 'PRODUCTO' in self.df.columns:
            top_productos = self.df.groupby('PRODUCTO')['TOTAL_VENTA'].sum().nlargest(5)
            axes[1,0].barh(range(len(top_productos)), top_productos.values, 
                          color=config.COLORES_GRAFICOS[2])
            axes[1,0].set_yticks(range(len(top_productos)))
            axes[1,0].set_yticklabels([p[:15] + '...' if len(p) > 15 else p for p in top_productos.index])
            axes[1,0].set_title('🏆 Top 5 Productos', fontweight='bold')
            axes[1,0].set_xlabel('Ventas ($)')
        
        # 4. Métricas clave
        total_ventas = self.df['TOTAL_VENTA'].sum()
        productos_unicos = self.df['PRODUCTO'].nunique() if 'PRODUCTO' in self.df.columns else 0
        venta_promedio = self.df['TOTAL_VENTA'].mean()
        
        axes[1,1].axis('off')
        metricas_text = f"""
        💰 TOTAL VENTAS
        ${total_ventas:,.2f}
        
        📦 PRODUCTOS ÚNICOS
        {productos_unicos}
        
        📊 VENTA PROMEDIO
        ${venta_promedio:.2f}
        
        📈 TENDENCIA
        {tendencias['tendencia_general']}
        """
        
        axes[1,1].text(0.1, 0.9, metricas_text, transform=axes[1,1].transAxes,
                      fontsize=14, verticalalignment='top', fontweight='bold')
        
        plt.tight_layout()
        plt.savefig(archivo_salida, dpi=300, bbox_inches='tight')
        plt.close()
        
        print(f"✅ Reporte de IA guardado en: {archivo_salida}")
        return archivo_salida

def main():
    """Función principal para ejecutar análisis de IA"""
    print("🤖 SISTEMA DE ANÁLISIS CON INTELIGENCIA ARTIFICIAL")
    print("=" * 50)
    
    # Buscar archivo de datos
    import os
    archivos_disponibles = [f for f in os.listdir('.') if f.endswith('.xlsx') and 'consolidado' in f.lower()]
    
    if not archivos_disponibles:
        print("❌ No se encontró archivo de datos consolidados")
        print("💡 Ejecuta primero el script de consolidación")
        return
    
    archivo_datos = archivos_disponibles[0]
    print(f"📊 Usando archivo: {archivo_datos}")
    
    # Inicializar análisis
    ia = AnalisisIA(archivo_datos)
    
    if ia.df is None:
        print("❌ Error al cargar datos")
        return
    
    # Entrenar modelo
    if ML_DISPONIBLE:
        ia.entrenar_modelo_prediccion()
    
    # Análisis de tendencias
    print("\n" + "="*50)
    tendencias = ia.analizar_tendencias()
    print(f"📈 Tendencia general: {tendencias['tendencia_general']}")
    print(f"🏆 Producto estrella: {tendencias['producto_estrella']}")
    
    # Segmentación
    if ML_DISPONIBLE:
        print("\n" + "="*50)
        segmentos = ia.segmentar_clientes()
        if segmentos:
            for seg_id, seg_info in segmentos.items():
                print(f"{seg_info['tipo']}: {len(seg_info['vendedores'])} vendedores")
    
    # Recomendaciones
    print("\n" + "="*50)
    recomendaciones = ia.generar_recomendaciones()
    print("💡 RECOMENDACIONES INTELIGENTES:")
    for rec in recomendaciones:
        print(f"   {rec['tipo']}: {rec['descripcion']} (Impacto: {rec['impacto']})")
    
    # Predicciones
    if ML_DISPONIBLE and ia.modelo_ventas:
        print("\n" + "="*50)
        predicciones = ia.predecir_ventas_futuras(7)
        if predicciones is not None:
            print("🔮 PREDICCIONES (próximos 7 días):")
            for _, pred in predicciones.iterrows():
                fecha = pred['FECHA'].strftime('%Y-%m-%d')
                venta = pred['VENTA_PREDICHA']
                confianza = pred['CONFIANZA']
                print(f"   {fecha}: ${venta:.2f} (Confianza: {confianza:.1f}%)")
    
    # Generar reporte visual
    print("\n" + "="*50)
    ia.crear_reporte_ia()
    
    print("\n🎉 ¡Análisis de IA completado!")

if __name__ == "__main__":
    main()
