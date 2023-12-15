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
    windows_manege_order.destroy()
    subprocess.call(["python", "Interfaz\Table_order.py"])
    
#Function add dish
def add_dish_to_table():
    validate = True
    num_order_ = e_num_order.get().strip()
    num_table_ = e_num_table.get().strip()

    # Check if any field is empty
    if not num_order_ or not num_table_ :
        messagebox.showerror("Error", "No blank spaces allowed.")
        validate = False
    if not num_order_[0] == "#":
        messagebox.showerror("Error", "The order number must start with #")
        e_num_order.delete(0, 'end')
        validate = False 
    if not num_order_[1:len(num_order_)].isdigit():
        messagebox.showerror("Error", "Number of order only contain numbers.")
        e_num_order.delete(0, 'end')
        validate = False
    elif validate == True:              # Save dish data to a JSON file
        with open('Data\Orders.json', 'a') as f:
            order_data = {'#Order': num_order_, '#Table':num_table_ }
            json.dump(order_data, f)
            f.write('\n')
        
        messagebox.showinfo("Success", "Data saved successfully")
        review_dish()

#---------------------------------------------------------------
# Create window and configure it 
windows_manege_order = Tk() 
windows_manege_order.title("Italian Restaurant")
windows_manege_order.resizable(width=False, height=False)
windows_manege_order.geometry("600x500")
windows_manege_order.configure(bg= "#D6D6D6")
#---------------------------------------------------------------
# Bandera italiana con labels (Configuracion y ubicacion)
greenflag = Label(windows_manege_order,bg="#009C45", height=5,width=20)
whiteflag=  Label(windows_manege_order,bg="#FFFFFF", height=5,width=21)
redflag = Label(windows_manege_order,bg="#B31200", height=5,width=20)
greenflag.place(x=70, y=100)
whiteflag.place(x=217, y=100)
redflag.place(x=370, y=100)
#---------------------------------------------------------------
# title and text description (Configuracion y ubicacion)
manegementtitle = Label(
    windows_manege_order, 
    text= "Italian Restaurant", 
    font= ("Arial", 40 , "bold"),
    bg= "#D6D6D6", 
    fg= "#DE0A0D", 
)
manegementtitle.place(x=70, y=20) 
#---------------------------------------------------------------
# label and entry of number the pedida (Configuracion y ubicacion)
num_order = Label(
    windows_manege_order, 
    text= "# Order", 
    font= ("Arial", 12, "bold"), 
    bg= "#D6D6D6"
) 
num_order.place(x=70, y=260) 
e_num_order = Entry(windows_manege_order, font=("Arial", 10), width=16) 
e_num_order.place(x=70, y=285) 
#---------------------------------------------------------------
# label and entry name dish (Configuracion y ubicacion)
num_table = Label(
    windows_manege_order, 
    text= "# Table", 
    font= ("Arial", 12, "bold"), 
    bg= "#D6D6D6")
num_table.place(x=290, y=260)
#Definimos las options
options = ["1","2","3","4","5","6","7","8","9","10"]
# Entry name 
e_num_table = Combobox(windows_manege_order, values=options, state="readonly")
e_num_table.place(x=290, y=285)
#---------------------------------------------------------------
# button add dish (Configuracion y ubicacion)
add_dish = Button(
    windows_manege_order, 
    text="Add dish", 
    font=("arial", 12, "bold"), 
    bg="#29A873",
    fg="#FFFFFF",
    command=add_dish_to_table
    )
add_dish.place(x=250, y=400 )
#---------------------------------------------------------------
windows_manege_order.mainloop()