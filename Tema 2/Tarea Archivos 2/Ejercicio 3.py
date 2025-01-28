from urllib.request import urlopen
ruta = input("Introduce la ruta del archivo que deseas leer:  ")
contador = 0
abri = urlopen(ruta)
for linea in abri:
    linea_nueva = ""
    linea_nueva = linea.split()
    print(linea_nueva)
    contador = contador + len(linea_nueva)
    

print(contador)


