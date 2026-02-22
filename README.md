# 🧮 Calculadora Básica con Flask

[![CI Pipeline](https://github.com/danielr9911/basic-python-calculator/actions/workflows/ci.yml/badge.svg)](https://github.com/danielr9911/basic-python-calculator/actions/workflows/ci.yml)
[![Python 3.12](https://img.shields.io/badge/python-3.12-blue.svg)](https://www.python.org/downloads/)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Aplicación web de calculadora básica desarrollada con Python 3 y Flask que realiza operaciones de suma, resta, multiplicación y división.

## 📋 Características

- ✅ Suma, resta, multiplicación y división
- ✅ Interfaz web moderna y responsiva
- ✅ API REST con JSON
- ✅ Pruebas unitarias con Pytest
- ✅ Cobertura de código > 80%
- ✅ Manejo de errores (división por cero, operaciones inválidas)
- ✅ Pipeline CI/CD con GitHub Actions
- ✅ Linting con Ruff (el linter más rápido para Python)
- ✅ Formateo automático con Black
- ✅ Análisis de seguridad con Bandit

## 🔄 Pipeline CI/CD

El proyecto incluye un pipeline automatizado de CI/CD con GitHub Actions que se ejecuta en cada push y pull request:

### Flujo del Pipeline (Orden según buenas prácticas DevOps):

1. **🔍 Linting (Ruff)**: Análisis de calidad de código y detección de errores potenciales
2. **🎨 Formatting (Black)**: Verificación del estilo y formato del código
3. **🧪 Testing (Pytest)**: Ejecución de pruebas unitarias con cobertura mínima del 80%
4. **🔒 Security (Bandit)**: Análisis de seguridad del código

### Características del Pipeline:

- ✅ Ejecuta en Python 3.12 (simplificado para propósitos educativos)
- ✅ Caché de dependencias para builds más rápidos
- ✅ Reportes de cobertura automáticos
- ✅ Integración con Codecov (opcional)
- ✅ Badges de estado en el README

### 🎓 Para Instructores/Estudiantes:

¿Quieres demostrar cómo el pipeline detecta y previene errores? Lee la **[Guía de Demostración de Fallos](DEMO_GUIA_FALLOS.md)** que incluye:

- 📝 Ejemplos de cómo introducir errores intencionales
- 🔍 Cómo cada etapa del pipeline detecta problemas específicos
- 💻 Script automatizado para generar demos: `./crear-demo-fallo.ps1`
- 🎯 Ejercicios prácticos para estudiantes

## 📁 Estructura del Proyecto

```
S6/
├── .github/
│   └── workflows/
│       └── ci.yml             # Pipeline de GitHub Actions
├── app.py                      # Aplicación Flask principal
├── calculator.py               # Lógica de la calculadora
├── requirements.txt            # Dependencias de producción
├── requirements-dev.txt        # Dependencias de desarrollo
├── pyproject.toml             # Configuración de herramientas
├── .bandit                     # Configuración de seguridad
├── .gitignore                 # Archivos ignorados por git
├── README.md                   # Este archivo
├── DEMO_GUIA_FALLOS.md        # 🎓 Guía para demostrar fallos del pipeline
├── crear-demo-fallo.ps1       # Script para crear demos automáticamente
├── templates/
│   └── index.html             # Interfaz web de la calculadora
└── tests/
    ├── __init__.py            # Inicializador del paquete de tests
    ├── test_calculator.py     # Pruebas del módulo Calculator
    └── test_app.py            # Pruebas de la aplicación Flask
```

## 🚀 Instalación

### 1. Clonar o descargar el proyecto

Ya tienes el proyecto en `c:\DEV\S6`

### 2. Crear un entorno virtual (recomendado)

```powershell
# Crear entorno virtual
python -m venv venv

# Activar entorno virtual
.\venv\Scripts\Activate
```

### 3. Instalar dependencias

```powershell
# Dependencias de producción
pip install -r requirements.txt

# Dependencias de desarrollo (linter, formatter, etc.)
pip install -r requirements-dev.txt
```

## ▶️ Ejecutar la Aplicación

```powershell
python app.py
```

La aplicación estará disponible en: **http://localhost:5000**

## 🛠️ Herramientas de Desarrollo

### Linting con Ruff

Ruff es el linter más rápido para Python, escrito en Rust. Analiza el código en busca de errores y problemas de estilo.

```powershell
# Verificar el código
ruff check .

# Auto-corregir problemas
ruff check . --fix

# Ver reglas específicas
ruff check . --show-source
```

### Formateo con Black

Black es el formateador de código estándar para Python que garantiza un estilo consistente.

```powershell
# Verificar formato (sin modificar archivos)
black --check .

# Formatear código automáticamente
black .

# Ver diferencias sin aplicar cambios
black --diff .
```

### Análisis de Seguridad con Bandit

Bandit identifica problemas de seguridad comunes en código Python.

```powershell
# Análisis básico
bandit -r .

# Análisis con nivel de severidad
bandit -r . -ll

# Generar reporte JSON
bandit -r . -f json -o bandit-report.json
```

### Ejecutar todas las verificaciones de calidad

```powershell
# Orden recomendado (como en el pipeline CI/CD)
ruff check .
black --check .
pytest --cov=. --cov-report=term-missing --cov-fail-under=80
bandit -r . -ll
```

## 🧪 Ejecutar Pruebas

### Ejecutar todas las pruebas

```powershell
pytest
```

### Ejecutar pruebas con salida detallada

```powershell
pytest -v
```

### Ejecutar pruebas de un archivo específico

```powershell
pytest tests/test_calculator.py
pytest tests/test_app.py
```

## 📊 Generar Reporte de Cobertura

### Ejecutar pruebas con cobertura

```powershell
pytest --cov=. --cov-report=term-missing
```

### Generar reporte HTML de cobertura

```powershell
pytest --cov=. --cov-report=html
```

El reporte HTML se generará en la carpeta `htmlcov/`. Abre `htmlcov/index.html` en tu navegador para ver el reporte completo.

### Generar reporte en la terminal con porcentajes

```powershell
pytest --cov=. --cov-report=term
```

### Verificar cobertura mínima del 80%

```powershell
pytest --cov=. --cov-report=term --cov-fail-under=80
```

Este comando fallará si la cobertura es menor al 80%.

## 📡 API REST

### Endpoint: `/calcular`

**Método:** POST  
**Content-Type:** application/json

**Cuerpo de la solicitud:**

```json
{
  "numero1": 10,
  "numero2": 5,
  "operacion": "suma"
}
```

**Operaciones disponibles:**
- `suma`
- `resta`
- `multiplicacion`
- `division`

**Respuesta exitosa (200):**

```json
{
  "resultado": 15,
  "operacion": "suma",
  "numero1": 10,
  "numero2": 5
}
```

**Respuesta de error (400):**

```json
{
  "error": "No se puede dividir por cero"
}
```

## 🧮 Uso de la Interfaz Web

1. Abre http://localhost:5000 en tu navegador
2. Ingresa el primer número
3. Ingresa el segundo número
4. Haz clic en el botón de la operación deseada
5. El resultado se mostrará automáticamente

## 🧪 Ejemplos de Uso con cURL

### Suma

```powershell
curl -X POST http://localhost:5000/calcular `
  -H "Content-Type: application/json" `
  -d '{\"numero1\": 10, \"numero2\": 5, \"operacion\": \"suma\"}'
```

### División

```powershell
curl -X POST http://localhost:5000/calcular `
  -H "Content-Type: application/json" `
  -d '{\"numero1\": 20, \"numero2\": 4, \"operacion\": \"division\"}'
```

## 🛠️ Tecnologías Utilizadas

### Producción
- **Python 3.12**
- **Flask 3.0.0** - Framework web
- **Pytest 7.4.3** - Framework de pruebas
- **pytest-cov 4.1.0** - Plugin de cobertura para Pytest

### Desarrollo y Calidad
- **Ruff 0.1.15** - Linter ultra-rápido (reemplaza flake8, isort, etc.)
- **Black 24.1.1** - Formateador de código
- **Bandit 1.7.6** - Análisis de seguridad
- **GitHub Actions** - CI/CD Pipeline

## ✅ Cobertura de Pruebas

El proyecto incluye pruebas exhaustivas que cubren:

- ✅ Todas las operaciones matemáticas (suma, resta, multiplicación, división)
- ✅ Casos con números positivos, negativos y decimales
- ✅ Manejo de errores (división por cero, operaciones inválidas)
- ✅ Endpoints de la API REST
- ✅ Validación de entrada de datos

La cobertura actual es superior al **80%** en todos los módulos.

## 📝 Comandos Rápidos

### Instalación
```powershell
# Instalar dependencias de producción
pip install -r requirements.txt

# Instalar dependencias de desarrollo
pip install -r requirements-dev.txt
```

### Ejecución
```powershell
# Ejecutar aplicación
python app.py
```

### Testing
```powershell
# Ejecutar pruebas
pytest

# Ejecutar pruebas con cobertura
pytest --cov=. --cov-report=term-missing

# Generar reporte HTML de cobertura
pytest --cov=. --cov-report=html

# Verificar cobertura mínima 80%
pytest --cov=. --cov-report=term --cov-fail-under=80
```

### Calidad de Código
```powershell
# Linting
ruff check .

# Formateo
black --check .

# Aplicar formateo
black .

# Análisis de seguridad
bandit -r . -ll
```

### Pipeline Completo (local)
```powershell
# Ejecutar todas las verificaciones como en CI/CD
ruff check . && black --check . && pytest --cov=. --cov-fail-under=80 && bandit -r . -ll
```

## 🐛 Manejo de Errores

La aplicación maneja los siguientes errores:

- **División por cero**: Retorna error 400 con mensaje descriptivo
- **Operación inválida**: Retorna error 400 si la operación no existe
- **Datos inválidos**: Retorna error 400/500 si los números no son válidos

## 👤 Autor

Calculadora Básica - Proyecto educativo con Flask y Python

## 📄 Licencia

Este proyecto es de código abierto y está disponible para uso educativo.
