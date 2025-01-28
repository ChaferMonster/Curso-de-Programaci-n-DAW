import sqlite3

conexion = sqlite3.connect("Music.db")

cursor = conexion.cursor()

cursor.execute("DROP TABLE IF EXISTS Temazos")
cursor.execute("CREATE TABLE IF NOT EXISTS Temazos (Título TEXT PRIMARY KEY, nºReproducciones INTEGRER)")

cursor.execute("INSERT INTO Temazos (Título, nºReproducciones) VALUES (?, ?)", ("A Sky Full of Stars ", 1000000000))
cursor.execute("INSERT INTO Temazos (Título, nºReproducciones) VALUES (?, ?)", ("Una foto en blanco y negro ", 1200000000))


conexion.commit()

cursor.execute("SELECT * FROM Temazos")
resultados = cursor.fetchall() #Contiene los resultados


print("Canciones guardadas: ")
for cancion in resultados:
    print(f"Título: {cancion[0]}\n NºReproducciones: {cancion[1]}")

conexion.close()