#Importamos las librerias necesarias para el funcionamiento del programa 
from tkinter import *
from tkinter import messagebox
import subprocess 
#Funciones para abrir las ventanas de menu dish , login y menu
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

#windowsmenu despues de iniciar sesion 
windowsmenu = Tk()
windowsmenu.withdraw()
windowsmenu.geometry("600x500")
windowsmenu.resizable(width = False , height = False)
windowsmenu.title("windowsmenu")
#----------------------------------------------------------------
 # Bandera italiana con labels en ventana de menu (Configuracion y ubicacion) 
redflag = Label(windowsmenu,bg = "green" ,height = 5 , width = 20)
whiteflag=  Label(windowsmenu,bg = "white", height = 5 , width = 21)
greenflag = Label(windowsmenu,bg = "red", height = 5 , width = 20)
redflag.place( x = 70, y = 100)
whiteflag.place( x = 217, y = 100)
greenflag.place( x = 370, y = 100)
#----------------------------------------------------------------
#title and subtitles en el menu de opciones configuracion and positions 
optionsmenutitle = Label(windowsmenu, text = "Italian Restaurant", font = ("Arial", 36 , "bold"), fg = "red")
optionsmenutitle.place(x = 100 , y = 10)
optionsmenusubtitle = Label(windowsmenu, text = "Welcome", font = ("Arial", 20, "bold" ))
optionsmenusubtitle.place(x = 240, y = 190 )
#----------------------------------------------------------------
#butonns del menu configuracion and postions 
optionsbutondish = Button(
    windowsmenu, 
    text="Dish management", 
    font=("arial", 12), 
    relief="raised",
    command=open_dish
)
optionsbutondish.place(x = 242, y = 240 )
optionsbutontable = Button(windowsmenu, text = "Table management", font = ("arial", 12), relief = "raised", command= open_table) 
optionsbutontable.place(x = 240, y = 300 )
optionsbutondelivery = Button(windowsmenu,text = "Order management",  font = ("arial", 12), relief = "raised", command = open_delivery )
optionsbutondelivery.place(x = 242 , y = 360 )
optionsbutonclose = Button(windowsmenu,text = "Log out", font = ("arial", 12), relief = "raised", command= close_program )
optionsbutonclose.place(x = 275 , y = 420 )