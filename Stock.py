class Stock:
    def __init__(self):
        self.ingredientes = {
            "papas": 0,
            "bebida": 0,
            "vienesa": 0,
            "pan completo": 0,
            "tomate": 0,
            "palta": 0,
            "pan hamburguesa": 0,
            "queso": 0,
            "churrasco de carne": 0
        }

# Diccionario para almacenar los ingredientes y sus cantidades

    def agregar_ingrediente(self, nombre, cantidad):
        if nombre in self.ingredientes:
            self.ingredientes[nombre] += cantidad
        else:
            self.ingredientes[nombre] = cantidad

    def eliminar_ingrediente(self, nombre):
        if nombre in self.ingredientes:
            del self.ingredientes[nombre]

    # def verificar_stock(self, menu):
    #     for ingrediente in menu.ingredientes:
    #         if ingrediente.nombre not in self.ingredientes or self.ingredientes[ingrediente.nombre] < ingrediente.cantidad:
    #             return False
    #     return True

    def consumir_ingredientes(self, menu):
        if self.verificar_stock(menu):
            for ingrediente in menu.ingredientes:
                self.ingredientes[ingrediente.nombre] -= ingrediente.cantidad
        else:
            raise Exception(f"No hay suficiente stock para {menu.nombre}")
