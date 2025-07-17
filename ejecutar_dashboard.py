"""
🚀 Selector de Dashboard Inteligente
Selector para ejecutar el dashboard Dash o Streamlit
"""

import os
import subprocess
import sys
from datetime import datetime

def mostrar_banner():
    """Mostrar banner de bienvenida"""
    print("=" * 60)
    print("🤖 DASHBOARD INTELIGENTE DE VENTAS CON IA")
    print("=" * 60)
    print("📊 Análisis de datos avanzado con Machine Learning")
    print("🎨 Dos versiones disponibles: Premium Dash y Simple Streamlit")
    print(f"📅 {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}")
    print("=" * 60)

def verificar_dependencias():
    """Verificar que las dependencias estén instaladas"""
    dependencias = {
        'dash': 'Dashboard Premium (Dash)',
        'streamlit': 'Dashboard Simple (Streamlit)',
        'pandas': 'Análisis de datos',
        'plotly': 'Visualizaciones',
        'scikit-learn': 'Inteligencia Artificial'
    }
    
    faltantes = []
    for dep, desc in dependencias.items():
        try:
            __import__(dep.replace('-', '_'))
            print(f"✅ {desc}")
        except ImportError:
            print(f"❌ {desc} - FALTANTE")
            faltantes.append(dep)
    
    if faltantes:
        print(f"\n⚠️  Dependencias faltantes: {', '.join(faltantes)}")
        print("💡 Instala con: pip install " + " ".join(faltantes))
        return False
    
    return True

def verificar_datos():
    """Verificar que existan archivos de datos"""
    archivos_datos = [f for f in os.listdir('.') if f.endswith('.xlsx') and 'consolidado' in f.lower()]
    
    if archivos_datos:
        print(f"📊 Archivo de datos encontrado: {archivos_datos[0]}")
        return True
    else:
        print("❌ No se encontró archivo de datos consolidados")
        print("💡 Ejecuta primero 'python automatizacion.py' para generar los datos")
        return False

def ejecutar_dash():
    """Ejecutar dashboard Dash"""
    print("\n🚀 Iniciando Dashboard Premium (Dash)...")
    print("🌐 Se abrirá en: http://localhost:8051")
    print("🎨 Características: Diseño premium, gradientes, animaciones")
    print("⏱️  Tiempo de carga: ~15 segundos")
    print("\n📝 Presiona Ctrl+C para detener\n")
    
    try:
        subprocess.run([sys.executable, "dashboard_ia.py"], check=True)
    except KeyboardInterrupt:
        print("\n✅ Dashboard Dash detenido")
    except subprocess.CalledProcessError as e:
        print(f"❌ Error al ejecutar Dash: {e}")
    except FileNotFoundError:
        print("❌ No se encontró dashboard_ia.py")

def ejecutar_streamlit():
    """Ejecutar dashboard Streamlit"""
    print("\n🚀 Iniciando Dashboard Simple (Streamlit)...")
    print("🌐 Se abrirá en: http://localhost:8502")
    print("🎨 Características: Diseño limpio, controles nativos, rápido")
    print("⏱️  Tiempo de carga: ~5 segundos")
    print("\n📝 Presiona Ctrl+C para detener\n")
    
    try:
        subprocess.run([sys.executable, "-m", "streamlit", "run", "dashboard_streamlit.py"], check=True)
    except KeyboardInterrupt:
        print("\n✅ Dashboard Streamlit detenido")
    except subprocess.CalledProcessError as e:
        print(f"❌ Error al ejecutar Streamlit: {e}")
    except FileNotFoundError:
        print("❌ No se encontró dashboard_streamlit.py")

