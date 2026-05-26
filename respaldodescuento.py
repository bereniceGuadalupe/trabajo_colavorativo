#nombre del equipo:berenice guadalupe cahuich maldonado y rosa elena utuy santos
#nombre del trabajo:descuento tendra sobre el total de su compra
#nombre del docente:wilfrido david lugo castillo
#fecha de elaboracion:18/05/26

import tkinter as tk
from tkinter import messagebox

def calcular():
   total = float(campo_total.get())
   color = campo_color.get()

   if color == "rojo":
        descuento = total * 0.40
        pagar = total - descuento
        resultado.config(text= "el cliente pagara: dinero" + str(pagar))

   elif color == "amarillo": 
        descuento = total * 0.25
        pagar = total - descuento
        resultado.config(text= "el cliente pagara: dinero" + str(pagar))

   else:
        pagar = total 

        resultado.config(text= "el cliente pagara: dinero" + str(pagar))



v = tk.Tk()
v.title("ventana descuento")
v.config(background= "pink")
v.minsize(100,100)
v.maxsize(400,400)
v.geometry("300x300+100+10")


msj_bienvenida = tk.Label(v, text= "Bienvenidos a la tienda", bg="pink")
msj_bienvenida.pack()


etiqueta_total_compra =  tk.Label(v, text="Escribe la cantidad tu compra ", bg="pink")
etiqueta_total_compra.pack()

campo_total = tk.Entry(v)
campo_total.pack()


etiqueta_color =tk.Label(v,text="ingresa el color de la bolita" , bg="pink")
etiqueta_color.pack()


campo_color = tk.Entry(v)
campo_color.pack()

calcula_total = tk.Button(v, text="calcular",command=calcular)
calcula_total.pack()

resultado = tk.Label(v, text="", bg=("pink"))
resultado.pack()

v.mainloop()

