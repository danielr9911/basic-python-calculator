# 📚 Guía de Demostración de Fallos en CI/CD

Esta guía te ayudará a demostrar a tus estudiantes cómo el pipeline CI/CD detecta y previene código de mala calidad.

## 🎯 Objetivo Educativo

Mostrar cómo cada etapa del pipeline (Linting, Formatting, Testing, Security) actúa como una **barrera de calidad** que previene que código problemático llegue a la rama `main`.

---

## 🔍 DEMO 1: Fallo de Linter (Ruff)

### ¿Qué detecta?
- Variables no usadas
- Imports sin usar
- Errores de sintaxis
- Código redundante
- Problemas de estilo

### Pasos para la demostración:

1. **Crear rama de demostración:**
```powershell
git checkout -b demo/linter-fail
```

2. **Introducir error en `calculator.py`:**
```python
# Agregar al inicio del archivo (línea 6)
import os  # Import sin usar - ERROR

# O agregar una variable sin usar en algún método:
def suma(a, b):
    resultado_temporal = a + b  # Variable sin usar - WARNING
    return a + b
```

3. **Probar localmente:**
```powershell
ruff check .
```

**Resultado esperado:**
```
calculator.py:6:1: F401 `os` imported but unused
calculator.py:15:8: F841 Local variable `resultado_temporal` is assigned to but never used
Found 2 errors.
```

4. **Hacer commit y push:**
```powershell
git add .
git commit -m "demo: Introducir error de linting"
git push origin demo/linter-fail
```

5. **Crear Pull Request** en GitHub hacia `main`

6. **Observar:** El pipeline fallará en el paso "Run Ruff Linter" ❌

7. **Limpiar:**
```powershell
git checkout main
git branch -D demo/linter-fail
```

---

## 🎨 DEMO 2: Fallo de Formatter (Black)

### ¿Qué detecta?
- Formato inconsistente
- Líneas muy largas
- Espacios incorrectos
- Comillas inconsistentes

### Pasos para la demostración:

1. **Crear rama de demostración:**
```powershell
git checkout -b demo/format-fail
```

2. **Introducir error en `app.py`:**
```python
# Cambiar línea 10 con formato incorrecto:
# ANTES (bien formateado):
calc = Calculator()

# DESPUÉS (mal formateado - múltiples espacios):
calc     =        Calculator(  )

# O agregar línea muy larga (>100 caracteres):
mensaje_muy_largo = "Este es un mensaje extremadamente largo que definitivamente excede los 100 caracteres permitidos por Black y debería generar un error de formateo"
```

3. **Probar localmente:**
```powershell
black --check .
```

**Resultado esperado:**
```
would reformat app.py
Oh no! 💥 💔 💥
1 file would be reformatted.
```

4. **Push y crear PR:**
```powershell
git add .
git commit -m "demo: Código sin formatear correctamente"
git push origin demo/format-fail
```

5. **Observar:** El pipeline fallará en "Check code formatting with Black" ❌

6. **Mostrar la solución:**
```powershell
black .  # Auto-corrige el formato
```

7. **Limpiar:**
```powershell
git checkout main
git branch -D demo/format-fail
```

---

## 🧪 DEMO 3: Fallo de Tests

### ¿Qué detecta?
- Funcionalidad rota
- Regresiones
- Cobertura insuficiente
- Lógica incorrecta

### Pasos para la demostración:

1. **Crear rama de demostración:**
```powershell
git checkout -b demo/test-fail
```

2. **Romper la lógica en `calculator.py`:**
```python
# Cambiar el método suma (línea ~20):
@staticmethod
def suma(a, b):
    """Suma dos números."""
    return a - b  # BUG INTENCIONAL: resta en vez de suma
```

3. **Probar localmente:**
```powershell
pytest -v
```

**Resultado esperado:**
```
tests/test_calculator.py::TestCalculator::test_suma_positivos FAILED
tests/test_calculator.py::TestCalculator::test_suma_negativos FAILED
...
FAILED tests/test_app.py::TestApp::test_calcular_suma - AssertionError: assert -2 == 8
=============== 15 failed, 16 passed in 1.23s ===============
```

4. **Push y crear PR:**
```powershell
git add .
git commit -m "demo: Romper funcionalidad de suma"
git push origin demo/test-fail
```

5. **Observar:** El pipeline fallará en "Run tests with coverage" ❌

6. **Limpiar:**
```powershell
git checkout main
git branch -D demo/test-fail
```

---

## 🔒 DEMO 4: Fallo de Seguridad (Bandit)

### ¿Qué detecta?
- Uso de funciones inseguras
- Hardcoded passwords
- SQL injection potencial
- Uso de `eval()` o `exec()`

### Pasos para la demostración:

1. **Crear rama de demostración:**
```powershell
git checkout -b demo/security-fail
```

2. **Introducir código inseguro en `app.py`:**
```python
# Agregar al final del archivo antes de if __name__:

@app.route('/eval', methods=['POST'])
def evaluar_codigo():
    """PELIGRO: Nunca hacer esto en producción"""
    data = request.get_json()
    codigo = data.get('codigo')
    resultado = eval(codigo)  # VULNERABILIDAD CRÍTICA
    return jsonify({'resultado': resultado})

# O agregar:
PASSWORD = "admin123"  # Hardcoded password - PELIGRO
API_KEY = "sk-1234567890abcdef"  # Hardcoded API key - PELIGRO
```

