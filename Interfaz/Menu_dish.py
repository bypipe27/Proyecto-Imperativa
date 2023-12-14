# Importamos las librerias necesarias para el funcionamiento de la ventana 
from tkinter import *
from tkinter import messagebox
import subprocess
#Funciones 
def open_manegedish():
    wmenu_dish.withdraw()
    subprocess.call(["python", "Interfaz\Manegeiment_dish.py"])

def open_tabledish():
    wmenu_dish.withdraw()
    subprocess.call(["python", "Interfaz\Table_dishes.py"])

#---------------------------------------------------------------
#Configure of windows 
wmenu_dish = Tk()
wmenu_dish.title("Menu - dish")
wmenu_dish.geometry("600x500")
wmenu_dish.resizable(width = False , height = False)
wmenu_dish.configure(bg = "#FFFFFF")
#---------------------------------------------------------------
# Bandera italiana con labels en ventana dish menu (Configuracion y ubicacion) 
greenflag = Label(wmenu_dish,bg = "#009C45" ,height = 5 , width = 20)
whiteflag=  Label(wmenu_dish,bg = "#FFFFFF", height = 5 , width = 21)
redflag = Label(wmenu_dish,bg = "#B31200", height = 5 , width = 20)
greenflag.place( x = 70, y = 100)
whiteflag.place( x = 217, y = 100)
redflag.place( x = 370, y = 100)
#----------------------------------------------------------------
# tittle and subtitles en el dishmenu
menudishtitle = Label(wmenu_dish, text = "Italian Restaurant", font = ("Arial", 36 , "bold"), fg = "#B31200")
menudishtitle.place(x = 100 , y = 10)
menudishsubtitle = Label(wmenu_dish, text = "Manegeiment dish", font = ("Arial", 20, "bold" ))
menudishsubtitle.place(x = 185, y = 190)
#----------------------------------------------------------------
#butoons add , decla , update of dish 
buttonadddish = Button(wmenu_dish,text = "Añadir plato", font = ("Arial", 12, "bold"), fg = "#FFFFFF", bg = "#000000", command = open_manegedish)
buttonadddish.place(x = 250, y = 260 )
buttondecladish = Button(wmenu_dish, text = "Eliminar plato", font = ("Arial", 12, "bold"), fg = "#FFFFFF", bg = "#000000",command= open_tabledish)
buttondecladish.place(x = 245 , y = 330 )
buttonupdatedish = Button(wmenu_dish, text = "Actualizar plato", font = ("Arial", 12, "bold"), fg = "#FFFFFF", bg = "#000000" ,command= open_tabledish)
buttonupdatedish.place(x = 240, y = 390 )

wmenu_dish.mainloop()
