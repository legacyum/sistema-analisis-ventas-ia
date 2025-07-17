# 🚀 Configuración para Repositorio Remoto

## 📋 Comandos para Subir a GitHub

### 1. Crear repositorio en GitHub
Ve a https://github.com/new y crea un repositorio llamado: `sistema-analisis-ventas-ia`

### 2. Conectar repositorio local con GitHub
```bash
# Agregar repositorio remoto
git remote add origin https://github.com/legacyum/sistema-analisis-ventas-ia.git

# Verificar conexión
git remote -v

# Subir código por primera vez
git push -u origin master

# Subir tags de versión
git push origin --tags
```

### 3. Comandos útiles para el futuro
```bash
# Subir cambios
git add .
git commit -m "feat: ✨ nueva funcionalidad"
git push

# Crear nueva versión
git tag -a v2.1.0 -m "🚀 Nueva versión"
git push origin v2.1.0

# Ver estado del repositorio
git status
git log --oneline -10
```

## 🌐 Configuración de GitHub Pages (Opcional)

Para documentación web automática:

### 1. En GitHub:
- Settings > Pages
- Source: Deploy from a branch
- Branch: master / docs (si tienes carpeta docs)

### 2. Agregar badge al README:
```markdown
[![Pages](https://img.shields.io/badge/GitHub-Pages-blue)](https://legacyum.github.io/sistema-analisis-ventas-ia/)
```

## 🔄 Flujo de Trabajo Diario

### Desarrollo normal:
```bash
# 1. Asegurar que tienes la última versión
git pull origin master

# 2. Crear rama para nueva función
git checkout -b feature/nueva-funcion

# 3. Hacer cambios y commit
git add .
git commit -m "feat: ✨ descripción"

# 4. Subir rama
git push origin feature/nueva-funcion

# 5. En GitHub: crear Pull Request
# 6. Después de aprobación: merge a master
```

### Releases:
```bash
# 1. Preparar release
git checkout master
git pull origin master

# 2. Actualizar CHANGELOG.md
# 3. Crear tag de versión
git tag -a v2.1.0 -m "🚀 Descripción del release"

# 4. Subir todo
git push origin master
git push origin v2.1.0
```

## 🛠️ Configuración de Colaboradores

### Agregar colaboradores:
1. Repository Settings > Manage access
2. Invite a collaborator
3. Asignar permisos (Read, Write, Admin)

### Protección de master:
1. Settings > Branches
2. Add rule para `master`
3. Require pull request reviews
4. Require status checks

## 📊 Integración Continua (Opcional)

### GitHub Actions para testing automático:
```yaml
# .github/workflows/test.yml
name: Tests
on: [push, pull_request]
jobs:
  test:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v2
    - name: Set up Python
      uses: actions/setup-python@v2
      with:
        python-version: 3.8
    - name: Install dependencies
      run: pip install -r requirements.txt
    - name: Run tests
      run: python demo_ia.py
```

## 🏷️ Template de Release Notes

Para cada nueva versión:

```markdown
## 🚀 Release v2.1.0 - Nombre del Release

### ✨ Nuevas Funcionalidades
- Nueva función X
- Mejora en Y

### 🐛 Correcciones
- Bug corregido en Z
- Problema de rendimiento solucionado

### 📚 Documentación
- README actualizado
- Nuevos ejemplos

### ⚠️ Breaking Changes
- Cambio incompatible (si aplica)

### 📊 Estadísticas
- X commits desde última versión
- Y archivos modificados
- Z líneas de código agregadas
```
