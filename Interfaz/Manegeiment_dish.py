#-----------------------------------------------------------------------------
#importamos librerias 
from tkinter import * 
from tkinter import messagebox
import subprocess
import json
#---------------------------------------------------------------

#Function to validate name 
def validate_name():
    name = var_name.get()
    if not name.isalpha():
        messagebox.showerror("Error", "Name should only contain letters.")
        var_name.set('')


#Function validate description
def validate_description(*args):
    description = var_description.get()
    description_without_spaces = description.replace(" ", "")
    if not description_without_spaces.isalpha():
        messagebox.showerror("Error", "Description should only contain letters and spaces.")
        var_description.set('')


#Function to validate price
def validate_price(*args):
    price = var_price.get()
    if not price.isdigit():
        messagebox.showerror("Error", "Price should be an integer.")
        var_price.set('')


#Function to validate stock 
def validate_stock():
    stock = stock_dish.get()
    if stock not in ["Si","No","SI","NO"]:
        invalid_stock()


def invalid_stock():
    messagebox.showerror("Error" ) 


def review_dish():
    windows_manege_dish.destroy()
    subprocess.call(["python", "Interfaz\Table_dishes.py"])


#Function add dish
def add_dish_to_table():
    
    name = dish_name.get().strip()
    price = entry_price_dish.get().strip()
    description = edescription_dish.get().strip()
    disponibility = stock_dish.get().strip()

    # Check if any field is empty
    if not name or not price or not description or not disponibility:
        messagebox.showerror("Error", "No blank spaces allowed.")
        return

    # Save dish data to a JSON file
    with open('Data\Dish.json', 'a') as f:
        dish_data = {'name': name, 'price': price, 'description': description, 'disponibility': disponibility}
        json.dump(dish_data, f)
        f.write('\n')

    # Show a success message
    messagebox.showinfo("Success", "Data saved successfully")
    review_dish()

# Create window and configure it 
windows_manege_dish = Tk() 
windows_manege_dish.title("Italian Restaurant")
windows_manege_dish.resizable(width = False, height = False)
windows_manege_dish.geometry("600x500")
windows_manege_dish.configure(bg = "white")
#---------------------------------------------------------------
# Bandera italiana con labels (Configuracion y ubicacion)
redflag = Label(windows_manege_dish,bg = "green" ,height = 5 , width = 20)
whiteflag=  Label(windows_manege_dish,bg = "white", height = 5 , width = 21)
greenflag = Label(windows_manege_dish,bg = "red", height = 5 , width = 20)

redflag.place( x = 70, y = 100)
whiteflag.place( x = 217, y = 100)
greenflag.place( x = 370, y = 100)
#---------------------------------------------------------------
# title and text description (Configuracion y ubicacion)
manegementtitle = Label(windows_manege_dish, text = "Italian Restaurant", font = ("Arial", 40 , "bold"), bg = "silver", fg = "red", relief = "raised")
manegementtitle.place(x = 70 , y = 20) 
#---------------------------------------------------------------
# label and entry name dish (Configuracion y ubicacion)
name_dish = Label(windows_manege_dish, text = "Name dish", font = ("Arial", 12), bg = "white")
name_dish.place(x = 70 , y = 200)
# Entry name 
dish_name = Entry(windows_manege_dish)
dish_name.place(x = 70 , y = 230)
#---------------------------------------------------------------
# label and entry price dish (Configuracion y ubicacion)
price_dish = Label(windows_manege_dish, text = "Price dish", font = ("Arial", 12), bg = "white")
price_dish.place(x = 70 , y = 260)
#Price entry 
var_price = StringVar()
var_price.trace('w', validate_price)
entry_price_dish = Entry(windows_manege_dish, textvariable = var_price)
entry_price_dish.place(x = 70 , y = 290)
#---------------------------------------------------------------
# label and entry description dish (Configuracion y ubicacion)
ldescrpit_dish = Label(windows_manege_dish, text = "Description dish", font = ("Arial", 12), bg = "white")
ldescrpit_dish.place(x = 70 , y = 320)
#Description entry 
var_description = StringVar()
var_description.trace('w', validate_description)
edescription_dish = Entry(windows_manege_dish, textvariable = var_description)
edescription_dish.place(x = 70 , y = 350)
#---------------------------------------------------------------
# label and entry availability dish (Configuracion y ubicacion)
availability_dish = Label(windows_manege_dish, text = "Availability dish", font = ("Arial", 12), bg = "white")
availability_dish.place(x = 70 , y = 380)
#Availability entry 
stock_dish = Entry(windows_manege_dish,validatecommand=validate_stock)
stock_dish.place(x = 70 , y = 410)
#---------------------------------------------------------------
# button add dish (Configuracion y ubicacion)
add_dish = Button(windows_manege_dish, text = "Add dish", font = ("arial", 12), bg = "gray", fg = "White", command = add_dish_to_table)
add_dish.place(x = 250, y = 450 )
#---------------------------------------------------------------
windows_manege_dish.mainloop()
