from tkinter import *
from tkinter import messagebox
from Modulos_Proyecto4 import *
# #B4E6E0 cian
# #C091E4 violet

registros = Read()

root = Tk()
root.title('Login')
root.geometry('925x500+300+200')
root.configure(bg="#FFFFFF")
root.resizable(False, False)

# def signin():
#     username=user.get()
#     password1=password.get()
#     
#     if username=='admin' and password1=='1234':
#         screen=Toplevel(root)
#         screen.title("App")
#         screen.geometry('925x500+300+200')
#         screen.config(bg="white")
#         Label(screen, text="Hello Everyone",bg='#FFFFFF',font=('Calibri(Body)',50,'bold')).pack(expand=True)
#         screen.mainloop()
#     elif username != 'admin' and password1 != '1234':
#         messagebox.showerror("Error","Invalid username or password")
#     elif password1 != '1234':
#         messagebox.showerror("Error","Invalid password")
#     elif username != 'admin':
#         messagebox.showerror("Error","Invalid username")
        
def SignIn():
    UserCreated = str(user.get())
    PasswordCreated = str(password.get())
    Exist = False
    for i in range(1,len(registros)):
        if (registros[i][0] == UserCreated and registros[i][1] == PasswordCreated):
            Exist = True
            screen=Toplevel(root)
            screen.title("App")
            screen.geometry('925x500+300+200')
            screen.config(bg="white")
            Label(screen, text="It works :3",bg='#FFFFFF',font=('Calibri(Body)',50,'bold')).pack(expand=True)
            screen.mainloop()
    if Exist == False:
        messagebox.showinfo(title = "Error", message = "Incorrect username or Password")

        
img = PhotoImage(file='login2.png')
Label(root, image=img, bg='white').place(x=40,y=60)

frame = Frame(root,width=350,height=350, bg='white')
frame.place(x=480,y=70)

heading = Label(frame,text='Sign in', fg='#BD81EB', bg='white', font=('Roboto',23,'bold'))
heading.place(x=100,y=5)

# Username__________________________________________________________________________________________________
def on_enter(e):
    user.delete(0, 'end')
    
def on_leave(e):
    name=user.get()
    if name=='':
        user.insert(0,'Username')
    
user = Entry(frame, width=25, fg='black', border=0, bg='white', font=('Roboto',11))
user.place(x=30,y=80)
user.insert(0,'Username')
user.bind('<FocusIn>', on_enter)
user.bind('<FocusOut>', on_leave)

Frame(frame, width=295, height=2, bg='black').place(x=25, y=107)

# Password__________________________________________________________________________________________________
def on_enter(e):
    password.delete(0, 'end')
    
def on_leave(e):
    name=password.get()
    if name=='':
        password.insert(0,'Password')

password = Entry(frame, width=25, fg='black', border=0, bg='white', font=('Roboto',11))
password.place(x=30,y=150)
password.insert(0,'Password')
password.bind('<FocusIn>', on_enter)
password.bind('<FocusOut>', on_leave)

Frame(frame, width=295, height=2, bg='black').place(x=25, y=177)

# Button S__________________________________________________________________________________________________
Button(frame,width=39,pady=7,text='Sign in', bg='#BD81EB', fg='white', border=0, command= SignIn).place(x=35, y=204)
label=Label(frame,text='¿No se ha registrado?', fg='black', bg='white', font=('Roboto',9))
label.place(x=75,y=270)

sign_up = Button(frame, width=6, text='Sign up', border=0, bg='white', cursor='hand2', fg='#B4E6E0')
sign_up.place(x=215,y=270)

root.mainloop()