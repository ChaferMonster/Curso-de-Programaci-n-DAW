
num1 = input("Introduce el número archivo que deséas buscar: ")
num2 = int(input("Introduce el número de la línea que deseas revisar: "))

def operacion():
    cont = 1
    
    try:
        fich = open (f"C:\\Users\\alvar\\Desktop\\Grado superior\\Programación\\Tema 2\\Tarea Archivos 2\\Archivos para tareas-20241125\\tabladel{num1}.txt", "r")
        while 1:
            linea = fich.readline()
            if cont == num2:
                print(f"La línea solicitada es {linea}")
                break
            cont+=1
    except:
        print("El fichero introducido no existe")
operacion()