class CuentaBancaria:
    def __init__(self, titular, saldo_inicial):
        self.titular = titular
        self.saldo_inicial = saldo_inicial

    @classmethod
    def desde_un_diccionario(cls, diccionario):
        return (cls (diccionario["Titular"], diccionario["Saldo"]))


    @staticmethod
    def interes_generado(saldo):
        interes = 10
        saldo = saldo + (interes*saldo/100)
        return print(f"El saldo actual con interes es de {saldo}€")
    
    def ingresar(self):
        ingresado = int(input("Introduce la cantidad que deseas ingresar: "))
        self.saldo_inicial = self.saldo_inicial + ingresado
        return print(f"El saldo restante es de {self.saldo_inicial}")

    def retirar(self):
        retirada = int(input("Introduce la cantidad que deseas retirar: "))
        self.saldo_inicial = self.saldo_inicial - retirada
        return print(f"El saldo restante es de {self.saldo_inicial}")

datos_cuenta1 = {
    "Titular":input("Introduce el nombre del titular de la cuenta: "),
    "Saldo":int(input("Introduce el saldo de la cuenta: "))
}

cuenta1 = CuentaBancaria.desde_un_diccionario(datos_cuenta1)
CuentaBancaria.interes_generado(cuenta1.saldo_inicial)
cuenta1.ingresar()
cuenta1.retirar()