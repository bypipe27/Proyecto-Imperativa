"""
Felipe Ortiz Calan - 2380642
Samuel Valdes Gomez - 2380346"""

#Importamos librerias

from tkinter import *
import subprocess 
#-----------------------------------------------------------------
# Funcion para abrir la ventana de login 

def open_login():
    windowscero.destroy()   #Close the windows_cero 
    subprocess.call(["python", "Interfaz\Login.py"]) #Open the windows_login 

def open_register():
    windowscero.destroy()   #Close the windows_cero 
    subprocess.call(["python", "Interfaz\Register.py"]) #Open the windows_register 

#----------------------------------------------------------------
# Definimos la ventana principal y configuramos
windowscero = Tk()
windowscero.title("Italian Restaurant")
windowscero.resizable(width = False, height = False)
windowscero.geometry("600x500")
windowscero.configure(bg = "white")
#----------------------------------------------------------------
# Bandera italiana con labels (Configuracion y ubicacion) 
redflag = Label(windowscero,bg = "green" ,height = 5 , width = 20)
whiteflag=  Label(windowscero,bg = "white", height = 5 , width = 21)
greenflag = Label(windowscero,bg = "red", height = 5 , width = 20)

redflag.place( x = 70, y = 100)
whiteflag.place( x = 217, y = 100)
greenflag.place( x = 370, y = 100)
#----------------------------------------------------------------
# title and text description (Configuracion y ubicacion)
cerotitle = Label(windowscero, text = "Italian Restaurant", font = ("Arial", 40 , "bold"), bg = "silver", fg = "red", relief = "raised")
cerotext =  Label(windowscero,
                text = (
"Enjoy authentic Italian flavors in our cozy restaurant." 
" From classic pastas to artisanal pizzas,"
"each bite is a unique experience." 
" Welcome to a place where passion meets quality in every dish."),
                font = ("Arial", 12),
                bg = "white",
                justify = "left",
                wraplength = 452)

cerotitle.place(x = 70 , y = 20)
cerotext.place(x = 70 , y = 200)
#----------------------------------------------------------------
# button register and button login ( Configure buttons and ubications )
cerologinbutton = Button(windowscero, text = "Iniciar sesion", font = ("arial", 12), bg = "gray", fg = "White", command = open_login)
ceroregisterbutton = Button(windowscero, text = "register account", font = ("arial", 12), bg = "gray", fg = "White", command = open_register)

cerologinbutton.place(x = 250, y = 300 )
ceroregisterbutton.place(x = 240 , y = 350 )

windowscero.mainloop() 


