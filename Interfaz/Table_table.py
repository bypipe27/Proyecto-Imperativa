from tkinter import *
from tkinter import ttk 
import subprocess 
import json
from tkinter import messagebox 
#---------------------------------------------------------------
def delete_row():
    selected = coltab.selection()
    if not selected:
        messagebox.showerror("Error", "No row selected.")
        return

    # Guardamos el nombre de la mesa seleccionada para eliminarla del JSON 
    table_name = int(coltab.item(selected)['values'][0])  # Convert to int for later comparison

    # Eliminamos la fila de la tabla 
    coltab.delete(selected)

    # Delete the row from the JSON file
    with open('Data\Table.json', 'r') as f:
        tables = [json.loads(line) for line in f] # Cargo la informacion del arhivo recorriendo linea por linea 
    tables = [table for table in tables if int(table['Table']) != table_name]  # Hacemos el cambio 
    with open('Data\Table.json', 'w') as f: # Escribimos la informacion para la linea 
        for table in tables:
            f.write(json.dumps(table) + '\n') # Sobre escribimos la informacion en el archivo 
#----------------------------------------------------------------------------- 
# Funcion para actualizar una fila de la tabla 
def update_row():
    selected = coltab.selection() #Selected row
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
    labtable_u = Label(update_window, text="Table").pack() #Label 
    Entry(update_window, textvariable=table_u).pack() #Entry 
    labdate_u = Label(update_window, text="Date").pack() #Label
    Entry(update_window, textvariable=date_u).pack() #Entry 
    labhour_u = Label(update_window, text="Hour").pack() #Label
    Entry(update_window, textvariable=hour_u).pack() #Entry  
    labpeople_u = Label(update_window, text="People").pack() #Label 
    Entry(update_window, textvariable=people_u).pack() #Entry 
    
    # Update button in the top windows 
    Button(update_window, text="Confirm", command=lambda: confirm_update(selected, table_u, date_u, hour_u, people_u)).pack()

def confirm_update(selected, table_u, date_u, hour_u, people_u):
    coltab.item(selected, values=(table_u.get(), date_u.get(), hour_u.get(), people_u.get()))
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
#Table
coltab = ttk.Treeview(frame_subtab, columns=("1", "2", "3","4"))

#Columns
coltab.column("#0",width=0, minwidth=0, anchor=CENTER)
coltab.column("1",width=55, minwidth=55, anchor=CENTER)
coltab.column("2",width=105, minwidth=105, anchor=CENTER)
coltab.column("3",width=105, minwidth=105, anchor=CENTER)
coltab.column("4",width=75, minwidth=75, anchor=CENTER)

#Headings 
coltab.heading("#1", text="Table")
coltab.heading("2", text="Date")
coltab.heading("3", text="Hour")
coltab.heading("4", text="People")

#Pack table
coltab.pack() 

boton_eliminar = Button(table_table,justify= "center",font= ('Arial,',10,"bold"),bg="#B31200",fg ="#FFFFFF" , text="Delete", command=delete_row , width= 7)
boton_eliminar.place(x=510, y=350)

boton_actualizar = Button(table_table,justify= "center", text="Update",bg="#009C45",font=('Arial',10,"bold"),fg ="#FFFFFF", command=update_row, width= 7)
boton_actualizar.place(x=510, y=390) 

table_table.mainloop()