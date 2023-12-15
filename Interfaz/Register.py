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
windowsregister.configure(bg = "#FFFFFF")
#--------------------------------------------------------------------------------------------------------------
#Funcion para verficar el correo
def verify_email():
    email = registerentryemail.get()
    password = registerentrypassword.get()
    conditions = ["gmail.com", "hotmail.com", "outlook.com" "yahoo.com", "live.com",
                  "icloud.com","mail.com", "correunivalle.edu","correounivalle.co" ]
    if "@" not in email or not any(condition in email for condition in conditions):
        messagebox.showerror("Error", "Email is required")
    elif (len(password) != 10 or 
        not any(character.isdigit() for character in password) or
        not any(character.isupper() for character in password) or
        not any(character.islower() for character in password) or
        not any(character in "!\?$@&/"  for character in password)):
        messagebox.showerror("Error", "Password invalid")
    else: 
        with open("register_inicio.txt", "a") as file:
            file.write(f"{email},{password}\n")
              # Guardamos el email y la contraseña en un archivo de texto
        passwordcrypt = hashlib.sha256(password.encode())   # Encryptamos the password 
        with open("password.txt", "a") as file:       
            file.write(f"{passwordcrypt.hexdigest()}\n")   # Guardamos el email y la contraseña en un archivo de texto
                                                                                          
        messagebox.showinfo("Success", "User registered") 
        windowsregister.destroy()                               # Cerramos la ventana de register y abrimos la de login
        subprocess.call(["python", "Login.py"]) 

#--------------------------------------------------------------------------------------------------------------
# Bandera italiana con labels en ventana de inciciar sesion (Configuracion y ubicacion) 
greenflag = Label(windowsregister,bg = "#009C45" ,height = 5 , width = 20)
whiteflag=  Label(windowsregister,bg = "#FFFFFF", height = 5 , width = 21)
redflag = Label(windowsregister,bg = "#B31200", height = 5 , width = 20)
greenflag.place( x = 70, y = 100)
whiteflag.place( x = 217, y = 100)
redflag.place( x = 370, y = 100)
#--------------------------------------------------------------------------------------------------------------
# title  (Configuracion y ubicacion) en ventana de register
registertitle = Label(windowsregister, 
                      text = "Italian Restaurant",
                      font = ("Arial", 40 , "bold"), 
                      bg = "#AAAAAA", fg = "red",
                      relief = "raised")
registertitle.place(x = 70 , y = 20)
#--------------------------------------------------------------------------------------------------------------
registersubtitle = Label(windowsregister,text = "Register", font = ("Arial", 29 , "bold"), bg ="#FFFFFF") 
registersubtitle.place(x = 120, y = 190)
#--------------------------------------------------------------------------------------------------------------
# labels para email, password, confirm password
registeremailabel = Label(windowsregister, 
                          text = "Email: ", 
                          font = ("arial", 12, "bold"), 
                          bg ="#FFFFFF" )
registeremailabel.place(x = 100, y = 260)
#--------------------------------------------------------------------------------------------------------------
registerpasswordlabel = Label(windowsregister, 
                              text = "Password: ", 
                              font = ("arial", 12, " bold"),
                              bg = "#FFFFFF")
registerpasswordlabel.place(x = 100, y = 320)
#--------------------------------------------------------------------------------------------------------------                     
registerconfirmlabel = Label(windowsregister, 
                             text = "Confirm Password: ", 
                             font = ("arial", 12, "bold"), 
                             bg = "#FFFFFF")
registerconfirmlabel.place(x = 100, y = 370)
#--------------------------------------------------------------------------------------------------------------
# entrys for email , password , confirm password
registerentryemail = Entry(windowsregister, width = 44, font = ("arial", 10))
registerentryemail.place(x = 170, y = 260)

registerentrypassword = Entry(windowsregister, width = 40, font = ("arial", 10),show="•")
registerentrypassword.place(x = 200, y = 320)

registerentryconfirm = Entry(windowsregister, width = 30, font = ("arial", 10), show="•")
registerentryconfirm.place (x = 270, y = 370)
#--------------------------------------------------------------------------------------------------------------
# button de registrado y regreso a inciar sesion 
registerbutton = Button(windowsregister,  
                        text = "Register", 
                        font = ("arial", 12),  
                        relief = "raised",
                        command= verify_email) 
registerbutton.place (x = 410, y = 410 )
#--------------------------------------------------------------------------------------------------------------
windowsregister.mainloop() 