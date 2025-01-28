def negativo(funcion):
    def decorador(self):
        if self.precio < 0:
            return print("Ha habido un error con el precio del producto")
        return funcion(self)
    return decorador


class productos():
    
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio


class productosConDescuento(productos):
    
    def __init__(self, nombre, precio, descuento):
        super().__init__(nombre, precio)
        self.descuento = descuento

    @negativo
    def hacerDescuento(self):
        self.precio = self.precio - (self.precio*self.descuento/100)
        print(f"Precio del producto {self.nombre} es de {self.precio}€")


class libro(productosConDescuento):
    
    def __init__(self, nombre, precio, descuento):
        super().__init__(nombre, precio, descuento)

class ropa(productosConDescuento):
    
    def __init__(self, nombre, precio, descuento):
        super().__init__(nombre, precio, descuento)

class material(productosConDescuento):
    
    def __init__(self, nombre, precio, descuento):
        super().__init__(nombre, precio, descuento)

libro1 = libro("Python para expertos", 25, 20)
ropa1 = ropa("Abrigo rojo mujer", 49, 10)
libro2 = libro("Libro", -13, 5)

libro1.hacerDescuento()
ropa1.hacerDescuento()
libro2.hacerDescuento()