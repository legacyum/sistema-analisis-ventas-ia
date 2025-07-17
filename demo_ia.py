"""
🎯 Demostración de Inteligencia Artificial
Script de demostración para mostrar las capacidades de IA del sistema
"""

import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import matplotlib.pyplot as plt
import os

def crear_datos_demo_ia():
    """Crear datos de demostración optimizados para IA"""
    print("🎯 Creando datos de demostración para IA...")
    
    # Configurar semilla para reproducibilidad
    np.random.seed(42)
    
    # Productos con diferentes características
    productos = [
        {"nombre": "iPhone 15 Pro", "categoria": "Electrónicos", "precio_base": 1299.99, "demanda": "alta"},
        {"nombre": "Samsung Galaxy S24", "categoria": "Electrónicos", "precio_base": 1199.99, "demanda": "alta"},
        {"nombre": "MacBook Pro", "categoria": "Computadoras", "precio_base": 2499.99, "demanda": "media"},
        {"nombre": "Dell XPS 13", "categoria": "Computadoras", "precio_base": 1499.99, "demanda": "media"},
        {"nombre": "iPad Air", "categoria": "Tablets", "precio_base": 699.99, "demanda": "alta"},
        {"nombre": "Surface Pro", "categoria": "Tablets", "precio_base": 1099.99, "demanda": "baja"},
        {"nombre": "AirPods Pro", "categoria": "Accesorios", "precio_base": 299.99, "demanda": "muy_alta"},
        {"nombre": "Magic Mouse", "categoria": "Accesorios", "precio_base": 99.99, "demanda": "baja"},
        {"nombre": "Monitor 4K", "categoria": "Monitores", "precio_base": 599.99, "demanda": "media"},
        {"nombre": "Webcam HD", "categoria": "Accesorios", "precio_base": 149.99, "demanda": "media"}
    ]
    
    # Vendedores con diferentes rendimientos
    vendedores = [
        {"nombre": "Ana García", "rendimiento": "excelente", "especialidad": "Electrónicos"},
        {"nombre": "Carlos López", "rendimiento": "bueno", "especialidad": "Computadoras"},
        {"nombre": "María Rodríguez", "rendimiento": "excelente", "especialidad": "Tablets"},
        {"nombre": "Juan Martínez", "rendimiento": "regular", "especialidad": "Accesorios"},
        {"nombre": "Laura Sánchez", "rendimiento": "bueno", "especialidad": "Monitores"},
        {"nombre": "Pedro González", "rendimiento": "regular", "especialidad": "Electrónicos"}
    ]
    
    # Factores de demanda por nivel
    factores_demanda = {
        "muy_alta": (3, 8),
        "alta": (2, 5),
        "media": (1, 3),
        "baja": (1, 2)
    }
    
    # Factores de rendimiento
    factores_rendimiento = {
        "excelente": 1.3,
        "bueno": 1.1,
        "regular": 0.9
    }
    
    # Generar datos para los últimos 90 días
    fecha_inicio = datetime.now() - timedelta(days=90)
    datos = []
    
    for dia in range(90):
        fecha = fecha_inicio + timedelta(days=dia)
        
        # Factor estacional (más ventas en fines de semana)
        factor_dia = 1.2 if fecha.weekday() >= 5 else 1.0
        
        # Factor mensual (simulando campañas de marketing)
        factor_mes = 1.3 if fecha.day <= 15 else 1.0
        
        # Número base de transacciones por día
        num_transacciones_base = np.random.poisson(12)
        
        for _ in range(num_transacciones_base):
            # Seleccionar producto basado en demanda
            producto = np.random.choice(productos, p=[0.15, 0.12, 0.08, 0.06, 0.13, 0.04, 0.20, 0.03, 0.07, 0.12])
            
            # Seleccionar vendedor (con tendencia a especialidad)
            if np.random.random() < 0.7:  # 70% de probabilidad de especialidad
                vendedores_especialidad = [v for v in vendedores if v["especialidad"] == producto["categoria"]]
                if vendedores_especialidad:
                    vendedor = np.random.choice(vendedores_especialidad)
                else:
                    vendedor = np.random.choice(vendedores)
            else:
                vendedor = np.random.choice(vendedores)
            
            # Calcular cantidad basada en demanda y rendimiento del vendedor
            min_cant, max_cant = factores_demanda[producto["demanda"]]
            cantidad_base = np.random.randint(min_cant, max_cant + 1)
            cantidad = max(1, int(cantidad_base * factores_rendimiento[vendedor["rendimiento"]] * factor_dia))
            
            # Calcular precio con variación
            variacion_precio = np.random.uniform(0.95, 1.05)
            precio_unitario = round(producto["precio_base"] * variacion_precio, 2)
            
            # Calcular total
            total_venta = cantidad * precio_unitario
            
            datos.append({
                "PRODUCTO": producto["nombre"],
                "CATEGORIA": producto["categoria"],
                "VENDEDOR": vendedor["nombre"],
                "CANTIDAD": cantidad,
                "PRECIO_UNITARIO": precio_unitario,
                "TOTAL_VENTA": round(total_venta, 2),
                "FECHA": fecha.strftime("%Y-%m-%d")
            })
    
    # Crear DataFrame y guardar
    df = pd.DataFrame(datos)
    archivo_salida = "ventas_demo_ia.xlsx"
    df.to_excel(archivo_salida, index=False)
    
    print(f"✅ Archivo creado: {archivo_salida}")
    print(f"📊 Total de registros: {len(df)}")
    print(f"📅 Período: {df['FECHA'].min()} a {df['FECHA'].max()}")
    print(f"💰 Total de ventas: ${df['TOTAL_VENTA'].sum():,.2f}")
    
    # Mostrar estadísticas por categoría
    print("\n📈 Estadísticas por categoría:")
    stats_categoria = df.groupby('CATEGORIA').agg({
        'TOTAL_VENTA': 'sum',
        'CANTIDAD': 'sum'
    }).round(2)
    print(stats_categoria)
    
    # Mostrar top vendedores
    print("\n🏆 Top vendedores:")
    top_vendedores = df.groupby('VENDEDOR')['TOTAL_VENTA'].sum().sort_values(ascending=False).head(3)
    for vendedor, ventas in top_vendedores.items():
        print(f"   {vendedor}: ${ventas:,.2f}")
    
    return archivo_salida

