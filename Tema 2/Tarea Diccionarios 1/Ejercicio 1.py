nombre = input("Introduce tu nombre: ")
dni = input("Introduce tu dni: ")
edad = int(input("Introduce tu edad: "))
direcc = input("Introduce la ciudad donde vives: ")
tel = int(input("Introduce tu teléfono: "))

diccionario = {
    "nombre":nombre,
    "DNI":dni,
    "edad":edad,
    "dirección":direcc,
    "teléfono":tel
    } 

print(f"{diccionario['nombre']} con DNI {diccionario['DNI']} tiene {diccionario["edad"]} años, vive en {diccionario['dirección']} y su número de teléfono es {diccionario['teléfono']}")                                                                                                                                               

