fich = input("Introduce la ruta: ")
def escribe(fich):
    fichero = open (fich,"w")
    mensaje = input("Introduce el mensaje que deseas escribir: ")

    fichero.write(mensaje +"\n")
    fichero.close()


def lee(fich):
    fichero = open (fich,"r")
    while 1:
            linea = fichero.readline()
            print(linea)
            if linea == "":
                break
    fichero.close()

escribe(fich)
lee(fich)