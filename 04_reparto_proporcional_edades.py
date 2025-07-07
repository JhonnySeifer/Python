import tkinter as tk
from tkinter import messagebox

def calcular_reparto():
    try:
        monto = float(txt_monto.get())
        e1 = int(txt_edad1.get())
        e2 = int(txt_edad2.get())
        e3 = int(txt_edad3.get())
        suma_edades = e1 + e2 + e3

        m1 = (e1 * monto) / suma_edades
        m2 = (e2 * monto) / suma_edades
        m3 = (e3 * monto) / suma_edades

        resultado = (
            f"Persona 1 recibe: S/. {m1:.2f}\n"
            f"Persona 2 recibe: S/. {m2:.2f}\n"
            f"Persona 3 recibe: S/. {m3:.2f}"
        )
        txt_resultado.config(state='normal')
        txt_resultado.delete(1.0, tk.END)
        txt_resultado.insert(tk.END, resultado)
        txt_resultado.config(state='disabled')
    except ValueError:
        messagebox.showerror("Error", "Ingrese datos válidos.")

ventana = tk.Tk()
ventana.title("Reparto proporcional por edad")
ventana.geometry("400x320")

tk.Label(ventana, text="Monto a repartir (S/):").place(x=20, y=20)
txt_monto = tk.Entry(ventana)
txt_monto.place(x=180, y=20)

tk.Label(ventana, text="Edad Persona 1:").place(x=20, y=60)
txt_edad1 = tk.Entry(ventana)
txt_edad1.place(x=180, y=60)

tk.Label(ventana, text="Edad Persona 2:").place(x=20, y=100)
txt_edad2 = tk.Entry(ventana)
txt_edad2.place(x=180, y=100)

tk.Label(ventana, text="Edad Persona 3:").place(x=20, y=140)
txt_edad3 = tk.Entry(ventana)
txt_edad3.place(x=180, y=140)

btn_calcular = tk.Button(ventana, text="Calcular", command=calcular_reparto)
btn_calcular.place(x=180, y=180)

txt_resultado = tk.Text(ventana, height=5, width=40, state='disabled')
txt_resultado.place(x=20, y=220)

ventana.mainloop()
