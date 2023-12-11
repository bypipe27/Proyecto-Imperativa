# importamos librerias
from tkinter import *
from tkinter import messagebox
import subprocess
import json

# ---------------------------------------------------------------
#Funciones
def open_manegetable():
    wmenu_table.withdraw()
    subprocess.call(["python", "Interfaz\Manegeiment_table.py"])

def open_tabletable():
    wmenu_table.withdraw()
    subprocess.call(["python", "Interfaz\Table_table.py"])

# Creamos y configuramos ventana para ordenar
wmenu_table = Tk()
wmenu_table.title("Order")
wmenu_table.resizable(width=False, height=False)
wmenu_table.geometry("600x500")
wmenu_table.configure(bg="white")
# ---------------------------------------------------------------
# Bandera italiana con labels (Configuracion y ubicacion)
redflag = Label(wmenu_table, bg="green", height=5, width=20)
whiteflag = Label(wmenu_table, bg="white", height=5, width=21)
greenflag = Label(wmenu_table, bg="red", height=5, width=20)

redflag.place(x=70, y=100)
whiteflag.place(x=217, y=100)
greenflag.place(x=370, y=100)
# ---------------------------------------------------------------
# tittle and subtitles en el dishmenu
menudishtitle = Label(wmenu_table, text = "Italian Restaurant", font = ("Arial", 36 , "bold"), fg = "red")
menudishtitle.place(x = 100 , y = 10)
menudishsubtitle = Label(wmenu_table, text = "Manegeiment order", font = ("Arial", 20, "bold" ))
menudishsubtitle.place(x = 185, y = 190)
# ---------------------------------------------------------------
#butoons add , decla , update of dish 
buttonadddish = Button(wmenu_table,text = "Añadir order", font = ("Arial", 12, "bold"), fg = "white", bg = "black", command = open_manegetable)
buttonadddish.place(x = 250, y = 260 )
buttondecladish = Button(wmenu_table, text = "Eliminar order", font = ("Arial", 12, "bold"), fg = "white", bg = "black",command= open_tabletable)
buttondecladish.place(x = 245 , y = 330 )
buttonupdatedish = Button(wmenu_table, text = "Actualizar order", font = ("Arial", 12, "bold"), fg = "white", bg = "black" ,command= open_tabletable)
buttonupdatedish.place(x = 240, y = 390 )
wmenu_table.mainloop()