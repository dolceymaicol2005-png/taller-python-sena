# 1. Pide una palabra y muestra cuántos caracteres tiene
palabra = "Programación"
print(f"1. Caracteres: {len(palabra)}")

# 2. Quitar espacios con strip() y pasar a mayúsculas
frase = " hola mundo "
print(f"2. '{frase.strip().upper()}'")

# 3. Contar cuántas veces aparece la letra 'a'
frase_a = "Aprendiendo Python en el SENA"
print(f"3. Veces que aparece 'a': {frase_a.lower().count('a')}")

# 4. Invertir cadena con [::-1] y verificar palíndromo
original = "anita lava la tina"
limpia = original.replace(" ", "")
print(f"4. Invertida: '{original[::-1]}'. ¿Es palíndromo?: {limpia == limpia[::-1]}")