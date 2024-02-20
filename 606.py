import tkinter as tk
from tkinter import messagebox
import pandas as pd
from datetime import datetime, timedelta

def update_date(date_entry, comprobante_pago_entry):
    # Get the current date
    current_date = datetime.now()
    previous_month_date = current_date - timedelta(days=current_date.day)
    # Format the date as YYYYMM
    formatted_date = previous_month_date.strftime("%Y%m")
    # Set the formatted date to the date entry widget
    date_entry.delete(0, tk.END)
    date_entry.insert(0, formatted_date)
    # Set the formatted date to the comprobante pago entry widget
    comprobante_pago_entry.delete(0, tk.END)
    comprobante_pago_entry.insert(0, formatted_date)


def update_entry_RNC_Type_value(event=None):
    # Get the value from entry_RNC
    rnc_value = entry_RNC.get()
    # Set the value of entry_RNC_Type based on the length of rnc_value
    entry_RNC_Type.delete(0, tk.END)  # Clear previous value
    if len(rnc_value) <= 9:
        entry_RNC_Type.insert(0, "1")
    else:
        entry_RNC_Type.insert(0, "2") 

def save_values():
    # Gather all the values from entry widgets
    rnc_compania = id_entry.get()
    periodo = date_entry.get()

    # Create the filename
    filename = f"DGII_F_606_101735122_{periodo}.txt"

    with open(filename, "w") as file:
        formatted_values = f"606|{rnc_compania}|{periodo}|Registros\n"
        file.write(formatted_values)
    messagebox.showinfo("Save", f"Values have been saved to {filename} successfully!")

def append_values():
    periodo = date_entry.get()
    rnc_cedula = entry_RNC.get()
    tipo_id = entry_RNC_Type.get()
    tipo_bienes_servicios = selected_option.get()
    ncf = entry_NCF.get()
    ncf_documento_modificado = entry_NCF_m.get()
    fecha_comprobante_pago = comprobante_pago_entry.get()
    monto_facturado_servicios = entry_Monto_s.get()
    monto_facturado_bienes = entry_Monto_b.get()
    total_monto_facturado = entry_total_monto_facturado.get()
    itbis_facturado = entry_itbis_facturado.get()
    itbis_retenido = entry_itbis_retenido.get()
    itbis_proporcionalidad = entry_itbis_proporcionalidad.get()
    itbis_llevado_costo = entry_itbis_llevado_costo.get()
    itbis_por_adelantar = entry_itbis_por_adelantar.get()
    itbis_percibido_compras = entry_itbis_percibido_compras.get()
    tipo_retencion_isr = selected_tipo_retencion_isr.get()
    monto_retencion_renta = entry_monto_retencion_renta.get()
    isr_percibido_compras = entry_isr_percibido_compras.get()
    impuesto_selectivo_consumo = entry_impuesto_selectivo_consumo.get()
    otros_impuestos_tasas = entry_otros_impuestos_tasas.get()
    monto_propina_legal = entry_monto_propina_legal.get()
    forma_pago = selected_forma_pago.get()

    filename = f"DGII_F_606_101735122_{periodo}.txt"

    formatted_values = f"{rnc_cedula}|{tipo_id}|{tipo_bienes_servicios}|{ncf}|{ncf_documento_modificado}|{fecha_comprobante_pago}|{fecha_comprobante_pago}|{monto_facturado_servicios}|{monto_facturado_bienes}|{total_monto_facturado}|{itbis_facturado}|{itbis_retenido}|{itbis_proporcionalidad}|{itbis_llevado_costo}|{itbis_por_adelantar}|{itbis_percibido_compras}|{tipo_retencion_isr}|{monto_retencion_renta}|{isr_percibido_compras}|{impuesto_selectivo_consumo}|{otros_impuestos_tasas}|{monto_propina_legal}|{forma_pago}\n"

    with open(filename, "a") as file:
        file.write(formatted_values)

# Create the main window
root = tk.Tk()
root.title("606 Fesisa")

# Label for RNC Compañia
id_label = tk.Label(root, text="RNC Compañia:")
id_label.grid(row=0, column=0, padx=10, pady=5, sticky="w")

# Entry widget for RNC Compañia
id_entry = tk.Entry(root)
id_entry.grid(row=0, column=1, padx=10, pady=5)
id_entry.insert(0, "101735122")  # Set default value

# Label for Periodo
date_label = tk.Label(root, text="Periodo:")
date_label.grid(row=0, column=2, padx=10, pady=5, sticky="w")

# Entry widget for Periodo
date_entry = tk.Entry(root)
date_entry.grid(row=0, column=3, padx=10, pady=5)

# Label for RNC or Cedula
label_RNC = tk.Label(root, text="RNC o Cedula:")
label_RNC.grid(row=2, column=0, padx=10, pady=5, sticky="w")

# Entry widget for RNC or Cedula
entry_RNC = tk.Entry(root)
entry_RNC.grid(row=2, column=1, padx=10, pady=5)
entry_RNC.bind("<KeyRelease>", update_entry_RNC_Type_value)  # Bind the function to key release event

