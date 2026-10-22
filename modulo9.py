# 1. Clase Aprendiz
class Aprendiz:
    def __init__(self, nombre, ficha):
        self.nombre, self.ficha = nombre, ficha
    def mostrar(self): print(f"1. Aprendiz: {self.nombre}, Ficha: {self.ficha}")
Aprendiz("Maicol", "3000001").mostrar()

# 2. Clase Rectangulo
class Rectangulo:
    def __init__(self, b, a): self.b, self.a = b, a
    def area(self): return self.b * self.a
    def perimetro(self): return 2 * (self.b + self.a)
r = Rectangulo(10, 5)
print(f"2. Rectángulo - Área: {r.area()}, Perímetro: {r.perimetro()}")

# 3. Cuenta con método retirar sin saldo negativo
class Cuenta:
    def __init__(self, saldo=0): self.saldo = saldo
    def retirar(self, val):
        if val <= self.saldo:
            self.saldo -= val
            print(f"3. Retiro exitoso. Saldo: {self.saldo}")
        else: print("3. Saldo insuficiente")
c = Cuenta(1000); c.retirar(400)

# 4. Herencia: Vehiculo y Moto
class Vehiculo:
    def describir(self): print("Vehículo genérico")
class Moto(Vehiculo):
    def describir(self): print("Soy una motocicleta deportiva")
print("4.", end=" "); Moto().describir()