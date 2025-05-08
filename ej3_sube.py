#--------------------------------------------------------------------------------------------------------------------------[ALTA]
def alta():
    saldo=int(0)
    print("-----------[Alta]-----------")
    ape=input("Ingrese su Apellido:")
    nom=input("Ingrese su Nombre:")
    dni=input("ingrese su DNI:")
    while(len(str(dni))!=8):
        print("ingrese un dni valido")
        dni=input("ingrese su DNI:")
    print("ingrese su genero")
    op=int(input("1)Masculino \n2)Femenino \n3)No Binario \n:"))
    while (op != 1 and op != 2 and op != 3 ):
        print("ERROR")
        op=int(input("1)Masculino \n2)Femenino \n3)No Binario \n:"))
    if(op==1):
        gen=str("M")
    if(op==2):
        gen=str("F")
    if(op==3):
        gen=str("X")
    print("Ingrese su fecha de nacimiento")
    dia=int(input("Ingrese el dia:"))
    while(dia<0 or dia>31):
        print("ERROR ")
        dia=int(input("Ingrese el dia:"))
    mes=int(input("ingrese el mes:"))
    while(mes<0 or mes>12):
        print("ERROR")
        mes=int(input("ingrese el mes:"))
    año=int(input("ingrese el año:"))
    while(año<0 or año>=2024):
        print("ERROR")
        año=int(input("ingrese el año:"))
    fecha=str(dia)+'/'+str(mes)+'/'+str(año)
    print("su fecha es:",fecha)
   
    nm_usr=dni
    contra=dni
    contador=open('contador.txt','a')
    contador.close()
    contador=open('contador.txt','r')
    lee=str(contador.readline())
    if(lee==''):
        lee=0
    else:
        lee=int(lee)
    sig=lee+1
    num_t = str("6061268200000000")
    num_t = int("6061268200000000")+sig
    contador.close()
    contador=open('contador.txt','w')
    contador.write(str(sig))
    contador.close()
    print("su numero de tarjeta es",num_t)
    print("su saldo es de:$",saldo)

    aux=str(ape)+" , "+str(nom)+" , "+str(dni)+" , "+str(gen)+" , "+str(fecha)+" , "+str(nm_usr)+" , "+str(contra)+" , "+str(num_t)+" , "+str(saldo)+"\n"
    archivo=open("sube_datos.txt","a")
    archivo.write(aux)
    archivo.close()
    menu()



   
#------------------------------------------------------------------------------------------------------------------------------------------------------------[MODIFICA]
def modifica():
    saldo=int(0)
    veri=int(input("ingrese su numero de tarjeta:"))
   
    archivo=open("sube_datos.txt","r")
    aux=open("cliente_aux.txt","w")
    lee=archivo.readline()
   
    while lee!='':
        lee_aux=lee.split(" , ",12)
        if str(lee_aux[0])!=str('X'):
            if veri != int(lee_aux[7]):
                aux.write(lee)
            else:
                print("el usuario a sido encontrado")
                print("ingrese los datos a modificar")
                ape=input("Ingrese su Apellido:")
                nom=input("Ingrese su Nombre:")
                dni=input("ingrese su DNI:")
                while(len(str(dni))!=8):
                    print("ingrese un dni valido")
                    dni=input("ingrese su DNI:")
                print("ingrese su genero")
                op=int(input("1)Masculino \n2)Femenino \n3)No Binario \n:"))
                while (op != 1 and op != 2 and op != 3 ):
                    print("ERROR")
                    op=int(input("1)Masculino \n2)Femenino \n3)No Binario \n:"))
                if(op==1):
                    gen=str("M")
                if(op==2):
                    gen=str("F")
                if(op==3):
                    gen=str("X")
                print("Ingrese su fecha de nacimiento")
                dia=int(input("Ingrese el dia:"))
                while(dia<0 or dia>31):
                    print("ERROR ")
                    dia=int(input("Ingrese el dia:"))
                mes=int(input("ingrese el mes:"))
                while(mes<0 or mes>12):
                    print("ERROR")
                    mes=int(input("ingrese el mes:"))
                año=int(input("ingrese el año:"))
                while(año<0 or año>=2024):
                    print("ERROR")
                    año=int(input("ingrese el año:"))
                fecha=str(dia)+'/'+str(mes)+'/'+str(año)
                print("su fecha es",dia,"/",mes,"/",año)
                nm_usr=dni
                contra=dni
                num_t=lee_aux[7]
                print("su numero de tarjeta es",num_t)
                aux2=str(ape)+" , "+str(nom)+" , "+str(dni)+" , "+str(gen)+" , "+str(fecha)+" , "+str(nm_usr)+" , "+str(contra)+" , "+str(num_t)+" , "+str(saldo)+"\n"
                aux.write(aux2)
            lee = archivo.readline()

   
    archivo.close()  
    aux.close()

    archivo = open('sube_datos.txt',"w")
    aux = open('cliente_aux.txt','r')
   
    lee=aux.readline()
   
    while(lee != ''):
        archivo.write(lee)
        lee=aux.readline()
       
    archivo.close()
    aux.close()

    aux = open('cliente_aux.txt','w')
    aux.close()
    menu()
#-----------------------------------------------------------------------------------------------[BORRAR]
def baja():
    num = input("Ingrese el numero de tarjeta del usuario que desea dar de baja:")
    archivo = open("sube_datos.txt", "r")
    aux = open("cliente_aux.txt", "w")

    lee = archivo.readline()
    while lee != '':
        lee_aux = lee.split(' , ')
        if(num!=lee_aux[7]):
            aux.write(lee)
            lee=archivo.readline()
        else:
            print("Usuario encontrado")
            aux.write('X')
            for i in range(len(lee_aux)):
                linea = str(lee_aux[i])
                aux.write(', '+linea)
            lee = archivo.readline()
    archivo.close()  
    aux.close()

    archivo = open('sube_datos.txt',"w")
    aux = open('cliente_aux.txt','r')
   
    lee=aux.readline()
   
    while(lee != ''):
        archivo.write(lee)
        lee=aux.readline()
       
    archivo.close()
    aux.close()

    aux = open('cliente_aux.txt','w')
    aux.close()
#----------------------------------------------------------------------------------------------[LISTAR]
def listar():
    archivo = open("sube_datos.txt","r")
    lee = archivo.readline()
    cont= 0
    while lee!= '':
        lee_aux = lee.split(',')
        if str(lee_aux[0])!=str('X'):
            print (cont,"-",lee)
            cont += 1
        lee = archivo.readline()
       
    archivo.close()
#--------------------------------------------------------------------------------------------------------------------------------------------------[MENU]
def menu():
    print("----------[MENU]----------")
    print("ingrese una opcion")
    opc=int(input("¿que desea hacer?\n1)Alta\n2)Modifica\n3)Baja\n4)Listar\n0)Salir\n:"))
    while opc!=0:
        if opc==1:
            alta()
        if opc==2:
            modifica()
        if opc==3:
            baja()
        if opc==4:
            listar()
        opc=int(input("¿que desea hacer?\n1)Alta\n2)Modifica\n3)Baja\n4)Listar\n0)Salir\n:"))
    print("hasta luego")

menu()

#------------------------------
#--------------------------------------
#---------------------------------------------
#--------------------------------------------------
#---------------------------------------------------------
