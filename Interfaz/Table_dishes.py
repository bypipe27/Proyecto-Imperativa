"""
Felipe Ortiz Calan - 2380642
Samuel Valdes Gomez - 2380346
Santiago Velasquez Bedoya  - 2380378

Proyecto final - Fundamentos de programacion Imperativa 
Grupo - 52 
Docente: Luis German Toro
"""
#-------------------------------------------------------------------------------
from tkinter import *
from tkinter import ttk 
import subprocess 
import json
from tkinter import messagebox 
from tkinter.ttk import Combobox 
#---------------------------------------------------------------
def delete_row():
    selected = table_di.selection()
    if not selected:
        messagebox.showerror("Error", "No row selected.")
        return

    # Guardamos el nombre del plato seleccionada para eliminarla del JSON 
    table_name = table_di.item(selected)['text']  # Convert to int for later comparison

    # Eliminamos la fila de la tabla 
    table_di.delete(selected)

    # Delete the row from the JSON file
    with open('Data/Dish.json', 'r') as f:
        tables = [json.loads(line) for line in f] # Cargo la informacion del arhivo recorriendo linea por linea 
    tables = [table for table in tables if table['name'] != table_name]  # Hacemos el cambio 
    with open('Data/Dish.json', 'w') as f: # Escribimos la informacion para la linea 
        for table in tables:
            f.write(json.dumps(table) + '\n') # Sobre escribimos la informacion en el archivo 
#----------------------------------------------------------------------------- 

#---------------------------------------------------------------            
# Funcion para actualizar una fila de la tabla 
def update_row():
    selected = table_di.selection() #Selected row
    if not selected:
        messagebox.showerror("Error", "No row selected.")
        return 
    # Creamos ventana para actualizar la fila 
    global update_window # la definimos como global para cerrala en la segunda funcion 
    update_window = Toplevel() #New window
    update_window.title("Update Dish")
    update_window.geometry("400x400") 
    #Definimos unas variables temporales para facilitar la actualizacion 
    name_u = StringVar()
    price_u = StringVar()
    descrip_u = StringVar()
    availability_u = StringVar() 
    # Create entry fields for each column
    tittle_u = Label(update_window, text="Update Dish", font=("Arial", 20)).pack() #Title 
    labname_u = Label(update_window, text="Name").pack() #Label 
    Entry(update_window, textvariable=name_u).pack() #Entry 
    labprice_u = Label(update_window, text="Price").pack() #Label
    Entry(update_window, textvariable=price_u).pack() #Entry 
    labdescrip_u = Label(update_window, text="Description").pack() #Label
    Entry(update_window, textvariable=descrip_u).pack() #Entry  
    # Definimos las options
    options = ["Yes","No"] 
    labdispon_u = Label(update_window, text="Availability").pack() #Label 
    Combobox(update_window, values=options, state="readonly" ,textvariable=availability_u).pack() #Entry 
    
    # Update button in the top windows 
    Button(
        update_window,
        justify="center",
        text="Confirm",
        font=("Arial", 12, "bold"),
        bg="#3B7CC2",
        fg="#FFFFFF",  
        command=lambda: confirm_update(selected, name_u, price_u, descrip_u, availability_u)).pack(pady=10)

def confirm_update(selected, name_u, price_u, descrip_u, availability_u):
    table_di.item(selected, values=(name_u.get(), price_u.get(), descrip_u.get(), availability_u.get()))
    update_window.destroy() #Close the window
#---------------------------------------------------------------
# Funcion para regresar al menu principal
def back_to_menu():
    table_table.destroy()
    subprocess.call(["python", "Interfaz\menu.py"]) 
table_table = Tk()
table_table.title("Managementc Dish")
table_table.geometry("600x500")
table_table.resizable(width=False, height=False)
table_table.configure(bg="#F0F0F0")
#---------------------------------------------------------------
# Bandera italiana con labels en ventana dish menu (Configuracion y ubicacion) 
greenflag = Label(table_table, bg="#009C45", height=3, width=20)
whiteflag=  Label(table_table,bg="#FFFFFF", height=3, width=21)
redflag = Label(table_table, bg="#B31200", height=3, width=20)
greenflag.place(x=70, y=100)
whiteflag.place(x=217, y=100)
redflag.place(x=370, y=100)
#----------------------------------------------------------------
# tittle and subtitles en el dishmenu
menudishtitle = Label(table_table, text="Italian Restaurant", font=("Arial", 36 , "bold"), fg="#B31200")
menudishtitle.place(x=100 , y=10)
menudishsubtitle = Label(table_table, text="Manegeiment dish", font=("Arial", 20, "bold" ))
menudishsubtitle.place(x=185, y=160)
#----------------------------------------------------------------

frame_subtab = Frame(table_table, bg="#FFFFFF", width=600, height=500)
frame_subtab.place(x=140, y=230)
#Table
table_di = ttk.Treeview(frame_subtab, columns=("1", "2", "3","4"))
#Columns
table_di.column("#0",width=0, minwidth=0, anchor=CENTER)
table_di.column("1",width=55, minwidth=55, anchor=CENTER)
table_di.column("2",width=105, minwidth=105, anchor=CENTER)
table_di.column("3",width=105, minwidth=105, anchor=CENTER)
table_di.column("4",width=75, minwidth=75, anchor=CENTER)

#Headings 
table_di.heading("#1", text="Name")
table_di.heading("2", text="Price $")
table_di.heading("3", text="Description")
table_di.heading("4", text="Availability")
#---------------------------------------------------------------
# Leemos y escribimos la data del json 
try:
    with open('Data\Dish.json', 'r') as f:
        tables = {record['name']: record for record in (json.loads(line) for line in f)}
except (FileNotFoundError, json.JSONDecodeError):
    tables = {}

# Add the data to the table
for key, record in tables.items():
    if isinstance(record, dict):
        table_di.insert(
            "", 
            'end', 
            values=(record.get('name'), 
                    record.get('price'), 
                    record.get('description'), 
                    record.get('disponibility'))
                    )
        
table_di.pack() 
#---------------------------------------------------------------
boton_delete = Button(
    table_table,
    justify= "center",
    font= ('Arial,',12,"bold"),
    bg="#B31200",fg ="#FFFFFF" , 
    text="Delete", command=delete_row , 
    width= 7)
boton_delete.place(x=510, y=350)
#---------------------------------------------------------------
boton_update = Button(
    table_table,
    justify= "center",
    text="Update",
    bg="#3B7CC2",
    font=('Arial',12,"bold"),
    fg="#FFFFFF",
    command=update_row, 
    width= 7)
boton_update.place(x=510, y=390) 
#---------------------------------------------------------------
#Boton para regresar al menu principal
button_back = Button(
    table_table,
    justify= "center",
    text="Back",
    bg="#63C2AC",
    font=('Arial',12,"bold"),
    fg="#FFFFFF",
    command=back_to_menu, 
    width= 7
) 
button_back.place(x=30, y=430) 
#--------------------------------------------------------------- 
table_table.mainloop()