class MaterialBiblioteca:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
        

class libros(MaterialBiblioteca):
    def __init__(self, titulo, autor, genero, unidad):
        super().__init__(titulo, autor)
        self.genero = genero
        self.unidad = unidad

    def mostrar(self):
        print(f"El título del libro es {self.titulo}.")
        print(f"El autor del libro es {self.autor}.")
        print(f"El genero del libro es {self.genero}.")
        print(f"Nos quedan {self.unidad} de unidades de este libro.")
        print("-------------------------")

    def prestar(self):
        if self.unidad>0:
            print(f"Este libro esta disponible para ser prestado. Disfruta")
            self.unidad = self.unidad-1
            print("-------------------------")
        else:
            print("Lo sentimos pero no nos quedan unidades para poder prestar este libro. Podrías escoger otro.")
            print("-------------------------")

    def devolver(self):       
        print(f"Muchas gracias por devolvernos el libro. Esperamos que le haya encantado tanto como a nosotros. \nVuelva pronto")
        self.unidad = self.unidad+1
        print("-------------------------")
        

class revistas(MaterialBiblioteca):
    def __init__(self, titulo, autor, categoria, unidad):
        super().__init__(titulo, autor)
        self.categoria = categoria
        self.unidad = unidad

    def mostrar(self):
        print(f"El título de la revista es {self.titulo}.")
        print(f"El autor de la revista es {self.autor}.")
        print(f"La categoría de la revista es {self.categoria}.")
        print(f"Nos quedan {self.unidad} de unidades de esta revista.")
        print("-------------------------")
        
    def prestar(self):
        if self.unidad>0:
            print(f"Esta revista esta disponible para ser prestada. Disfrute")
            self.unidad = self.unidad-1
            print("-------------------------")
        else:
            print("Lo sentimos pero no nos quedan unidades para poder prestar este libro. Podrías escoger otro.")
            print("-------------------------")

    def devolver(self):       
        print(f"Muchas gracias por devolvernos la revista. Esperamos que le haya encantado tanto como a nosotros. \nVuelva pronto")
        self.unidad = self.unidad+1
        print("-------------------------")


libro1 = libros("The Shadow", "Stephen King", "Terror", 2)

revista1 = revistas("DeCora", "Index", "Moda y varios", 20)

libro1.mostrar()
libro1.prestar()
libro1.devolver()
libro1.prestar()
libro1.mostrar()

revista1.mostrar()
revista1.prestar()
revista1.devolver()
revista1.prestar()
revista1.mostrar()
