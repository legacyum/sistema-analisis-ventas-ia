# 🤝 Guía de Contribución

## 🎯 Cómo Contribuir

¡Gracias por tu interés en contribuir al Sistema de Análisis de Ventas con IA! 

### 📋 Antes de Empezar

1. **Fork** del repositorio
2. **Clona** tu fork localmente
3. **Crea una rama** para tu feature/bugfix
4. **Haz tus cambios** siguiendo las convenciones
5. **Testea** tu código
6. **Envía un Pull Request**

### 🛠️ Configuración del Entorno

```bash
# Clonar tu fork
git clone https://github.com/TU_USUARIO/sistema-analisis-ventas.git
cd sistema-analisis-ventas

# Instalar dependencias
pip install -r requirements.txt

# Configurar upstream (repositorio original)
git remote add upstream https://github.com/ORIGINAL_USUARIO/sistema-analisis-ventas.git
```

### 📝 Convenciones de Código

#### Python:
- Usar **PEP 8** para formato
- **Docstrings** en todas las funciones
- **Type hints** cuando sea posible
- **Nombres descriptivos** para variables y funciones

#### Ejemplo:
```python
def analizar_ventas_por_vendedor(df: pd.DataFrame, vendedor: str) -> dict:
    """
    Analiza las ventas de un vendedor específico.
    
    Args:
        df: DataFrame con datos de ventas
        vendedor: Nombre del vendedor a analizar
        
    Returns:
        dict: Métricas del vendedor
    """
    # Código aquí...
```

### 🧪 Testing

Antes de enviar cambios, asegúrate de que:

```bash
# Ejecutar tests básicos
python demo_ia.py  # Genera datos demo
python dashboard_ia.py  # Verifica dashboard IA
python dashboard_streamlit.py  # Verifica Streamlit
```

### 📊 Tipos de Contribuciones

#### 🆕 Nuevas Funcionalidades
- Nuevos algoritmos de IA
- Tipos de gráficos adicionales
- Integraciones con APIs
- Mejoras en dashboards

#### 🐛 Corrección de Bugs
- Errores en cálculos
- Problemas de rendimiento
- Bugs en interfaz de usuario
- Compatibilidad entre versiones

#### 📚 Documentación
- Mejorar README
- Agregar ejemplos
- Traducir documentación
- Crear tutoriales

#### 🎨 Mejoras de UI/UX
- Diseño de dashboards
- Experiencia de usuario
- Responsividad móvil
- Accesibilidad

### 🏷️ Pull Request Guidelines

#### Título del PR:
```
[TIPO] Descripción corta del cambio

Ejemplos:
[FEAT] Agregar predicciones con LSTM
[FIX] Corregir error en carga de archivos Excel
[DOCS] Actualizar guía de instalación
```

#### Descripción del PR:
```markdown
## 🎯 Qué hace este PR
Descripción clara del cambio

## 🧪 Cómo testear
Pasos para probar el cambio

## 📷 Screenshots (si aplica)
Capturas de pantalla de cambios visuales

## ✅ Checklist
- [ ] Código testeado
- [ ] Documentación actualizada
- [ ] Sigue convenciones de código
```

### 🚀 Proceso de Review

1. **Automated checks** - Tests automáticos
2. **Code review** - Revisión por mantenedores
3. **Testing** - Pruebas adicionales si es necesario
4. **Merge** - Integración al proyecto principal

### 🎁 Reconocimientos

Todos los contribuidores serán reconocidos en:
- **README.md** - Lista de contribuidores
- **CHANGELOG.md** - Créditos por versión
- **Commits** - Autoría preservada

### 📞 Contacto

- **Issues**: Para reportar bugs o sugerir features
- **Discussions**: Para preguntas generales
- **Email**: Para temas sensibles

### 🏆 Niveles de Contribución

- **🥉 Contribuidor**: 1+ PR aceptado
- **🥈 Colaborador Regular**: 5+ PRs, ayuda en reviews
- **🥇 Mantenedor**: Acceso completo, toma decisiones

¡Esperamos tus contribuciones! 🚀