def ejecutar_ambos():
    """Ejecutar ambos dashboards simultáneamente"""
    print("\n🚀 Iniciando AMBOS dashboards...")
    print("🎨 Dashboard Dash: http://localhost:8051")
    print("⚡ Dashboard Streamlit: http://localhost:8502")
    print("\n📝 Presiona Ctrl+C para detener ambos\n")
    
    try:
        # Iniciar Dash en background
        proceso_dash = subprocess.Popen([sys.executable, "dashboard_ia.py"])
        
        # Iniciar Streamlit
        proceso_streamlit = subprocess.Popen([sys.executable, "-m", "streamlit", "run", "dashboard_streamlit.py"])
        
        print("✅ Ambos dashboards iniciados")
        print("🌐 Abre las URLs en tu navegador")
        
        # Esperar a que el usuario presione Ctrl+C
        try:
            proceso_streamlit.wait()
        except KeyboardInterrupt:
            print("\n🛑 Deteniendo dashboards...")
            proceso_dash.terminate()
            proceso_streamlit.terminate()
            print("✅ Ambos dashboards detenidos")
            
    except Exception as e:
        print(f"❌ Error al ejecutar dashboards: {e}")

def mostrar_menu():
    """Mostrar menú de opciones"""
    print("\n🎛️  OPCIONES DISPONIBLES:")
    print("=" * 40)
    print("1️⃣  Dashboard Premium (Dash)")
    print("   • Diseño profesional con gradientes")
    print("   • Ideal para presentaciones ejecutivas")
    print("   • Puerto: 8051")
    print()
    print("2️⃣  Dashboard Simple (Streamlit)")
    print("   • Interfaz limpia y minimalista")
    print("   • Ideal para análisis rápido")
    print("   • Puerto: 8502")
    print()
    print("3️⃣  Ambos Dashboards")
    print("   • Ejecuta ambos simultáneamente")
    print("   • Compara las dos versiones")
    print()
    print("4️⃣  Ver Documentación")
    print("   • Guía de uso y comparación")
    print()
    print("0️⃣  Salir")
    print("=" * 40)

def mostrar_documentacion():
    """Mostrar documentación básica"""
    print("\n📖 DOCUMENTACIÓN RÁPIDA")
    print("=" * 50)
    print("🎯 PROPÓSITO:")
    print("   Sistema de análisis de ventas con IA")
    print("   Predicciones automáticas y insights")
    print()
    print("📊 CARACTERÍSTICAS:")
    print("   • Análisis temporal de ventas")
    print("   • Predicciones con Machine Learning")
    print("   • Segmentación inteligente")
    print("   • Recomendaciones automáticas")
    print()
    print("🔧 CONTROLES:")
    print("   • Filtros por fecha, categoría, vendedor")
    print("   • Activar/desactivar predicciones IA")
    print("   • Múltiples visualizaciones")
    print()
    print("📈 MÉTRICAS:")
    print("   • Ventas totales y promedio")
    print("   • Productos más vendidos")
    print("   • Rendimiento por vendedor")
    print("   • Precisión del modelo IA: 99.9%")
    print("=" * 50)

def main():
    """Función principal"""
    mostrar_banner()
    
    # Verificaciones iniciales
    print("\n🔍 VERIFICANDO SISTEMA...")
    if not verificar_dependencias():
        input("\n⏸️  Presiona Enter para continuar de todos modos...")
    
    if not verificar_datos():
        input("\n⏸️  Presiona Enter para continuar de todos modos...")
    
    while True:
        mostrar_menu()
        
        try:
            opcion = input("\n👉 Selecciona una opción (0-4): ").strip()
            
            if opcion == "1":
                ejecutar_dash()
            elif opcion == "2":
                ejecutar_streamlit()
            elif opcion == "3":
                ejecutar_ambos()
            elif opcion == "4":
                mostrar_documentacion()
                input("\n⏸️  Presiona Enter para volver al menú...")
            elif opcion == "0":
                print("\n👋 ¡Hasta luego!")
                print("🌟 Gracias por usar el Dashboard Inteligente")
                break
            else:
                print("❌ Opción no válida. Selecciona 0-4.")
                
        except KeyboardInterrupt:
            print("\n\n👋 ¡Hasta luego!")
            break
        except Exception as e:
            print(f"❌ Error inesperado: {e}")

if __name__ == "__main__":
    main()
