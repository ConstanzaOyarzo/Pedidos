class Stock:
    def __init__(self):
        """
        Inicializa el stock vacío.
        """
        self.ingredientes = {}  # Diccionario para almacenar los ingredientes y sus cantidades

    def agregar_ingrediente(self, nombre, cantidad):
        """
        Agrega una cierta cantidad de un ingrediente al stock.
        
        :param nombre: Nombre del ingrediente (str)
        :param cantidad: Cantidad del ingrediente (int o float)
        """
        if nombre in self.ingredientes:
            self.ingredientes[nombre] += cantidad
        else:
            self.ingredientes[nombre] = cantidad

    def eliminar_ingrediente(self, nombre):
        """
        Elimina completamente un ingrediente del stock.
        
        :param nombre: Nombre del ingrediente a eliminar (str)
        """
        if nombre in self.ingredientes:
            del self.ingredientes[nombre]

    def verificar_stock(self, menu):
        """
        Verifica si hay suficiente stock para los ingredientes de un menú.
        
        :param menu: Objeto Menus para verificar el stock.
        :return: True si hay suficiente stock, False en caso contrario.
        """
        for ingrediente in menu.ingredientes:
            if ingrediente.nombre not in self.ingredientes or self.ingredientes[ingrediente.nombre] < ingrediente.cantidad:
                return False
        return True

    def consumir_ingredientes(self, menu):
        """
        Consume los ingredientes necesarios para un menú, disminuyendo las cantidades del stock.
        
        :param menu: Objeto Menus del cual se consumen los ingredientes.
        """
        if self.verificar_stock(menu):
            for ingrediente in menu.ingredientes:
                self.ingredientes[ingrediente.nombre] -= ingrediente.cantidad
        else:
            raise Exception(f"No hay suficiente stock para {menu.nombre}")
