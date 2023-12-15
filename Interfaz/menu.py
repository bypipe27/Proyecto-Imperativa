"""
Felipe Ortiz Calan - 2380642
Samuel Valdes Gomez - 2380346
Santiago Velasquez Bedoya  - 2380378

Proyecto final - Fundamentos de programacion Imperativa 
Grupo - 52 
Docente: Luis German Toro
"""
#--------------------------------------------------------------------------------
#Importamos las librerias necesarias para el funcionamiento del programa 
from tkinter import *
from tkinter import messagebox
import subprocess 
#--------------------------------------------------------------------------------
#Funciones para abrir las ventanas de menu dish, login y menu
def open_dish():
    windowsmenu.withdraw()
    subprocess.call(["python", "Interfaz/Menu_dish.py"])
    
def open_table():
    windowsmenu.withdraw()
    subprocess.call(["python", "Interfaz/Menu_Table.py"])

def open_delivery():
    windowsmenu.withdraw()
    subprocess.call(["python", "Interfaz/Menu_order.py"])

def close_program():
    windowsmenu.destroy()
    subprocess.call(["python", "Interfaz/windows_0.py"])

#--------------------------------------------------------------------------------
#windowsmenu despues de iniciar sesion 
windowsmenu = Tk()
windowsmenu.geometry("600x500")
windowsmenu.resizable(width = False , height = False)
windowsmenu.title("windowsmenu")
#-------------------------------------------------------------------------------------------------
 # Bandera italiana con labels en ventana de menu (Configuracion y ubicacion) 
greenflag = Label(windowsmenu,bg = "#009C45" ,height = 5 , width = 20)
whiteflag=  Label(windowsmenu,bg = "#FFFFFF", height = 5 , width = 21)
redflag = Label(windowsmenu,bg = "#B31200", height = 5 , width = 20)
greenflag.place( x = 70, y = 100)
whiteflag.place( x = 217, y = 100)
redflag.place( x = 370, y = 100)
#-------------------------------------------------------------------------------------------------
#title and subtitles en el menu de opciones configuracion and positions 
optionsmenutitle = Label(
    windowsmenu, 
    text = "Italian Restaurant", 
    font = ("Arial", 36 , "bold"), 
    fg = "#DE0A0D"
)
optionsmenutitle.place(x = 100 , y = 10)
#-------------------------------------------------------------------------------------------------
optionsmenusubtitle = Label(windowsmenu, text = "Welcome", font = ("Arial", 20, "bold" ))
optionsmenusubtitle.place(x = 240, y = 190 )
#-------------------------------------------------------------------------------------------------
#butonns del menu configuracion and postions 
optionsbutondish = Button(
    windowsmenu,
    text="Dish management", 
    font=("arial", 12, "bold"), 
    relief="raised",
    fg="#F9F6FF",
    bg="#1A9DDE",
    command=open_dish
)
optionsbutondish.place(x = 232, y = 240 )
#--------------------------------------------------------------------------------------------------
#Boton que abre la ventana de menu de mesas 
optionsbutontable = Button(
    windowsmenu, 
    text = "Table management", 
    font = ("arial", 12, "bold"), 
    relief = "raised",
    fg="#F9F6FF", 
    bg="#DEAD1B",
    command= open_table
) 
optionsbutontable.place(x = 230, y = 300 )
#-----------------------------------------------------------------------------------------------------
#Boton que abre la ventana de menu de pedidos 
optionsbutondelivery = Button(
    windowsmenu,
    text = "Order management",  
    font = ("arial", 12,"bold"), 
    relief = "raised",
    fg="#F9F6FF", 
    bg="#16A340",
    command = open_delivery 
)
optionsbutondelivery.place(x = 228 , y = 360 )
#-----------------------------------------------------------------------------------------------------
#Boton que cierra la ventana de menu
optionsbutonclose = Button(windowsmenu,
                           text = "Log out", 
                           font = ("arial", 12, "bold"), 
                           relief = "raised", 
                           bg="#CC0206",
                           fg="#F9F6FF",
                           command= close_program )
optionsbutonclose.place(x = 275 , y = 420 )
#-------------------------------------------------------------------------------------
windowsmenu.mainloop() 