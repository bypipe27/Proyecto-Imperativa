from tkinter import ttk
from tkinter import * 

prueba = Tk()

data = 'Data\Dish.json'
# Crear la tabla
table = ttk.Treeview(prueba, columns=list(data[0].keys()), show='headings')

# Agregar los encabezados de las columnas
for column in data[0].keys():
    table.heading(column, text=column)

# Agregar los datos a la tabla
for item in data:
    table.insert('', 'end', values=list(item.values()))

# Mostrar la tabla
table.pack()

prueba.mainloop() 