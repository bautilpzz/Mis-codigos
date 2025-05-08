import random
from tkinter import ttk
from tkinter import messagebox
from tkinter import *
import time
from functools import partial
from tkinter import PhotoImage
#--------------------------------------------------[\n' +]

def crea_matriz():
    mat=[None]*8
    for f in range(8):
        mat[f]=[None]*8
    return(mat)

def carga_matriz(mat):
    for f in range(8):
        for c in range (8):
            mat[f][c]=random.randint(0,7)
    muestra_mat(mat)

def muestra_mat(mat):
    for f in range(8):
        for c in range(8):
            print(mat[f][c], end='  ')
        print()



"""
def crea_mat_label(mat_lbl):
    for i in range(4):
        v_aux=[None]*8
        mat_lbl.append(v_aux)

def carga_imagen (mat_lbl):
    vec_img.append(PhotoImage(file='tesoro.png'))



def teclas(event):
    print(event.keysym)
    if(event.keysym == '1'):
        btn_click(0, v_btn,v_col,jugadas)
    elif(event.keysym == '2'):
        btn_click(1, v_btn,v_col,jugadas)
    elif(event.keysym == '3'):
        btn_click(2, v_btn,v_col,jugadas)
    elif(event.keysym == '4'):
        btn_click(3, v_btn,v_col,jugadas)
    elif(event.keysym == 'Return'):
        verifica(v_btn,v_col,jugadas)
    elif(event.keysym == 'space'):
        comenzar(v_btn,v_col,jugadas)
    elif(event.keysym == 's'):
        crea(v_btn,v_col,v_col2)

"""
#programa principal
ventana = Tk()
ventana.geometry('700x700')
ventana.title('busqueda del tesoro')


mat = crea_matriz()
carga_matriz(mat)
muestra_mat(mat)
vec_image=[]

inicio_btn = Button(text='INICIAR')
inicio_btn.place(width=150, heigh=70, x=280,y=600)

historia_label = Label(text='habia una vez un muchacho llamdo Lionel Andres Messi en busqueda de un tesoro llamado LA COPA DEL MUNDO, ayuda a Messi a conseguirlo y salir campeon ')
historia_label.place(width=700, heigh=40, x=0,y=0)
    
