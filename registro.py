import tkinter as tk

#------------------ pp -----------------
registro = tk.Tk()
registro.title("Registrarse Match5")
registro.geometry("1027x570") 
registro.resizable(False, False)

#-------------- fondo --------------
fondo_r = tk.PhotoImage(file="fondo.png") 
fondo_label = tk.Label(registro, image=fondo_r)
fondo_label.place(x=0, y=0, relwidth=1, relheight=1)

#-------------- frame --------------    
frame_r = tk.Frame(registro, bg="#497051")
frame_r.place(relx=0.50, rely=0.6, anchor="center", width=350, height=400)

#-------------- titulo --------------
titulor = tk.Label(frame_r, text="Registrarse", bg="#497051", fg="white", font=("DM sans", 12))
titulor.pack(pady=(10,10))  #el pady es el espacio entre el frame y el texto (para q nos quede de nota)

#-------------- campo mail y contraseña --------------
nombre_entry = tk.Entry(frame_r, width=30, font=("Arial", 12), justify="center")
nombre_entry.pack(pady=(10,5))
nombre_entry.insert(0, "Nombre")

apellido_entry = tk.Entry(frame_r, width=30, font=("Arial", 12), justify="center")
apellido_entry.pack(pady=(10,5))
apellido_entry.insert(0, "Apellido")

#-------------- DNI --------------
dni_entry = tk.Entry(frame_r, width=30, font=("Arial", 12), justify="center")
dni_entry.pack(pady=(10,5))
dni_entry.insert(0, "DNI")

#-------------- fecha de nacimiento --------------
f_d_N_entry = tk.Entry(frame_r, width=30, font=("Arial", 12), justify="center")
f_d_N_entry.pack(pady=(10,5))
f_d_N_entry.insert(0, "Fecha de Nacimiento")

#-------------- img --------------


btn = tk.Button(frame_r, text="⮕", width=10, height=1, font=("Arial", 12), justify="center", bd=0)
btn.pack(pady=(50,5))  # Ensure the button is packed
btn1 = tk.Button(frame_r, text="¿Tiene cuenta? Inicie Sesion", bg="#497051", fg="white", font=("DM sans", 10), bd=0, activebackground="#497051", borderwidth=0, highlightthickness=0)
btn1.pack(pady=(10, 5))

#-------------- fondo label image ----------------
fondo_label.image = fondo_r  # Keep a reference to the image

# Function to clear placeholder text on click
def on_click(event, entry_field, placeholder, show_password=False):
    if entry_field.get() == placeholder:
        entry_field.delete(0, "end")
        if show_password:
            entry_field.config(show="*")

# Function to restore placeholder text on focus out if no input was provided
def on_focus_out(event, entry_field, placeholder, show_password=False):
    if entry_field.get() == "":
        entry_field.insert(0, placeholder)
        if show_password:
            entry_field.config(show="")

# Bind events to the entry fields
nombre_entry.bind("<FocusIn>", lambda event: on_click(event, nombre_entry, "Nombre"))
nombre_entry.bind("<FocusOut>", lambda event: on_focus_out(event, nombre_entry, "Nombre"))

apellido_entry.bind("<FocusIn>", lambda event: on_click(event, apellido_entry, "Apellido"))
apellido_entry.bind("<FocusOut>", lambda event: on_focus_out(event, apellido_entry, "Apellido"))

dni_entry.bind("<FocusIn>", lambda event: on_click(event, dni_entry, "DNI"))
dni_entry.bind("<FocusOut>", lambda event: on_focus_out(event, dni_entry, "DNI"))

f_d_N_entry.bind("<FocusIn>", lambda event: on_click(event, f_d_N_entry, "Fecha de Nacimiento"))
f_d_N_entry.bind("<FocusOut>", lambda event: on_focus_out(event, f_d_N_entry, "Fecha de Nacimiento"))

# Start the main loop
registro.mainloop()
