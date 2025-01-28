diccionario = {}
total = 0
cobrado = 0

def anyadir():
    global total
    
    num = int(input("Introduce el número de factura: "))
    coste = int(input("Introduce el coste de la factura: "))
    total = total + coste
    otro = {
        num:coste
    }
    diccionario.update(otro)
    print(f"Las facturas existentes son {diccionario}")
    print(f"La cantidad pendiente de cobro es de {total}€")
    print(f"La contidad cobrada es de {cobrado}€")

    return total, diccionario

def pagar():
    global cobrado
    fact = int(input("Introduce el número de la factura que deseas pagar: "))
    resto = diccionario.get(fact, "No existe esa factura o ya está pagada.")
    print(resto)
    diccionario.pop(fact, "No existe esa factura o ya está pagada.")
    if resto == True:
        cobrado = cobrado + resto

    print(f"Las facturas existentes son {diccionario}")
    print(f"La cantidad pendiente de cobro es de {total}€")
    print(f"La contidad cobrada es de {cobrado}€")

    return diccionario, cobrado



def menu():
    i = 0
    while i<1:
        print("Lista de facturas: ")
        print(diccionario)
        print("---------------------------")
        print("Que operación deseas hacer: ")
        print("1) Añadir una factura.")
        print("2) Pagar una factura")
        print("3) Terminar")
        opcion = int(input(""))
        if opcion == 1:
            anyadir()
            print("¿Deseas realizar otra operación?")
            print("1) Si")
            print("2) No")
            opi = int(input(""))
            if opi == 2:
                print("ADIÓS")
                i+=1
        elif opcion == 2:
            print("¿Deseas realizar otra operación?")
            print("1) Si")
            print("2) No")
            opi = int(input(""))
            if opi == 2:
                print("ADIÓS")
                i+=1
        elif opcion == 3:
            print(f"Las facturas existentes son {diccionario}")
            print(f"La cantidad pendiente de cobro es de {total}€")
            print(f"La contidad cobrada es de {cobrado}€")
            print("ADIÓS")
            i+=1
        else:
            print("Creo que te has equivocado de opción, vuelve a intentrlo.")

menu()