# 1. Lista con 5 ciudades de Colombia e imprime la primera y la última
ciudades = ['Cali', 'Bogotá', 'Medellín', 'Barranquilla', 'Cartagena']
print("1. Primera:", ciudades[0], "| Última:", ciudades[-1])

# 2. Agrega dos ciudades más y elimina una
ciudades.append('Pereira')
ciudades.append('Manizales')
ciudades.remove('Bogotá')
print("2. Lista final:", ciudades)

# 3. Ordena una lista de 6 números de mayor a menor
nums = [4, 12, 7, 3, 19, 8]
nums.sort(reverse=True)
print("3. Números de mayor a menor:", nums)

# 4. Suma, mayor y menor de una lista usando sum, max y min
lista_nums = [15, 8, 23, 42, 4]
print("4. Suma:", sum(lista_nums), "| Mayor:", max(lista_nums), "| Menor:", min(lista_nums))