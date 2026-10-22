import math
import random
from datetime import date

# 1. Área de círculo con math y round
print(f"1. Área redondeada: {round(math.pi * (5 ** 2), 2)}")

# 2. Simular dado 5 veces
print("2. Lanzamientos de dado:", [random.randint(1, 6) for _ in range(5)])

# 3. Módulo calculadora (simulado)
def sumar(a, b): return a + b
print(f"3. Módulo calculadora (suma): {sumar(10, 5)}")

# 4. Fecha de hoy con datetime
print(f"4. Fecha de hoy: {date.today()}")