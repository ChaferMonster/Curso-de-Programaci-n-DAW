from urllib.request import urlopen
diccionario = {}
with open("C:\\Users\\alu\\Desktop\\clase\\Programación\\codigos visual+\\Tema 2\\Tarea 13\\Fichero.txt","r") as fichero:
    with open("C:\\Users\\alu\\Desktop\\clase\\Programación\\codigos visual+\\Tema 2\\Tarea 13\\Fichero.txt","w") as copia:
        while 1:
            linea = fichero.readline()
            linea2 = fichero.readline()
            linea3 = fichero.readline()

            if linea == "":
                break

