# 1. Positivo, negativo o cero
num = -5
if num > 0: print("1. Positivo")
elif num < 0: print("1. Negativo")
else: print("1. Cero")

# 2. Año bisiesto
anio = 2024
es_bisiesto = (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0)
print(f"2. ¿El año {anio} es bisiesto?: {es_bisiesto}")

# 3. Saludo según la hora (0 a 23)
hora = 14
if 6 <= hora < 12: print("3. Buenos días")
elif 12 <= hora < 18: print("3. Buenas tardes")
else: print("3. Buenas noches")

# 4. Promedio de tres notas y aprobación
n1, n2, n3 = 3.5, 4.0, 2.8
prom = (n1 + n2 + n3) / 3
print(f"4. Promedio: {prom:.2f} -> {'Aprobado' if prom >= 3.0 else 'Reprobado'}")