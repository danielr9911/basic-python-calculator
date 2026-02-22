# Script de Demostración de Fallos CI/CD
# Este script crea ramas de demostración con errores intencionales

param(
    [Parameter(Mandatory=$false)]
    [ValidateSet('linter', 'formatter', 'test', 'security', 'coverage', 'all')]
    [string]$Tipo = 'linter'
)

Write-Host "🎓 Generador de Demos de Fallos CI/CD" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan

function New-LinterDemo {
    Write-Host "`n🔍 Creando demo de fallo de Linter..." -ForegroundColor Yellow
    
    git checkout -b demo/linter-fail
    
    # Agregar import sin usar en calculator.py
    $content = Get-Content "calculator.py"
    $newContent = @"
"""
Módulo de calculadora con operaciones básicas.
"""
import os  # ERROR: Import sin usar - Ruff lo detectará


"@ + ($content -join "`n")
    
    Set-Content "calculator.py" $newContent
    
    Write-Host "✅ Error de linting introducido en calculator.py" -ForegroundColor Green
    Write-Host "   - Import 'os' sin usar" -ForegroundColor Gray
}

function New-FormatterDemo {
    Write-Host "`n🎨 Creando demo de fallo de Formatter..." -ForegroundColor Yellow
    
    git checkout -b demo/formatter-fail
    
    # Agregar código mal formateado en app.py
    $content = Get-Content "app.py"
    $malFormateado = @"
# ERROR: Código mal formateado - Black lo detectará
mensaje_muy_largo_que_excede_los_cien_caracteres = "Este es un mensaje extremadamente largo que definitivamente excede los 100 caracteres permitidos por Black configurado en pyproject.toml"
calc     =        Calculator(  )  # Espacios incorrectos


"@
    
    $newContent = ($content[0..4] -join "`n") + "`n" + $malFormateado + "`n" + ($content[5..($content.Length-1)] -join "`n")
    Set-Content "app.py" $newContent
    
    Write-Host "✅ Error de formato introducido en app.py" -ForegroundColor Green
    Write-Host "   - Línea muy larga" -ForegroundColor Gray
    Write-Host "   - Espacios incorrectos" -ForegroundColor Gray
}

function New-TestDemo {
    Write-Host "`n🧪 Creando demo de fallo de Tests..." -ForegroundColor Yellow
    
    git checkout -b demo/test-fail
    
    # Romper la función suma
    $content = Get-Content "calculator.py"
    $content = $content -replace 'return a \+ b', 'return a - b  # BUG INTENCIONAL: resta en vez de suma'
    
    Set-Content "calculator.py" $content
    
    Write-Host "✅ Error de lógica introducido en calculator.py" -ForegroundColor Green
    Write-Host "   - Método suma() ahora resta (BUG)" -ForegroundColor Gray
}

function New-SecurityDemo {
    Write-Host "`n🔒 Creando demo de fallo de Seguridad..." -ForegroundColor Yellow
    
    git checkout -b demo/security-fail
    
    # Agregar código inseguro
    $content = Get-Content "app.py"
    $inseguro = @"

# ERROR: Código inseguro - Bandit lo detectará
PASSWORD = "admin123"  # Hardcoded password - PELIGRO
API_KEY = "sk-1234567890abcdef"  # Hardcoded API key - PELIGRO


@app.route('/eval', methods=['POST'])
def evaluar_codigo():
    '''PELIGRO: Esta función usa eval() - NUNCA hacer en producción'''
    data = request.get_json()
    codigo = data.get('codigo')
    resultado = eval(codigo)  # VULNERABILIDAD CRÍTICA
    return jsonify({'resultado': resultado})


"@
    
    $lineaIfMain = ($content | Select-String -Pattern "if __name__" | Select-Object -First 1).LineNumber - 1
    $newContent = ($content[0..($lineaIfMain-1)] -join "`n") + $inseguro + "`n" + ($content[$lineaIfMain..($content.Length-1)] -join "`n")
    
    Set-Content "app.py" $newContent
    
    Write-Host "✅ Código inseguro introducido en app.py" -ForegroundColor Green
    Write-Host "   - Hardcoded passwords" -ForegroundColor Gray
    Write-Host "   - Uso de eval() peligroso" -ForegroundColor Gray
}

