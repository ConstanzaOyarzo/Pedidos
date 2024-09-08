class Pedido:
    def __init__(self):
        """
        Inicializa un pedido vacío.
        """
        self.menus = []  # Lista de menús en el pedido

    def agregar_menu(self, menu):
        """
        Agrega un menú al pedido. Si ya existe, incrementa la cantidad.
        
        :param menu: Objeto Menus que se agrega al pedido.
        """
        for item in self.menus:
            if item['menu'].nombre == menu.nombre:
                item['cantidad'] += 1
                return
        self.menus.append({"menu": menu, "cantidad": 1})

    def eliminar_menu(self, nombre_menu):
        """
        Elimina un menú del pedido según el nombre.
        
        :param nombre_menu: Nombre del menú a eliminar (str)
        """
        self.menus = [item for item in self.menus if item['menu'].nombre != nombre_menu]

    def calcular_total(self):
        """
        Calcula el costo total del pedido sumando los precios de los menús.
        
        :return: Total del pedido (float)
        """
        total = 0
        for item in self.menus:
            total += item['menu'].precio * item['cantidad']
        return total
