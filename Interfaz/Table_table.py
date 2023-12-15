from tkinter import *
from tkinter import ttk 
import subprocess 
import json
from tkinter import messagebox 
from tkinter.ttk import Combobox
#---------------------------------------------------------------
#----------------------------------------------------------------------------- 
#Funcion para eliminar una table
def delete_row():
    selection = table_t.selection()
    if not selection:
        messagebox.showerror("Error", "No row selected.")
        return 
    
    # Guardamos el nombre de la mesa seleccionada para eliminarla del JSON
    table_name = int(table_t.item(selection)['values'][0])  # Convert to int for later comparison

    # Eliminamos la fila de la tabla 
    table_t.delete(selection) 
    # Delete the row from the JSON file
    with open('Data\Table.json', 'r') as f:
        tables = [json.loads(line) for line in f] # Cargo la informacion del arhivo recorriendo linea por linea
    tables = [table for table in tables if int(table['Table']) != table_name]  # Convert to int before comparing
    with open('Data\Table.json', 'w') as f: # Write the information in the file
        for table in tables:
            f.write(json.dumps(table) + '\n') # Write information with leap line
            
def update_row():
    selected = table_t.selection() #Selected row
    if not selected:
        messagebox.showerror("Error", "No row selected.")
        return 
    # Creamos ventana para actualizar la fila 
    global update_window # la definimos como global para cerrala en la segunda funcion 
    update_window = Toplevel() #New window
    update_window.title("Update Row")
    update_window.geometry("400x400") 
    #Definimos unas variables temporales para facilitar la actualizacion 
    table_u = StringVar()
    date_u = StringVar()
    hour_u = StringVar()
    people_u = StringVar() 
    # Create entry fields for each column
    tittle_u = Label(update_window, text="Update Row", font=("Arial", 20)).pack() #Title 
    # Definimos las options
    options = ["1","2","3","4","5","6","7","8","9","10"]
    labtable_u = Label(update_window, text="Table").pack() #Label 
    Combobox(update_window,values= options , state= "readonly" ,textvariable=table_u).pack() #Entry 
    labdate_u = Label(update_window, text="Date").pack() #Label
    Entry(update_window, textvariable=date_u).pack() #Entry 
    labhour_u = Label(update_window, text="Hour").pack() #Label
    Entry(update_window, textvariable=hour_u).pack() #Entry  
    labpeople_u = Label(update_window, text="People").pack() #Label 
    Combobox(update_window,values=options, state= "readonly",textvariable=people_u).pack() #Entry 
    
    # Update button in the top windows 
    Button(update_window, text="Confirm", command=lambda: confirm_update(selected, table_u, date_u, hour_u, people_u)).pack()

def confirm_update(selected, table_u, date_u, hour_u, people_u):
    table_t.item(selected, values=(table_u.get(), date_u.get(), hour_u.get(), people_u.get()))
    update_window.destroy() #Close the window
#---------------------------------------------------------------
table_table = Tk()
table_table.title("Manage table")
table_table.geometry("600x500")
table_table.resizable(width=False, height=False)
table_table.configure(bg="#F0F0F0")
#---------------------------------------------------------------
# Bandera italiana con labels en ventana dish menu (Configuracion y ubicacion) 
greenflag = Label(table_table,bg = "#009C45" ,height = 3 , width = 20)
whiteflag=  Label(table_table,bg = "#FFFFFF", height = 3 , width = 21)
redflag = Label(table_table,bg = "#B31200", height = 3 , width = 20)
greenflag.place( x = 70, y = 100)
whiteflag.place( x = 217, y = 100)
redflag.place( x = 370, y = 100)
#----------------------------------------------------------------
# tittle and subtitles en el dishmenu
menudishtitle = Label(table_table, text = "Italian Restaurant", font = ("Arial", 36 , "bold"), fg = "#B31200")
menudishtitle.place(x = 100 , y = 10)
menudishsubtitle = Label(table_table, text = "Manegeiment Table", font = ("Arial", 20, "bold" ))
menudishsubtitle.place(x = 185, y = 160)
#----------------------------------------------------------------

frame_subtab = Frame(table_table, bg="#FFFFFF", width=600, height=500)
frame_subtab.place(x=140, y= 230)
#---------------------------------------------------------------
#Table
table_t = ttk.Treeview(frame_subtab, columns=("1", "2", "3","4"))

#Columns
table_t.column("#0",width=0, minwidth=0, anchor=CENTER)
table_t.column("1",width=55, minwidth=55, anchor=CENTER)
table_t.column("2",width=105, minwidth=105, anchor=CENTER)
table_t.column("3",width=105, minwidth=105, anchor=CENTER)
table_t.column("4",width=75, minwidth=75, anchor=CENTER)

#Headings 
table_t.heading("#1", text="Table")
table_t.heading("2", text="Date")
table_t.heading("3", text="Hour")
table_t.heading("4", text="People")
#---------------------------------------------------------------
# leemos y escribimos la informacion del archivo json
try:
    with open('Data\Table.json', 'r') as f:
        tables = {record['Table']: record for record in (json.loads(line) for line in f)}
except (FileNotFoundError, json.JSONDecodeError): # Una try para encapsular posibles errores con el json 
    tables = {}

# Añadimos la informacion a la tabla 
for key, record in tables.items():
    if isinstance(record, dict):
        table_t.insert(
            "", 
            'end', 
            values=(record.get('Table'), 
                    record.get('Date'), 
                    record.get('Hour'), 
                    record.get('N.person'))
                    )

#---------------------------------------------------------------
#Pack table
table_t.pack() 

boton_eliminar = Button(table_table,
                        justify= "center",
                        font= ('Arial,',10,"bold"),
                        bg="#B31200",
                        fg ="#FFFFFF",
                        text="Delete", 
                        command= delete_row,
                        width= 7)
boton_eliminar.place(x=510, y=350)

boton_actualizar = Button(table_table,
                        justify= "center",
                        text="Update",
                        bg="#009C45",
                        font=('Arial',10,"bold"),
                        fg ="#FFFFFF",
                        command=update_row,
                        width= 7)
boton_actualizar.place(x=510, y=390) 
#---------------------------------------------------------------
table_table.mainloop()