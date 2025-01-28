def mayusculas(funcion):
    def decorador():
        result = funcion()
        return result.upper()
    return decorador

@mayusculas
def inicio():
    return "Buenos días"

@mayusculas
def interludio():
    return "Buenas tardes"

@mayusculas
def final():
    return "Buenas noches"

print(inicio())
print(interludio())
print(final())