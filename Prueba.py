#Contador de carácteres usando .read
"""fich = input("Introduce ruta: ")
archivo = open(fich,"r")

cont = 0

while 1:
    caracter = archivo.read(1)

    if caracter == "":
        break
    cont +=1

archivo.close()
print(f"{cont}")"""

#Importar urlopen para ver el código fuente de una página web
"""from urllib.request import urlopen
fichero = urlopen("https://www.umh.es")

for linea in fichero:
    print(f"({linea})")"""

#Leer línea a línea en un archivo con .readline()
"""fich = input("Introduce ruta: ")
archivo = open(fich,"r")

while 1:
    linea = archivo.readline()

    if linea == "":
        break
    print(f"{linea}")
   
archivo.close()"""

#Copiar cosas de un archivo a otro con "w"
"""fich = input("Introduce ruta: ")
archivo = open(fich,"r")
salida = open("C:\\Users\\alu\\Desktop\\clase\\Programación\\codigos visual+\\Tema 2\\archivos\\Texto.txt","w")

while 1:
    linea = archivo.readline()
    salida.write(linea)
    if linea =="":
        break
    print(f"{linea}")

archivo.close()
salida.close()"""

#Escribir listas en archivos nuevos con .write
"""fichero = open("C:\\Users\\alu\\Desktop\\clase\\Programación\\codigos visual+\\Tema 2\\archivos\\Lista.txt","w")

lista = ["oro", "plata", "bronce"]

for valor in lista:
    fichero.write(valor + "\n")

fichero.close"""

#Con este método no hace falta cerrar el close
"""lista = ["oro\n", "plata\n", "bronce\n"]
with open("C:\\Users\\alu\\Desktop\\clase\\Programación\\codigos visual+\\Tema 2\\archivos\\Lista.txt","w") as fich:
    fich.writelines(lista)"""

#Crear un diccionario
"""diccionario = {
    "llave":"valor", 
    "nombre":"Alvaro",
    "Edad":22
    }

print(f"{diccionario["nombre"]}")
"""
#Cambiar el valor de una llave en un diccionario
"""diccionario["nombre"] = "Pedro"

print(f"{diccionario["nombre"]}")"""

#Añadir una clave y un valor posteriormente
"""diccionario["ciudad"] = "Alicante"

print(diccionario)"""

#Immpreme las llaves
"""for var in diccionario:
    print(var)
"""
#Imprime los valores indicando primero el diccionario y luego entre corchete para los valores
"""for var4 in diccionario:
        print(diccionario[var4])
"""
#llave = var2, clave = var3. De esta forma imprimes las llaves y los valores.
"""for var2, var3 in diccionario.items():
    print(var2, var3)"""

#diferentes atributos para los diccionarios
"""diccionario = {
    "a":1,
    "b":5
}"""

#buscar la el valor relacionado con la llave. en caso de que no exista la llave, sale el mensaje puesto tras la coma
"""print(f"{diccionario.get("a", "no encontrado")}")
print(f"{diccionario.get("x", "no encontrado")}")"""

#Keys saca las claves y value devuelve los valores
"""claves = diccionario.keys()
print(f"{claves}")

valores = diccionario.values()
print(f"{valores}")"""

#Pop elimina elementos (llave, valor) y ademas muestra el valor de ellos. Tras coma, devuelve lo escrito en caso de que no este la clave/elemento
"""print(f"{diccionario.pop("a")}")

diccionario = {
    "a":1,
    "b":5
}
otrodiccionario = {
    "a":54, 
    "c":33
}

diccionario.update(otrodiccionario)
print(diccionario)"""

"""class Primera:
    var1iable=0
#Método constructor
    def __init__(self):
        self.variable1=5
        print("Acabo de crear un objeto de la clase primaria")
        print(f"El valor de variable 1 es {self.variable1}")

#Método trabajando
    def trabajando(self):
        self.variable1=10
        print("Estamos trabajando")
        print(f"Ahora vale {self.variable1}")

#Método destructor
    def __del__(self):
        print(f"Llamando al destructor")

#Programa principal
objeto1 = Primera() #Llama akl constructor
objeto1.trabajando() #Llama al método trabajando
objeto2 = Primera()
objeto3 = Primera()

del objeto1 #Llama al método destructor"""

