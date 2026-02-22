"""
Módulo de calculadora con operaciones básicas.
"""


class Calculator:
    """Clase que implementa operaciones matemáticas básicas."""

    @staticmethod
    def suma(a, b):
        """
        Suma dos números.

        Args:
            a (float): Primer número
            b (float): Segundo número

        Returns:
            float: Resultado de la suma
        """
        return a + b

    @staticmethod
    def resta(a, b):
        """
        Resta dos números.

        Args:
            a (float): Primer número
            b (float): Segundo número

        Returns:
            float: Resultado de la resta
        """
        return a - b

    @staticmethod
    def multiplicacion(a, b):
        """
        Multiplica dos números.

        Args:
            a (float): Primer número
            b (float): Segundo número

        Returns:
            float: Resultado de la multiplicación
        """
        return a * b

    @staticmethod
    def division(a, b):
        """
        Divide dos números.

        Args:
            a (float): Dividendo
            b (float): Divisor

        Returns:
            float: Resultado de la división

        Raises:
            ValueError: Si el divisor es cero
        """
        if b == 0:
            raise ValueError("No se puede dividir por cero")
        return a / b
