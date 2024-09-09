from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, 'Boleta Restaurante', 0, 1, 'C')
        self.cell(0, 10, 'Razón Social del Negocio', 0, 1, 'C')
        self.cell(0, 10, 'RUT: 12345678-9', 0, 1, 'C')
        self.cell(0, 10, 'Dirección: Calle Falsa 123', 0, 1, 'C')
        self.cell(0, 10, 'Teléfono: +56 9 1234 5678', 0, 1, 'C')
        self.ln(10)

    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.cell(0, 10, 'Gracias por su compra. Para cualquier consulta, llámenos al +56 9 1234 5678.', 0, 0, 'C')

    def create_table(self, header, data):
        self.set_font('Arial', 'B', 12)
        for col in header:
            self.cell(45, 10, col, 1)
        self.ln()
        self.set_font('Arial', '', 12)
        for row in data:
            for item in row:
                self.cell(45, 10, str(item), 1)
            self.ln()

# Datos de la tabla
header = ['Nombre', 'Cantidad', 'Precio Unitario', 'Subtotal']
data = [
    ['Papas Fritas', 2, '$500.00', '$1000.00'],
    ['Completo', 2, '$1800.00', '$3600.00'],
    ['Pepsi', 3, '$1100.00', '$3300.00'],
    ['Hamburguesa', 2, '$3500.00', '$7000.00']
]

# Totales
subtotal = '$14900.00'
iva = '$2831.00'
total = '$17731.00'

# Crear PDF
pdf = PDF()
pdf.add_page()

# Agregar tabla
pdf.create_table(header, data)

# Agregar totales
pdf.ln(10)
pdf.set_font('Arial', 'B', 12)
pdf.cell(0, 10, f'Subtotal: {subtotal}', 0, 1, 'R')
pdf.cell(0, 10, f'IVA (19%): {iva}', 0, 1, 'R')
pdf.cell(0, 10, f'Total: {total}', 0, 1, 'R')

# Guardar PDF
pdf.output('boleta.pdf')

print("PDF generado correctamente.")
