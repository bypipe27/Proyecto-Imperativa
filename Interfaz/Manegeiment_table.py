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
from datetime import datetime 
from tkinter.ttk import Combobox 
#---------------------------------------------------------------


def review_table():
    wmanege_table.destroy()
    subprocess.call(["python", "Interfaz\Table_table.py"])

#Function add dish
def add_dish_to_table():
    validate = True 
    table = combo_table_table.get().strip()
    date = entry_table_date.get().strip()
    hour = entry_table_hour.get().strip()
    number = combo_table_npersons.get().strip()

    # Check if any field is empty
    if not date or not hour :
        messagebox.showerror("Error", "No blank spaces allowed.")
        validate = False
    if not table or not number :
        messagebox.showerror("Error", "selected a option.")
        validate = False
    if len(date) != 10:  # If the date is not complete, show an error
            messagebox.showerror("Error", "Invalid date. Please enter the date in the format 'YYYY-MM-DD'")
            entry_table_date.delete(0, 'end')
            validate = False 
    if len(date) == 10:  # Only validate if the date is complete
        try:
            entrytime = datetime.strptime(date, '%Y/%m/%d')
            timenow = datetime.now() 
            if entrytime.date() < timenow.date():
                messagebox.showerror("Error", "La fecha no puede ser anterior a la fecha actual.")
                entry_table_date.delete(0, 'end')
                validate = False 
        except ValueError:
            messagebox.showerror("Error", "Fecha inválida. Por favor, introduzca la fecha en el formato 'YYYY-MM-DD'")
            entry_table_date.delete(0, 'end')
            validate = False              
    if len(hour) != 5:  # Only validate if the hour is complete
        try:
            datetime.strptime(hour, '%H:%M')
        except ValueError:
            messagebox.showerror("Error", "Invalid time. Please enter the time in the format 'HH:MM'")
            entry_table_hour.delete(0, 'end')
            validate = False 
    if len(hour) >= 3 and ":" not in hour:  # If ":" is not in the input and the input has at least 3 characters, show an error
        messagebox.showerror("Error", "Invalid time. Please enter the time in the format 'HH:MM'")
        entry_table_hour.delete(0, 'end')
        validate = False       
    elif validate == True:                                                                  #Save table data to a JSON file
        with open('Data\Table.json', 'a') as f:
            table_data = {'Table': table, 'Date': date, 'Hour': hour, 'N.person': number}
            json.dump(table_data, f)
            f.write('\n')
        messagebox.showinfo("Success", "Data saved successfully")
        review_table()                                                                 # Show a success message
        
#---------------------------------------------------------------
# Create window and configure it 
wmanege_table = Tk() 
wmanege_table.title("Italian Restaurant")
wmanege_table.resizable(width=False, height=False)
wmanege_table.geometry("600x500")
wmanege_table.configure(bg="#D6D6D6")
#---------------------------------------------------------------
# Bandera italiana con labels (Configuracion y ubicacion)
greenflag = Label(wmanege_table,bg="#009C45" , height=5,width=20)
whiteflag=  Label(wmanege_table,bg="#FFFFFF", height=5,width=21)
redflag = Label(wmanege_table,bg="#B31200", height=5,width=20)
greenflag.place(x=70, y=100)
whiteflag.place(x=217, y=100)
redflag.place(x=370, y=100)
#---------------------------------------------------------------
# title and text description (Configuracion y ubicacion)
manegement_title = Label(wmanege_table, 
                         text="Italian Restaurant", 
                         font=("Arial", 40 , "bold"), 
                         bg="#D6D6D6", 
                         fg="#B31200", 
)
manegement_title.place(x=70, y=20) 
#---------------------------------------------------------------
# label and entry of number the table (Configuracion y ubicacion)
table_table_label = Label(wmanege_table, 
                          text="# Table", 
                          font=("Arial", 14, "bold"), 
                          bg="#D6D6D6")
table_table_label.place(x=70, y=200)
#Definimos las options 
options = [" ","1","2","3","4","5","6","7","8","9","10"] 
# Entry name 
combo_table_table = Combobox(wmanege_table, values= options, state= "readonly" )
combo_table_table.current(0) 
combo_table_table.place(x=70, y=230)
#---------------------------------------------------------------
# label and entry date table (Configuracion y ubicacion) 
date_table_label = Label(wmanege_table, 
                         text="Date", 
                         font=("Arial", 14, "bold"), 
                         bg="#D6D6D6",
)
date_table_label.place(x=70, y=280)
# entry date 
entry_table_date = Entry(wmanege_table, width=24)
entry_table_date.place(x=70, y=310)
#---------------------------------------------------------------
# label and entry hour table (Configuracion y ubicacion)
hour_table_label = Label(
    wmanege_table, 
    text="Hour",
    font=("Arial", 14, "bold"), 
    bg="#D6D6D6",
)
hour_table_label.place(x=300, y=200)
# entry hour
entry_table_hour = Entry(wmanege_table, width=24)
entry_table_hour.place(x=300, y=230)
#---------------------------------------------------------------
# label and entry anumber of diners (Configuracion y ubicacion) 
number_table_label = Label(
    wmanege_table, 
    text="# Diners ", 
    font=("Arial", 14, "bold"), 
    bg="#D6D6D6"
)    
number_table_label.place(x=300, y=280)
#Definimos las options 
options = [" ","1","2","3","4","5","6","7","8","9","10"] 
# Entry name 
combo_table_npersons = Combobox(wmanege_table, values= options , state= "readonly" )
combo_table_npersons.current(0) 
combo_table_npersons.place(x=300, y=310)
#---------------------------------------------------------------
# button add table (Configuracion y ubicacion)
add_dish = Button(
    wmanege_table, 
    text="Add Table", 
    font=("arial", 12, "bold"), 
    bg="#29A873", 
    fg="#FFFFFF", 
    command=add_dish_to_table)
add_dish.place(x=240, y=400)
#---------------------------------------------------------------
wmanege_table.mainloop()