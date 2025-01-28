class calculadora:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def suma(self):
        operacion = self.num1 + self.num2
        print(f"El resultado de la operación es: {operacion}")
    
    def resta(self):
        operacion = self.num1 - self.num2
        print(f"El resultado de la operación es: {operacion}")
    
    def multiplicacion(self):
        operacion = self.num1 * self.num2
        print(f"El resultado de la operación es: {operacion}")
    

    def division(self):
        operacion = self.num1 / self.num2
        print(f"El resultado de la operación es: {operacion}")
    

cosa1 = calculadora(2,4)

cosa2 = calculadora(25,5)

cosa1.suma()
cosa1.resta()
cosa1.multiplicacion()
cosa1.division()

cosa2.suma()
cosa2.resta()
cosa2.multiplicacion()
cosa2.division()