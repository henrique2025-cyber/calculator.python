from flask import Flask, render_template, request, jsonify
import math

app = Flask(__name__)

FUNCOES = {
    "sqrt": math.sqrt,
    "raiz": math.sqrt,
    "abs": abs,
    "pow": pow,
    "sin": math.sin,
    "cos": math.cos,
    "tan": math.tan,
    "log": math.log10,
    "ln": math.log,
    "pi": math.pi,
    "e": math.e,
    "round": round,
    "int": int,
    "max": max,
    "min": min,
    "floor": math.floor,
    "ceil": math.ceil,
}


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/api/calcular", methods=["POST"])
def calcular():
    try:
        data = request.get_json()
        a = float(data.get("a", 0))
        b = float(data.get("b", 0))
        c = float(data.get("c", 0))
        formula = data.get("formula", "").strip()

        if not formula:
            return jsonify({"error": "Fórmula vazia!"}), 400

        namespace = {"__builtins__": {}, "a": a, "b": b, "c": c, **FUNCOES}
        resultado = eval(formula, namespace)

        return jsonify({"resultado": resultado, "formula": formula})
    except ZeroDivisionError:
        return jsonify({"error": "Divisão por zero!"}), 400
    except Exception as e:
        return jsonify({"error": f"Erro: {str(e)}"}), 400


if __name__ == "__main__":
    app.run(debug=True, port=5001)
