import sqlite3

conexion = sqlite3.connect("bbdd1.db")

cursor = conexion.cursor()

cursor.execute("DROP TABLE IF EXISTS articulos")
cursor.execute("CREATE TABLE IF NOT EXISTS articulos(codigo INT PRIMARY KEY, Descripcion TEXT, Precio REAL)")

cursor.execute("INSERT INTO articulos(Descripcion, Precio, Codigo) VALUES (?, ?, ?)", ("USB 8 GB", 9.99, 1))
cursor.execute("INSERT INTO articulos(Descripcion, Precio, Codigo) VALUES (?, ?, ?)", ("USB 16 GB", 14.99, 2))
cursor.execute("INSERT INTO articulos(Descripcion, Precio, Codigo) VALUES (?, ?, ?)", ("USB 32 GB", 21.99, 3))

conexion.commit()

def ver_tabla():
    cursor.execute("SELECT * FROM articulos")
    articulos = cursor.fetchall()

    print("Articulos de la tienda")

    for i in articulos:
        print(i)

def revision_articulo():
    codigo = int(input("Introduce el código del producto que deseas obtener información: 1, 2 o 3:\n"))
    cursor.execute("SELECT Descripcion, Precio from articulos WHERE Codigo =?", (codigo, ))
    b = cursor.fetchone()
    if b!=None:
        print(b)
    else:
        print("No existe un artículo con ese codigo")

def actualizar():
    print("Vamos a cambiar los precios de los productos a un precio menor")


    cursor.execute("DROP TABLE IF EXISTS articulos")
    cursor.execute("CREATE TABLE IF NOT EXISTS articulos(codigo INT PRIMARY KEY, Descripcion TEXT, Precio REAL)")

    a = 9.99
    b = 14.99
    c = 21.99

    z = True

    while z == True:
        d = float(input(f"Introduce un precio menor a {a}: "))
        e = float(input(f"Introduce un precio menor a {b}: "))
        f = float(input(f"Introduce un precio menor a {c}: "))
        if d < a and e < b and f < c: 
            z = False


    cursor.execute("INSERT INTO articulos(Descripcion, Precio, Codigo) VALUES (?, ?, ?)", ("USB 8 GB", d, 1))
    cursor.execute("INSERT INTO articulos(Descripcion, Precio, Codigo) VALUES (?, ?, ?)", ("USB 16 GB", e, 2))
    cursor.execute("INSERT INTO articulos(Descripcion, Precio, Codigo) VALUES (?, ?, ?)", ("USB 32 GB", f, 3))

    conexion.commit()

    ver_tabla()

ver_tabla()
revision_articulo()
actualizar()
revision_articulo()

conexion.close()