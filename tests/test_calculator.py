"""
Pruebas unitarias para el módulo Calculator.
"""

import pytest

from calculator import Calculator


class TestCalculator:
    """Clase de pruebas para la clase Calculator."""

    @pytest.fixture
    def calc(self):
        """Fixture que provee una instancia de Calculator."""
        return Calculator()

    # Pruebas para suma
    def test_suma_positivos(self, calc):
        """Prueba suma de números positivos."""
        assert calc.suma(5, 3) == 8
        assert calc.suma(10, 20) == 30

    def test_suma_negativos(self, calc):
        """Prueba suma de números negativos."""
        assert calc.suma(-5, -3) == -8
        assert calc.suma(-10, -20) == -30

    def test_suma_mixtos(self, calc):
        """Prueba suma de números positivos y negativos."""
        assert calc.suma(5, -3) == 2
        assert calc.suma(-5, 3) == -2

    def test_suma_con_cero(self, calc):
        """Prueba suma con cero."""
        assert calc.suma(5, 0) == 5
        assert calc.suma(0, 5) == 5
        assert calc.suma(0, 0) == 0

    def test_suma_decimales(self, calc):
        """Prueba suma de números decimales."""
        assert calc.suma(2.5, 3.5) == 6.0
        assert abs(calc.suma(0.1, 0.2) - 0.3) < 0.0001

    # Pruebas para resta
    def test_resta_positivos(self, calc):
        """Prueba resta de números positivos."""
        assert calc.resta(10, 3) == 7
        assert calc.resta(20, 5) == 15

    def test_resta_negativos(self, calc):
        """Prueba resta de números negativos."""
        assert calc.resta(-5, -3) == -2
        assert calc.resta(-10, -20) == 10

    def test_resta_mixtos(self, calc):
        """Prueba resta de números positivos y negativos."""
        assert calc.resta(5, -3) == 8
        assert calc.resta(-5, 3) == -8

    def test_resta_con_cero(self, calc):
        """Prueba resta con cero."""
        assert calc.resta(5, 0) == 5
        assert calc.resta(0, 5) == -5
        assert calc.resta(0, 0) == 0

    def test_resta_decimales(self, calc):
        """Prueba resta de números decimales."""
        assert calc.resta(5.5, 2.5) == 3.0
        assert abs(calc.resta(0.3, 0.1) - 0.2) < 0.0001

    # Pruebas para multiplicación
    def test_multiplicacion_positivos(self, calc):
        """Prueba multiplicación de números positivos."""
        assert calc.multiplicacion(5, 3) == 15
        assert calc.multiplicacion(10, 4) == 40

    def test_multiplicacion_negativos(self, calc):
        """Prueba multiplicación de números negativos."""
        assert calc.multiplicacion(-5, -3) == 15
        assert calc.multiplicacion(-10, -4) == 40

    def test_multiplicacion_mixtos(self, calc):
        """Prueba multiplicación de números positivos y negativos."""
        assert calc.multiplicacion(5, -3) == -15
        assert calc.multiplicacion(-5, 3) == -15

    def test_multiplicacion_con_cero(self, calc):
        """Prueba multiplicación con cero."""
        assert calc.multiplicacion(5, 0) == 0
        assert calc.multiplicacion(0, 5) == 0
        assert calc.multiplicacion(0, 0) == 0

    def test_multiplicacion_decimales(self, calc):
        """Prueba multiplicación de números decimales."""
        assert calc.multiplicacion(2.5, 4) == 10.0
        assert abs(calc.multiplicacion(0.1, 0.2) - 0.02) < 0.0001

    # Pruebas para división
    def test_division_positivos(self, calc):
        """Prueba división de números positivos."""
        assert calc.division(10, 2) == 5
        assert calc.division(15, 3) == 5

    def test_division_negativos(self, calc):
        """Prueba división de números negativos."""
        assert calc.division(-10, -2) == 5
        assert calc.division(-15, -3) == 5

    def test_division_mixtos(self, calc):
        """Prueba división de números positivos y negativos."""
        assert calc.division(10, -2) == -5
        assert calc.division(-10, 2) == -5

    def test_division_decimales(self, calc):
        """Prueba división de números decimales."""
        assert calc.division(5.0, 2.0) == 2.5
        assert abs(calc.division(1.0, 3.0) - 0.3333333333333333) < 0.0001

    def test_division_por_cero(self, calc):
        """Prueba que la división por cero lanza ValueError."""
        with pytest.raises(ValueError, match="No se puede dividir por cero"):
            calc.division(10, 0)

        with pytest.raises(ValueError, match="No se puede dividir por cero"):
            calc.division(-10, 0)

        with pytest.raises(ValueError, match="No se puede dividir por cero"):
            calc.division(0, 0)

    def test_division_de_cero(self, calc):
        """Prueba división de cero entre número."""
        assert calc.division(0, 5) == 0
        assert calc.division(0, -5) == 0
