class Menus:
    def __init__(self, nombre, precio, imagen, ingredientes=None):
        """
        Inicializa un menú con nombre, precio, imagen y opcionalmente una lista de ingredientes.
        
        :param nombre: Nombre del menú (str)
        :param precio: Precio del menú (float o int)
        :param imagen: Imagen asociada al menú (por ejemplo, un objeto PhotoImage de Tkinter)
        :param ingredientes: Lista de ingredientes necesarios para el menú (list of Ingrediente objects)
        """
        self.nombre = nombre
        self.precio = precio
        self.imagen = imagen
        self.ingredientes = ingredientes if ingredientes is not None else []

    def agregar_ingrediente(self, ingrediente):



        """
        Agrega un ingrediente a la lista de ingredientes del menú.
        
        :param ingrediente: Objeto Ingrediente que se agrega al menú.
        """
        self.ingredientes.append(ingrediente)
    

    def __str__(self):
        """
        Retorna la representación en cadena del menú, mostrando el nombre, precio e ingredientes.
        """
        ingredientes_str = ", ".join([i.nombre for i in self.ingredientes]) if self.ingredientes else "Sin ingredientes"
        return f"Menú: {self.nombre}, Precio: {self.precio}, Ingredientes: {ingredientes_str}"
