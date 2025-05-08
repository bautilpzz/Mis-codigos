#ti amo bb :3

from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from functools import partial
#---------------------------
def crear_matriz(filas,columnas):
    matriz=[None]*filas
    for i in range(filas):
        matriz[i]=[None]*columnas
    return(matriz)

def crear_tk(matriz):
    if(ent_filas.get() != ''  and ent_columnas.get() != ''):
        filas = int(ent_filas.get())
        columnas = int(ent_columnas.get())
        crear_matriz(filas, columnas)
        messagebox.showinfo(title='Listo',message='Se creo la matriz')

def cargar_matriz(matriz, filas, columnas):
    for f in range (filas):
        for c in range (columnas):
            matriz[f][c] = random.randint(0,9)      
        

#--------------------------
matriz=[]
app = Tk()
app.geometry('700x700')
app.title('Menu matriz')
txt= Text(width= 65, height= 25)

btn_crear =  Button(text='Crear Matriz',command = partial(crear_tk,matriz),width=25)
btn_cargar = Button(text= 'Cargar matriz', command = partial(cargar_matriz),width = 25)
btn_mostrar = Button (text= 'Mostrar matriz', command = partial(mostrar_matriz),width = 25)
btn_ordenar_m_m = (text= 'Ordenar de mayor a menor', command = partial(ordena_matriz),width = 25)
btn_ordenar_c = (text= 'Ordenar matriz por columnas de mayor a menor', command = partial(ordenar_c),width = 25)
btn_ordenar_f = (text= 'Mostrar matriz', command = partial(mostrar_matriz),width = 25)
btn_repetidos = (text= 'Mostrar cuantas veces se repiten los valores en la matriz', command = partial(mostrar_repetidos),width = 25)

'''Crear componentes'''
lbl_filas= Label(text='Ingrese Cantidad de Filas:',  )
lbl_columnas= Label(text='Ingrese Cantidad de Columnas:')

ent_filas= Entry(width=25)
ent_columnas= Entry(width=25)


btn_crear.pack()

lbl_filas.pack()
ent_filas.pack()

lbl_columnas.pack()
ent_columnas.pack()
#---------------------------------

txt.pack()


app.mainloop()
