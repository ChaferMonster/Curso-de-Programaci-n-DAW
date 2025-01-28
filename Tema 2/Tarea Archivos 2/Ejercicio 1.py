
def numero():
    n = 0
    x = int(input("Introduce el número que quieras saber su tabla de multiplicar: "))
    fichero = (f"C:\\Users\\alu\\Desktop\\clase\\Programación\\codigos visual+\\Tema 2\\archivos\\tabladel{x}.txt")

    try:
        
        fich = open(fichero,"r")
        while 1:
            new = fich.readline()
            print (new)
            if new == "":
                break
        fich.close()
    except:
        print("El fichero no existe.")
    
    
numero()
