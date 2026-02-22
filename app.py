"""
Aplicación Flask - Calculadora Básica
"""

from flask import Flask, jsonify, render_template, request

from calculator import Calculator

app = Flask(__name__)
calc = Calculator()


@app.route("/")
def index():
    """Renderiza la página principal de la calculadora."""
    return render_template("index.html")

@app.route("/calcular", methods=["POST"])
def calcular():
    """
    Endpoint para realizar cálculos.

    Espera un JSON con:
        - numero1: primer número
        - numero2: segundo número
        - operacion: tipo de operación (suma, resta, multiplicacion, division)

    Returns:
        JSON con el resultado o mensaje de error
    """
    try:
        data = request.get_json()
        numero1 = float(data.get("numero1"))
        numero2 = float(data.get("numero2"))
        operacion = data.get("operacion")

        operaciones = {
            "suma": calc.suma,
            "resta": calc.resta,
            "multiplicacion": calc.multiplicacion,
            "division": calc.division,
        }

        if operacion not in operaciones:
            return jsonify({"error": "Operación no válida"}), 400

        resultado = operaciones[operacion](numero1, numero2)

        return jsonify(
            {"resultado": resultado, "operacion": operacion, "numero1": numero1, "numero2": numero2}
        )

    except ValueError as e:
        return jsonify({"error": str(e)}), 400
    except Exception as e:
        return jsonify({"error": f"Error en el cálculo: {e!s}"}), 500


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
