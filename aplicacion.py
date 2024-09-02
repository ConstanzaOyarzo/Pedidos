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

        # Pestana 1
        self.configurar_pestana1()

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
    
    def ingresar_ingrediente(self):
        pass

    def eliminar_ingrediente(self):
        pass

if __name__ == "__main__":
    ctk.set_appearance_mode("System")
    ctk.set_default_color_theme("blue")

    app = AplicacionConPestanas()
    app.mainloop()
