from tkinter import ttk
from tkinter import *
import time
import random
from functools import partial

#----------------------------------------

def caminos(mat,f,c,cont_cam,m):
    m[f][c].configure(image="pasto.png")
    ventana.update()
    time.sleep(0.5)
    m[f][c].configure(bg="red")
    if(f < 4):
        mat[f][c] = 8
        if(f > 0 and mat[f-1][c]==0):     
            caminos(mat,f-1,c,cont_cam,m)
        if(f > 0 and c < 4 and mat[f-1][c+1]==0): 
            caminos(mat,f-1,c+1,cont_cam,m)
        if(c < 4 and mat[f][c+1]==0):  
            caminos(mat,f,c+1,cont_cam,m)
        if(c < 4 and mat[f+1][c+1]==0):   
            caminos(mat,f+1,c+1,cont_cam,m)
        if(f < 4 and mat[f+1][c]==0):            
            caminos(mat,f+1,c,cont_cam,m)
        if(f < 4 and c > 0 and mat[f+1][c-1]==0):
            caminos(mat,f+1,c-1,cont_cam,m)
        if(c > 0 and mat[f][c-1]== 0):
            caminos(mat,f,c-1,cont_cam,m)
        if(c > 0 and f > 0 and mat[f-1][c-1]==0): 
            caminos(mat,f-1,c-1,cont_cam,m)
        mat[f][c]=0
    elif(f == 4):
        cont_cam[0]+=1
        print(cont_cam)


def carga_imagen(vec_image):
    vec_image.append(PhotoImage(file="pasto.png"))
    vec_image.append(PhotoImage(file="pared.png"))

def inicio(n):
    if(n==0):
        cont_cam = [0]
        matriz =   [[1,0,1,0,1],
                    [1,0,1,1,0],
                    [0,1,0,0,1],
                    [1,0,1,0,1]]
        m = [None] * 4
        for i in range(4):
            v = [None] * 4
            m[i] = v
        for i in range (4):
            for e in range(4):
                m[i][e]= Label(text = str(matriz[i][e]),height=4,width=4,image="pasto.png")
                m[i][e].place(x=40+(e*40),y=30+(i*40))
                time.sleep(.02)
                ventana.update() 
        for c in range(4):
            if(matriz[0][c] == 0):
                caminos(matriz,0,c,cont_cam,m)
    elif(n==1):
        cont_cam = [0]
        matriz = [None]*10
        for i in range(10):
            v = [None] * 10
            
            matriz[i] = v
        for i in range(10):
            for e in range(10):
                random.seed(None)
                matriz[i][e] = random.randint(0,1)
        m = [None]*10
        for i in range(10):
            v = [None] * 10
            m[i] = v
        for i in range (10):
            for e in range(10):
                m[i][e]= Label(text = str(matriz[i][e]),height=4,width=4,image="pasto.png")
                m[i][e].place(x=40+(e*40),y=30+(i*40))
                time.sleep(.02)
                ventana.update()
        for c in range(10):
            if(matriz[0][c] == 0):
                caminos(matriz,0,c,cont_cam,m)
        
            

#-------------------[Tk]-------------------------------------------------------------------
                
ventana = Tk()
ventana.title("Laberinto")
ventana.geometry("500x700")
#----------------------------------------------------------------------------------------
btn_buscar = Button(text="Laberinto", bg='red', height=2, width=25,command=partial(inicio,0))
B_generar_matriz = Button(text="Matriz", bg='red', height=2, width=25, command=partial(inicio,1))
#----------------------------------------------------------------------------------------
btn_buscar.place(x=50,y=600)
B_generar_matriz.place(x=250,y=600)
#----------------------------------------------------------------------------------------
vec_image=[]
carga_imagen(vec_image)

ventana.mainloop()

