#Ejercicio 1
def calculo(r, h, n):
    global m
    m = (h*r)/(1-(1+r)**(-12*n))
    return m


def r(i):
    global c
    c = i/(100*12)
    return c
    

def bucle():
    b = 0
    while b < 1:
        print("VAMOS A CALCULAR LA MENSUALIDAD DE UNA HIPOTECA: ")
        h = int(input("1) Introduce la hipoteca: "))
        n = int(input("2) Introduce el total de años a pagar: "))
        i = float(input("3) Introduce el interés anual: "))
        r(i)
        calculo(c, h, n)
        round(m,2)
        print(f"La cuota mensual con los datos introducidos son: {m}€")
        cont = input("¿Deseas calcular otra cuota mensual?: ")
        print("1) Si")
        print("2) No")
        if cont == 2:
            b+=1
        elif cont != 1 and cont !=2:    
            print("Has seleccionado una opción incorrecta. SYSTEM ERROR") 
        else:
            print("ADIÓS")

bucle()


#Ejercicio 2
from math import*
def area(s,a,b,v):
    global z
    z = sqrt(s*(s-a)*(s-b)*(s-v)) 
    return z


def s(a,b,v):
    global s
    s = (a+b+v)/2.
    return s
a = int(input("Dime un lado del triángulo: "))
b = int(input("Dime otro lado del triángulo: "))
v = int(input("Dime otro lado del triángulo: "))

s(a,b,v)
area(s,a,b,v)

print(f" El área del triángulo es {z}")