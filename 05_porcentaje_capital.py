import tkinter as tk
from tkinter import messagebox

def calcular():
    try:
        p1 = float(txt_p1.get())
        p2 = float(txt_p2.get())
        p3 = float(txt_p3.get())
        total = p1 + p2 + p3
        por1 = (p1 / total) * 100
        por2 = (p2 / total) * 100
        por3 = (p3 / total) * 100

        resultado = (
            f"Capital total: S/. {total:.2f}\n"
            f"Débora aporta: {por1:.2f}%\n"
            f"Raquel aporta: {por2:.2f}%\n"
            f"Séfora aporta: {por3:.2f}%"
        )
        txt_resultado.config(state='normal')
        txt_resultado.delete(1.0, tk.END)
        txt_resultado.insert(tk.END, resultado)
        txt_resultado.config(state='disabled')
    except ValueError:
        messagebox.showerror("Error", "Ingrese valores válidos.")

ventana = tk.Tk()
ventana.title("Capital y Porcentajes")
ventana.geometry("400x300")

tk.Label(ventana, text="Débora (S/):").place(x=20, y=20)
txt_p1 = tk.Entry(ventana)
txt_p1.place(x=150, y=20)

tk.Label(ventana, text="Raquel (S/):").place(x=20, y=60)
txt_p2 = tk.Entry(ventana)
txt_p2.place(x=150, y=60)

tk.Label(ventana, text="Séfora (S/):").place(x=20, y=100)
txt_p3 = tk.Entry(ventana)
txt_p3.place(x=150, y=100)

btn_calcular = tk.Button(ventana, text="Calcular", command=calcular)
btn_calcular.place(x=150, y=140)

txt_resultado = tk.Text(ventana, height=6, width=38, state='disabled')
txt_resultado.place(x=20, y=180)

ventana.mainloop()
