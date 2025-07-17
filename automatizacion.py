import pandas as pd
import os # Biblioteca para manejar archivos y carpetas
import sys # Para manejo de errores del sistema

def ajustar_columnas_excel(worksheet):
    """
    Función para ajustar automáticamente el ancho de las columnas en Excel
    """
    for column in worksheet.columns:
        max_length = 0
        column_letter = column[0].column_letter
        
        for cell in column:
            try:
                if len(str(cell.value)) > max_length:
                    max_length = len(str(cell.value))
            except:
                pass
        
        # Agregar padding y establecer ancho máximo para evitar columnas muy anchas
        adjusted_width = min(max_length + 2, 50)
        worksheet.column_dimensions[column_letter].width = adjusted_width

# --- CONFIGURACIÓN ---
# Ruta de la carpeta donde están tus archivos de Excel (carpeta actual por defecto)
carpeta_ventas = os.path.dirname(os.path.abspath(__file__))  # Carpeta del script actual
archivo_salida = 'Reporte_Consolidado.xlsx'

# --- LÓGICA DEL SCRIPT ---
# 1. Verificar que la carpeta existe
if not os.path.exists(carpeta_ventas):
    print(f"Error: La carpeta '{carpeta_ventas}' no existe.")
    sys.exit(1)

# 2. Crear una lista vacía para guardar los datos de cada archivo
lista_de_datos = []

# 3. Buscar archivos de Excel en la carpeta
archivos_excel = [archivo for archivo in os.listdir(carpeta_ventas) if archivo.endswith(('.xlsx', '.xls'))]

if not archivos_excel:
    print(f"No se encontraron archivos de Excel en la carpeta '{carpeta_ventas}'")
    print("Asegúrate de que los archivos tengan extensión .xlsx o .xls")
    sys.exit(1)

# 4. Recorrer cada archivo en la carpeta especificada
print(f"Se encontraron {len(archivos_excel)} archivos de Excel")
print("Leyendo archivos...")

for archivo in archivos_excel:
    ruta_completa = os.path.join(carpeta_ventas, archivo)
    print(f" > Procesando {archivo}...")
    
    try:
        # Leer el archivo de Excel y añadir sus datos a la lista
        df = pd.read_excel(ruta_completa)
        if not df.empty:
            lista_de_datos.append(df)
        else:
            print(f"   Advertencia: El archivo {archivo} está vacío")
    except Exception as e:
        print(f"   Error al leer {archivo}: {e}")
        continue

# 5. Combinar todos los datos en un único DataFrame
if not lista_de_datos:
    print("Error: No se pudo leer ningún archivo válido.")
    sys.exit(1)

print("Consolidando información...")
df_consolidado = pd.concat(lista_de_datos, ignore_index=True)

# 6. (Opcional) Realizar cálculos. Por ejemplo, calcular el total de la venta
if 'PRECIO_UNITARIO' in df_consolidado.columns and 'CANTIDAD' in df_consolidado.columns:
    df_consolidado['TOTAL_VENTA'] = df_consolidado['PRECIO_UNITARIO'] * df_consolidado['CANTIDAD']
    print("Se calculó la columna TOTAL_VENTA")
else:
    print("Advertencia: No se encontraron las columnas PRECIO_UNITARIO y CANTIDAD para calcular el total")

# 7. Guardar el resultado en un nuevo archivo de Excel con columnas ajustadas
try:
    ruta_salida = os.path.join(carpeta_ventas, archivo_salida)
    
    # Usar ExcelWriter para tener más control sobre el formato
    with pd.ExcelWriter(ruta_salida, engine='openpyxl') as writer:
        # Escribir los datos
        df_consolidado.to_excel(writer, index=False, sheet_name='Datos Consolidados')
        
        # Obtener el objeto worksheet y ajustar las columnas
        worksheet = writer.sheets['Datos Consolidados']
        ajustar_columnas_excel(worksheet)
    
    print(f"\n¡Proceso finalizado! El reporte ha sido guardado en '{ruta_salida}'")
    print(f"Total de registros consolidados: {len(df_consolidado)}")
    print("✅ Las columnas se han ajustado automáticamente")
    
    # Preguntar si desea ejecutar el dashboard
    print("\n" + "="*50)
    respuesta = input("¿Deseas ejecutar el dashboard interactivo? (s/n): ").lower()
    if respuesta in ['s', 'si', 'sí', 'y', 'yes']:
        print("🚀 Iniciando dashboard...")
        try:
            import subprocess
            import sys
            subprocess.Popen([sys.executable, 'dashboard.py'], cwd=carpeta_ventas)
            print("✅ Dashboard iniciado en segundo plano")
            print("📱 Abre tu navegador en: http://localhost:8050")
        except Exception as e:
            print(f"❌ Error al iniciar dashboard: {e}")
            print("💡 Puedes ejecutarlo manualmente con: python dashboard.py")
    
except Exception as e:
    print(f"Error al guardar el archivo: {e}")
    sys.exit(1)