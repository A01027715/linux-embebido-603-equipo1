import tkinter as tk
from tkinter import simpledialog

def pedir_usuario_y_cerrar():
    usuario = simpledialog.askstring("Ingresar Usuario", "Por favor ingrese su nombre de usuario:")
    if usuario:
        root.destroy()  # Cierra la ventana principal si se ingresa un nombre de usuario válido

# Crear la ventana principal
root = tk.Tk()
root.title("Tkinter Interactivo")

# No mostrar la ventana inicialmente
root.withdraw()

# Pedir el usuario
pedir_usuario_y_cerrar()

# Iniciar el bucle principal de la interfaz gráfica
root.mainloop()
