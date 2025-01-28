cena = {"Martin","Hugo","Turpin", "David"}
juegos = {"David","Lou","Tomas", "Turpin"}


cena = set(cena)
juegos = set(juegos)

fiesta = cena.union(juegos)
print(f"Todas las personas que han asistido a la fiesta son {fiesta}")

cenajuego = cena & juegos
print(f"Todas las personas que han asistido a la cena y a los juegos son {cenajuego}")

solocena = cena - juegos
print(f"Todas las personas que solo han asistido a la cena son {solocena}")

solojuegos = juegos - cena
print(f"Todas las personas que solo han asistido a los juegos son {solojuegos}")

fiesta = cena.union(juegos)
print(f"Todas las personas que han asistido a la cena o a la sesión de juegos son {fiesta}")

simetria = cena ^ juegos 
print(f"Todas las personas que han asistido a la cena o a los juegos  son {simetria}")
