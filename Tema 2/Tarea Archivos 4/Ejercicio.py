print("AGENDA DE CONTACTOS")

#Función para buscar el número de teléfono
def buscar (nombre,apellido):
    
    with open("C:\\Users\\alu\\Desktop\\clase\\Programación\\codigos visual+\\Tema 2\\Tarea Archivos 4\\Contactos.txt","r") as agenda:
        while 1:
            linea = agenda.readline()
            linea2 = agenda.readline()
            linea3 = agenda.readline()

            if linea == "":
                break

            if (nombre == linea[:-1]) and (apellido == linea2[:-1]):
                return(print(f"{linea3[:-1]}"))

#Función para añadir un contacto
def crear(nombre,apellido,numero):
        
        with open("C:\\Users\\alu\\Desktop\\clase\\Programación\\codigos visual+\\Tema 2\\Tarea Archivos 4\\Contactos.txt","a") as agenda:
            agenda.write(nombre + "\n")
            agenda.write(apellido + "\n")
            agenda.write(numero + "\n")
            print("Se ha añadido correctamente")

#Función para eliminar un contacto
def eliminar(nombre,apellido):
       
    with open("C:\\Users\\alu\\Desktop\\clase\\Programación\\codigos visual+\\Tema 2\\Tarea Archivos 4\\Contactos.txt","r",) as agenda:
        with open("C:\\Users\\alu\\Desktop\\clase\\Programación\\codigos visual+\\Tema 2\\Tarea Archivos 4\\Contactos_Copia.txt","w") as copia:
            while 1:
                linea = agenda.readline()
                linea2 = agenda.readline()
                linea3 = agenda.readline()

                if (linea != nombre[:-1]) or (linea2 != apellido[:-1]):
                    copia.write(linea)
                    copia.write(linea2)
                    copia.write(linea3)

                if linea == "":
                    break
                

    #En esta parte copiamos de la copia a la agenda principal
    with open("C:\\Users\\alu\\Desktop\\clase\\Programación\\codigos visual+\\Tema 2\\Tarea Archivos 4\\Contactos.txt","w",) as agenda:
            with open("C:\\Users\\alu\\Desktop\\clase\\Programación\\codigos visual+\\Tema 2\\Tarea Archivos 4\\Contactos_Copia.txt","r") as copia:
                while 1:
                    linea = copia.readline()
                    linea2 = copia.readline()
                    linea3 = copia.readline()

                    agenda.write(linea)
                    agenda.write(linea2)
                    agenda.write(linea3)

                    if linea == "":
                        break
        
                    
    return (print("Contacto eliminado"))

#Esta función sirve para ver la agenda entera
def ver_agenda():

    with open("C:\\Users\\alu\\Desktop\\clase\\Programación\\codigos visual+\\Tema 2\\Tarea Archivos 4\\Contactos.txt","r",) as agenda:
        while 1:
            linea = agenda.readline()
            linea2 = agenda.readline()
            linea3 = agenda.readline()

            print(linea)
            print(linea2)
            print(linea3)
            
            if linea == "":
                        break
#Función del menú de opciones
def menu():

    while 1:
        print("Opción 1: Buscar un contacto.")
        print("Opción 2: Añadir un nuevo contacto.")
        print("opción 3: Borrar un contacto.")
        print("Opción 4: Mostrar la Agenda de Contactos.")
        print("Opción 5: Salir de la Agenda de Contactos.")

        opcion = int(input("Elige tu opción: "))

        if opcion == 1:
            nombre = input("Introduce el nombre de la persona que deseas buscar: ")
            apellido = input("Introduce el apellido de la persona que deseas buscar: ")
            nombre = nombre.lower()
            apellido = apellido.lower()
            buscar(nombre,apellido)
            print("---------------------------------------------")

        elif opcion == 2:
            nombre = input("Introduce el nombre que deseas añadir: ")
            apellido = input("Introduce el apellido que deseas añadir: ")
            numero = input("Introduce el teléfono que deseas añadir: ")
            nombre = nombre.lower()
            apellido = apellido.lower()
            crear(nombre,apellido,numero)
            print("---------------------------------------------")

        elif opcion == 3:
            nombre = input("Introduce el nombre de la persona que deseas eliminar: ")
            apellido = input("Introduce el apellido de la persona que deseas eliminar: ")
            nombre = nombre.lower()
            apellido = apellido.lower()
            eliminar(nombre,apellido)
            print("---------------------------------------------")

        elif opcion == 4:
            ver_agenda()
            print("---------------------------------------------")
            
        elif opcion == 5:
            print("Adiós")
            break

        else:
            print("El creador de este código cree que te has equivocado.")
            print("Vamos a volver a probar...")
            print("---------------------------------------------")
menu()