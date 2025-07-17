# 🏷️ Sistema de Etiquetas de Versión

## 📋 Convención de Versionado (Semantic Versioning)

Usamos el formato: `MAJOR.MINOR.PATCH`

- **MAJOR**: Cambios incompatibles de API
- **MINOR**: Nueva funcionalidad compatible 
- **PATCH**: Correcciones de bugs compatibles

## 🎯 Convención de Commits

### Tipos de commits:
- `feat:` ✨ Nueva funcionalidad
- `fix:` 🐛 Corrección de bugs
- `docs:` 📚 Documentación
- `style:` 🎨 Cambios de formato (no código)
- `refactor:` ♻️ Refactorización de código
- `test:` 🧪 Agregar o modificar tests
- `chore:` 🔧 Mantenimiento

### Ejemplos:
```bash
git commit -m "feat: ✨ agregar predicciones con IA"
git commit -m "fix: 🐛 corregir error en carga de Excel"
git commit -m "docs: 📚 actualizar README con nuevas funciones"
```

## 🏷️ Etiquetas de Versión

### Crear nueva versión:
```bash
# Versión mayor (cambios grandes)
git tag -a v2.0.0 -m "🚀 Sistema completo con IA"

# Versión menor (nuevas funciones)
git tag -a v2.1.0 -m "✨ Nuevo dashboard Streamlit"

# Parche (correcciones)
git tag -a v2.1.1 -m "🐛 Corrección en filtros"
```

### Ver versiones:
```bash
git tag -l
git show v2.0.0
```

## 🌟 Flujo de Trabajo Recomendado

### 1. Desarrollo de nuevas funciones:
```bash
git checkout -b feature/nueva-funcion
# ... hacer cambios ...
git add .
git commit -m "feat: ✨ descripción de la nueva función"
git checkout master
git merge feature/nueva-funcion
```

### 2. Corrección de bugs:
```bash
git checkout -b hotfix/corregir-bug
# ... hacer correcciones ...
git add .
git commit -m "fix: 🐛 descripción del bug corregido"
git checkout master
git merge hotfix/corregir-bug
```

### 3. Preparar release:
```bash
git add .
git commit -m "chore: 🔧 preparar release v2.1.0"
git tag -a v2.1.0 -m "🚀 Release v2.1.0"
```

## 📊 Historial de Versiones

- **v2.0.0** - Sistema completo con IA y múltiples dashboards
- **v1.0.0** - Sistema básico de consolidación Excel
