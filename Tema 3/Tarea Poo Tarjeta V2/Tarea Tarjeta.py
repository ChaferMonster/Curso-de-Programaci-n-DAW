class tarjeta:
    saldo = 0
    def __init__(self, identificador):
        self.identidicador = identificador   

    def mostrar_saldo(self):
        print(self.saldo)

    def sumar_saldo(self):
        compra = int(input("Introduce la cantidad de dinero que ha costado la compra: "))
        self.saldo = compra + self.saldo
        print(f"La compra ha costado {compra}€")
        print(f"El saldo actual de la tarjeta es de {self.saldo}")

    def restar_saldo(self):
        devolución = input(int("Introduce la cantidad de dinero que ha costado la compra: "))
        self.saldo = self.saldo - devolución
        print(f"La devolución ha devuelto {devolución}€ a tu cuenta")
        print(f"El saldo actual de la tarjeta es de {self.saldo}")

    def fin_de_mes(self):
        self.saldo = 0
        print(f"Se ha combrado todo el saldo a tu cuenta bancaria.\nActualmente tu saldo esta en {self.saldo}")


class tar_descuento(tarjeta):
    saldo = 0
    def __init__(self, identificador,descuento):
        super().__init__(identificador)
        self.descuento = descuento

    def mostrar_descuento(self):
        if self.saldo>=500 and self.saldo<=1000:
            self.descuento = self.descuento+2
        elif self.saldo>=1000 and self.saldo<=2000:
            self.descuento = self.descuento+3
        elif self.saldo>=2000:
            self.descuento = self.descuento+4
        print(f"El descuento actual es del {self.descuento}%")

    def sumar_saldo(self):
        compra = int(input("Introduce la cantidad de dinero que ha costado la compra: "))
        self.saldo = (compra-(compra*self.descuento/100)) + self.saldo
        print(f"La compra ha costado {compra}€")
        print(f"El saldo actual de la tarjeta es de {self.saldo}€")
        self.mostrar_descuento()

    def restar_saldo(self):
        devolución = int(input("Introduce la cantidad de dinero que ha costado la compra: "))
        devlucion_rebajada = (devolución-(devolución*self.descuento/100))
        self.saldo = self.saldo - devlucion_rebajada
        print(f"La devolución ha devuelto {devlucion_rebajada}€ a tu cuenta")
        print(f"El saldo actual de la tarjeta es de {self.saldo}€")
        self.mostrar_descuento()

    def fin_de_mes(self):
        self.saldo = 0
        print(f"Se ha cobrado todo el saldo a tu cuenta bancaria.\nActualmente tu saldo esta en {self.saldo}€")
        

tarjeta1 = tarjeta(123)

tarjeta2 = tar_descuento(123,10)

tarjeta1.sumar_saldo()
tarjeta1.mostrar_saldo()

tarjeta2.sumar_saldo()
tarjeta2.sumar_saldo()

tarjeta2.restar_saldo()
tarjeta2.mostrar_saldo()
tarjeta2.fin_de_mes()
