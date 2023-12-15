"""
Felipe Ortiz Calan - 2380642
Samuel Valdes Gomez - 2380346
Santiago Velasquez Bedoya  - 2380378

Proyecto final - Fundamentos de programacion Imperativa 
Grupo - 52 
Docente: Luis German Toro
"""
#---------------------------------------------------------------
#Importamos librerias 
from tkinter import *
from tkinter import messagebox 
import subprocess
import hashlib
#---------------------------------------------------------------
# Creamos y configuramos ventana para iniciar sesion 
windowslogin = Tk()
windowslogin.title("Login")
windowslogin.resizable(width= False, height = False)
windowslogin.geometry("600x500")
windowslogin.configure(bg= "#D6D6D6")
#---------------------------------------------------------------
# Funcion para verificar el correo y la contraseña 
def verify_email_login():
    email2 = loginentryuser.get()
    password2 = loginentrypassword.get() 
    passwordcrypt = hashlib.sha256(password2.encode()).hexdigest()
    if email2 == "" or password2 == "":
        messagebox.showerror("Error", "Email and password is required")
        return 
    with open('Data\password.txt', 'r') as f: 
        if passwordcrypt not in f.read():
            messagebox.showinfo("Error", "User not registereeed")
            return 
    with open('Data\Register_inicio.txt', 'r') as f:
                for line in f:
                    email1, password1 = line.strip().split(',')
                    if email1 == email2 and password1 == password2:
                        messagebox.showinfo("Success", "User logged in")
                        open_menu() 
                messagebox.showerror("Error", "Email and passssword incorrect")

#--------------------------------------------------------------- 
# funcion que va al menu 
def open_menu():
    windowslogin.destroy()
    subprocess.call(["python", "Interfaz/menu.py"]) 

# funcion para ir al registro                
def register():
    windowslogin.destroy()
    subprocess.call(["python", "Interfaz\Register.py"])                 
#----------------------------------------------------------------
# Bandera italiana con labels en ventana de inciciar sesion (Configuracion y ubicacion) 
greenflag = Label(windowslogin, bg="#009C45", height=5, width=20)
whiteflag=  Label(windowslogin, bg="#FFFFFF", height=5, width=21)
redflag = Label(windowslogin, bg="#B31200", height=5, width=20)
greenflag.place( x=70, y=100)
whiteflag.place( x=217, y=100)
redflag.place( x=370, y=100)
#----------------------------------------------------------------
# title  (Configuracion y ubicacion) en ventana de login 
logintitle = Label(windowslogin, 
    text= "Italian Restaurant", 
    font= ("Arial", 40, "bold"), 
    bg= "#D6D6D6", 
    fg= "#DE0A0D"
)
logintitle.place(x=70, y=20)
#----------------------------------------------------------------
loginsubtitle = Label(windowslogin,
    text= "Login", 
    font= ("Arial", 29, "bold"), 
    bg= "#D6D6D6"
) 
loginsubtitle.place(x=160, y=190)
#----------------------------------------------------------------
#configuramos las etiquetas para el login 
loginlabelemail = Label(windowslogin, 
    text= "Email: ", 
    font= ("Arial", 20, "bold"), 
    bg= "#D6D6D6")
loginlabelemail.place(x=40, y=245)
#----------------------------------------------------------------
loginlabelpassword = Label(windowslogin,  
    text= "Password: ", 
    font= ("Arial", 20, "bold"), 
    bg= "#D6D6D6")
loginlabelpassword.place(x=40, y=305)
#----------------------------------------------------------------
# Configuramos entrada de password y email en el login 
loginentryuser = Entry(windowslogin, width= 26, font= ("arial",16 ))
loginentryuser.place(x=200, y=250)
loginentrypassword = Entry(windowslogin, width=26,  font=("arial",16), show="•")
loginentrypassword.place(x=200, y=310)
#----------------------------------------------------------------
#Label del  registro
loginlabelregister = Label(windowslogin, 
    text= "¿You don't have an account?", 
    font= ("Arial", 12), 
    bg= "#D6D6D6")
loginlabelregister.place(x=55, y=415) 
#----------------------------------------------------------------
# Configure button de register en el login y ubicamos
buttonregister = Button(windowslogin, 
    width=10, 
    text= "Sign up",  
    font= ("arial", 14),
    fg= "#FFFFFF",
    bg= "#3B7CC2", 
    relief= "raised", 
    command= register)
buttonregister.place(x=280, y=410)
#----------------------------------------------------------------
# Configure button de login en el login y ubicamos 
buttonloginsession = Button(windowslogin, 
    width= 10, 
    text= "Login",  
    font= ("arial", 14),
    fg= "#FFFFFF",
    bg= "#29A873", 
    relief= "raised", 
    command= verify_email_login)
buttonloginsession.place(x=280, y=360)
#----------------------------------------------------------------
# mainloop
windowslogin.mainloop()