function New-CoverageDemo {
    Write-Host "`n📊 Creando demo de fallo de Cobertura..." -ForegroundColor Yellow
    
    git checkout -b demo/coverage-fail
    
    # Agregar funciones sin tests
    $content = Get-Content "calculator.py"
    $sinTests = @"

    @staticmethod
    def potencia(base, exponente):
        '''Calcula la potencia de un número (SIN TESTS).'''
        return base ** exponente
    
    @staticmethod
    def raiz_cuadrada(numero):
        '''Calcula la raíz cuadrada (SIN TESTS).'''
        if numero < 0:
            raise ValueError("No se puede calcular raíz de número negativo")
        return numero ** 0.5
"@
    
    $newContent = ($content -join "`n") + $sinTests
    Set-Content "calculator.py" $newContent
    
    Write-Host "✅ Funciones sin tests agregadas en calculator.py" -ForegroundColor Green
    Write-Host "   - potencia() sin tests" -ForegroundColor Gray
    Write-Host "   - raiz_cuadrada() sin tests" -ForegroundColor Gray
}

# Guardar estado actual
$currentBranch = git branch --show-current

# Ejecutar demo seleccionada
switch ($Tipo) {
    'linter' { New-LinterDemo }
    'formatter' { New-FormatterDemo }
    'test' { New-TestDemo }
    'security' { New-SecurityDemo }
    'coverage' { New-CoverageDemo }
    'all' {
        New-LinterDemo
        git add .
        git commit -m "demo: Error de linting"
        git checkout $currentBranch
        
        New-FormatterDemo
        git add .
        git commit -m "demo: Error de formato"
        git checkout $currentBranch
        
        New-TestDemo
        git add .
        git commit -m "demo: Error de tests"
        git checkout $currentBranch
        
        New-SecurityDemo
        git add .
        git commit -m "demo: Error de seguridad"
        git checkout $currentBranch
        
        New-CoverageDemo
        git add .
        git commit -m "demo: Error de cobertura"
        git checkout $currentBranch
    }
}

if ($Tipo -ne 'all') {
    Write-Host "`n📝 Siguientes pasos:" -ForegroundColor Cyan
    Write-Host "1. Verificar el error localmente:" -ForegroundColor White
    
    switch ($Tipo) {
        'linter' { Write-Host "   ruff check ." -ForegroundColor Gray }
        'formatter' { Write-Host "   black --check ." -ForegroundColor Gray }
        'test' { Write-Host "   pytest -v" -ForegroundColor Gray }
        'security' { Write-Host "   bandit -r ." -ForegroundColor Gray }
        'coverage' { Write-Host "   pytest --cov=. --cov-fail-under=80" -ForegroundColor Gray }
    }
    
    Write-Host "`n2. Hacer commit y push:" -ForegroundColor White
    Write-Host "   git add ." -ForegroundColor Gray
    Write-Host "   git commit -m 'demo: Introducir error de $Tipo'" -ForegroundColor Gray
    Write-Host "   git push origin demo/$Tipo-fail" -ForegroundColor Gray
    
    Write-Host "`n3. Crear Pull Request en GitHub hacia main" -ForegroundColor White
    Write-Host "   https://github.com/danielr9911/basic-python-calculator/compare" -ForegroundColor Gray
    
    Write-Host "`n4. Observar el pipeline fallar ❌" -ForegroundColor White
    
    Write-Host "`n5. Limpiar después de la demo:" -ForegroundColor White
    Write-Host "   git checkout $currentBranch" -ForegroundColor Gray
    Write-Host "   git branch -D demo/$Tipo-fail" -ForegroundColor Gray
}

Write-Host "`n✨ Demo lista! Revisa los archivos modificados con 'git diff'" -ForegroundColor Green
