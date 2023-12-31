"""
Felipe Ortiz Calan - 2380642
Samuel Valdes Gomez - 2380346
Santiago Velasquez Bedoya  - 2380378

Proyecto final - Fundamentos de programacion Imperativa 
Grupo - 52 
Docente: Luis German Toro
"""
#----------------------------------------------------------------
from tkinter import *
from tkinter import ttk 
import subprocess 
import json
from tkinter import messagebox 
from tkinter.ttk import Combobox 
#---------------------------------------------------------------


#---------------------------------------------------------------
def delete_row():
    selected = table_or.selection()
    if not selected:
        messagebox.showerror("Error", "No row selected.")
        return

    # Guardamos el nombre del plato seleccionada para eliminarla del JSON 
    table_name = table_or.item(selected)['text']  # Convert to int for later comparison

    # Eliminamos la fila de la tabla 
    table_or.delete(selected)

    # Delete the row from the JSON file
    with open('Data/Dish.json', 'r') as f:
        tables = [json.loads(line) for line in f] # Cargo la informacion del arhivo recorriendo linea por linea 
    tables = [table for table in tables if table['name'] != table_name]  # Hacemos el cambio 
    with open('Data/Dish.json', 'w') as f: # Escribimos la informacion para la linea 
        for table in tables:
            f.write(json.dumps(table) + '\n') # Sobre escribimos la informacion en el archivo 
#----------------------------------------------------------------------------- 
         
# Funcion para actualizar una fila de la tabla 
def update_row():
    selected = table_or.selection() #Selected row
    if not selected:
        messagebox.showerror("Error", "No row selected.")
        return 
    # Creamos ventana para actualizar la fila 
    global update_window # la definimos como global para cerrala en la segunda funcion 
    update_window = Toplevel() #New window
    update_window.title("Update Order")
    update_window.geometry("300x300") 
    #Definimos unas variables temporales para facilitar la actualizacion 
    numor_u = StringVar()
    numtab_u = StringVar()
    # Create entry fields for each column
    tittle_u = Label(update_window, text="Update Order", font=("Arial", 20)).pack() #Title 
    labnum_u = Label(update_window, text="Number Order").pack() #Label 
    Entry(update_window, textvariable=numor_u).pack() #Entry 
    labtab_u = Label(update_window, text="Number table").pack() #Label
    Entry(update_window, textvariable=numtab_u).pack() #Entry 
    # Update button in the top windows 
    Button(
    update_window, 
    text="Confirm",
    justify="center",
    font=("Arial", 12, "bold"),
    bg="#3B7CC2",
    fg="#FFFFFF", 
    command=lambda: confirm_update(selected, numor_u, numtab_u)).pack(pady=10
)

def confirm_update(selected, numor_u, numtab_u):
    table_or.item(selected, values=(numor_u.get(), numtab_u.get())) #Update the table 
    update_window.destroy() #Close the window 
#---------------------------------------------------------------
# Funcion para regresar al menu principal
def back_to_menu():
    table_order.destroy()
    subprocess.call(["python", "Interfaz\Menu.py"])
#---------------------------------------------------------------
# Funcion para tomar una orden
def take_order():
    selected = table_or.selection() #Selected row 
    if not selected:
        messagebox.showerror("Error", "No row selected.")
        return 
    else:
        messagebox.showinfo("Success", "Order taken successfully")
        table_or.item(selected) # Convert to int for later comparison
        table_or.delete(selected)
#---------------------------------------------------------------
# Create window and configure 
table_order = Tk()
table_order.title("Table Order")
table_order.geometry("600x500")
table_order.resizable(width=False, height=False)
table_order.configure(bg="#F0F0F0")
#---------------------------------------------------------------
# Bandera italiana con labels en ventana dish menu (Configuracion y ubicacion) 
greenflag = Label(table_order, bg="#009C45", height=3, width=20)
whiteflag=  Label(table_order, bg="#FFFFFF", height=3, width=21)
redflag = Label(table_order, bg="#B31200", height=3, width=20)
greenflag.place(x=70, y=100)
whiteflag.place(x=217, y=100)
redflag.place(x=370, y=100)
#----------------------------------------------------------------
# tittle and subtitles en el order menu
menu_order_title = Label(table_order, text="Italian Restaurant", font=("Arial", 36 , "bold"), fg="#DE0A0D")
menu_order_title.place(x=100 , y=10)
menu_order_subtitle = Label(table_order, text="Table orders", font=("Arial", 20, "bold" ))
menu_order_subtitle.place(x=185, y=160)
#----------------------------------------------------------------

frame_subtab = Frame(table_order, bg="#FFFFFF", width=600, height=500)
frame_subtab.place(x=140, y= 230)
#Table
table_or = ttk.Treeview(frame_subtab, columns=("1","2"), height=10,)

#Columns
table_or.column("#0", width=20, minwidth=0 , anchor=CENTER )
table_or.column("1", width=50, minwidth=40, anchor=CENTER)
table_or.column("2", width=50, minwidth=40, anchor=CENTER)

#Headings 
table_or.heading("1", text="#Order")
table_or.heading("2", text="#Table")
#---------------------------------------------------------------
# Leemos y escribimos la data del json 
try:
    with open('Data\Orders.json', 'r') as f:
        tables = {record['#Order']: record for record in (json.loads(line) for line in f)}
except (FileNotFoundError, json.JSONDecodeError):
    tables = {}

# Add the data to the table
for key, record in tables.items():
    if isinstance(record, dict):
        table_or.insert(
            "", 
            'end', 
            values=(record.get('#Order'), 
                    record.get('#Table'))
            )

#---------------------------------------------------------------
#Pack table
table_or.pack() 

boton_delete = Button(
    table_order,
    justify= "center",
    font= ('Arial,',12,'bold'),
    bg="#B31200",
    fg ="#FFFFFF",
    text="Delete",
    command=delete_row,
    width= 8
)
boton_delete.place(x=345, y=320)

boton_update = Button(
    table_order,
    justify= "center",
    text="Update",
    bg="#3B7CC2",
    font=('Arial',12,'bold'),
    fg ="#FFFFFF",
    command=update_row, 
    width= 8
)
boton_update.place(x=345, y=360) 
#---------------------------------------------------------------
#boton para regresar al menu principal
button_back = Button(
    table_order, 
    text="Back", 
    font=("Arial", 12, "bold"), 
    fg="#FFFFFF", 
    bg="#63C2AC",
    width=8,
    command=back_to_menu
)
button_back.place(x=30, y=435)
#---------------------------------------------------------------
#Butoon for take a order
button_take_order = Button(
    table_order, 
    text="Take order", 
    font=("Arial", 12, "bold"), 
    fg="#FFFFFF", 
    bg="#29A873",
    command=take_order,
    width= 8
)
button_take_order.place(x=345, y=405)

table_order.mainloop()