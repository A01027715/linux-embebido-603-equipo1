from flask import Flask, render_template, jsonify, request
import tkinter as tk
from tkinter import simpledialog

app = Flask(__name__)

estado = ""  # Estado inicial
respuesta = "Zoe"

def pedir_usuario_y_cerrar():
    usuario = simpledialog.askstring("Ingresar Usuario", "Por favor ingrese su nombre de usuario:")
    if usuario:
        root.destroy()  # Cierra la ventana principal si se ingresa un nombre de usuario válido

if respuesta == "Zoe":

    # Crear la ventana principal
    root = tk.Tk()
    root.title("Tkinter Interactivo")

    # No mostrar la ventana inicialmente
    root.withdraw()

    # Pedir el usuario
    pedir_usuario_y_cerrar()

    # Iniciar el bucle principal de la interfaz gráfica
    root.mainloop()


    @app.route('/')
    def index():
        return render_template('index.html', message="Ingrese Contraseña", page_class="home")

    @app.route('/home')
    def home():
        return render_template('index.html', message="Ingrese Contraseña", page_class="home")

    @app.route('/access')
    def access():
        return render_template('index.html', message="Bienvenido", page_class="welcome")

    @app.route('/denied')
    def denied():
        return render_template('index.html', message="Acceso Denegado", page_class="denied")

    @app.route('/update_status', methods=['POST'])
    def update_status():
        global estado
        data = request.get_json()
        estado = data['estado']
        return 'Estado actualizado', 200

    @app.route('/check_status')
    def check_status():
        global estado
        return jsonify({'estado': estado})

    if __name__ == '__main__':
        app.run(debug=True, port=5000)
