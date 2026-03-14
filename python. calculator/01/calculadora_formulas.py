# Arquivo: calculadora_formulas.py
"""
Calculadora de Fórmulas do Mestre — Versão Melhorada
Suporta variáveis a, b, c e funções matemáticas avançadas.
"""
import math

# Funções matemáticas seguras
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


def calcular(a, b, c, formula):
    """Calcula a fórmula de forma segura usando as variáveis a, b, c."""
    namespace = {"__builtins__": {}, "a": a, "b": b, "c": c, **FUNCOES}
    return eval(formula, namespace)


def mostrar_ajuda():
    print("\n" + "=" * 50)
    print("  FUNÇÕES DISPONÍVEIS")
    print("=" * 50)
    print("  +  adição       -  subtração")
    print("  *  multiplicar  /  dividir")
    print("  ** potência     // divisão inteira")
    print("  %  resto (módulo)")
    print()
    print("  sqrt(x)  raiz quadrada     abs(x)  absoluto")
    print("  sin(x)   seno              cos(x)  cosseno")
    print("  tan(x)   tangente          log(x)  log base 10")
    print("  ln(x)    log natural       round(x) arredondar")
    print("  floor(x) arredondar baixo  ceil(x) arredondar cima")
    print("  max(x,y) maior             min(x,y) menor")
    print("  Constantes: pi, e")
    print("=" * 50 + "\n")


def main():
    print("=" * 50)
    print("  CALCULADORA DE FÓRMULAS DO MESTRE")
    print("=" * 50)
    print("  Use variáveis a, b, c nas fórmulas.")
    print("  Digite 'ajuda' para ver funções.")
    print("  Digite 'sair' para encerrar.\n")

    historico = []

    while True:
        print("-" * 50)
        formula = input("  Fórmula: ").strip()

        if formula.lower() == "sair":
            break
        if formula.lower() == "ajuda":
            mostrar_ajuda()
            continue
        if not formula:
            print("  ⚠ Fórmula vazia!")
            continue

        try:
            a = float(input("  Valor de a: "))
            b = float(input("  Valor de b: "))
            c = float(input("  Valor de c: "))
        except ValueError:
            print("  ⚠ Digite apenas números!")
            continue

        try:
            resultado = calcular(a, b, c, formula)
            historico.append((formula, resultado))
            print(f"\n  ✅ {formula} = {resultado}\n")
        except ZeroDivisionError:
            print("\n  ❌ Divisão por zero!\n")
        except Exception as erro:
            print(f"\n  ❌ Erro: {erro}\n")

        if historico:
            print("  📋 Histórico:")
            for i, (f, r) in enumerate(historico[-5:], 1):
                print(f"     {i}. {f} = {r}")
            print()

    print(f"\n  Até mais! Total: {len(historico)} cálculos. 👋\n")


if __name__ == "__main__":
    main()
