import tkinter as tk
from tkinter import ttk

# lo que hace el focus es que cuando el campo de texto tiene el texto por defecto, 
# al hacer click se borra y se puede escribir, y si no se escribe nada se vuelve a poner el texto por defecto
# en el caso de la contraseña, al hacer click se borra el texto por defecto y se pone el caracter de contraseña, 
# y si no se escribe nada se vuelve a poner el texto por defecto y se quita el caracter de contraseña para tenerlo nero

#------------- Funciones de focus para campos -------------

def on_email_click(event):
    if email_entry.get() == "Email":
        email_entry.delete(0, "end")

def on_email_focus_out(event):
    if email_entry.get() == "":
        email_entry.insert(0, "Email")

def on_pass_click(event):
    if password_entry.get() == "Contraseña":
        password_entry.delete(0, "end")
        password_entry.config(show="*")

def on_pass_focus_out(event):
    if password_entry.get() == "":
        password_entry.insert(0, "Contraseña")
        password_entry.config(show="")

#------------- Ventana -------------

menu = tk.Tk()
menu.title("Menu Match5")
menu.resizable(False, False)
menu.geometry("1027x570")

# Fondo
fondo = tk.PhotoImage(file="fondo.png")
fondo_label = tk.Label(menu, image=fondo)
fondo_label.place(x=0, y=0, relwidth=1, relheight=1)

# Frame principal
frame = tk.Frame(menu, bg="#497051", bd=2, relief="flat")
frame.place(relx=0.50, rely=0.6, anchor="center", width=350, height=400)

# Título
label = tk.Label(frame, text="Inicie Sesión", bg="#497051", fg="white", font=("DM sans", 15))
label.pack(pady=(30, 10))

#------------- Campo EMAIL con ícono centrado -------------
email_frame = tk.Frame(frame, bg="#497051")
email_frame.pack(pady=15)

email_inner = tk.Frame(email_frame, bg="#497051")
email_inner.pack(anchor="center")

icon_email = tk.PhotoImage(file="icono_email.png").subsample(20, 20)  # achicar imagen
icon_label = tk.Label(email_inner, image=icon_email, bg="#497051")
icon_label.pack(side="left", padx=(0, 8))

email_entry = tk.Entry(email_inner, width=25, font=("Arial", 12), justify="center")
email_entry.insert(0, "Email")
email_entry.pack(side="left", ipady=5)
email_entry.bind("<FocusIn>", on_email_click)
email_entry.bind("<FocusOut>", on_email_focus_out)

#------------- Campo CONTRASEÑA con ícono centrado -------------
pass_frame = tk.Frame(frame, bg="#497051")
pass_frame.pack(pady=5)

pass_inner = tk.Frame(pass_frame, bg="#497051")
pass_inner.pack(anchor="center")

icon_pass = tk.PhotoImage(file="icon_pass.png").subsample(23, 20)
icon_pass_label = tk.Label(pass_inner, image=icon_pass, bg="#497051")
icon_pass_label.pack(side="left",ipadx=0 ,padx=(0, 8))

password_entry = tk.Entry(pass_inner, width=25, font=("Arial", 12), justify="center")
password_entry.insert(0, "Contraseña")
password_entry.pack(side="left", ipady=5)
password_entry.bind("<FocusIn>", on_pass_click)
password_entry.bind("<FocusOut>", on_pass_focus_out)

#------------- Botones -------------
btn1 = tk.Button(frame, text="¿Olvidaste tu contraseña? Toca para recuperarla", bg="#497051", fg="white", font=("DM sans", 10), bd=0, activebackground="#497051", borderwidth=0, highlightthickness=0)
btn1.pack(pady=(30, 2), ipady=0, ipadx=20)

btn2 = tk.Button(frame, text="¿No tiene cuenta? Regístrese", bg="#497051", fg="white", font=("DM sans", 10), bd=0, activebackground="#497051", borderwidth=0, highlightthickness=0)
btn2.pack(pady=(2, 0), ipady=10, ipadx=20)

btn3 = tk.Button(frame, text="Iniciar Sesión", bg="#5b7b62", fg="white", font=("DM sans", 12))
btn3.pack(pady=15, ipady=5, ipadx=20)



#------------- Referencias a imágenes para que no se borren -------------
fondo_label.image = fondo
icon_label.image = icon_email
icon_pass_label.image = icon_pass

menu.mainloop()
