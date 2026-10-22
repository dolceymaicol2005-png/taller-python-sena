# 1. Datos de un libro
libro = {"titulo": "Cien años de soledad", "autor": "García Márquez", "anio": 1967}
print("1. Libro:", libro)

# 2. Productos y total
prods = {"arroz": 3500, "aceite": 8000, "huevos": 18000, "pan": 2500}
print(f"2. Total productos: ${sum(prods.values())}")

# 3. Diccionario de traducción
trad = {"casa": "house", "perro": "dog"}
palabra = "perro"
print(f"3. Traducción de {palabra}: {trad.get(palabra, 'No existe')}")

# 4. Conteo de palabras en una frase
frase_c = "python es facil y python es divertido"
conteo = {}
for p in frase_c.split():
    conteo[p] = conteo.get(p, 0) + 1
print("4. Conteo:", conteo)