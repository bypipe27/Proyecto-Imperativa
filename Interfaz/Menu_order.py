# Importamos las librerias necesarias 
from tkinter import *
from tkinter import messagebox
import subprocess
# ---------------------------------------------------------------
# Funciones
def open_manegeorder():
    wmenu_order.withdraw()
    subprocess.call(["python", "Interfaz\Manegeiment_order.py"])

def open_tableorder():
    wmenu_order.withdraw()
    subprocess.call(["python", "Interfaz\Table_order.py"]) 

# Creamos y configuramos ventana para ordenar
wmenu_order = Tk()
wmenu_order.title("Order")
wmenu_order.resizable(width=False, height=False)
wmenu_order.geometry("600x500")
wmenu_order.configure(bg="white")
# ---------------------------------------------------------------
# Bandera italiana con labels (Configuracion y ubicacion)
redflag = Label(wmenu_order, bg="green", height=5, width=20)
whiteflag = Label(wmenu_order, bg="white", height=5, width=21)
greenflag = Label(wmenu_order, bg="red", height=5, width=20)

redflag.place(x=70, y=100)
whiteflag.place(x=217, y=100)
greenflag.place(x=370, y=100)
# ---------------------------------------------------------------
# tittle and subtitles en el dishmenu
menudishtitle = Label(wmenu_order, text = "Italian Restaurant", font = ("Arial", 36 , "bold"), fg = "red")
menudishtitle.place(x = 100 , y = 10)
menudishsubtitle = Label(wmenu_order, text = "Manegeiment order", font = ("Arial", 20, "bold" ))
menudishsubtitle.place(x = 185, y = 190)
# ---------------------------------------------------------------
#butoons add , decla , update of dish 
buttonadddish = Button(wmenu_order,text = "Añadir order", font = ("Arial", 12, "bold"), fg = "white", bg = "black", command = open_manegeorder)
buttonadddish.place(x = 250, y = 260 )
buttondecladish = Button(wmenu_order, text = "Eliminar order", font = ("Arial", 12, "bold"), fg = "white", bg = "black",command= open_tableorder)
buttondecladish.place(x = 245 , y = 330 )
buttonupdatedish = Button(wmenu_order, text = "Actualizar order", font = ("Arial", 12, "bold"), fg = "white", bg = "black" ,command= open_tableorder)
buttonupdatedish.place(x = 240, y = 390 )
wmenu_order.mainloop()