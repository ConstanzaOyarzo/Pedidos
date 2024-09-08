class Menus:
    def __init__(self, nombre, precio, icono_menu):
        self.nombre = nombre
        self.precio = precio
        self.icono_menu = icono_menu
        # self.ingredientes = []

    def __str__(self):
        return f"{self.nombre}, {self.precio}, {self.icono_menu}"
    
    # def agregar_menu(self, menu):
    #     pass