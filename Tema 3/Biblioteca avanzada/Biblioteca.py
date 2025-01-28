import sqlite3

def abir():
    global conexion
    global cursor
    conexion = sqlite3.connect("biblio.bd")
    cursor = conexion.cursor()

def listar():
    conexion.commit()
    libros = cursor.fetchall()
    for i in libros:
        print(i)

def crear():
    try:
        cursor.execute("DROP TABLE IF EXISTS libros")
        cursor.execute("CREATE TABLE IF NOT EXISTS libros(id INT PRIMARY KEY, titulo TEXT, autor TEXT, genero TEXT, anio_publi INT)")
    except:
        print("No se ha podido crear la tabla.")

def insertar(id, titulo, autor, genero, anio_publi):
    try:
        cursor.execute("INSERT INTO libros(id, titulo, autor, genero, anio_publi)VALUES (?, ?, ?, ?, ?)", (id, titulo, autor, genero, anio_publi))
        
    except:
        print("Ha ocurrido un error al intentar introducir un libro en la base de datos.")

def ver_libros():
    try:
        cursor.execute("SELECT * FROM libros")
        listar()
    except:
        print("Ha ocurrido un error al intentar visualizar los libros.")

def verxautor(autor):
    try:
        cursor.execute("SELECT * FROM libros WHERE autor = ?", (autor, ))
        listar()
    except:
        print("Ha ocurrido un error al intentar ver los libros por ese autor.")

def ver_anio_mayor(anio_publi):
    try:
        cursor.execute("SELECT * FROM libros WHERE anio_publi > ? ", (anio_publi, ))
        listar()
    except:
        print("Ha ocurrido un error al intentar listar los libros a partir de ese año.")

def verxgenero(genero):
    try:
        cursor.execute("SELECT * FROM libros WHERE genero = ?", (genero, ))
        listar()
    except:
        print("Ha ocurrido un error al intentar listar los libros por ese género")



abir()
crear()
insertar(1, "La sombra", "Stephen", "Terror", 1900)
insertar(2, "La madre", "Stephen", "Terror", 1900)
insertar(3, "La hija", "King", "Fantasia", 1900)
insertar(4, "La nieta", "Stephen", "Terror", 1800)
ver_libros()
verxautor("Stephen")
ver_anio_mayor(1899)
verxgenero("Fantasia")

conexion.close()