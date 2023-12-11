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

    # Save the name of the table before deleting the row
    table_name = int(coltab.item(selected)['values'][0])  # Convert to int for later comparison

    # Delete the row from the table
    coltab.delete(selected)

    # Delete the row from the JSON file
    with open('Data\Dishes.json', 'r') as f:
        tables = [json.loads(line) for line in f] # Load the data from the file line by line
    tables = [table for table in tables if int(table['Table']) != table_name]  # Convert to int before comparing
    with open('Data\Dishes.json', 'w') as f: #Write the information in the file
        for table in tables:
            f.write(json.dumps(table) + '\n') #Write information with leap line


def update_row():
    selected = coltab.selection() #Selected row
    if not selected:
        messagebox.showerror("Error", "No row selected.")
        return

    # Create a new window
    update_window = Toplevel() #New window
    update_window.title("Update Row")

    # Create entry fields for each column
    table_var = StringVar()
    date_var = StringVar()
    hour_var = StringVar()
    people_var = StringVar()
    Entry(update_window, textvariable=table_var).pack()
    Entry(update_window, textvariable=date_var).pack()
    Entry(update_window, textvariable=hour_var).pack()
    Entry(update_window, textvariable=people_var).pack()

    # Update button in the new window
    Button(update_window, text="Confirm", command=lambda: confirm_update(selected, table_var, date_var, hour_var, people_var)).pack()

def confirm_update(selected, table_var, date_var, hour_var, people_var):
    coltab.item(selected, values=(table_var.get(), date_var.get(), hour_var.get(), people_var.get()))
#---------------------------------------------------------------
table_mane_dish = Tk()
table_mane_dish.title("Managementc Dish")
table_mane_dish.geometry("600x500")
table_mane_dish.resizable(width=False, height=False)
table_mane_dish.configure(bg="white")



frame_subtab = Frame(table_mane_dish, bg="white", width=600, height=500)
frame_subtab.place(x=0, y=0)
#Table
coltab = ttk.Treeview(frame_subtab, columns=("1", "2", "3","4"))

#Columns
coltab.column("#0",width=0, minwidth=0, anchor=CENTER)
coltab.column("1",width=50, minwidth=50, anchor=CENTER)
coltab.column("2",width=100, minwidth=100, anchor=CENTER)
coltab.column("3",width=100, minwidth=100, anchor=CENTER)
coltab.column("4",width=70, minwidth=70, anchor=CENTER)

# coltab.heading("#0",text="Table")
coltab.heading("#1", text="Table")
coltab.heading("2", text="Date")
coltab.heading("3", text=" # Hour")
coltab.heading("4", text=" # People")

#Pack table
coltab.pack()

boton_eliminar = Button(table_mane_dish, text="Delete", command=delete_row)
boton_eliminar.place(x=500, y=100)

boton_actualizar = Button(table_mane_dish, text="Update", command=update_row)
boton_actualizar.place(x=500, y=150) 





table_mane_dish.mainloop()