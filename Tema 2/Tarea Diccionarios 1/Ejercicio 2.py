fruteria = {
    "Fruta":"Precio",
    "kiwi":1.55,
    "melón":0.55,
    "uva":2.55, 
    "fresa":3.43
}

fruta = input("Introduce la fruta que deseas: ")
kilos = int(input("Introduce el número de kilos que deseas: "))

fruta = fruta.lower()


if fruta in fruteria:
    resultado = fruteria[fruta]*kilos
    
    print(f"El precio de la/el {fruta} es de {resultado}")
else:
    print(f"La fruta {fruta} no la tenemos en esta frutería.")