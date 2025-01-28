from abc import abstractmethod
from abc import ABCMeta

class empleado(metaclass=ABCMeta):
    @abstractmethod
    def calcular_salario(self):
        pass
class empleadoAsalariado(empleado):
    def __init__(self, nombre, salario):
        self.salario = salario
        self.nombre = nombre
    
    def calcular_salario(self):
        print(f"El salario de {self.nombre} de este mes es de {self.salario}")


class empleadoXhoras(empleado):
    def __init__(self, nombre, ):

        self.nombre = nombre

    def calcular_salario(self):
        horas = int(input("Introduce el total de horas trabajadas: "))
        salario = int(input("Introduce el salario que cobras por hora: "))
        print(f"El salario de {self.nombre} total de este mes es de {4*horas *salario}")

class gerente(empleado):
    def __init__(self, nombre, salario):
        self.salario = salario
        self.nombre = nombre

    def calcular_salario(self):
        bonus = int(input("Introduce el bonus recibido este mes: "))
        print(f"El salario total de {self.nombre} de este mes es de {self.salario + bonus}")


a=input("Introduce tu nombre: ")
b=int(input("Introduce tu salario: "))


empleado2 = empleadoAsalariado(a, b)
a=input("Introduce tu nombre: ")
empleado3 = empleadoXhoras(a)
a=input("Introduce tu nombre: ")
b=int(input("Introduce tu salario: "))
empleado4 = gerente(a, b)


empleado2.calcular_salario()
empleado3.calcular_salario()
empleado4.calcular_salario()