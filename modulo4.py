# 1. Presentación con f-strings
nombre_p, edad_p, ciudad_p = "Maicol", 38, "Cali"
print(f"1. Me llamo {nombre_p}, tengo {edad_p} años y vivo en {ciudad_p}.")

# 2. Precio de 1999.5 con dos decimales
precio = 1999.5
print(f"2. Precio: {precio:.2f}")

# 3. Con .format(), tabla de multiplicar del 7 hasta el 3
print("3. Tabla del 7 hasta el 3:")
for i in range(1, 4):
    print("7 x {} = {}".format(i, 7 * i))

# 4. Número entero con ceros a la izquierda (007)
n = 7
print(f"4. Formato 007: {n:03d}")