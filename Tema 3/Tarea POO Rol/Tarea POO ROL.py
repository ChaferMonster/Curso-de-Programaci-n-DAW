class personaje:
    def __init__(self, nombre, salud, ataque):
        self.nombre = nombre
        self.salud = salud
        self.ataque = ataque
        
    def atacar(self, objetivo):
        print(f"{objetivo.nombre} recibe {self.ataque} de puntos de daño.")
        if objetivo.salud < self.ataque:
            print(f"{objetivo.nombre} ha sido debilitado.") 
            objetivo.salud = 0
        else: 
            objetivo.salud = objetivo.salud - self.ataque
            print(f"{objetivo.nombre} ha sobrevivido con {objetivo.salud} puntos de salud.")
        

    def atacado(self):
        daño = int(input(f"Introduce el daño que va a recibir {self.nombre}:\n"))
        if daño > self.salud:
            print(f"{self.nombre} ha sido debilitado.") 
            self.salud = 0
        else: 
            self.salud = self.salud - daño
            print(f"{self.nombre} ha sobrevivido con {self.salud} puntos de salud.")

class mago(personaje):
    def __init__(self, nombre, salud, ataque, magia):
        super().__init__(nombre, salud, ataque)
        self.magia = magia

    def atacar(self, objetivo):
        self.ataque = self.ataque + self.magia
        print(f"{objetivo.nombre} recibe {self.ataque} de puntos de daño.")
        if objetivo.salud < self.ataque:
            print(f"{objetivo.nombre} ha sido debilitado.") 
            objetivo.salud = 0
        else: 
            objetivo.salud = objetivo.salud - self.ataque
            print(f"{objetivo.nombre} ha sobrevivido con {objetivo.salud} puntos de salud.")
        

    def atacado(self):
        daño = int(input(f"Introduce el daño que va a recibir {self.nombre}:\n"))
        if daño > self.salud:
            print(f"{self.nombre} ha sido debilitado.") 
            self.salud = 0
        else: 
            self.salud = self.salud - daño
            print(f"{self.nombre} ha sobrevivido con {self.salud} puntos de salud.")

def elegir():
    opcion = 1
    while opcion in range (1,3):
        print("Elige tu personaje. Por favor introduce 1, 2 o 3")
        print("1) Guardían")
        print("2) Asesino")
        print("3) Mago")

        opcion = (int(input()))

        if opcion == 1:
            print("Has escogido al gran guerrero guardián.")
            eleccion = "Guardian"
            num = 1
        elif opcion == 2:
            print("Has escogido al temido asesino de las sombras.")
            eleccion = "Asesino"
            num = 1
        elif opcion == 3:
            print("Has escogido al poderoso mago.")
            eleccion = "Mago"
            num = 2
        else:
            print("Porfavor selecciona un personaje válido.")

        if num == 1:
            print("Vamos a seleccionar los atributos de tu personaje.")
            nombre = input(f"Selecciona el nombre de tu {eleccion}:\n")
            salud = int(input(f"Introduce los puntos de salud del {eleccion} {nombre}:\n"))
            ataque = int(input(f"Introduce los puntos de ataque del {eleccion} {nombre}:\n"))
            personaje1 = personaje(nombre,salud,ataque)

        elif num == 2:
            print("Vamos a seleccionar los atributos de tu personaje.")
            nombre = input(f"Selecciona el nombre de tu {eleccion}:\n")
            salud = int(input(f"Introduce los puntos de salud del {eleccion} {nombre}:\n"))
            ataque = int(input(f"Introduce los puntos de ataque del {eleccion} {nombre}:\n"))
            magia = int(input(f"Introduce los puntos de magia del {eleccion} {nombre}:\n"))
            personaje1 = mago(nombre,salud,ataque,magia)

        return personaje1
    

personaje1 = elegir()

objetivo = personaje("Rey Demonio",10000, 10000)

personaje1.atacar(objetivo)
objetivo.atacar(personaje1)

objetivo.atacado()
