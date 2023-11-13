def sumar(a, b):
    if isinstance(a, (int, float)) and isinstance(b, (int, float)):
        return a + b
    else:
        return "Error: Ambos parámetros deben ser int o float"

def restar(a, b):
    if isinstance(a, (int, float)) and isinstance(b, (int, float)):
        return a - b
    else:
        return "Error: Ambos parámetros deben ser int o float"

def multiplicar(a, b):
    if isinstance(a, (int, float)) and isinstance(b, (int, float)):
        result = 0
        for _ in range(abs(int(b))):
            result += a if b > 0 else -a
        return result
    else:
        return "Error: Ambos parámetros deben ser int o float"

# Ejemplos de uso:
print(sumar(3, 4))         # Salida: 7
print(restar(8.5, 2.5))     # Salida: 6.0
print(multiplicar(2, 3))    # Salida: 6
