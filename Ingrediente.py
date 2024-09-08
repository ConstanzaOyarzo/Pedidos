class Ingrediente:
    def __init__(self, nombre, cantidad):
        """
        Inicializa un ingrediente con nombre y cantidad.
        
        :param nombre: Nombre del ingrediente (str)
        :param cantidad: Cantidad del ingrediente (int o float)
        """
        self.nombre = nombre
        self.cantidad = cantidad

    def __str__(self):
        """
        Retorna la representación en cadena del ingrediente.
        """
        return f"{self.nombre}: {self.cantidad}"