3. **Probar localmente:**
```powershell
bandit -r app.py
```

**Resultado esperado:**
```
>> Issue: [B307:blacklist] Use of possibly insecure function - consider using safer alternative.
   Severity: Medium   Confidence: High
   Location: app.py:65

>> Issue: [B105:hardcoded_password_string] Possible hardcoded password: 'admin123'
   Severity: Low   Confidence: Medium
   Location: app.py:68
```

4. **Nota:** Como configuramos Bandit con `continue-on-error: true`, **NO** detendrá el pipeline, pero mostrará advertencias.

5. **Para que sí falle, modifica `.github/workflows/ci.yml`:**
```yaml
- name: Run security check with Bandit
  run: |
    echo "🔒 Running security analysis..."
    bandit -r . -ll
  continue-on-error: false  # Cambiar a false
```

6. **Limpiar:**
```powershell
git checkout main
git branch -D demo/security-fail
```

---

## 🔒 DEMO 5: Fallo de Cobertura de Tests

### Pasos para la demostración:

1. **Crear rama de demostración:**
```powershell
git checkout -b demo/coverage-fail
```

2. **Agregar función sin tests en `calculator.py`:**
```python
@staticmethod
def potencia(base, exponente):
    """Calcula la potencia de un número."""
    return base ** exponente

@staticmethod
def raiz_cuadrada(numero):
    """Calcula la raíz cuadrada."""
    if numero < 0:
        raise ValueError("No se puede calcular raíz de número negativo")
    return numero ** 0.5
```

3. **Probar cobertura:**
```powershell
pytest --cov=. --cov-fail-under=80
```

**Resultado esperado:**
```
TOTAL     45      7    84.44%
Coverage failure: total of 84% is less than fail-under=80%
```

4. **Observar:** Si la cobertura baja del 80%, el pipeline falla.

---

## 🎓 Flujo Completo de Demostración

### Opción A: Demostración Individual
Haz cada demo por separado como se describe arriba.

### Opción B: Crear rama con múltiples errores

```powershell
git checkout -b demo/multiples-errores

# Introducir varios errores a la vez
# - Import sin usar (Linter fail)
# - Formato incorrecto (Formatter fail)  
# - Test roto (Test fail)

git add .
git commit -m "demo: Múltiples problemas de calidad"
git push origin demo/multiples-errores
```

Crea un Pull Request y muestra cómo **cada etapa del pipeline falla secuencialmente**.

---

## 📊 Checklist de Demostración

Para cada demo, muestra a tus estudiantes:

- [ ] **Código local** - El error introducido
- [ ] **Ejecución local** - Cómo detectar el error antes de hacer commit
- [ ] **Commit y Push** - Subir el código problemático
- [ ] **Pull Request** - Intentar merge a main
- [ ] **Pipeline Fail** - Ver el pipeline fallar en GitHub Actions
- [ ] **Logs detallados** - Revisar qué salió mal
- [ ] **Protección de main** - Explicar que no se puede hacer merge
- [ ] **Corrección** - Mostrar cómo arreglar el problema
- [ ] **Pipeline Success** - Ver el pipeline pasar en verde ✅

---

## 🛡️ Configurar Protección de Rama (Opcional pero Recomendado)

Para demostrar que **realmente no se puede hacer merge** si el pipeline falla:

1. Ve a GitHub → Settings → Branches
2. Add branch protection rule para `main`
3. Marca:
   - ✅ Require status checks to pass before merging
   - ✅ Require branches to be up to date before merging
   - Selecciona: `quality-and-tests`
4. Save changes

Ahora GitHub **bloqueará físicamente** el botón de merge si el pipeline falla.

---

## 💡 Puntos Clave para Estudiantes

1. **El pipeline es tu red de seguridad** - Detecta errores antes de que lleguen a producción
2. **Falla rápido** - Mejor detectar errores en desarrollo que en producción
3. **Ejecución local primero** - Siempre ejecuta las herramientas localmente antes de push
4. **Automatización** - El pipeline verifica lo que los humanos pueden olvidar
5. **Calidad obligatoria** - No es opcional, es parte del proceso

---

## 🎯 Resumen de Comandos Útiles

```powershell
# Verificar TODO localmente antes de push
ruff check .                                    # Linting
black --check .                                 # Formato
pytest --cov=. --cov-fail-under=80 -v          # Tests
bandit -r . -q                                  # Seguridad

# Auto-corregir problemas
ruff check . --fix                              # Auto-fix linting
black .                                         # Auto-format

# Ver estado del pipeline en GitHub
# https://github.com/danielr9911/basic-python-calculator/actions
```

---

## 📝 Ejercicio para Estudiantes

**Tarea:** Cada estudiante debe:
1. Crear una rama con su nombre
2. Introducir intencionalmente 1 error de cada tipo
3. Hacer push y crear PR
4. Documentar qué errores encontró el pipeline
5. Corregir los errores
6. Lograr que el pipeline pase en verde
7. Hacer merge a main

Esto les enseñará el ciclo completo de CI/CD en la práctica.
