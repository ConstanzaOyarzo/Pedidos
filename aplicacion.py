import customtkinter as ctk
from tkinter import ttk
import re
from CTkMessagebox import CTkMessagebox
from PIL import Image, ImageTk
from Menus import Menus
from Ingrediente import Ingrediente
from Pedido import Pedido
from Stock import Stock  # Asumiendo que tienes esta clase


class AplicacionConPestanas(ctk.CTk):
    def __init__(self):
        super().__init__()

        # Ventana principal
        self.title("Gestion de ingredientes y pedidos")
        self.geometry("1200x700")

        # Inicializar stock y pedido
        self.stock = Stock()  # Inicializar la clase que maneja los ingredientes
        self.pedido = Pedido()  # Inicializar la clase que maneja el pedido

        self.load_images()
        
        # Crear pestañas
        self.tabview = ctk.CTkTabview(self, width=1200, height=900)
        self.tabview.pack(padx=20, pady=20)

        self.crear_pestanas()

    def load_images(self):
        # Cargar imágenes de los menús
        self.icono_pepsi = ctk.CTkImage(Image.open("icono_pepsi.png").resize((64, 64)))
        self.icono_hamburguesa = ctk.CTkImage(Image.open("icono_hamburguesa.png").resize((64, 64)))
        self.icono_completo = ctk.CTkImage(Image.open("icono_completo.png").resize((64, 64)))
        self.icono_papas_fritas = ctk.CTkImage(Image.open("icono_papas_fritas.png").resize((64, 64)))

    def crear_pestanas(self):
        # Crear y configurar las pestañas
        self.tab1 = self.tabview.add("Ingreso Ingredientes")
        self.tab2 = self.tabview.add("Pedido")

        # Pestañas 1 y 2
        self.configurar_pestana1()
        self.configurar_pestana2()

    def configurar_pestana1(self):
        # Dividir en dos frames
        frame_formulario = ctk.CTkFrame(self.tab1)
        frame_formulario.pack(side="left", fill="both", expand=True, padx=10, pady=10)

        frame_treeview = ctk.CTkFrame(self.tab1)
        frame_treeview.pack(side="right", fill="both", expand=True, padx=10, pady=10)

        # Formulario primer frame
        label_nombre_ingrediente = ctk.CTkLabel(frame_formulario, text="Nombre Ingrediente:")
        label_nombre_ingrediente.pack(pady=5)
        self.entry_nombre_ingrediente = ctk.CTkEntry(frame_formulario)
        self.entry_nombre_ingrediente.pack(pady=5)

        label_cantidad = ctk.CTkLabel(frame_formulario, text="Cantidad:")
        label_cantidad.pack(pady=5)
        self.entry_cantidad = ctk.CTkEntry(frame_formulario)
        self.entry_cantidad.pack(pady=5)

        # Botón de ingreso
        self.boton_ingresar = ctk.CTkButton(frame_formulario, text="Ingresar Ingrediente", command=self.ingresar_ingrediente)
        self.boton_ingresar.pack(pady=10)

        # Botón para eliminar arriba del Treeview
        self.boton_eliminar = ctk.CTkButton(frame_treeview, text="Eliminar Ingrediente", fg_color="black", text_color="white", command=self.eliminar_ingrediente)
        self.boton_eliminar.pack(pady=10)

        # Treeview en el segundo frame
        self.tree = ttk.Treeview(frame_treeview, columns=("Nombre", "Cantidad"), show="headings", height=8)
        self.tree.heading("Nombre", text="Nombre")
        self.tree.heading("Cantidad", text="Cantidad")
        self.tree.pack(expand=True, fill="both", padx=10, pady=10)

        # Botón para generar menú
        self.boton_generar = ctk.CTkButton(frame_treeview, text="Generar menú", fg_color="blue", text_color="white", command=self.boton_generar)
        self.boton_generar.pack(pady=10)

    def configurar_pestana2(self):
        # Frame superior para las tarjetas de menú
        frame_imagenes = ctk.CTkFrame(self.tab2)
        frame_imagenes.pack(side="top", fill="x", padx=10, pady=10)

        # Frame inferior para mostrar el pedido y los botones
        frame_pedido = ctk.CTkFrame(self.tab2)
        frame_pedido.pack(side="top", fill="both", expand=True, padx=10, pady=10)

        # Frame para el total y el botón de eliminar menú
        frame_total_botones = ctk.CTkFrame(frame_pedido)
        frame_total_botones.pack(side="top", fill="x", padx=10, pady=10)

        # Botón para eliminar un menú
        self.boton_eliminar_menu = ctk.CTkButton(frame_total_botones, text="Eliminar Menú", fg_color="black", text_color="white", command=self.eliminar_menu)
        self.boton_eliminar_menu.pack(side="right", padx=10, pady=10)

        # Etiqueta para mostrar el total
        self.label_total = ctk.CTkLabel(frame_total_botones, text="Total: $0.00", anchor="e")
        self.label_total.pack(side="right", padx=10)

        # Treeview para mostrar el pedido
        self.tree_pedido = ttk.Treeview(frame_pedido, columns=("Nombre del menú", "Cantidad", "Precio unitario"), show="headings", height=8)
        self.tree_pedido.heading("Nombre del menú", text="Nombre del menú")
        self.tree_pedido.heading("Cantidad", text="Cantidad")
        self.tree_pedido.heading("Precio unitario", text="Precio unitario")
        self.tree_pedido.pack(fill="both", padx=10, pady=10)

        # Botón para generar boleta
        self.boton_generar_boleta = ctk.CTkButton(frame_pedido, text="Generar Boleta", fg_color="blue", text_color="white", command=self.generar_boleta)
        self.boton_generar_boleta.pack(side="bottom", pady=10)

        # Crear tarjetas de menú con imágenes
        self.menus = [
            Menus("Papas Fritas", 500, self.icono_papas_fritas),
            Menus("Completo", 1800, self.icono_completo),
            Menus("Pepsi", 1100, self.icono_pepsi),
            Menus("Hamburguesa", 3500, self.icono_hamburguesa)
        ]

        for menu in self.menus:
            self.crear_tarjeta(menu, frame_imagenes)

    def ingresar_ingrediente(self):
        nombre = self.entry_nombre_ingrediente.get()
        cantidad = self.entry_cantidad.get()

        if not nombre or not cantidad:
            CTkMessagebox(title="Error", message="Por favor, completa todos los campos.", icon="warning")
            return

        if not cantidad.isdigit():
            CTkMessagebox(title="Error", message="La cantidad debe ser un número.", icon="warning")
            return

        self.tree.insert("", "end", values=(nombre, cantidad))
        self.entry_nombre_ingrediente.delete(0, 'end')
        self.entry_cantidad.delete(0, 'end')

    def eliminar_ingrediente(self):
        seleccion = self.tree.selection()

        if not seleccion:
            CTkMessagebox(title="Error", message="Por favor, selecciona un ingrediente para eliminar.", icon="warning")
            return

        self.tree.delete(seleccion)

    def boton_generar(self):
        CTkMessagebox(title="Generar Menú", message="Menú generado en base a los ingredientes ingresados.", icon="info")

    def actualizar_treeview_pedido(self):
    #Actualiza el Treeview con la lista de menús del pedido.
    
    # Limpiar el Treeview actual
        for row in self.tree_pedido.get_children():
            self.tree_pedido.delete(row)

        # Insertar los menús actualizados en el Treeview
        for item in self.pedido.menus:
            menu = item['menu']  # Objeto Menus
            cantidad = item['cantidad']  # Cantidad
            precio_unitario = menu.precio  # Precio unitario del menú

            # Insertar los valores en el Treeview
            self.tree_pedido.insert("", "end", values=(menu.nombre, cantidad, f"${precio_unitario:.2f}"))


    def eliminar_menu(self):
        seleccion = self.tree_pedido.selection()
        if not seleccion:
            CTkMessagebox(title="Error", message="Por favor, selecciona un menú para eliminar.", icon="warning")
            return

        item = self.tree_pedido.item(seleccion)
        nombre_menu = item['values'][0]

        self.pedido.eliminar_menu(nombre_menu)
        self.actualizar_treeview_pedido()

        total = self.pedido.calcular_total()
        self.label_total.configure(text=f"Total: ${total:.2f}")

    def generar_boleta(self):
        total = self.pedido.calcular_total()
        CTkMessagebox(title="Boleta Generada", message=f"Total del pedido: ${total:.2f}", icon="info")

    def crear_tarjeta(self, menu, tarjetas_frame):

        num_tarjetas = len(self.menus)
        for num_tarjetas, menu in enumerate(self.menus):
            fila = num_tarjetas // 2
            columna = num_tarjetas % 2

            tarjeta = ctk.CTkFrame(tarjetas_frame, corner_radius=10, border_width=2)
            tarjeta.grid(row=fila, column=columna, padx=10, pady=10)

            imagen_label = ctk.CTkLabel(tarjeta, image=menu.imagen, text="")
            imagen_label.pack()

            nombre_label = ctk.CTkLabel(tarjeta, text=menu.nombre)
            nombre_label.pack()

            tarjeta.bind("<Button-1>", lambda event, m=menu: self.tarjeta_click(m))

    def tarjeta_click(self, menu):
        if self.stock.verificar_stock(menu):
            self.pedido.agregar_menu(menu)
            self.actualizar_treeview_pedido()

            total = self.pedido.calcular_total()
            self.label_total.configure(text=f"Total: ${total:.2f}")
        else:
            CTkMessagebox(title="Stock Insuficiente", message=f"No hay suficiente stock para {menu.nombre}", icon="warning")


if __name__ == "__main__":
    app = AplicacionConPestanas()
    app.mainloop()