# Label for Tipo Id
label_RNC_Type = tk.Label(root, text="Tipo Id")
label_RNC_Type.grid(row=2, column=2, padx=10, pady=5, sticky="w")

# Entry widget for Tipo Id
entry_RNC_Type = tk.Entry(root)
entry_RNC_Type.grid(row=2, column=3, padx=10, pady=5)

# Dropdown menu options
tipo_bienes_servicios = [f"{i:02d}" for i in range(1, 12)] 

# Variable to store selected option
selected_option = tk.StringVar(root)
selected_option.set(tipo_bienes_servicios[0])  # Set default option

# Label for dropdown menu
dropdown_label = tk.Label(root, text="Tipo Bienes y Servicios Comprados:")
dropdown_label.grid(row=3, column=0, padx=10, pady=5, sticky="w")

# Dropdown menu
dropdown_menu = tk.OptionMenu(root, selected_option, *tipo_bienes_servicios)
dropdown_menu.grid(row=3, column=1, padx=10, pady=5, sticky="w")

# Label for NCF
label_NCF = tk.Label(root, text="NCF")
label_NCF.grid(row=3, column=2, padx=10, pady=5, sticky="w")

# Entry widget for NCF
entry_NCF = tk.Entry(root)
entry_NCF.grid(row=3, column=3, padx=10, pady=5)

#Label for NCF o Documento modificado
label_NCF_m = tk.Label(root, text="NCF o Documento Modificado:")
label_NCF_m.grid(row=4, column=0, padx=10, pady=5, sticky="w")

#Entry widget for NCF o Documento modificado
entry_NCF_m = tk.Entry(root)
entry_NCF_m.grid(row=4, column=1, padx=10, pady=5, sticky="w") 

# Label for Fecha Comprobante y Fecha Pago
date_label = tk.Label(root, text="Comprobante y Pago:")
date_label.grid(row=4, column=2, padx=10, pady=5, sticky="w")

# Entry widget for Fecha Comprobante y Fecha Pago
comprobante_pago_entry = tk.Entry(root)
comprobante_pago_entry.grid(row=4, column=3, padx=10, pady=5)

#Label for Monto Facturado
label_Monto_s = tk.Label(root, text="Monto Facturado en Servicios:")
label_Monto_s.grid(row=5, column=0, padx=10, pady=5, sticky="w")

#Entry widget for Monto Facturado
entry_Monto_s = tk.Entry(root)
entry_Monto_s.grid(row=5, column=1, padx=10, pady=5)

#Label for Monto Facturado
label_Monto_b = tk.Label(root, text="Monto Facturado en Bienes:")
label_Monto_b.grid(row=5, column=2, padx=10, pady=5, sticky="w")

#Entry widget for Monto Facturado
entry_Monto_b = tk.Entry(root)
entry_Monto_b.grid(row=5, column=3, padx=10, pady=5)

# Label for Total Monto Facturado
label_total_monto_facturado = tk.Label(root, text="Total Monto Facturado:")
label_total_monto_facturado.grid(row=6, column=0, padx=10, pady=5, sticky="w")

# Entry widget for Total Monto Facturado
entry_total_monto_facturado = tk.Entry(root)
entry_total_monto_facturado.grid(row=6, column=1, padx=10, pady=5)

# Label for ITBIS Facturado
label_itbis_facturado = tk.Label(root, text="ITBIS Facturado:")
label_itbis_facturado.grid(row=6, column=2, padx=10, pady=5, sticky="w")

# Entry widget for ITBIS Facturado
entry_itbis_facturado = tk.Entry(root)
entry_itbis_facturado.grid(row=6, column=3, padx=10, pady=5)

# Label for ITBIS Retenido
label_itbis_retenido = tk.Label(root, text="ITBIS Retenido:")
label_itbis_retenido.grid(row=7, column=0, padx=10, pady=5, sticky="w")

# Entry widget for ITBIS Retenido
entry_itbis_retenido = tk.Entry(root)
entry_itbis_retenido.grid(row=7, column=1, padx=10, pady=5)

# Label for ITBIS sujeto a Proporcionalidad (Art. 349)
label_itbis_proporcionalidad = tk.Label(root, text="ITBIS sujeto a Proporcionalidad (Art. 349):")
label_itbis_proporcionalidad.grid(row=7, column=2, padx=10, pady=5, sticky="w")

# Entry widget for ITBIS sujeto a Proporcionalidad (Art. 349)
entry_itbis_proporcionalidad = tk.Entry(root)
entry_itbis_proporcionalidad.grid(row=7, column=3, padx=10, pady=5)

# Label for ITBIS llevado al Costo
label_itbis_llevado_costo = tk.Label(root, text="ITBIS llevado al Costo:")
label_itbis_llevado_costo.grid(row=8, column=0, padx=10, pady=5, sticky="w")

# Entry widget for ITBIS llevado al Costo
entry_itbis_llevado_costo = tk.Entry(root)
entry_itbis_llevado_costo.grid(row=8, column=1, padx=10, pady=5)

