class Menus:
    def __init__(self, nombre, precio, imagen, ingredientes=None):
        self.nombre = nombre
        self.precio = precio
        self.imagen = imagen
        self.ingredientes = ingredientes if ingredientes is not None else []

<<<<<<< HEAD
    def agregar_ingrediente(self, ingrediente):



        """
        Agrega un ingrediente a la lista de ingredientes del menú.
        
        :param ingrediente: Objeto Ingrediente que se agrega al menú.
        """
        self.ingredientes.append(ingrediente)
    
=======
    # def agregar_ingrediente(self, ingrediente):
    #     self.ingredientes.append(ingrediente)
>>>>>>> 2fa6c08071a02ec14cb481d3f0a4905c320338f7

    def __str__(self):
        return f"M{self.nombre}, {self.precio}, {self.imagen}"
