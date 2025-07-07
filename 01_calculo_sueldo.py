"""
Se ingresan las horas trabajadas (txt_horas) y la tarifa por hora (txt_tarifa).
Se calcula:
sueldo_básico   = horas x tarifa
bonificación    = 20% del sueldo básico
sueldo bruto    = sueldo básico + bonificación
descuento       = 10% del sueldo bruto
sueldo neto     = sueldo bruto - descuento
"""

import tkinter as tk
from tkinter import messagebox

# Definir la función antes de usarla
def calcular_sueldo():
    try:
        horas = float(txt_horas.get())
        tarifa = float(txt_tarifa.get())

        sueldo_basico = horas * tarifa
        bonificacion = sueldo_basico * 0.20
        sueldo_bruto = sueldo_basico + bonificacion
        descuento = sueldo_bruto * 0.10
        sueldo_neto = sueldo_bruto - descuento

        resultado = (
            f"Sueldo básico : S/. {sueldo_basico:.2f}\n"
            f"Bonificación  : S/. {bonificacion:.2f}\n"
            f"Sueldo bruto  : S/. {sueldo_bruto:.2f}\n"
            f"Descuento     : S/. {descuento:.2f}\n"
            f"Sueldo neto   : S/. {sueldo_neto:.2f}"
        )
        txt_resultado.config(state='normal')
        txt_resultado.delete(1.0, tk.END)
        txt_resultado.insert(tk.END, resultado)
        txt_resultado.config(state='disabled')
    except ValueError:
        messagebox.showerror("Error", "Ingrese valores válidos.")

# Construcción de la interfaz
ventana = tk.Tk()
ventana.title("Cálculo de Sueldo")
ventana.geometry("400x300")

tk.Label(ventana, text="Horas trabajadas:").place(x=20, y=20)
txt_horas = tk.Entry(ventana)
txt_horas.place(x=150, y=20)

tk.Label(ventana, text="Tarifa por hora:").place(x=20, y=60)
txt_tarifa = tk.Entry(ventana)
txt_tarifa.place(x=150, y=60)

btn_calcular = tk.Button(ventana, text="Calcular", command=calcular_sueldo)
btn_calcular.place(x=310, y=20)

txt_resultado = tk.Text(ventana, height=8, width=40, state='disabled')
txt_resultado.place(x=20, y=150)

ventana.mainloop()
