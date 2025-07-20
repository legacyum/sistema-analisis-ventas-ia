#!/usr/bin/env python3
"""
🚀 SISTEMA COMPLETO DE ANÁLISIS DE VENTAS
=========================================

Este script principal coordina todo el proceso de análisis:
1. Consolidación de datos de Excel
2. Generación de reportes gráficos
3. Dashboard interactivo

Autor: GitHub Copilot
Fecha: Julio 2025
"""

import os
import sys
import subprocess
from datetime import datetime

def mostrar_banner():
    """Mostrar banner del sistema"""
    banner = """
    ╔═══════════════════════════════════════════════════════════════╗
    ║                🚀 SISTEMA DE ANÁLISIS DE VENTAS 🚀             ║
    ║                                                               ║
    ║  📊 Consolidación automática de archivos Excel                ║
    ║  📈 Reportes gráficos detallados                             ║
    ║  🌐 Dashboard interactivo en tiempo real                     ║
    ║  📋 Tablas dinámicas y filtros avanzados                     ║
    ╚═══════════════════════════════════════════════════════════════╝
    """
    print(banner)
    print(f"⏰ Fecha y hora: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}")
    print("=" * 67)

def mostrar_menu():
    """Mostrar menú de opciones"""
    menu = """
    🎯 ¿Qué deseas hacer?
    
    1. 📊 Consolidar archivos Excel y generar reporte
    2. 📈 Generar reporte gráfico (estático)
    3. 🌐 Ejecutar dashboard interactivo
    4. 🤖 Ejecutar dashboard con IA
    5. 🧠 Análisis completo con IA
    6. 📝 Crear datos de ejemplo
    7. 🎯 Demo completo con IA
    8. 🚀 Proceso completo (1 + 2 + 3)
    9. 🔥 VISTA FÁCIL - Interfaz simplificada
    10. ❌ Salir
    """
    print(menu)

def ejecutar_script(script_name, descripcion):
    """Ejecutar un script Python"""
    print(f"\n🔄 {descripcion}...")
    try:
        result = subprocess.run([sys.executable, script_name], 
                              capture_output=True, text=True, cwd=os.getcwd())
        
        if result.returncode == 0:
            print(f"✅ {descripcion} completado exitosamente")
            if result.stdout:
                print("📄 Salida:", result.stdout)
            return True
        else:
            print(f"❌ Error en {descripcion}")
            if result.stderr:
                print("🚨 Error:", result.stderr)
            return False
    except FileNotFoundError:
        print(f"❌ No se encontró el archivo {script_name}")
        return False
    except Exception as e:
        print(f"❌ Error inesperado: {e}")
        return False

def ejecutar_dashboard():
    """Ejecutar dashboard en segundo plano"""
    print("\n🚀 Iniciando dashboard interactivo...")
    try:
        # Ejecutar dashboard en segundo plano
        process = subprocess.Popen([sys.executable, 'dashboard.py'], 
                                 cwd=os.getcwd())
        print("✅ Dashboard iniciado exitosamente")
        print("📱 Abre tu navegador en: http://localhost:8050")
        print("💡 Presiona Ctrl+C para detener el dashboard")
        
        # Esperar a que el usuario presione Ctrl+C
        try:
            process.wait()
        except KeyboardInterrupt:
            print("\n🛑 Deteniendo dashboard...")
            process.terminate()
            process.wait()
            print("✅ Dashboard detenido")
            
    except FileNotFoundError:
        print("❌ No se encontró el archivo dashboard.py")
    except Exception as e:
        print(f"❌ Error al iniciar dashboard: {e}")

def ejecutar_dashboard_ia():
    """Ejecutar dashboard con IA en segundo plano"""
    print("\n🤖 Iniciando dashboard con IA...")
    try:
        # Ejecutar dashboard IA en segundo plano
        process = subprocess.Popen([sys.executable, 'dashboard_ia.py'], 
                                 cwd=os.getcwd())
        print("✅ Dashboard IA iniciado exitosamente")
        print("🧠 Abre tu navegador en: http://localhost:8051")
        print("💡 Presiona Ctrl+C para detener el dashboard")
        
        # Esperar a que el usuario presione Ctrl+C
        try:
            process.wait()
        except KeyboardInterrupt:
            print("\n🛑 Deteniendo dashboard IA...")
            process.terminate()
            process.wait()
            print("✅ Dashboard IA detenido")
            
    except FileNotFoundError:
        print("❌ No se encontró el archivo dashboard_ia.py")
    except Exception as e:
        print(f"❌ Error al iniciar dashboard IA: {e}")

def ejecutar_analisis_ia():
    """Ejecutar análisis completo con IA"""
    print("\n🧠 Ejecutando análisis con IA...")
    ejecutar_script('analisis_ia.py', 'Análisis inteligente con IA')

