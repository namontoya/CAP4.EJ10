#Capitulo 4. Ejercicio resuelto 10

import tkinter as tk
from tkinter import messagebox

def calcular_pago():
    try:
        ni = entry_numero_inscripcion.get()
        nom = entry_nombres.get()
        pat = float(entry_patrimonio.get())
        est = float(entry_estrato_social.get())
        pagmat = 50000

        if (pat > 2000000) and (est > 3):
            pagmat = pagmat + 0.03 * pat

        messagebox.showinfo("Resultado", f"EL ESTUDIANTE CON NÚMERO DE INSCRIPCION {ni} Y NOMBRE {nom} DEBE PAGAR ${pagmat}")
    except ValueError:
        messagebox.showerror("Error", "Por favor ingrese valores válidos.")

root = tk.Tk()
root.title("Cálculo de Pago de Matrícula")

label_numero_inscripcion = tk.Label(root, text="Número de inscripción:")
label_numero_inscripcion.grid(row=0, column=0, padx=10, pady=10)

entry_numero_inscripcion = tk.Entry(root)
entry_numero_inscripcion.grid(row=0, column=1, padx=10, pady=10)

label_nombres = tk.Label(root, text="Nombre:")
label_nombres.grid(row=1, column=0, padx=10, pady=10)

entry_nombres = tk.Entry(root)
entry_nombres.grid(row=1, column=1, padx=10, pady=10)

label_patrimonio = tk.Label(root, text="Patrimonio:")
label_patrimonio.grid(row=2, column=0, padx=10, pady=10)

entry_patrimonio = tk.Entry(root)
entry_patrimonio.grid(row=2, column=1, padx=10, pady=10)

label_estrato_social = tk.Label(root, text="Estrato social:")
label_estrato_social.grid(row=3, column=0, padx=10, pady=10)

entry_estrato_social = tk.Entry(root)
entry_estrato_social.grid(row=3, column=1, padx=10, pady=10)

button_calcular = tk.Button(root, text="Calcular Pago", command=calcular_pago)
button_calcular.grid(row=4, columnspan=2, pady=20)

root.mainloop()
