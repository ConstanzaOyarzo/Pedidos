import customtkinter as ctk
from tkinter import ttk
import re
from CTkMessagebox import CTkMessagebox
from PIL import Image, ImageTk
from Menus import Menus

class AplicacionConPestanas(ctk.CTk):
    def __init__(self):
        super().__init__() # ????

        # Ventana principal
        self.title("Gestion de ingredientes y pedidos")
        self.geometry("1200x700")

        # Iniciar ingredientes ??

        # self.ingredientes = Ingredientes() ???

        # Crear pestañas
        self.tabview = ctk.CTkTabview(self, width=1200, height=900)
        self.tabview.pack(padx=20, pady=20)

        self.crear_pestanas()

    def crear_pestanas(self):
        # Crear y configurar las pestanas
        self.tab1 = self.tabview.add("Ingreso Ingredientes")
        self.tab2 = self.tabview.add("Pedido")

        # Pestana 1 y 2
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

        # Boton ingreso
        self.boton_ingresar = ctk.CTkButton(frame_formulario, text="Ingresar Ingrediente")
        self.boton_ingresar.configure(command=self.ingresar_ingrediente)
        self.boton_ingresar.pack(pady=10)
        

        # Botón para eliminar arriba del Treeview
        self.boton_eliminar = ctk.CTkButton(frame_treeview, text="Eliminar Ingrediente", fg_color="black", text_color="white")
        self.boton_eliminar.configure(command=self.eliminar_ingrediente)
        self.boton_eliminar.pack(pady=10)

        # Treeview en el segundo frame
        self.tree = ttk.Treeview(frame_treeview, columns=("Nombre", "Cantidad"), show="headings", height=8)

        self.tree.heading("Nombre", text="Nombre")
        self.tree.heading("Cantidad", text="Cantidad")

        self.tree.pack(expand=True, fill="both", padx=10, pady=10)
        # Botón para generar arriba del Treeview
        self.boton_generar = ctk.CTkButton(frame_treeview, text="Generar menú", fg_color="blue", text_color="white")
        self.boton_generar.configure(command=self.boton_generar)
        self.boton_generar.pack(pady=10)

    def configurar_pestana2(self):
        # Frame superior para las tarjetas de menú
        frame_imagenes = ctk.CTkFrame(self.tab2)
        frame_imagenes.pack(side="top", fill="x", padx=10, pady=10)

        # Frame inferior para mostrar el pedido y los botones
        frame_pedido = ctk.CTkFrame(self.tab2)
        frame_pedido.pack(side="top", fill="both", expand=True, padx=10, pady=10)

        # Frame para el total y el botón de eliminar menú (arriba de la tabla)
        frame_total_botones = ctk.CTkFrame(frame_pedido)
        frame_total_botones.pack(side="top", fill="x", padx=10, pady=10)

        # Botón para eliminar un menú
        self.boton_eliminar_menu = ctk.CTkButton(frame_total_botones, text="Eliminar Menú", fg_color="black", text_color="white")
        self.boton_eliminar_menu.pack(side="right", padx=10, pady=10)

        # Etiqueta para mostrar el total (alineada a la derecha)
        self.label_total = ctk.CTkLabel(frame_total_botones, text="Total: $0.00", anchor="e")
        self.label_total.pack(side="right", padx=10)

        # Treeview para mostrar el pedido
        self.tree_pedido = ttk.Treeview(frame_pedido, columns=("Nombre del menú", "Cantidad", "Precio unitario"), show="headings", height=8)
        self.tree_pedido.heading("Nombre del menú", text="Nombre del menú")
        self.tree_pedido.heading("Cantidad", text="Cantidad")
        self.tree_pedido.heading("Precio unitario", text="Precio unitario")
        self.tree_pedido.pack(fill="both", padx=10, pady=10)

        # Botón para generar la boleta (debajo de la tabla, centrado)
        self.boton_generar_boleta = ctk.CTkButton(frame_pedido, text="Generar Boleta", fg_color="blue", text_color="white")
        self.boton_generar_boleta.pack(side="bottom", pady=10)

        # Cargar imágenes de los menús
        icono_pepsi = ImageTk.PhotoImage(Image.open("icono_pepsi.png"))
        icono_hamburguesa = ImageTk.PhotoImage(Image.open("icono_hamburguesa.png"))
        icono_completo = ImageTk.PhotoImage(Image.open("icono_completo.png"))
        icono_papas_fritas = ImageTk.PhotoImage(Image.open("icono_papas_fritas.png"))

        # instancias
        papas_fritas = Menus("Papas Fritas", 500, self.icono_papas_fritas)
        completo = Menus("Completo", 1800, self.icono_completo)
        pepsi = Menus("Pepsi", 1100, self.icono_pepsi)
        hamburguesa = Menus("Hamburguesa", 3500, self.icono_hamburguesa)

        # for menu in self.menus:
        #     self.crear_tarjeta(menu, frame_imagenes)

    def ingresar_ingrediente(self):
        pass

    def eliminar_ingrediente(self):
        pass
    
    # Instancia de menu
    # menu = Menus(menu, precio, ingredientes)


