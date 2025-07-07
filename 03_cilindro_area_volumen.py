import tkinter as tk
from tkinter import messagebox
import math

def calcular():
    try:
        r = float(txt_radio.get())
        h = float(txt_altura.get())
        area = 2 * math.pi * r * (r + h)
        volumen = math.pi * r**2 * h

        resultado = (
            f"Área total   : {area:.2f} u²\n"
            f"Volumen      : {volumen:.2f} u³"
        )
        txt_resultado.config(state='normal')
        txt_resultado.delete(1.0, tk.END)
        txt_resultado.insert(tk.END, resultado)
        txt_resultado.config(state='disabled')
    except ValueError:
        messagebox.showerror("Error", "Ingrese valores válidos.")

ventana = tk.Tk()
ventana.title("Área y Volumen de un Cilindro")
ventana.geometry("380x270")

tk.Label(ventana, text="Radio (r):").place(x=20, y=20)
txt_radio = tk.Entry(ventana)
txt_radio.place(x=120, y=20)

tk.Label(ventana, text="Altura (h):").place(x=20, y=60)
txt_altura = tk.Entry(ventana)
txt_altura.place(x=120, y=60)

btn_calcular = tk.Button(ventana, text="Calcular", command=calcular)
btn_calcular.place(x=120, y=100)

txt_resultado = tk.Text(ventana, height=5, width=34, state='disabled')
txt_resultado.place(x=20, y=150)

ventana.mainloop()
