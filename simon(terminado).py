from distutils import command
from email import message
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import font
from functools import partial
import time 
import random
from turtle import width
#-----------------[ventana]------------------------------------
ventana=Tk()
ventana.geometry("400x400")
ventana.title("simon")
#---------------------[funciones]----------------------------
def click (i,jugada,colores):
    print(i)
    jugada[1]+=(str(i))
    print(jugada)
    vec[i].configure(background=colores[i])
    time.sleep(.2)
    ventana.update()
    vec[i].configure(background=colores[4])
    time.sleep(.2)
    ventana.update()

def crea_vector (vec,jugada,colores):
    for i in range(4):
        vec.append(Button(text="",command=partial(click,i,jugada,colores)))
        vec[i].place(x=i*100,y=0,height=50,width=100 )
        bttn_com=Button(text="comenzar",command=partial(comenzar,vec,jugada,colores))
        bttn_com.place(x=100,y=100,height=50,width=200)
        bttn_verif=Button(text="verificar",command=partial(verificar,vec,jugada,colores))
        bttn_verif.place(x=100,y=150,height=50,width=200)

def verificar (vec,jugada,colores):
    print(vec, jugada,colores)
    random.seed(None)
    if  jugada[0]==jugada[1]:
        jugada[1]=""
        a=random.randint(0,3)
        jugada[0]+=str(a)
        efecto_jugada(vec,jugada,colores)
        jugada[1]=""
    else:
        messagebox,messagebox.showerror(message="te equivocaste",title="perdiste")
            
def comenzar(vec,jugada,colores):
    a=random.randint(0,2)
    jugada[0]=str(a)
    jugada[1]=""
    vec[a].configure(background=colores[a])
    time.sleep(.2)
    ventana.update()
    vec[a].configure(background=colores[4])
    time.sleep(.2)
    ventana.update   

def efecto_jugada(vec,jugada,colores):
    for i in range (len(jugada[0])):
        vec[int(jugada[0][i])].configure(background=colores[int(jugada[0][i])])
        time.sleep(.2)
        ventana.update()
        vec[int(jugada[0][i])].configure(background=colores[4])
        time.sleep(.2)
        ventana.update()
       
        

#-------------------------------------------------------------------
vec=[]
jugada=["",""]
colores=["blue","red","yellow","green","white"]
crea_vector(vec,jugada,colores)




ventana.mainloop()