import tkinter as tk
from tkinter import messagebox

def calcular_descuento():
    try:
        precio_unitario = float(txt_precio.get())
        cantidad = int(txt_cantidad.get())
        importe = precio_unitario * cantidad
        descuento = importe * 0.11
        total_pagar = importe - descuento

        resultado = (
            f"Importe de compra : S/. {importe:.2f}\n"
            f"Descuento (11%)   : S/. {descuento:.2f}\n"
            f"Total a pagar     : S/. {total_pagar:.2f}"
        )
        txt_resultado.config(state='normal')
        txt_resultado.delete(1.0, tk.END)
        txt_resultado.insert(tk.END, resultado)
        txt_resultado.config(state='disabled')
    except ValueError:
        messagebox.showerror("Error", "Ingrese datos válidos.")

ventana = tk.Tk()
ventana.title("Descuento del 11%")
ventana.geometry("400x280")

tk.Label(ventana, text="Precio unitario (S/):").place(x=20, y=20)
txt_precio = tk.Entry(ventana)
txt_precio.place(x=180, y=20)

tk.Label(ventana, text="Cantidad:").place(x=20, y=60)
txt_cantidad = tk.Entry(ventana)
txt_cantidad.place(x=180, y=60)

btn_calcular = tk.Button(ventana, text="Calcular", command=calcular_descuento)
btn_calcular.place(x=180, y=100)

txt_resultado = tk.Text(ventana, height=6, width=40, state='disabled')
txt_resultado.place(x=20, y=150)

ventana.mainloop()
