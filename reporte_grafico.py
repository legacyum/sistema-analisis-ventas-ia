import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime
import os
import numpy as np

def generar_reporte_grafico(archivo_excel='Reporte_Consolidado.xlsx'):
    """
    Genera un reporte completo con gráficos estáticos
    """
    
    # Configurar estilo de matplotlib
    plt.style.use('seaborn-v0_8')
    sns.set_palette("husl")
    
    try:
        # Cargar datos
        if os.path.exists(archivo_excel):
            df = pd.read_excel(archivo_excel)
            print(f"✅ Datos cargados: {len(df)} registros")
        else:
            print(f"❌ No se encontró el archivo {archivo_excel}")
            return
        
        # Procesar fechas
        if 'FECHA' in df.columns:
            df['FECHA'] = pd.to_datetime(df['FECHA'], errors='coerce')
        
        # Crear figura con subplots
        fig = plt.figure(figsize=(20, 15))
        fig.suptitle('📊 REPORTE COMPLETO DE VENTAS', fontsize=20, fontweight='bold', y=0.98)
        
        # 1. Gráfico de ventas en el tiempo
        if 'FECHA' in df.columns and 'TOTAL_VENTA' in df.columns:
            plt.subplot(3, 3, 1)
            ventas_diarias = df.groupby('FECHA')['TOTAL_VENTA'].sum()
            plt.plot(ventas_diarias.index, ventas_diarias.values, marker='o', linewidth=2)
            plt.title('📈 Evolución de Ventas Diarias', fontsize=14, fontweight='bold')
            plt.xlabel('Fecha')
            plt.ylabel('Ventas ($)')
            plt.xticks(rotation=45)
            plt.grid(True, alpha=0.3)
        
        # 2. Top 10 productos más vendidos
        if 'PRODUCTO' in df.columns and 'TOTAL_VENTA' in df.columns:
            plt.subplot(3, 3, 2)
            top_productos = df.groupby('PRODUCTO')['TOTAL_VENTA'].sum().nlargest(10)
            bars = plt.barh(range(len(top_productos)), top_productos.values)
            plt.yticks(range(len(top_productos)), top_productos.index, fontsize=10)
            plt.title('🏆 Top 10 Productos por Ventas', fontsize=14, fontweight='bold')
            plt.xlabel('Ventas ($)')
            
            # Añadir valores en las barras
            for i, bar in enumerate(bars):
                width = bar.get_width()
                plt.text(width + max(top_productos.values)*0.01, bar.get_y() + bar.get_height()/2, 
                        f'${width:,.0f}', ha='left', va='center', fontsize=9)
        
        # 3. Distribución por categorías
        if 'CATEGORIA' in df.columns and 'TOTAL_VENTA' in df.columns:
            plt.subplot(3, 3, 3)
            ventas_categoria = df.groupby('CATEGORIA')['TOTAL_VENTA'].sum()
            colors = plt.cm.Set3(np.linspace(0, 1, len(ventas_categoria)))
            wedges, texts, autotexts = plt.pie(ventas_categoria.values, labels=ventas_categoria.index, 
                                              autopct='%1.1f%%', colors=colors, startangle=90)
            plt.title('🎯 Distribución por Categorías', fontsize=14, fontweight='bold')
        
        # 4. Ventas por vendedor
        if 'VENDEDOR' in df.columns and 'TOTAL_VENTA' in df.columns:
            plt.subplot(3, 3, 4)
            ventas_vendedor = df.groupby('VENDEDOR')['TOTAL_VENTA'].sum().sort_values(ascending=True)
            bars = plt.barh(ventas_vendedor.index, ventas_vendedor.values)
            plt.title('👥 Ventas por Vendedor', fontsize=14, fontweight='bold')
            plt.xlabel('Ventas ($)')
            
            # Colorear barras según el valor
            for i, bar in enumerate(bars):
                bar.set_color(plt.cm.viridis(i / len(bars)))
        
        # 5. Cantidad vs Precio Unitario
        if 'CANTIDAD' in df.columns and 'PRECIO_UNITARIO' in df.columns:
            plt.subplot(3, 3, 5)
            scatter = plt.scatter(df['CANTIDAD'], df['PRECIO_UNITARIO'], 
                                c=df['TOTAL_VENTA'] if 'TOTAL_VENTA' in df.columns else 'blue',
                                alpha=0.6, s=50, cmap='viridis')
            plt.xlabel('Cantidad')
            plt.ylabel('Precio Unitario ($)')
            plt.title('💰 Cantidad vs Precio Unitario', fontsize=14, fontweight='bold')
            if 'TOTAL_VENTA' in df.columns:
                plt.colorbar(scatter, label='Total Venta ($)')
        
        # 6. Histograma de ventas
        if 'TOTAL_VENTA' in df.columns:
            plt.subplot(3, 3, 6)
            plt.hist(df['TOTAL_VENTA'], bins=20, edgecolor='black', alpha=0.7)
            plt.xlabel('Total Venta ($)')
            plt.ylabel('Frecuencia')
            plt.title('📊 Distribución de Ventas', fontsize=14, fontweight='bold')
            plt.axvline(df['TOTAL_VENTA'].mean(), color='red', linestyle='--', 
                       label=f'Promedio: ${df["TOTAL_VENTA"].mean():,.0f}')
            plt.legend()
        
        # 7. Mapa de calor de ventas por vendedor y categoría
        if all(col in df.columns for col in ['VENDEDOR', 'CATEGORIA', 'TOTAL_VENTA']):
            plt.subplot(3, 3, 7)
            tabla_cruzada = df.pivot_table(values='TOTAL_VENTA', index='VENDEDOR', 
                                         columns='CATEGORIA', aggfunc='sum', fill_value=0)
            sns.heatmap(tabla_cruzada, annot=True, fmt='.0f', cmap='YlOrRd')
            plt.title('🔥 Mapa de Calor: Vendedor x Categoría', fontsize=14, fontweight='bold')
            plt.xticks(rotation=45)
            plt.yticks(rotation=0)
        
        # 8. Tendencia de ventas (media móvil)
        if 'FECHA' in df.columns and 'TOTAL_VENTA' in df.columns:
            plt.subplot(3, 3, 8)
            ventas_diarias = df.groupby('FECHA')['TOTAL_VENTA'].sum().sort_index()
            media_movil = ventas_diarias.rolling(window=7, center=True).mean()
            
            plt.plot(ventas_diarias.index, ventas_diarias.values, alpha=0.3, label='Ventas Diarias')
            plt.plot(media_movil.index, media_movil.values, linewidth=3, label='Media Móvil (7 días)')
            plt.title('📈 Tendencia de Ventas', fontsize=14, fontweight='bold')
            plt.xlabel('Fecha')
            plt.ylabel('Ventas ($)')
            plt.legend()
            plt.xticks(rotation=45)
        
        # 9. Métricas resumen
        plt.subplot(3, 3, 9)
        plt.axis('off')
        
        # Calcular métricas
        total_ventas = df['TOTAL_VENTA'].sum() if 'TOTAL_VENTA' in df.columns else 0
        total_productos = df['CANTIDAD'].sum() if 'CANTIDAD' in df.columns else 0
        promedio_venta = df['TOTAL_VENTA'].mean() if 'TOTAL_VENTA' in df.columns else 0
        num_productos_unicos = df['PRODUCTO'].nunique() if 'PRODUCTO' in df.columns else 0
        
        metricas_text = f"""
        📊 MÉTRICAS CLAVE
        
        💰 Total de Ventas: ${total_ventas:,.0f}
        📦 Productos Vendidos: {total_productos:,}
        🛍️ Venta Promedio: ${promedio_venta:,.0f}
        🏷️ Productos Únicos: {num_productos_unicos}
        📅 Período: {df['FECHA'].min().strftime('%d/%m/%Y') if 'FECHA' in df.columns and not df['FECHA'].isna().all() else 'N/A'} - {df['FECHA'].max().strftime('%d/%m/%Y') if 'FECHA' in df.columns and not df['FECHA'].isna().all() else 'N/A'}
        
        🎯 Mejor Vendedor: {df.groupby('VENDEDOR')['TOTAL_VENTA'].sum().idxmax() if 'VENDEDOR' in df.columns and 'TOTAL_VENTA' in df.columns else 'N/A'}
        🏆 Mejor Producto: {df.groupby('PRODUCTO')['TOTAL_VENTA'].sum().idxmax() if 'PRODUCTO' in df.columns and 'TOTAL_VENTA' in df.columns else 'N/A'}
        """
        
        plt.text(0.1, 0.9, metricas_text, transform=plt.gca().transAxes, fontsize=12,
                verticalalignment='top', bbox=dict(boxstyle='round', facecolor='lightblue', alpha=0.8))
        
        # Ajustar layout y guardar
        plt.tight_layout()
        plt.subplots_adjust(top=0.95)
        
        # Guardar el reporte
        nombre_archivo = f'Reporte_Grafico_Ventas_{datetime.now().strftime("%Y%m%d_%H%M%S")}.png'
        plt.savefig(nombre_archivo, dpi=300, bbox_inches='tight')
        print(f"✅ Reporte gráfico guardado: {nombre_archivo}")
        
        # Mostrar el gráfico
        plt.show()
        
        return nombre_archivo
        
    except Exception as e:
        print(f"❌ Error al generar reporte: {e}")
        return None

if __name__ == "__main__":
    print("🎨 Generando reporte gráfico completo...")
    generar_reporte_grafico()
