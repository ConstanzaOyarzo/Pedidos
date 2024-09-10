class Pedido:
    def __init__(self):
        self.menus = []  # Lista de menús en el pedido

    def agregar_menu(self, menu):
        for item in self.menus:
            if item['menu'].nombre == menu.nombre:
                item['cantidad'] += 1
                return
        self.menus.append({"menu": menu, "cantidad": 1})

    def eliminar_menu(self, nombre_menu):
        self.menus = [item for item in self.menus if item['menu'].nombre != nombre_menu]

    def calcular_total(self):
        total = 0
        for item in self.menus:
            total += item['menu'].precio * item['cantidad']
        return total

    def obtener_detalles(self):
        detalles = []
        for item in self.menus:
            menu = item['menu']
            detalles.append({
                "nombre": menu.nombre,
                "cantidad": item['cantidad'],
                "precio_unitario": menu.precio
            })
        return detalles