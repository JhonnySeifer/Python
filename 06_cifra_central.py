import tkinter as tk
from tkinter import messagebox

def obtener_cifra_central():
    try:
        numero = txt_numero.get()
        if len(numero) != 5 or not numero.isdigit():
            raise ValueError
        cifra = numero[2]  # índice 2 = tercer carácter (posición central)
        txt_resultado.config(state='normal')
        txt_resultado.delete(1.0, tk.END)
        txt_resultado.insert(tk.END, f"La cifra central es: {cifra}")
        txt_resultado.config(state='disabled')
    except ValueError:
        messagebox.showerror("Error", "Ingrese un número entero de 5 cifras.")

ventana = tk.Tk()
ventana.title("Cifra Central")
ventana.geometry("350x200")

tk.Label(ventana, text="Número de 5 cifras:").place(x=20, y=20)
txt_numero = tk.Entry(ventana)
txt_numero.place(x=160, y=20)

btn_calcular = tk.Button(ventana, text="Calcular", command=obtener_cifra_central)
btn_calcular.place(x=160, y=60)

txt_resultado = tk.Text(ventana, height=3, width=35, state='disabled')
txt_resultado.place(x=20, y=110)

ventana.mainloop()