# Label for ITBIS por Adelantar
label_itbis_por_adelantar = tk.Label(root, text="ITBIS por Adelantar:")
label_itbis_por_adelantar.grid(row=8, column=2, padx=10, pady=5, sticky="w")

# Entry widget for ITBIS por Adelantar
entry_itbis_por_adelantar = tk.Entry(root)
entry_itbis_por_adelantar.grid(row=8, column=3, padx=10, pady=5)

# Label for ITBIS Percibido en compras
label_itbis_percibido_compras = tk.Label(root, text="ITBIS Percibido en compras:")
label_itbis_percibido_compras.grid(row=9, column=0, padx=10, pady=5, sticky="w")

# Entry widget for ITBIS Percibido en compras
entry_itbis_percibido_compras = tk.Entry(root)
entry_itbis_percibido_compras.grid(row=9, column=1, padx=10, pady=5)

# Dropdown menu options for Tipo de Retención en ISR
tipo_retencion_isr_options = [""]+ [f"{i:02d}" for i in range(1, 9)]  # Add your options here

# Variable to store selected option for Tipo de Retención en ISR
selected_tipo_retencion_isr = tk.StringVar(root)
selected_tipo_retencion_isr.set(tipo_retencion_isr_options[0])  # Set default option

# Label for dropdown menu for Tipo de Retención en ISR
label_tipo_retencion_isr = tk.Label(root, text="Tipo de Retención en ISR:")
label_tipo_retencion_isr.grid(row=9, column=2, padx=10, pady=5, sticky="w")

# Dropdown menu for Tipo de Retención en ISR
tipo_retencion_isr_menu = tk.OptionMenu(root, selected_tipo_retencion_isr, *tipo_retencion_isr_options)
tipo_retencion_isr_menu.grid(row=9, column=3, padx=10, pady=5)

# Label for Monto Retencion Renta
label_monto_retencion_renta = tk.Label(root, text="Monto Retencion Renta:")
label_monto_retencion_renta.grid(row=10, column=0, padx=10, pady=5, sticky="w")

# Entry widget for Monto Retencion Renta
entry_monto_retencion_renta = tk.Entry(root)
entry_monto_retencion_renta.grid(row=10, column=1, padx=10, pady=5)

# Label for ISR Percibido en compras
label_isr_percibido_compras = tk.Label(root, text="ISR Percibido en compras:")
label_isr_percibido_compras.grid(row=10, column=2, padx=10, pady=5, sticky="w")

# Entry widget for ISR Percibido en compras
entry_isr_percibido_compras = tk.Entry(root)
entry_isr_percibido_compras.grid(row=10, column=3, padx=10, pady=5)

# Label for Impuesto Selectivo al Consumo
label_impuesto_selectivo_consumo = tk.Label(root, text="Impuesto Selectivo al Consumo:")
label_impuesto_selectivo_consumo.grid(row=11, column=0, padx=10, pady=5, sticky="w")

# Entry widget for Impuesto Selectivo al Consumo
entry_impuesto_selectivo_consumo = tk.Entry(root)
entry_impuesto_selectivo_consumo.grid(row=11, column=1, padx=10, pady=5)

# Label for Otros Impuestos / Tasas
label_otros_impuestos_tasas = tk.Label(root, text="Otros Impuestos / Tasas:")
label_otros_impuestos_tasas.grid(row=11, column=2, padx=10, pady=5, sticky="w")

# Entry widget for Otros Impuestos / Tasas
entry_otros_impuestos_tasas = tk.Entry(root)
entry_otros_impuestos_tasas.grid(row=11, column=3, padx=10, pady=5)

# Label for Monto Propina Legal
label_monto_propina_legal = tk.Label(root, text="Monto Propina Legal:")
label_monto_propina_legal.grid(row=12, column=0, padx=10, pady=5, sticky="w")

# Entry widget for Monto Propina Legal
entry_monto_propina_legal = tk.Entry(root)
entry_monto_propina_legal.grid(row=12, column=1, padx=10, pady=5)


# Dropdown menu options for Forma de Pago
forma_pago_options = [f"{i:02d}" for i in range(1, 8)]

# Variable to store selected option for Forma de Pago
selected_forma_pago = tk.StringVar(root)
selected_forma_pago.set(forma_pago_options[0])  # Set default option

# Label for dropdown menu for Forma de Pago
forma_pago_label = tk.Label(root, text="Forma de Pago:")
forma_pago_label.grid(row=12, column=2, padx=10, pady=5, sticky="w")

# Dropdown menu for Forma de Pago
forma_pago_menu = tk.OptionMenu(root, selected_forma_pago, *forma_pago_options)
forma_pago_menu.grid(row=12, column=3, padx=10, pady=5, sticky="w")


# Button to save values
save_button = tk.Button(root, text="Guardar Título", command=save_values)
save_button.grid(row=13, column=0, columnspan=4, padx=10, pady=5)
#Append Values
save_button = tk.Button(root, text="Añadir nueva linea", command=append_values)
save_button.grid(row=13, column=1, columnspan=4, padx=10, pady=5)

# Call the function to update both entry widgets
update_date(date_entry, comprobante_pago_entry)

# Run the Tkinter event loop
root.mainloop()