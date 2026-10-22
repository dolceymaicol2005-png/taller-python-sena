# 1. Operaciones básicas
n1, n2 = 20, 4
print(f"1. Suma: {n1+n2}, Resta: {n1-n2}, Mult: {n1*n2}, Div: {n1/n2}")

# 2. Guardar en registro.txt
with open("registro.txt", "w", encoding="utf-8") as f:
    f.write("Nombre: Maicol Montaño\nFicha: 3000001\n")
print("2. Guardado en registro.txt")

# 3. Leer registro.txt línea por línea
print("3. Leyendo archivo:")
with open("registro.txt", "r", encoding="utf-8") as f:
    for linea in f: print("   ->", linea.strip())

# 4. Promedio y guardar estado
notas = [3.8, 4.2, 3.5]
promedio = sum(notas) / len(notas)
estado = "Aprobó" if promedio >= 3.0 else "No aprobó"
with open("resultado.txt", "w", encoding="utf-8") as f:
    f.write(f"Promedio: {promedio:.2f} - {estado}\n")
print(f"4. Guardado en resultado.txt: {promedio:.2f} ({estado})")