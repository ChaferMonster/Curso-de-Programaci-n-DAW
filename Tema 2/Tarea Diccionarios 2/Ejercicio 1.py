#Se asignan las variables
diccionario = {}
i = 0

while i<3:
    #Introduce los datos que solicitamos
    trabajador = input("Introduce el nombre del trabajador: ")
    salario = input("Introduce el salario del trabajador: ")
    #Se van añadiendo los datos a un diccionario que se reconstruirá con los nuevos datos en cada bucle
    otrodiccionario = {
        trabajador:salario
    }
    #se actualizan los datos de manera que en este diccionario no se borran sino que se guardan nuevos en cada bucle.
    diccionario.update(otrodiccionario)
    i+=1
    
print(diccionario)

