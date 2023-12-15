"""
Felipe Ortiz Calan - 2380642
Samuel Valdes Gomez - 2380346
Santiago Velasquez Bedoya  - 2380378

Proyecto final - Fundamentos de programacion Imperativa 
Grupo - 52 
Docente: Luis German Toro
"""
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
wmenu_order.configure(bg="#D6D6D6")
# ---------------------------------------------------------------
# Bandera italiana con labels (Configuracion y ubicacion)
greenflag = Label(wmenu_order,bg = "#009C45" ,height = 5 , width = 20)
whiteflag=  Label(wmenu_order,bg = "#FFFFFF", height = 5 , width = 21)
redflag = Label(wmenu_order,bg = "#B31200", height = 5 , width = 20)
greenflag.place( x = 70, y = 100)
whiteflag.place( x = 217, y = 100)
redflag.place( x = 370, y = 100)
# ----------------------------------------------------------------
# tittle and subtitles en el order_menu
menu_order_title = Label(
    wmenu_order, 
    text = "Italian Restaurant", 
    font = ("Arial", 36 , "bold"), 
    fg = "#DE0A0D",
    bg="#D6D6D6",
)
menu_order_title.place(x = 100 , y = 10)
# ---------------------------------------------------------------
menu_order_subtitle = Label(
    wmenu_order, 
    text = "Manegeiment order", 
    font = ("Arial", 20, "bold" ),
    bg="#D6D6D6"
)
menu_order_subtitle.place(x = 185, y = 190)
# ---------------------------------------------------------------
#butoons add , decla , update of order
button_add_order = Button(
    wmenu_order,
    text = "Order", 
    font = ("Arial", 12, "bold"), 
    fg = "#FFFFFF", 
    bg = "#29A873",
    width=12,
    command = open_manegeorder
)
button_add_order.place(x = 240, y = 260 )
#---------------------------------------------------------------
button_decla_order = Button(
    wmenu_order, 
    text="Delete order", 
    font=("Arial", 12, "bold"),
    fg="#FFFFFF",
    bg="#DE0A0D",
    width=12, 
    command=open_tableorder
)
button_decla_order.place(x = 240 , y = 330 )
#--------------------------------------------------------------- 
button_update_order = Button(
    wmenu_order,
    text="Update order",
    font=("Arial", 12, "bold"), 
    fg="#FFFFFF", 
    bg="#3B7CC2",
    width= 12, 
    command=open_tableorder
)
button_update_order.place(x=240, y=390 )
#---------------------------------------------------------------
wmenu_order.mainloop()