def factorial_recursivo(numero):
    """
    Calcula el factorial de un número de forma recursiva.

    Parámetros:
    numero (int): Número entero positivo.

    Retorna:
    int: El factorial del número.
    """
    if numero == 0 or numero == 1:
        return 1
    else:
        return numero * factorial_recursivo(numero - 1)

numero_entero = 5
resultado_recursivo = factorial_recursivo(numero_entero)
print(f"El factorial de {numero_entero} es: {resultado_recursivo}")