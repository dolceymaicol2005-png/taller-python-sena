# 1. Función es_par(n)
def es_par(n): return n % 2 == 0
print(f"1. ¿4 es par?: {es_par(4)}")

# 2. area_circulo(radio) con pi = 3.1416
def area_circulo(radio): return 3.1416 * (radio ** 2)
print(f"2. Área círculo radio 5: {area_circulo(5)}")

# 3. Número mayor de una lista sin usar max
def obtener_mayor(lista):
    m = lista[0]
    for num in lista:
        if num > m: m = num
    return m
print(f"3. Mayor de [3, 9, 2, 15, 6]: {obtener_mayor([3, 9, 2, 15, 6])}")

# 4. Factorial con un ciclo
def factorial(n):
    res = 1
    for i in range(1, n + 1): res *= i
    return res
print(f"4. Factorial de 5: {factorial(5)}")