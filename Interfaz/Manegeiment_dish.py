"""
Felipe Ortiz Calan - 2380642
Samuel Valdes Gomez - 2380346
Santiago Velasquez Bedoya  - 2380378

Proyecto final - Fundamentos de programacion Imperativa 
Grupo - 52 
Docente: Luis German Toro
"""
#-----------------------------------------------------------------------------
#importamos librerias 
from tkinter import * 
from tkinter import messagebox
import subprocess
import json
from tkinter.ttk import Combobox 
#---------------------------------------------------------------
def review_dish():
    windows_manege_dish.destroy()
    subprocess.call(["python", "Interfaz\Table_dishes.py"])
    
#Function add dish
def add_dish_to_table():
    validate = True
    name = entry_dish_name.get().strip()
    price = entry_price_dish.get().strip()
    description = entry_dish_description.get().strip()
    disponibility = entry_stock_dish.get().strip()

    # Check if any field is empty
    if not name or not price or not description or not disponibility:
        messagebox.showerror("Error", "No blank spaces allowed.")
        validate = False
    if not name.isalpha():
        messagebox.showerror("Error", "Name should only contain letters.")
        entry_dish_name.delete (0, 'end')
        validate = False
    if not price.isdigit():
        messagebox.showerror("Error", "Price should be an integer.")
        entry_price_dish.delete(0,'end')
        validate = False
    if  not description.isalpha():
        messagebox.showerror("Error", "Description should only contain letterrs.")
        entry_dish_description.delete(0, 'end')
        validate = False 
    if not disponibility:
        messagebox.showerror("Error", "Selected a option")
        validate = False
    elif validate == True:              # Save dish data to a JSON file
        with open('Data\Dish.json', 'a') as f:
            dish_data = {'name': name, 
                         'price': price, 
                         'description': description, 
                         'disponibility': disponibility}
            json.dump(dish_data, f)
            f.write('\n')
        
        messagebox.showinfo("Success", "Data saved successfully")
        review_dish()


#---------------------------------------------------------------
# Create window and configure it 
windows_manege_dish = Tk() 
windows_manege_dish.title("Italian Restaurant")
windows_manege_dish.resizable(width= False, height= False)
windows_manege_dish.geometry("600x500")
windows_manege_dish.configure(bg= "#D6D6D6")
#---------------------------------------------------------------
# Bandera italiana con labels (Configuracion y ubicacion)
greenflag = Label(windows_manege_dish,bg="#009C45", height=5, width=20)
whiteflag=  Label(windows_manege_dish,bg="#FFFFFF", height=5, width=21)
redflag = Label(windows_manege_dish,bg="#B31200", height=5, width=20)
greenflag.place(x=70, y=100)
whiteflag.place(x=217, y=100)
redflag.place(x=370, y=100)
#---------------------------------------------------------------
# title and text description (Configuracion y ubicacion)
manegementtitle = Label(
    windows_manege_dish, 
    text="Italian Restaurant", 
    font=("Arial", 40 , "bold"), 
    bg="#D6D6D6", 
    fg="#DE0A0D", 
)
manegementtitle.place(x=70, y=20) 
#---------------------------------------------------------------
# label and entry name dish (Configuracion y ubicacion)
name_dish = Label(
    windows_manege_dish, 
    text="Name dish", 
    font=("Arial", 12, "bold"), 
    bg="#D6D6D6"
)
name_dish.place(x=70, y=200)
# Entry name 
entry_dish_name = Entry(windows_manege_dish, width=23)
entry_dish_name.place(x=70, y=230)
#---------------------------------------------------------------
# label and entry price dish (Configuracion y ubicacion)
price_dish = Label(
    windows_manege_dish, 
    text= "Price dish", 
    font= ("Arial", 12, "bold"), 
    bg= "#D6D6D6"
)
price_dish.place(x=350, y=200)
#Price entry 

entry_price_dish = Entry(windows_manege_dish, width=23)
entry_price_dish.place(x=350, y=230)
#---------------------------------------------------------------
# label and entry description dish (Configuracion y ubicacion)
ldescrpit_dish = Label(
    windows_manege_dish, 
    text= "Description dish", 
    font= ("Arial", 12, "bold"), 
    bg= "#D6D6D6"
)
ldescrpit_dish.place(x=70, y=280)
#Description entry 
entry_dish_description = Entry(windows_manege_dish, width=23)
entry_dish_description.place(x=70, y=310)
#---------------------------------------------------------------
# label and entry availability dish (Configuracion y ubicacion)
availability_dish = Label(
    windows_manege_dish, 
    text= "Availability dish", 
    font= ("Arial", 12, "bold"), 
    bg= "#D6D6D6"
)
availability_dish.place(x=350, y=280)
#Definimos las options
options = [" ","Yes","No"] 
#Availability entry 
entry_stock_dish = Combobox(windows_manege_dish, values=options, state="readonly" )
entry_stock_dish.place(x=350, y=310)
#---------------------------------------------------------------
# button add dish (Configuracion y ubicacion)
add_dish = Button(
    windows_manege_dish, 
    text="Add dish", 
    font=("arial", 12, "bold"), 
    bg="#29A873", 
    fg="#FFFFFF", 
    command=add_dish_to_table)
add_dish.place(x=240, y=350)
#---------------------------------------------------------------
windows_manege_dish.mainloop()