import sqlite3

conexion = sqlite3.connect("base.db")
cursor = conexion.cursor()

cursor.execute("DROP TABLE IF EXISTS usuarios")
cursor.execute("CREATE TABLE IF NOT EXISTS usuarios (id INTEGER PRIMARY KEY AUTOINCREMENT, nombre TEXT, edad INTEGER)")

def insertar_user():
    nombre = input("Introduce el nombre del usuario:\n")
    edad = int(input("Inserta la edad del usuario:\n"))
    cursor.execute("INSERT INTO usuarios (nombre, edad) VALUES (?, ?)", (nombre, edad))
    conexion.commit()

def modificar():
    opcion = 0
    while opcion == 0:
        print("¿Qué deseas modificar?")
        print("1) Nombre")
        print("2) Edad")
        print("3) Ambos")
        opcion = int(input(""))
        if opcion == 1:
            nombre = input("Introduce el nombre del usuario que deseas modificar:\n")
            nombre2 = input("Introduce el nuevo nombre del usuario:\n")
            cursor.execute(f"UPDATE usuarios SET nombre = '{nombre2}' WHERE nombre = '{nombre}'")
            conexion.commit()
        
        elif opcion == 2:
            nombre = input("Introduce el nombre del usuario que deseas modificar:\n")
            edad = int(input("Introduce la nueva edad del usuario:\n"))
            cursor.execute(f"UPDATE usuarios SET edad = {edad} WHERE nombre = '{nombre}'")
            conexion.commit()

        elif opcion == 3:
            nombre = input("Introduce el nombre del usuario que deseas modificar:\n")
            nombre2 = input("Introduce el nuevo nombre del usuario:\n")
            edad = int(input("Introduce la nueva edad del usuario:\n"))
            cursor.execute(f"UPDATE usuarios SET nombre = {nombre2} WHERE nombre = '{nombre}'")
            cursor.execute(f"UPDATE usuarios SET edad = {edad} WHERE nombre = '{nombre2}'")
            conexion.commit()

        else:
            opcion = 0 


def eliminar():
    nombre = input("Introduce el nombre del usuario que deseas eliminar:\n")
    cursor.execute(f"DELETE FROM usuarios WHERE nombre = '{nombre}'")
    conexion.commit()


def mostrar():
    print("¿Deseas ver los usuarios disponibles por nombre o por edad?")
    print("1) Nombre")
    print("2) Edad")
    opcion = int(input(""))
    if opcion == 1:
        cursor.execute("SELECT nombre FROM usuarios")
        usuarios = cursor.fetchall()
        i=1
        for us in usuarios:
            print(f"Usuario {i}:{us}")
            i+=1
        
    elif opcion == 2:
        cursor.execute("SELECT edad FROM usuarios")
        usuarios = cursor.fetchall()
        i=1
        for us in usuarios:
            print(f"Usuario {i}:{us}")
            i+=1

    else:
            opcion = 0 

    
insertar_user()
insertar_user()
insertar_user()
modificar()
eliminar()
mostrar()