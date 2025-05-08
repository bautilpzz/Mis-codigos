import tkinter as tk

# Variables para guardar el último rectángulo y su centro
last_color_item = None
last_start_x = None

# Función de animación para agrandar horizontalmente desde una posición inicial
def animate_zoom_horizontal(color_item, start_x, final_left, final_right):
    current_coords = canvas.bbox(color_item)
    left = current_coords[0]
    right = current_coords[2]

    if left > final_left:
        left = max(left - 9, final_left)
    if right < final_right:
        right = min(right + 9, final_right)

    canvas.coords(color_item, left, 0, right, 568)

    if left > final_left or right < final_right:
        canvas.after(30, animate_zoom_horizontal, color_item, start_x, final_left, final_right)
    else:
        boton_reverso.place(x=1080, y=282, width=30, height=30)

def animate_zoom_inverse(color_item, target_x):
    current_coords = canvas.bbox(color_item)
    left = current_coords[0]
    right = current_coords[2]

    if left < target_x:
        left = min(left + 9, target_x)
    if right > target_x:
        right = max(right - 9, target_x)

    canvas.coords(color_item, left, 0, right, 568)

    if left < target_x or right > target_x:
        canvas.after(30, animate_zoom_inverse, color_item, target_x)
    else:
        canvas.delete(color_item)
        boton_reverso.place_forget()
        canvas.delete("jugador_img")  # Ocultar imagen cuando se revierte

def section_click(event, section_name, color, start_x):
    global last_color_item, last_start_x

    print(f"Has seleccionado: {section_name}")
    
    if section_name == "Jugador":
        canvas.create_image(0, 0, anchor="nw", image=jugador_img, tags="jugador_img")
        mask_rect = canvas.create_rectangle(start_x, 0, start_x + 1, 568, outline="", fill="", tags="mask")
        last_color_item = mask_rect
        last_start_x = start_x
        animate_zoom_horizontal(mask_rect, start_x, 0, 1115)
    else:
        color_item = canvas.create_rectangle(start_x, 0, start_x + 1, 568, outline="", fill=color, tags=section_name)
        last_color_item = color_item
        last_start_x = start_x
        animate_zoom_horizontal(color_item, start_x, 0, 1115)

def reverse_animation():
    if last_color_item and last_start_x is not None:
        animate_zoom_inverse(last_color_item, last_start_x)

#------------------------------- pp

eleccion = tk.Tk()
eleccion.title("Elección Match5")
eleccion.resizable(False, False)
eleccion.geometry("1115x568")

fondo_e = tk.PhotoImage(file="Elec.png")
jugador_img = tk.PhotoImage(file="Jugador_eee.png")  # 🔄 Imagen actualizada

canvas = tk.Canvas(eleccion, width=1115, height=568)
canvas.pack()
canvas.create_image(0, 0, anchor="nw", image=fondo_e)

canvas.create_rectangle(0, 0, 300, 568, outline="", fill="", tags="section1")
canvas.create_rectangle(300, 0, 600, 568, outline="", fill="", tags="section2")
canvas.create_rectangle(600, 0, 900, 568, outline="", fill="", tags="section3")
canvas.create_rectangle(900, 0, 1115, 568, outline="", fill="", tags="section4")

canvas.tag_bind("section1", "<Button-1>", lambda event: section_click(event, "Jugador", "#FF6347", 150))
canvas.tag_bind("section2", "<Button-1>", lambda event: section_click(event, "Equipo", "#FFD700", 450))
canvas.tag_bind("section3", "<Button-1>", lambda event: section_click(event, "Estadio", "#32CD32", 750))
canvas.tag_bind("section4", "<Button-1>", lambda event: section_click(event, "Árbitro", "#1E90FF", 1007))

boton_reverso = tk.Button(eleccion, text="←", command=reverse_animation, font=("Arial", 10), bg="#cccccc")

eleccion.mainloop()
