import random

def predecir_siguiente_numero(secuencia):
    if len(secuencia) < 2:
        return "La secuencia debe tener al menos dos números para hacer una predicción."

    # Calcular la diferencia común
    diferencia = secuencia[1] - secuencia[0]

    # Predecir el siguiente número
    siguiente_numero = secuencia[-1] + diferencia
    return siguiente_numero

# Ejemplo de uso
secuencia = [2, 4, 6, 8]  # Puedes cambiar esta lista por la secuencia que quieras
resultado = predecir_siguiente_numero(secuencia)
print("El siguiente número en la secuencia es:", resultado)
