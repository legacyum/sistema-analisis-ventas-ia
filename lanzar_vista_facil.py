#!/usr/bin/env python3
"""
🎯 LANZADOR VISTA FÁCIL
======================

Lanzador directo para la Vista Fácil del Sistema de Análisis de Ventas.
Este archivo permite acceder directamente a la interfaz simplificada.

Uso:
    python lanzar_vista_facil.py

El lanzador:
- Verifica dependencias automáticamente
- Instala paquetes faltantes si es necesario
- Abre la Vista Fácil en el navegador
- Proporciona instrucciones claras

Autor: GitHub Copilot
Fecha: Julio 2025
"""

import sys
import subprocess
import os
import webbrowser
import time
import threading

def verificar_e_instalar_dependencias():
    """Verificar e instalar dependencias necesarias"""
    dependencias = [
        'dash',
        'dash-bootstrap-components', 
        'plotly',
        'pandas',
        'openpyxl'
    ]
    
    print("🔍 Verificando dependencias...")
    
    faltantes = []
    for dep in dependencias:
        try:
            __import__(dep.replace('-', '_'))
            print(f"  ✅ {dep}")
        except ImportError:
            print(f"  ❌ {dep} - Faltante")
            faltantes.append(dep)
    
    if faltantes:
        print(f"\n📦 Instalando dependencias faltantes: {', '.join(faltantes)}")
        try:
            subprocess.check_call([
                sys.executable, '-m', 'pip', 'install', '--user'
            ] + faltantes)
            print("✅ Dependencias instaladas correctamente")
        except subprocess.CalledProcessError as e:
            print(f"❌ Error instalando dependencias: {e}")
            return False
    
    return True

def mostrar_banner():
    """Mostrar banner de bienvenida"""
    banner = """
╔══════════════════════════════════════════════════════════════════╗
║                    🎯 VISTA FÁCIL                                ║
║            Sistema de Análisis de Ventas Simplificado           ║
╚══════════════════════════════════════════════════════════════════╝

🌟 Características:
   • Interfaz web moderna y fácil de usar
   • Un clic para generar datos de demostración  
   • Acceso directo a todos los dashboards
   • Estado visual del sistema en tiempo real
   • Configuración automática

🚀 Perfecto para:
   • Usuarios nuevos que quieren probar el sistema
   • Acceso rápido sin menús complejos
   • Presentaciones y demostraciones
   • Usuarios que prefieren interfaces web
"""
    print(banner)

def verificar_archivo_vista_facil():
    """Verificar que existe el archivo vista_facil.py"""
    if not os.path.exists('vista_facil.py'):
        print("❌ Error: No se encontró vista_facil.py")
        print("💡 Asegúrate de ejecutar este script desde el directorio del proyecto")
        return False
    return True

def abrir_navegador_automatico(puerto=8053, delay=3):
    """Abrir navegador automáticamente después de un delay"""
    def abrir():
        time.sleep(delay)
        url = f"http://localhost:{puerto}"
        print(f"🌐 Abriendo navegador en: {url}")
        try:
            webbrowser.open(url)
        except Exception as e:
            print(f"⚠️  No se pudo abrir el navegador automáticamente: {e}")
            print(f"   Abre manualmente: {url}")
    
    thread = threading.Thread(target=abrir)
    thread.daemon = True
    thread.start()

def main():
    """Función principal del lanzador"""
    mostrar_banner()
    
    print("🔧 PREPARANDO VISTA FÁCIL...")
    print("=" * 50)
    
    # Verificar archivo
    if not verificar_archivo_vista_facil():
        input("\n⏸️  Presiona Enter para salir...")
        return
    
    # Verificar e instalar dependencias
    if not verificar_e_instalar_dependencias():
        print("\n❌ No se pudieron instalar las dependencias necesarias")
        input("⏸️  Presiona Enter para salir...")
        return
    
    print("\n✅ Sistema verificado correctamente")
    print("🚀 Iniciando Vista Fácil...")
    print("=" * 50)
    
    # Configurar apertura automática del navegador
    abrir_navegador_automatico()
    
    try:
        # Ejecutar Vista Fácil
        from vista_facil import VistaFacil
        vista = VistaFacil()
        
        print("\n🎯 VISTA FÁCIL ACTIVA")
        print("=" * 30)
        print("🌐 URL: http://localhost:8053")
        print("🔄 Estado: Ejecutándose")
        print("⚡ Modo: Lanzador automático")
        print("💡 Presiona Ctrl+C para detener")
        print("=" * 30)
        
        vista.ejecutar()
        
    except KeyboardInterrupt:
        print("\n\n✅ Vista Fácil detenida por el usuario")
    except ImportError as e:
        print(f"\n❌ Error importando Vista Fácil: {e}")
        print("💡 Verifica que vista_facil.py esté en el directorio actual")
    except Exception as e:
        print(f"\n❌ Error inesperado: {e}")
    
    print("\n👋 ¡Gracias por usar Vista Fácil!")

if __name__ == "__main__":
    main()