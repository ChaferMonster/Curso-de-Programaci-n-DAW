class tarjeta:
    saldo = 0
    def __init__(self, identificador):
        self.identidicador = identificador   

    def mostrar_saldo(self):
        print(self.saldo)

class tar_descuento(tarjeta):
    def __init__(self, identificador,descuento):
        super().__init__(identificador)
        self.descuento = descuento

    def mostrar_descuento(self):
        print(f"{self.descuento}")
        
    


tarjeta1 = tar_descuento(123,"10%")

tarjeta1.mostrar_saldo()
tarjeta1.mostrar_descuento()