def ejecutar_demo_completo():
    """Ejecutar demostración completa del sistema con IA"""
    print("🚀 DEMOSTRACIÓN COMPLETA DEL SISTEMA CON IA")
    print("=" * 60)
    
    # Paso 1: Crear datos de demostración
    archivo_demo = crear_datos_demo_ia()
    
    # Paso 2: Consolidar datos (simular)
    print(f"\n🔄 Consolidando datos desde {archivo_demo}...")
    
    # Paso 3: Mostrar capacidades de IA disponibles
    print("\n🤖 CAPACIDADES DE IA DISPONIBLES:")
    print("   ✅ Predicciones de ventas futuras")
    print("   ✅ Análisis de tendencias automatizado")
    print("   ✅ Segmentación de vendedores")
    print("   ✅ Recomendaciones inteligentes")
    print("   ✅ Dashboard interactivo con IA")
    print("   ✅ Reportes visuales con ML")
    
    # Paso 4: Instrucciones para el usuario
    print("\n📋 PRÓXIMOS PASOS:")
    print("1. Ejecuta: python main.py")
    print("2. Selecciona opción 5: '🧠 Análisis completo con IA'")
    print("3. O selecciona opción 4: '🤖 Ejecutar dashboard con IA'")
    print("4. Explora las predicciones y recomendaciones")
    
    print(f"\n🎉 ¡Demo preparado! Usa el archivo '{archivo_demo}' para las pruebas.")
    
    return archivo_demo

if __name__ == "__main__":
    ejecutar_demo_completo()