def crear_datos_ejemplo():
    """Crear datos de ejemplo para pruebas"""
    print("\n📝 Creando datos de ejemplo...")
    ejecutar_script('crear_ejemplo.py', 'Creación de datos de ejemplo')

def ejecutar_demo_ia():
    """Ejecutar demostración completa con IA"""
    print("\n🎯 Ejecutando demostración completa con IA...")
    ejecutar_script('demo_ia.py', 'Demostración completa con IA')

def ejecutar_vista_facil():
    """Ejecutar Vista Fácil en segundo plano"""
    print("\n🎯 Iniciando Vista Fácil...")
    try:
        # Ejecutar Vista Fácil en segundo plano
        process = subprocess.Popen([sys.executable, 'vista_facil.py'], 
                                 cwd=os.getcwd())
        print("✅ Vista Fácil iniciada exitosamente")
        print("🌐 Abre tu navegador en: http://localhost:8053")
        print("💡 Presiona Ctrl+C para detener la Vista Fácil")
        
        # Esperar a que el usuario presione Ctrl+C
        try:
            process.wait()
        except KeyboardInterrupt:
            print("\n🛑 Deteniendo Vista Fácil...")
            process.terminate()
            process.wait()
            print("✅ Vista Fácil detenida")
            
    except FileNotFoundError:
        print("❌ No se encontró el archivo vista_facil.py")
    except Exception as e:
        print(f"❌ Error al iniciar Vista Fácil: {e}")

def verificar_archivos():
    """Verificar que todos los archivos necesarios existen"""
    archivos_necesarios = [
        'automatizacion.py',
        'dashboard.py', 
        'reporte_grafico.py',
        'dashboard_ia.py',
        'analisis_ia.py',
        'crear_ejemplo.py',
        'vista_facil.py'
    ]
    
    archivos_faltantes = []
    for archivo in archivos_necesarios:
        if not os.path.exists(archivo):
            archivos_faltantes.append(archivo)
    
    if archivos_faltantes:
        print("❌ Faltan los siguientes archivos:")
        for archivo in archivos_faltantes:
            print(f"   - {archivo}")
        return False
    
    return True

def proceso_completo():
    """Ejecutar el proceso completo"""
    print("\n🚀 INICIANDO PROCESO COMPLETO")
    print("=" * 50)
    
    # Paso 1: Consolidar datos
    if ejecutar_script('automatizacion.py', 'Consolidación de archivos Excel'):
        print("✅ Paso 1 completado: Datos consolidados")
    else:
        print("❌ Error en consolidación de datos")
        return False
    
    # Paso 2: Generar reporte gráfico
    if ejecutar_script('reporte_grafico.py', 'Generación de reporte gráfico'):
        print("✅ Paso 2 completado: Reporte gráfico generado")
    else:
        print("⚠️ Advertencia: Error en reporte gráfico, pero continuando...")
    
    # Paso 3: Preguntar por dashboard
    print("\n" + "="*50)
    respuesta = input("¿Deseas ejecutar el dashboard interactivo? (s/n): ").lower()
    if respuesta in ['s', 'si', 'sí', 'y', 'yes']:
        ejecutar_dashboard()
    
    print("\n🎉 ¡PROCESO COMPLETO FINALIZADO!")
    return True

def main():
    """Función principal"""
    mostrar_banner()
    
    # Verificar archivos
    if not verificar_archivos():
        print("\n❌ No se pueden ejecutar todas las funciones sin los archivos necesarios")
        print("💡 Asegúrate de tener todos los scripts en el directorio actual")
        return
    
    while True:
        mostrar_menu()
        
        try:
            opcion = input("👉 Selecciona una opción (1-10): ").strip()
            
            if opcion == '1':
                ejecutar_script('automatizacion.py', 'Consolidación de archivos Excel')
                
            elif opcion == '2':
                ejecutar_script('reporte_grafico.py', 'Generación de reporte gráfico')
                
            elif opcion == '3':
                ejecutar_dashboard()
                
            elif opcion == '4':
                ejecutar_dashboard_ia()
                
            elif opcion == '5':
                ejecutar_analisis_ia()
                
            elif opcion == '6':
                crear_datos_ejemplo()
                
            elif opcion == '7':
                ejecutar_demo_ia()
                
            elif opcion == '8':
                proceso_completo()
                
            elif opcion == '9':
                ejecutar_vista_facil()
                
            elif opcion == '10':
                print("\n👋 ¡Hasta luego!")
                break
                
            else:
                print("❌ Opción no válida. Por favor, selecciona 1-10.")
            
            # Pausa antes de mostrar el menú nuevamente
            input("\n⏸️  Presiona Enter para continuar...")
            print("\n" + "="*67)
            
        except KeyboardInterrupt:
            print("\n\n👋 ¡Hasta luego!")
            break
        except Exception as e:
            print(f"\n❌ Error inesperado: {e}")
            input("⏸️  Presiona Enter para continuar...")

if __name__ == "__main__":
    main()
