# 🧮 Calculadora Básica con Flask

Aplicación web de calculadora básica desarrollada con Python 3 y Flask que realiza operaciones de suma, resta, multiplicación y división.

## 📋 Características

- ✅ Suma, resta, multiplicación y división
- ✅ Interfaz web moderna y responsiva
- ✅ API REST con JSON
- ✅ Pruebas unitarias con Pytest
- ✅ Cobertura de código > 80%
- ✅ Manejo de errores (división por cero, operaciones inválidas)

## 📁 Estructura del Proyecto

```
S6/
├── app.py                      # Aplicación Flask principal
├── calculator.py               # Lógica de la calculadora
├── requirements.txt            # Dependencias del proyecto
├── README.md                   # Este archivo
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
pip install -r requirements.txt
```

## ▶️ Ejecutar la Aplicación

```powershell
python app.py
```

La aplicación estará disponible en: **http://localhost:5000**

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

- **Python 3**
- **Flask 3.0.0** - Framework web
- **Pytest 7.4.3** - Framework de pruebas
- **pytest-cov 4.1.0** - Plugin de cobertura para Pytest

## ✅ Cobertura de Pruebas

El proyecto incluye pruebas exhaustivas que cubren:

- ✅ Todas las operaciones matemáticas (suma, resta, multiplicación, división)
- ✅ Casos con números positivos, negativos y decimales
- ✅ Manejo de errores (división por cero, operaciones inválidas)
- ✅ Endpoints de la API REST
- ✅ Validación de entrada de datos

La cobertura actual es superior al **80%** en todos los módulos.

## 📝 Comandos Rápidos

```powershell
# Instalar dependencias
pip install -r requirements.txt

# Ejecutar aplicación
python app.py

# Ejecutar pruebas
pytest

# Ejecutar pruebas con cobertura
pytest --cov=. --cov-report=term-missing

# Generar reporte HTML de cobertura
pytest --cov=. --cov-report=html

# Verificar cobertura mínima 80%
pytest --cov=. --cov-report=term --cov-fail-under=80
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
