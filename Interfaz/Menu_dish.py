# Importamos las librerias necesarias para el funcionamiento de la ventana 
from tkinter import *
import subprocess
#Funciones 
def open_manedish():
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
wmenu_dish.resizable(width=False, height=False)
wmenu_dish.configure(bg="#D6D6D6")
#---------------------------------------------------------------
# Bandera italiana con labels en ventana dish menu (Configuracion y ubicacion) 
greenflag = Label(wmenu_dish,bg = "#009C45" ,height = 5 , width = 20)
whiteflag=  Label(wmenu_dish,bg = "#FFFFFF", height = 5 , width = 21)
redflag = Label(wmenu_dish,bg = "#B31200", height = 5 , width = 20)
greenflag.place(x=70, y=100)
whiteflag.place(x=217, y=100)
redflag.place(x=370, y=100)
#----------------------------------------------------------------
# tittle and subtitles en el dishmenu
menu_dish_title = Label(wmenu_dish, 
                        text="Italian Restaurant", 
                        font=("Arial", 36 , "bold"),
                        bg="#D6D6D6", 
                        fg="#DE0A0D")
menu_dish_title.place(x=100, y=10)
menu_dish_subtitle = Label(wmenu_dish, 
                           text="Manegeiment dish", 
                           font=("Arial",20,"bold" ),
                           bg="#D6D6D6")
menu_dish_subtitle.place(x=185, y=190)
#----------------------------------------------------------------
#butoons add , decla , update of dish 
button_add_dish = Button(wmenu_dish,
                       text="Add dish", 
                       font=("Arial", 12, "bold"), 
                       fg="#FFFFFF", 
                       bg="#3B7CC2",
                       width=12, 
                       command = open_manedish) 
button_add_dish.place(x=240, y=260)
#----------------------------------------------------------------
button_decla_dish = Button(
    wmenu_dish, 
    text="Delete dish", 
    font=("Arial", 12, "bold"), 
    fg="#FFFFFF", 
    bg="#DE0A0D",
    width=12,
    command=open_tabledish
)
button_decla_dish.place(x=240 , y=330)
#----------------------------------------------------------------
button_update_dish = Button(wmenu_dish, 
                          text="Update dish", 
                          font=("Arial", 12, "bold"), 
                          fg="#FFFFFF", 
                          bg="#29A873" ,
                          width=12,
                          command= open_tabledish)
button_update_dish.place(x=240, y=390)
#----------------------------------------------------------------
#mainloop
wmenu_dish.mainloop()
