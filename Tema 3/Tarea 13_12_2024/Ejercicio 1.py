#Creamos el diccionario
diccionario = {}

#Abrimos el archivo deseado en modo lectura y abrimos el archivo deseado a escribir en modo escritura.
with open ("C:\\Users\\alu\Desktop\\clase\\Programación\codigos visual+\\Tema 3\\Tarea 13_12_2024\\archivo.txt","r") as archivo:
    with open ("C:\\Users\\alu\Desktop\\clase\\Programación\codigos visual+\\Tema 3\\Tarea 13_12_2024\\nuevo_archivo.txt","w") as nuevo:
        while True:
            #Leemos cada linea
            nombre = archivo.readline()
            
            apellido = archivo.readline()
            
            edad = archivo.readline()

            #Añadimos al nuevo archivo las lineas en el orden deseado
            nuevo.write(apellido)
            nuevo.write(nombre)
            nuevo.write(edad)

            #Comprobamos de esta manera si la última línea está vacía
            if edad == "":
                break
            
            #Añadimos al diccionario la clave y el valor en una lista ya que son dos y los queremos con la misma llave.
            otrodiccionario= {
                nombre[:-1]:[apellido[:-1],edad[:-1]]
                }
            diccionario.update(otrodiccionario)        
        
print(diccionario)