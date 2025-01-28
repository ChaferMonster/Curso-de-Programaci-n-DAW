diccionaro = {
    1:"a",
    2:23,
    3:1,
    5:6,
    23:"r"
}

valores = diccionaro.values()
print (valores)
suma_total = 0

for i in valores:

    b = type(i)
    
    if b == int:
        suma_total = suma_total+i

print (suma_total)