"""#
class animal: #Clase padre
    def __init__(self,especie,edad): #Metodo constructor
        self.especie  = especie
        self.edad = edad

    def hablar(self): #Metodo hablar
        pass

    def moverse(self): #Metodo moverse
        pass

class perro(animal): #Clase hijo
    def __init__(self,especie,edad): #Metodo constructor
         super().__init__(especie, edad)

    def hablar(self): #Metodo hablar
        print("GUAU")

    def moverse(self): #Metodo moverse
        print("Me muevo a 4 patas")

class gato(animal): #Clase hijo
    def __init__(self, especie, edad): #Metodo constructor
         super().__init__(especie, edad)

    def hablar(self): #Metodo hablar
        print("MIAU")
      
    def moverse(self): #Metodo moverse
        print("Me muevo a 4 patas")

class abeja(animal): #Clase hijo
    def __init__(self, especie, edad): #Metodo constructor
        super().__init__(especie, edad)

    def hablar(self): #Metodo hablar
        print("ZZZZ")
      
    def moverse(self): #Metodo moverse
        print("Me muevo volando")

    def picar(self): #Metodo picar
        print("Te he picado")
    

#Programa

miperr = perro("mamifero", 5)
migato = gato("mamifero", 3)
miabeja = abeja("insecto", 2)

miperr.hablar()
miperr.moverse()
migato.hablar()
migato.moverse()
miabeja.hablar()
miabeja.moverse()
miabeja.picar()"""

"""class clase1:
    def print_clase1(self):
        print("clase1")
class clase2:
    def print_clase2(self):
        print("clase2")
class clase3(clase1,clase2):
    def print_clase3(self):
        print("clase3")



objeto = clase3()
objeto.print_clase3()
objeto.print_clase2()"""


"""import sqlite3

conexion = sqlite3.connect("estudiantes.db")

cursor = conexion.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS estudiantes (id INTEGRER PRIMARY KEY, nombre TEXT, edad INTEGRER)")

cursor.execute("INSERT INTO estudiantes (nombre, edad) VALUES (?, ?)", ("María", 14))
cursor.execute("INSERT INTO estudiantes (nombre, edad) VALUES (?, ?)", ("Luis", 15))

conexion.commit()

cursor.execute("SELECT * FROM estudiantes")
resultados = cursor.fetchall() #Contiene los resultados

print("Estudianes guardados: ")
for estudiante in resultados:
    print(f"ID: {estudiante[0]}, Nombre: {estudiante[1]}, Edad: {estudiante[2]}")

conexion.close()"""

"""from abc import abstractmethod
from abc import ABCMeta

class Mando(metaclass=ABCMeta):
    @abstractmethod
    
    def __init__(self):
        pass

    def siguiente(self):
        pass
    
    def anterior(self):
        pass

class mandosamsung(Mando):
    def __init__(self):
        super().__init__()

    def siguiente(self):
        print("LG->Siguiente")

    def anterior(self):
        print("LG->anterior")

"""


"""def requiere_autenticacion(funcion):
    def envoltura():
        usuario_autenticado = True

        if usuario_autenticado:
            print("Usuario autenticado. Ejecutando...")
            return funcion()
        else:
            print("Error")

    return envoltura

@requiere_autenticacion
def funcion_restringida():
    print("Esto solo se ejecuta si estas autenticado")

funcion_restringida()"""

class pizza:
    def __init__(self, ingredientes):
        self.ingredientes = ingredientes
        
    @classmethod
    def margarita(cls):
        return cls(["tomate", "queso", "oregano"])
    
    def agregar_ingrediente(self, ingrediente):
        self.ingredientes.append(ingrediente)

    def ver_ingrediente(self):
        for ing in self.ingredientes:
            print(f"{ing}")


    @staticmethod
    def es_vegetariana(pizza):
        if (pizza.ingredientes not in ["jamon", "pollo"]):
            print("Es vegetariana")


pizza1 = pizza.margarita()
pizza1.ver_ingrediente()
pizza1.agregar_ingrediente("cebolla")
pizza1.ver_ingrediente()
pizza.es_vegetariana(pizza1)
