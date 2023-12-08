
#Importamos librerias 
from tkinter import *
from tkinter import messagebox 
import subprocess
import hashlib

# Creamos y configuramos ventana para iniciar sesion 
windowslogin = Tk()
windowslogin.title("Login")
windowslogin.resizable(width = False, height = False)
windowslogin.geometry("600x500")
windowslogin.configure(bg = "white")

#---------------------------------------------------------------
# Funcion para verificar el correo y la contraseña 

def verify_email_login():
    email2 = loginentryuser.get()
    password2 = loginentrypassword.get() 
    passwordcrypt = hashlib.sha256(password2.encode()).hexdigest()
    if email2 == "" or password2 == "":
        messagebox.showerror("Error", "Email and password is required")
        return 
    with open('password.txt', 'r') as f: 
        if passwordcrypt not in f.read():
            messagebox.showinfo("Error", "User not registereeed")
            return 
    with open('register_inicio.txt', 'r') as f:
                for line in f:
                    email1, password1 = line.strip().split(',')
                    if email1 == email2 and password1 == password2:
                        messagebox.showinfo("Success", "User logged in")
                        windowslogin.destroy()
                        subprocess.call(["python", "menu.py"])
                        return 
                messagebox.showerror("Error", "Email and passssword incorrect")
        
                

       
#----------------------------------------------------------------
# Bandera italiana con labels en ventana de inciciar sesion (Configuracion y ubicacion) 
redflag = Label(windowslogin,bg = "green" ,height = 5 , width = 20)
whiteflag=  Label(windowslogin,bg = "white", height = 5 , width = 21)
greenflag = Label(windowslogin,bg = "red", height = 5 , width = 20)

redflag.place( x = 70, y = 100)
whiteflag.place( x = 217, y = 100)
greenflag.place( x = 370, y = 100)
#----------------------------------------------------------------
# title  (Configuracion y ubicacion) en ventana de login 
logintitle = Label(windowslogin, text = "Italian Restaurant", font = ("Arial", 40 , "bold"), bg = "Silver", fg = "red", relief = "raised")
logintitle.place(x = 70 , y = 20)
loginsubtitle = Label(windowslogin,text = "Login", font = ("Arial", 29 , "bold"), bg = "white") 
loginsubtitle.place(x = 160, y = 190)
#----------------------------------------------------------------
#configuramos las etiquetas para el login 
loginlabelemail = Label(windowslogin, text = "Email: ", font = ("Arial", 20 , "bold"), bg = "white")
loginlabelemail.place(x = 40 , y = 245)
loginlabelpassword = Label(windowslogin,  text = "Password: ", font = ("Arial", 20 , "bold"), bg = "white")
loginlabelpassword.place(x = 40 , y = 305)
#----------------------------------------------------------------
# Configuramos entrada de password y email en el login 
loginentryuser = Entry(windowslogin, width = 26, font = ("arial", 16 ))
loginentryuser.place(x = 200 , y = 250)
loginentrypassword = Entry(windowslogin, width = 26,  font = ("arial", 16))
loginentrypassword.place(x = 200, y = 310)
#----------------------------------------------------------------
# Configure button de login en el login y ubicamos 
buttonloginsession = Button(windowslogin, width = 20, text = "Iniciar sesión",  font = ("arial", 14),fg = "white",bg = "black", relief = "solid", command= verify_email_login)
buttonloginsession.place(x = 280, y = 360)

windowslogin.mainloop()