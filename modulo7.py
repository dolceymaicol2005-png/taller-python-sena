# 1. Números pares del 1 al 50
print("1. Pares:", list(range(2, 51, 2)))

# 2. Suma de los números del 1 al 100
print(f"2. Suma 1 al 100: {sum(range(1, 101))}")

# 3. Tabla de multiplicar de un número ingresado
num_t = 5
print(f"3. Tabla del {num_t}:")
for i in range(1, 11):
    print(f"{num_t} x {i} = {num_t * i}")

# 4. Validación con while (Simulado)
clave_correcta = "secreto"
intentos = ["123", "clave", "secreto"]
for clave in intentos:
    if clave == clave_correcta:
        print("4. ¡Clave correcta con while!")
        break