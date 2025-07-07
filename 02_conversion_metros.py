import tkinter as tk
from tkinter import messagebox

def convertir():
    try:
        metros = float(txt_metros.get())
        centimetros = metros * 100
        pulgadas = centimetros / 2.54
        pies = pulgadas / 12
        yardas = pies / 3

        resultado = (
            f"Centímetros: {centimetros:.2f}\n"
            f"Pulgadas   : {pulgadas:.2f}\n"
            f"Pies       : {pies:.2f}\n"
            f"Yardas     : {yardas:.2f}"
        )
        txt_resultado.config(state='normal')
        txt_resultado.delete(1.0, tk.END)
        txt_resultado.insert(tk.END, resultado)
        txt_resultado.config(state='disabled')
    except ValueError:
        messagebox.showerror("Error", "Ingrese un valor numérico.")

ventana = tk.Tk()
ventana.title("Conversión de Metros")
ventana.geometry("380x270")

tk.Label(ventana, text="Metros:").place(x=20, y=20)
txt_metros = tk.Entry(ventana)
txt_metros.place(x=100, y=20)

btn_convertir = tk.Button(ventana, text="Convertir", command=convertir)
btn_convertir.place(x=100, y=60)

txt_resultado = tk.Text(ventana, height=8, width=32, state='disabled')
txt_resultado.place(x=20, y=110)

ventana.mainloop()
