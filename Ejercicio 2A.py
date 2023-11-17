def factorial_iterativo(numero):
    """
    Calcula el factorial de un número de forma iterativa.

    Parámetros:
    numero (int): Número entero positivo.

    Retorna:
    int: El factorial del número.
    """
    if numero < 0:
        return None
    factorial = 1
    for i in range(1, numero + 1):
        factorial *= i
    return factorial

numero_entero = 5
resultado_iterativo = factorial_iterativo(numero_entero)
print(f"El factorial de {numero_entero} es: {resultado_iterativo}")



