import customtkinter as ctk
from tkinter import ttk
import re
from CTkMessagebox import CTkMessagebox
from PIL import Image, ImageTk
from Menus import Menus
from Ingrediente import Ingrediente
from Pedido import Pedido
from Stock import Stock  
from fpdf import FPDF
import os
from datetime import datetime


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
        self.icono_pepsi = ctk.CTkImage(Image.open("icono_pepsi.png"), size=(64, 64))
        self.icono_hamburguesa = ctk.CTkImage(Image.open("icono_hamburguesa.png"), size=(64, 64))
        self.icono_completo = ctk.CTkImage(Image.open("icono_completo.png"), size=(64, 64))
        self.icono_papas_fritas = ctk.CTkImage(Image.open("icono_papas_fritas.png"), size=(64, 64))

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
        self.boton_eliminar = ctk.CTkButton(frame_treeview, text="Eliminar Ingrediente", command=self.eliminar_ingrediente)
        self.boton_eliminar.pack(pady=10)

        # Treeview en el segundo frame
        self.tree = ttk.Treeview(frame_treeview, columns=("Nombre", "Cantidad"), show="headings", height=8)
        self.tree.heading("Nombre", text="Nombre")
        self.tree.heading("Cantidad", text="Cantidad")
        self.tree.pack(expand=True, fill="both", padx=10, pady=10)

        # Botón para generar menú
        self.boton_generar = ctk.CTkButton(frame_treeview, text="Generar menú", command=self.boton_generar)
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
        self.boton_eliminar_menu = ctk.CTkButton(frame_total_botones, text="Eliminar Menú", command=self.eliminar_menu)
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
        self.boton_generar_boleta = ctk.CTkButton(frame_pedido, text="Generar Boleta", command=self.generar_boleta)
        self.boton_generar_boleta.pack(side="bottom", pady=10)

        # Crear tarjetas de menú con imágenes
        self.menus = [
        Menus("Papas Fritas", 500, self.icono_papas_fritas, {"papas": 5}),
        Menus("Completo", 1800, self.icono_completo, {
            "vienesa": 1,
            "pan completo": 1,
            "tomate": 1,
            "palta": 1
        }),
        Menus("Pepsi", 1100, self.icono_pepsi, {"bebida": 1}),
        Menus("Hamburguesa", 3500, self.icono_hamburguesa, {
            "pan hamburguesa": 1,
            "queso": 1,
            "churrasco de carne": 1
        })
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
            menu = item['menu']
            cantidad = item['cantidad']
            precio_unitario = menu.precio

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
        # Genera la boleta en formato PDF usando los detalles del pedido.
        detalles_pedido = self.pedido.obtener_detalles()
        total = self.pedido.calcular_total()
        iva = total * 0.19
        total_final = total + iva

        # Crear PDF
        pdf = FPDF()
        pdf.add_page()

        pdf.set_font("Arial", 'B', 16)
        pdf.cell(200, 10, "Boleta Restaurante", ln=True, align='C')

        pdf.set_font("Arial", size=12)
        pdf.cell(200, 10, "Razón Social del Negocio", ln=True, align='L')
        pdf.cell(200, 10, "RUT: 12.345.678-9", ln=True, align='L')
        pdf.cell(200, 10, "Dirección: Calle Falsa 123, Ciudad", ln=True, align='L')
        pdf.cell(200, 10, "Teléfono: +56 9 1234 5678", ln=True, align='L')
        pdf.cell(200, 10, f"Fecha: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}", ln=True, align='L')
        pdf.ln(10)

        # Agregar los detalles del pedido
        pdf.set_font("Arial", 'B', 12)
        pdf.cell(50, 10, "Nombre", 1)
        pdf.cell(30, 10, "Cantidad", 1)
        pdf.cell(50, 10, "Precio Unitario", 1)
        pdf.cell(50, 10, "Subtotal", 1)
        pdf.ln()

        pdf.set_font("Arial", size=12)
        for item in detalles_pedido:
            nombre = item['nombre']
            cantidad = item['cantidad']
            precio_unitario = item['precio_unitario']
            subtotal = cantidad * precio_unitario

            pdf.cell(50, 10, nombre, 1)
            pdf.cell(30, 10, str(cantidad), 1)
            pdf.cell(50, 10, f"${precio_unitario:.2f}", 1)
            pdf.cell(50, 10, f"${subtotal:.2f}", 1)
            pdf.ln()

        # Agregar los totales
        pdf.cell(200, 10, f"Subtotal: ${total:.2f}", ln=True, align='R')
        pdf.cell(200, 10, f"IVA (19%): ${iva:.2f}", ln=True, align='R')
        pdf.cell(200, 10, f"Total: ${total_final:.2f}", ln=True, align='R')

        # Guardar el PDF
        pdf_file = "boleta.pdf"
        pdf.output(pdf_file)

        # Abrir el archivo PDF (en Windows)
        os.startfile(pdf_file)

    def crear_tarjeta(self, menu, tarjetas_frame):

        num_tarjetas = len(self.menus)
        for num_tarjetas, menu in enumerate(self.menus):
            fila = num_tarjetas // 2
            columna = num_tarjetas % 2

            tarjeta = ctk.CTkFrame(tarjetas_frame,corner_radius=10, border_width=2)
            tarjeta.grid(row=fila, column=columna, padx=10, pady=10,)

            imagen_label = ctk.CTkLabel(tarjeta, image=menu.imagen, text="")
            imagen_label.pack()

            nombre_label = ctk.CTkLabel(tarjeta, text=menu.nombre)
            nombre_label.pack()

            tarjeta.bind("<Button-1>", lambda event, m=menu: self.tarjeta_click(m))

            # Cambiar el color del borde cuando el mouse pasa sobre la tarjeta
            tarjeta.bind("<Enter>", lambda event: tarjeta.configure(border_color="#FF0000"))  # Cambia a rojo al pasar el mouse
            tarjeta.bind("<Leave>", lambda event: tarjeta.configure(border_color="#4CAF50"))  # Vuelve al verde al salir

    def tarjeta_click(self, menu):
        self.pedido.agregar_menu(menu)
        # self.stock.reducir_stock(menu)  
        self.actualizar_treeview_pedido()

        total = self.pedido.calcular_total()
        self.label_total.configure(text=f"Total: ${total:.2f}")

        # if self.stock.verificar_stock(menu):
        #     self.pedido.agregar_menu(menu)
        #     self.stock.reducir_stock(menu)  
        #     self.actualizar_treeview_pedido()

        #     total = self.pedido.calcular_total()
        #     self.label_total.configure(text=f"Total: ${total:.2f}")
        # else:
        #     CTkMessagebox(title="Stock Insuficiente", message=f"No hay suficiente stock para {menu.nombre}", icon="warning")


if __name__ == "__main__":
    app = AplicacionConPestanas()
    app.mainloop()

