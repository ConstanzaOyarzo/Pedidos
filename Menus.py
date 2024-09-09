class Menus:
    def __init__(self, nombre, precio, imagen, ingredientes=None):
        self.nombre = nombre
        self.precio = precio
        self.imagen = imagen
        self.ingredientes = ingredientes if ingredientes is not None else []

    # def agregar_ingrediente(self, ingrediente):
    #     self.ingredientes.append(ingrediente)

    def __str__(self):
        return f"M{self.nombre}, {self.precio}, {self.imagen}"
