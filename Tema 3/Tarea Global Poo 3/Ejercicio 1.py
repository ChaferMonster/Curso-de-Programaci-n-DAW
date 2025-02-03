

class cliente():
    def __init__(self, nombre, DNI):
        self.nombre = nombre
        self.DNI = DNI

    def ver(self):
        print("Estos son los datos del cliente: ")
        print(f"El cliente se llama {self.nombre} y su DNI es {self.DNI}")

    def comprar(self):
        global cesta2
        producto = input("Introduce el artículo que deseas comprar: ")
        cantidad = int(input("Introduce el número de unidades que deseas comprar: "))
        cesta1 = {
            producto:cantidad,
        }

        cesta2 = {}
        cesta2.update(cesta1)
        print(cesta2)
        return cesta2

    def compras(self):
        print(f"Vamos a ver las compras realizadas del cliente {self.nombre}")
        for i in cesta2:
            print(i)
        











































































































cliente1 = cliente("Pepe", 2001)
cliente1.ver()
cliente1.comprar()
cliente1.comprar()
cliente1.compras()