# 1. Variables con nombre, edad, estatura y si eres aprendiz
nombre = "Maicol"
edad = 38
estatura = 1.75
es_aprendiz = True
print("1.", nombre, edad, estatura, es_aprendiz)

# 2. Mostrar el tipo de cada variable
print("2.", type(nombre), type(edad), type(estatura), type(es_aprendiz))

# 3. Convertir texto '3.75' a decimal y sumar 1
resultado = float('3.75') + 1
print("3.", resultado)

# 4. Intercambiar valores de x e y sin tercera variable
x = 10
y = 20
x, y = y, x
print("4. x =", x, ", y =", y)