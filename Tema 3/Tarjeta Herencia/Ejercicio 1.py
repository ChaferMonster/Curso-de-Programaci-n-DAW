class tarjeta:
    saldo = 0
    def __init__(self, identificador):
        self.identidicador = identificador 

    def mostrar_saldo(self):
        print(self.saldo)

tarjeta1 = tarjeta(123)

tarjeta1.mostrar_saldo()