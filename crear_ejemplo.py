import pandas as pd

# Crear datos de ejemplo con nombres más largos para probar el ajuste automático
datos_ejemplo = {
    'PRODUCTO': ['Smartphone Samsung Galaxy Ultra', 'Laptop Dell Inspiron 15 Pulgadas', 'Auriculares Bluetooth Sony WH-1000XM4'],
    'CANTIDAD': [10, 5, 8],
    'PRECIO_UNITARIO': [1299.99, 1899.50, 349.99],
    'FECHA': ['2025-01-01', '2025-01-02', '2025-01-03'],
    'CATEGORIA': ['Electrónicos', 'Computadoras', 'Accesorios'],
    'VENDEDOR': ['María González', 'Carlos Rodríguez', 'Ana Martínez']
}

df_ejemplo = pd.DataFrame(datos_ejemplo)

# Guardar archivo de ejemplo con ExcelWriter y columnas ajustadas
with pd.ExcelWriter('ventas_ejemplo.xlsx', engine='openpyxl') as writer:
    df_ejemplo.to_excel(writer, index=False, sheet_name='Ventas')
    
    # Ajustar automáticamente las columnas
    worksheet = writer.sheets['Ventas']
    for column in worksheet.columns:
        max_length = 0
        column_letter = column[0].column_letter
        
        for cell in column:
            try:
                if len(str(cell.value)) > max_length:
                    max_length = len(str(cell.value))
            except:
                pass
        
        adjusted_width = min(max_length + 2, 50)
        worksheet.column_dimensions[column_letter].width = adjusted_width

print(f'Archivo de ejemplo creado con columnas ajustadas: ventas_ejemplo.xlsx')
