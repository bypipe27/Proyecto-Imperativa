"""
Felipe Ortiz Calan - 2380642
Samuel Valdes Gomez - 2380346
Santiago Velasquez Bedoya  - 2380378

Proyecto final - Fundamentos de programacion Imperativa 
Grupo - 52 
Docente: Luis German Toro
"""
#-----------------------------------------------------------------
#Importamos librerias
from tkinter import * 
import subprocess 
#-----------------------------------------------------------------
# Funcion para abrir la ventana de login 
def open_login():
    windowscero.destroy()   # Destroy the windows_cero (Destruir el windows_cero)
    subprocess.call(["python", "Interfaz\Login.py"]) # Open the script windows_login (Abrir el script ventana_inicio_sesion)

def open_register():
    windowscero.destroy()   # Destroy the windows_cero (Destruir el windows_cero) 
    subprocess.call(["python", "Interfaz\Register.py"]) #Open the script windows_register (Abrir el script ventana_registrarse)
#----------------------------------------------------------------
# Definimos la ventana principal y configuramos (Define the main window and configure)
windowscero = Tk()
windowscero.title("Italian Restaurant")
windowscero.resizable(width = False, height = False)
windowscero.geometry("600x500")
windowscero.configure(bg = "#D6D6D6")
#----------------------------------------------------------------
# Bandera italiana con labels (Configuracion y ubicacion) 
greenflag = Label(windowscero,bg = "#009C45" ,height = 5 , width = 20)
whiteflag=  Label(windowscero,bg = "#FFFFFF", height = 5 , width = 21)
redflag = Label(windowscero,bg = "#B31200", height = 5 , width = 20)
greenflag.place( x = 70, y = 100)
whiteflag.place( x = 217, y = 100)
redflag.place( x = 370, y = 100)
#----------------------------------------------------------------
# title and text description (Configuracion y ubicacion)
cero_title = Label(
    windowscero, 
    text = "Italian Restaurant", 
    font = ("Arial", 40 , "bold"), 
    bg = "#D6D6D6", 
    fg = "#E81522", 
)
cero_text =  Label(
    windowscero,
    text = (
"Enjoy authentic Italian flavors in our cozy restaurant." 
" From classic pastas to artisanal pizzas,"
"each bite is a unique experience." 
" Welcome to a place where passion meets quality in every dish."),
    font = ("Arial", 12),
    bg = "#D6D6D6",
    justify = "left",
    wraplength = 452
)
# Ubicacion de los labels 
cero_title.place(x = 70 , y = 20)
cero_text.place(x = 70 , y = 200)
#----------------------------------------------------------------
# button register and button login ( Configure buttons and ubications )
cero_login_button = Button(
    windowscero, 
    text="Login", 
    font=("arial", 12, "bold"), 
    bg="#3B7CC2", 
    fg="#FFFFFF", 
    command=open_login
)
cero_login_button.place(x=250, y=300 )

cero_register_button = Button(
    windowscero, 
    text="Register account", 
    font=("arial", 12, "bold"), 
    bg="#29A873", 
    fg="#FFFFFF", 
    command=open_register
)
cero_register_button.place(x=210 , y=350 )
#----------------------------------------------------------------
# mainloop the windows 
windowscero.mainloop() 


