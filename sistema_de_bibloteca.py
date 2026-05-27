#libreria de tkinter
import tkinter as tk
from tkinter import Grid, ttk, messagebox

class libro:
    def __init__(self,nombre_alumno, nombre_libro, dias_prestamo, tipo_usuario):
        self.nombre_alumno = nombre_alumno
        self.nombre_libro = nombre_libro
        self.dias_prestamo = dias_prestamo
        self.tipo_usuario = tipo_usuario

    def precio_por_dias(self):
        if self.nombre_libro == "python":
            return 15
        elif self.nombre_libro == "redes":
            return 20
        elif self.nombre_libro == "base de datos":
            return 25
        else:
            return 5
        
    def calcular_precio(self):
        return self.dias_prestamo * self.precio_por_dias()
    
    def mostrar_datos(self):
        f"alumno : {self.nombre_alumno}/n"
        f"libro : {self.nombre_libro}/n"
        f"dias de prestamo : {self.dias_prestamo}/n"
        f"tipo de usuario : {self.tipo_usuario}/n"
        f"precio por dias : {self.precio_por_dias}/n"
        f"{'-'* 30}/n"
        f"total a pagar: {self.calcular_precio():.2f}/n"

#crear ventana principal

v = tk.Tk()
v.title("sistema de bibloteca")
v.config(background="white")
v.resizable(False, False)#no permite que cambie de tamaño
v.geometry("400x500")

titulo = tk.Label(v, text="SISTEMA DE BIBLOTECA", font=("Arial", 12, "bold"), bg= "white", fg= "#2F4F4F")
titulo.pack(pady=10)

frame = tk.Frame(v, bg="white")
frame.pack(pady=10)

#colocar etiqueta y campo de nombre
tk.Label(frame, text="nombre del alumno: ", bg="white" ).grid(row=0, column=0, pady=5, padx=5)
entrada_nombre = tk.Entry(frame, width=25)
entrada_nombre.grid(row=0, column=1, pady=5)

#colocar etiqueta y campo para el nombre del libro
tk.Label(frame, text="nombre del libro", bg= "white").grid(row=1, column=0, pady=5, padx=5)
combo_libro = ttk.Combobox(frame, values=["python", "redes", "base de datos"], state="readonly", width=22)
combo_libro.current(0)#seleciona la primera opcion
combo_libro.grid(row=1, column=1, pady=5)

#etiqueta y campo dias de prestamo
tk.Label(frame, text="dias de prestamo" )
entrada_dias = tk.Entry(frame, width=25)
entrada_dias.grid(row=2, column=1, pady=5)

#colocar etiqueta y campo para el tipo de usuario
tk.Label(frame, text="tipo de usuario", bg= "white").grid(row=3, column=0, pady=5, padx=5)
combo_usuario = ttk.Combobox(frame, values=["alumno", "maestro", "administrativo"], state="readonly", width=22)
combo_usuario.current(0)#seleciona la primera opcion
combo_usuario.grid(row=3, column=1, pady=5)

v.mainloop()
