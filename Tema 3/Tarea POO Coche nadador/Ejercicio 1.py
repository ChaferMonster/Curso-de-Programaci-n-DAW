class coche:
    def __init__(self, color, aceleracion):
        self.color = color
        self.aceleracion = aceleracion
        self.velocidad = 0

    def acelerar(self):
        self.velocidad = self.velocidad + self.aceleracion

    def frenar(self):
        self.velocidad = self.velocidad - self.aceleracion
        if self.velocidad <= 0:
            print(f"La velocidad del coche es de {self.velocidad}. El coche esta parado")
            self.velocidad = 0


class nadador(coche):
    def __init__(self, color, aceleracion, estaNadando):
        super().__init__(color, aceleracion)
        self.estaNadando = False
    def nada(self):
        self.estaNadando = True

#Programa prinicpal
c1 = coche("negro", 100)
c2 = coche("blanco", 50)
cN = nadador("Amarillo", 300, False)

print("COCHE 1")

c1.acelerar() #Llamamos al método con el objeto que queramos
print(f"El coche acelera {c1.aceleracion}km/h")
print(f"La velocidad es de {c1.velocidad}km/h")

c1.acelerar()
print(f"El coche acelera {c1.aceleracion}km/h")
print(f"La velocidad es de {c1.velocidad}km/h")

c1.frenar()
print(f"El coche frena {c1.aceleracion}km/h")
print(f"La velocidad es de {c1.velocidad}km/h")

print("")
print("COCHE 2")

c2.acelerar() #Llamamos al método con el objeto que queramos
print(f"El coche acelera {c2.aceleracion}km/h")
print(f"La velocidad es de {c2.velocidad}km/h")

c2.acelerar()
print(f"El coche acelera {c2.aceleracion}km/h")
print(f"La velocidad es de {c2.velocidad}km/h")

c2.frenar()
print(f"El coche frena {c2.aceleracion}km/h")
print(f"La velocidad es de {c2.velocidad}km/h")

print("")
print("Coche N")

print(cN.aceleracion)
cN.nada()
print(cN.estaNadando)