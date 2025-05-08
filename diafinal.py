import random
from tkinter import ttk
from tkinter import messagebox
from tkinter import *
import time
from functools import partial
from tkinter import PhotoImage
#--------------------------------------------------[\n' +]

def crea_matriz_rdm():
    mat=[None]*8
    for f in range(8):
        mat[f]=[None]*8
    return(m)

def carga_matriz(mat):
    for f in range(8):
        for c in range (8):
            mat[f][c]=random.randint(0,5)
    muestra_mat(mat)

def muestra_mat(mat):
    for f in range(8):
        for c in range(8):
            print(mat[f][c], end='  ')
        print()

def crea_escenario(mat,mat_img,vec_img):
    for f in range(8):
        for c in range(8):
            mat_img[f][c]=Label(ventana, image=vec_img[mat[f][c]])
            mat_img[f][c].place(x=c*50,y=f*50,height=50,width=50)
    ventana.update()

    '''vida=Label(ventana,text='vidas:')
    vida.place(x=450,y=50)
    score=Label(ventana,text='puntos:')
    score.place(x=450,y=100)
    messi.lift()'''

#-----------------------[mapa propio]
def mat_prop(f,c):
    mat_aux=[None]*f
    for i in range(f):
        mat_aux[i]=[None]*c
    return(mat_aux)


def archivo(f,c,mat_aux):
    mat=open("matriz_prop.txt","r",encoding="utf-8")
    f=int(0)
    linea=mat.readline()
    while(linea != ''):
        aux=linea.split(',',8)
        for c in range(8):
            mat_aux[f][c]=int(aux[c])
        f+=1
        linea=mat.readline()

    mat.close()
        

def escenario_prop(mat_aux,mat_img,vec_img):
    vidas[0]=int(3)
    puntos[0]=int(0)
    for f in range(8):
        for c in range(8):
            mat_img[f][c]=Label(image = vec_img[mat_aux[c][f]])
            mat_img[f][c].place(x=c*50,y=f*50,height=50,width=50)
            if(mat_aux[f][c] == 3):
                mat_img[f][c].configure(image=vec_img[5])
    
#-----------------------------------------------------------------------------------------------------[Teclas]

def teclas_propio(event):
    if(event.keysym == "Up" ):
        if(mat_aux[pos_xy[0]][pos_xy[1]-1] != 2 and mat_aux[pos_xy[0]][pos_xy[1]-1] != 4):
            messi.place(x=messi.winfo_x(), y=messi.winfo_y()-50)
            pos_xy[1] -=1
            if(mat_aux[pos_xy[0]][pos_xy[1]] == 3):
                boom[0] -= 1
                vidas[0] -=1
            print(pos_xy,boom)
            if(mat_aux[pos_xy[0]][pos_xy[1]]==0):
              puntos[0]+=1
            
    elif(event.keysym == "Down" ):
        if(mat_aux[pos_xy[0]][pos_xy[1]+1] != 2 and mat_aux[pos_xy[0]][pos_xy[1]+1] != 4):
            messi.place(x=messi.winfo_x(), y=messi.winfo_y()+50)
            pos_xy[1] +=1
            if(mat_aux[pos_xy[0]][pos_xy[1]] == 3):
                boom[0] -= 1
                vidas[0] -=1
            print(pos_xy,boom)
            if(mat_aux[pos_xy[0]][pos_xy[1]]==0):
              puntos[0]+=1

    elif(event.keysym == "Left" ):
        if(mat_aux[pos_xy[0]-1][pos_xy[1]] != 2 and mat_aux[pos_xy[0]-1][pos_xy[1]] != 4):
            messi.place(x=messi.winfo_x()-50, y=messi.winfo_y())
            pos_xy[0] -=1
            if(mat_aux[pos_xy[0]][pos_xy[1]] == 3):
                boom[0] -= 1
                vidas[0] -=1
            print(pos_xy,boom)
            if(mat_aux[pos_xy[0]][pos_xy[1]]==0):
              puntos[0]+=1
            
    elif(event.keysym == "Right"):
        if(mat_aux[pos_xy[0]+1][pos_xy[1]] != 2 and mat_aux[pos_xy[0]+1][pos_xy[1]] != 4):
            messi.place(x=messi.winfo_x()+50, y=messi.winfo_y())
            pos_xy[0] +=1
            if(mat_aux[pos_xy[0]][pos_xy[1]] == 3):
               boom[0] -= 1
               vidas[0] -=1
            print(pos_xy,boom)
            if(mat_aux[pos_xy[0]][pos_xy[1]]==0):
              puntos[0]+=1
              
    vidas=Label(ventana,text='vidas:'+str(boom))
    vidas.place(x=450,y=50)

    pun=Label(ventana,text='puntos:'+str(puntos))
    pun.place(x=450,y=100)

   
       
    if(puntos[0] == 2):
        for f in range(8):
            for c in range(8):
                mat_img[f][c].destroy()
        crea_escenario(mat,mat_img,vec_img)


    ventana.update()
     
#imagen---------------------------------------------------------------------------------
def carga_imagen():
    vec_img=[]
    vec_img.append(PhotoImage(file='copa1.png'))#0
    vec_img.append(PhotoImage(file='pasto.png'))#1
    vec_img.append(PhotoImage(file='limites.png'))#2
    vec_img.append(PhotoImage(file='boom.png'))#3
    vec_img.append(PhotoImage(file='barrera.png'))#4
    vec_img.append(PhotoImage(file='camino.png'))#5
    return(vec_img)

#programa principal-------------------------------------
ventana = Tk()
ventana.geometry('700x500')
ventana.title('busqueda del tesoro')

#------------------------[propia]
boom =[None]
boom[0] = int(3)

vidas = [None]
vidas[0] = int(3)

puntos = [None]
puntos[0] = int(0)

f = 8
c = 8
mat_aux=mat_prop(f,c)
mat_img=mat_prop(f,c)
archivo(f,c,mat_aux)
vec_img=carga_imagen()

escenario_prop(mat_aux,mat_img,vec_img)




#------------------------------------
mesi=PhotoImage(file='messicorre.png')
messi=Label(ventana,image=mesi)
messi.place(x=50,y=50)
pos_xy=[1,0]
#------------------------------------
ventana.bind("<Key>",teclas_propio)
ventana.mainloop()