# metodo de ayuda para crear targetas con menus solicitados
    def crear_tarjeta(self, menu):
        # Obtener el número de columnas y filas actuales
        num_tarjetas = len(self.menus_creados)
        fila = num_tarjetas // 2
        columna = num_tarjetas % 2

        # Crear la tarjeta con un tamaño fijo
        tarjeta = ctk.CTkFrame(tarjetas_frame, corner_radius=10, border_width=1, border_color="#4CAF50", width=64, height=140, fg_color="transparent")
        tarjeta.grid(row=fila, column=columna, padx=15, pady=15)

        # Hacer que la tarjeta sea completamente clickeable 
        tarjeta.bind("<Button-1>", lambda event: self.tarjeta_click(event, menu))

        # Cambiar el color del borde cuando el mouse pasa sobre la tarjeta
        tarjeta.bind("<Enter>", lambda event: tarjeta.configure(border_color="#FF0000"))  # Cambia a rojo al pasar el mouse
        tarjeta.bind("<Leave>", lambda event: tarjeta.configure(border_color="#4CAF50"))  # Vuelve al verde al salir

        # Verifica si hay una imagen asociada con el menú
        if menu.icono_menu:
            # Crear y empaquetar el CTkLabel con la imagen, sin texto y con fondo transparente
            imagen_label = ctk.CTkLabel(tarjeta, image=menu.icono_menu, width=64, height=64, text="", bg_color="transparent")
            imagen_label.pack(anchor="center", pady=5, padx=10)
            imagen_label.bind("<Button-1>", lambda event: self.tarjeta_click(event, menu))  # Asegura que el clic en la imagen funcione

            # Agregar un Label debajo de la imagen para mostrar el nombre del menú
            texto_label = ctk.CTkLabel(tarjeta, text=f"{menu.nombre}", text_color="black", font=("Helvetica", 12, "bold"), bg_color="transparent")
            texto_label.pack(anchor="center", pady=1)
            texto_label.bind("<Button-1>", lambda event: self.tarjeta_click(event, menu))  # Asegura que el clic en el texto funcione

        else:
            print(f"No se pudo cargar la imagen para el menú '{menu.nombre}'")

    #codigo de ayuda para desarrollar el evento que se debe gatillar, cuando se presiona cada targeta(Menu)
    def tarjeta_click(self, event, menu):
            # Verificar si hay suficientes ingredientes en el stock para preparar el menú
            suficiente_stock = True
            if self.stock.lista_ingredientes == []:
                suficiente_stock = False
            for ingrediente_necesario in menu.ingredientes:
                for ingrediente_stock in self.stock.lista_ingredientes:
                    if ingrediente_necesario.nombre == ingrediente_stock.nombre:
                        if int(ingrediente_stock.cantidad) < int(ingrediente_necesario.cantidad):
                            suficiente_stock = False
                            break
                if not suficiente_stock:
                    break
            
            if suficiente_stock:
                # Descontar los ingredientes del stock
                for ingrediente_necesario in menu.ingredientes:
                    for ingrediente_stock in self.stock.lista_ingredientes:
                        if ingrediente_necesario.nombre == ingrediente_stock.nombre:
                            ingrediente_stock.cantidad = str(int(ingrediente_stock.cantidad) - int(ingrediente_necesario.cantidad))
                
                # Agregar el menú al pedido
                self.pedido.agregar_menu(menu)
                
                # Actualizar el Treeview
                self.actualizar_treeview_pedido()

                # Actualizar el total del pedido
                total = self.pedido.calcular_total()
                self.label_total.configure(text=f"Total: ${total:.2f}")
            else:
                # Mostrar un mensaje indicando que no hay suficientes ingredientes usando CTkMessagebox
                CTkMessagebox(title="Stock Insuficiente", message=f"No hay suficientes ingredientes para preparar el menú '{menu.nombre}'.", icon="warning")


#iniciacion de pantalla
if __name__ == "__main__":
    ctk.set_appearance_mode("System")
    ctk.set_default_color_theme("blue")

    app = AplicacionConPestanas()
    app.mainloop()

    
