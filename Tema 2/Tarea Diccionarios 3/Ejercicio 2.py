listaclave = [1,2,"a","b","c"]
listavalores = [3,89,58,"hola"]

diccionario = {}
con = 0
while con<len(listaclave) and con<len(listavalores):
    nuevo_diccionario = {
        listaclave[con]:listavalores[con]
    }
    con +=1
    diccionario.update(nuevo_diccionario)
    print(nuevo_diccionario)
print(nuevo_diccionario)
print(diccionario)