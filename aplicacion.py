import customtkinter as ctk
from tkinter import ttk
import re
from CTkMessagebox import CTkMessagebox

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

    def configurar_pestana2(self):
        frame_imagenes = ctk.CTkFrame(self.tab2)
        frame_imagenes.pack(side="top", fill="both", expand=True, padx=10, pady=10)

        frame_treeview2 = ctk.CTkFrame(self.tab2)
        frame_treeview2.pack(side="bottom", fill="both", expand=True, padx=10, pady=10)
        
        tarjetas_frame = ctk.CTkFrame(self.tab2)
        tarjetas_frame.pack(side="left", fill="both", expand=True, padx=10, pady=10)

        label_nombre_ingrediente = ctk.CTkLabel(frame_imagenes, text="Nombre Ingrediente:")
        label_nombre_ingrediente.pack(pady=5)
        self.entry_nombre_ingrediente = ctk.CTkEntry(frame_imagenes)
        self.entry_nombre_ingrediente.pack(pady=5)

        label_cantidad = ctk.CTkLabel(frame_imagenes, text="Cantidad:")
        label_cantidad.pack(pady=5)
        self.entry_cantidad = ctk.CTkEntry(frame_imagenes)
        self.entry_cantidad.pack(pady=5)
        
        self.tree = ttk.Treeview(frame_treeview2, columns=("Nombre del menu", "Cantidad", "Precio unitario"), show="headings", height=8)

        self.tree.heading("Nombre del menu", text="Nombre del menu")
        self.tree.heading("Cantidad", text="Cantidad")
        self.tree.heading("Precio unitario", text="Precio unitario")

        self.tree.pack(expand=True, fill="both", padx=10, pady=10)
        
        


       

    
    
     
    def ingresar_ingrediente(self):
        pass

    def eliminar_ingrediente(self):
        pass

#metodo de ayuda para crear targetas con menus solicitados
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
            if self.stock.lista_ingredientes==[]:
                suficiente_stock=False
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

    
