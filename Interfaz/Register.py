"""
Felipe Ortiz Calan - 2380642
Samuel Valdes Gomez - 2380346
Santiago Velasquez Bedoya  - 2380378

Proyecto final - Fundamentos de programacion Imperativa 
Grupo - 52 
Docente: Luis German Toro
"""

#importamos librerias 
from tkinter import *
from tkinter import messagebox 
import subprocess
import hashlib

#--------------------------------------------------------------------------------------------------------------
# #Configuramos la ventana de registrar ususario 
windowsregister = Tk()
windowsregister.title ("Register")
windowsregister.resizable(width = False, height = False)
windowsregister.geometry("600x500")
windowsregister.configure(bg = "#D6D6D6")
#--------------------------------------------------------------------------------------------------------------
#Funcion para verficar el correo
def verify_email():
    email = register_entry_email.get()
    password = register_entry_password.get()
    conditions = ["gmail.com", "hotmail.com", "outlook.com" "yahoo.com", "live.com",
                  "icloud.com","mail.com", "correunivalle.edu","correounivalle.co" ]
    if "@" not in email or not any(condition in email for condition in conditions):
        messagebox.showerror("Error", "Email is required")
    elif (len(password) != 10 or 
        not any(character.isdigit() for character in password) or
        not any(character.isupper() for character in password) or
        not any(character.islower() for character in password) or
        not any(character in "!\?$@&/"  for character in password)):
        messagebox.showerror("Error", "Password invalid (10 characters, 1 uppercase, 1 lowercase, 1 number, 1 special character))")
    else: 
        with open("Data\Register_inicio.txt", "a") as file:
            file.write(f"{email},{password}\n")
              # Guardamos el email y la contraseña en un archivo de texto
        passwordcrypt = hashlib.sha256(password.encode())   # Encryptamos the password 
        with open("Data\password.txt", "a") as file:       
            file.write(f"{passwordcrypt.hexdigest()}\n")   # Guardamos el email y la contraseña en un archivo de texto
                                                                                          
        messagebox.showinfo("Success", "User registered")
        back_to_login()                                    # Volvemos a la ventana de login 


def back_to_login():     
    windowsregister.destroy()                               # Cerramos la ventana de register y abrimos la de login
    subprocess.call(["python", "Interfaz\Login.py"]) 

#--------------------------------------------------------------------------------------------------------------
# Bandera italiana con labels en ventana de inciciar sesion (Configuracion y ubicacion) 
greenflag = Label(windowsregister, bg="#009C45", height=5, width=20)
whiteflag=  Label(windowsregister, bg="#FFFFFF", height=5, width=21)
redflag = Label(windowsregister,bg="#B31200", height=5 , width=20)
greenflag.place( x=70, y=100)
whiteflag.place( x=217, y=100)
redflag.place( x=370, y=100)
#--------------------------------------------------------------------------------------------------------------
# title  (Configuracion y ubicacion) en ventana de register
register_title = Label(
    windowsregister, 
    text="Italian Restaurant",
    font=("Arial", 40 , "bold"), 
    bg="#D6D6D6", 
    fg="#DE0A0D"
)
register_title.place(x=70, y=20)
#--------------------------------------------------------------------------------------------------------------
register_subtitle = Label(windowsregister, text="Register", font=("Arial", 29 , "bold"), bg="#D6D6D6") 
register_subtitle.place(x=120, y=190)
#--------------------------------------------------------------------------------------------------------------
# labels para email, password, confirm password
register_email_label = Label(
    windowsregister, 
    text="Email: ", 
    font=("arial", 12, "bold"), 
    bg="#D6D6D6" )
register_email_label.place(x=100, y=260)
#--------------------------------------------------------------------------------------------------------------
register_password_label = Label(
    windowsregister, 
    text="Password: ", 
    font=("arial", 12, " bold"),
    bg="#D6D6D6")
register_password_label.place(x=100, y=320)
#--------------------------------------------------------------------------------------------------------------                     
register_confirm_label = Label(
    windowsregister, 
    text="Confirm Password: ", 
    font=("arial", 12, "bold"), 
    bg="#D6D6D6")
register_confirm_label.place(x=100, y=370)
#--------------------------------------------------------------------------------------------------------------
# entrys for email , password , confirm password
register_entry_email = Entry(windowsregister, width=44, font=("arial", 10))
register_entry_email.place(x=170, y=260)

register_entry_password = Entry(windowsregister, width=40, font=("arial", 10), show="•")
register_entry_password.place(x=200, y=320)

register_entry_confirm = Entry(windowsregister, width=30, font=("arial", 10), show="•")
register_entry_confirm.place (x=270, y=370)
#--------------------------------------------------------------------------------------------------------------
# button de registrado y regreso a inciar sesion 
register_button = Button(
    windowsregister,  
    text="Register", 
    font=("arial", 12, "bold"), 
    bg="#3B7CC2",
    fg="#FFFFFF",
    relief="raised",
    command=verify_email) 
register_button.place (x=410, y=410)
#--------------------------------------------------------------------------------------------------------------
windowsregister.mainloop() 