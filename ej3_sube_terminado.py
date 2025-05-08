def veri_dni(dni,num_t):

    archivo=open("sube_datos.txt","a")
    archivo.close()
    archivo=open("sube_datos.txt","r")
    datos=archivo.readline()

    while (datos!=""):
        aux=datos.split(",",8)
        if(int(aux[7]) != int(num_t)):
            if (int(aux[2])==int(dni)):
                return(True)
        datos=archivo.readline()
#--------------------------------------------------------------------------------------------------------------------------[ALTA]
def alta():
    cont=int(0)
    archivo=open("sube_datos.txt","a")
    archivo.close()
    saldo=int(0)
    print("-----------[Alta]-----------")
    ape=input("Ingrese su Apellido:")
    nom=input("Ingrese su Nombre:")
    archivo = open ("sube_datos.txt","r")
    lee = archivo.readline()
    dni = int(input("Ingrese el DNI: "))
    while(len(str(dni)) != 8):
        print("ERROR dni incorrecto")
        dni = int(input("Ingrese el DNI: "))
    while(lee != ""):
        aux = lee.split(",",12)
        aux2 = int(aux[5])
        cont+=1

        while(aux2 == dni):
            print("el dni ingresado ya existe")
            dni = int(input("Ingrese el DNI: "))
            while(len(str(dni)) != 8):
                print("ERROR dni incorrecto")
                dni = int(input("Ingrese el DNI: "))
        lee = archivo.readline()
    if(cont == 0):
        dni = dni
    archivo.close()
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
    año=int(input("ingrese el año:"))
    while(año<1700 or año>=2024):
        print("Erron el año")
        año=int(input("ingrese el año:"))
       
    mes=int(input("ingrese el mes:"))
    while(mes<0 or mes>12):
        print("Error mes incorrcto")
        mes=int(input("ingrese el mes:"))

    dia=int(input("Ingrese el dia: "))
    if año % 4 == 0 and (año % 100 != 0 or año % 400 == 0):
        dias=[31,29,31,30,31,30,31,31,30,31,30,31]
    else:
        dias=[31,28,31,30,31,30,31,31,30,31,30,31]
    while(dia>dias[mes-1] or dia<1):
        print("error de fecha")
        dia=int(input("Ingrese el dia: "))

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
    bandera=str("o")
    contador.close()
    contador=open('contador.txt','w')
    contador.write(str(sig))
    contador.close()
    print("su numero de tarjeta es",num_t)
    print("su saldo es de:$",saldo)

    aux=str(ape.lower())+","+str(nom.lower())+","+str(dni)+","+str(gen)+","+str(fecha)+","+str(nm_usr)+","+str(contra)+","+str(num_t)+","+str(saldo)+","+str(bandera)+"\n"
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
        lee_aux=lee.split(",",12)
        if str(lee_aux[9])!=str('X'):
            if veri != int(lee_aux[7]):
                aux.write(lee)
            else:
                print("el usuario a sido encontrado")
                print("ingrese los datos a modificar")
                ape=input("Ingrese su Apellido:")
                nom=input("Ingrese su Nombre:")
                dni = int(input("Ingrese el DNI: "))
                while(len(str(dni)) != 8):
                    print("ERROR dni incorrecto")
                    dni = int(input("Ingrese el DNI: "))
                dni_ocu=veri_dni(dni,veri)
                while(dni_ocu):
                    print("el dni ya existe")
                    dni=input("ingrese su DNI:")
                    dni_ocu=veri_dni(dni,veri)
                    while(len(str(dni)) != 8):
                        print("ERROR dni incorrecto")
                        dni = int(input("Ingrese el DNI: "))
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
               
                año=int(input("ingrese el año:"))
                while(año<0 or año>=2024):
                    print("Error año invalido")
                    año=int(input("ingrese el año:"))

                mes=int(input("ingrese el mes:"))
                while(mes<0 or mes>12):
                    print("error sobrepasa el mes")
                    mes=int(input("ingrese el mes:"))
                   
                dia=int(input("Ingrese el dia: "))
                if año % 4 == 0 and (año % 100 != 0 or año % 400 == 0):
                    dias=[31,29,31,30,31,30,31,31,30,31,30,31]
                else:
                    dias=[31,28,31,30,31,30,31,31,30,31,30,31]
                while(dia>dias[mes-1] or dia<1):
                    print("error de fecha")
                    dia=int(input("Ingrese el dia: "))
                fecha=str(dia)+'/'+str(mes)+'/'+str(año)
                print("su fecha es",dia,"/",mes,"/",año)
                nm_usr=dni
                contra=dni
                bandera=str("o")
                num_t=lee_aux[7]
                print("su numero de tarjeta es",num_t)
                aux2=str(ape.lower())+","+str(nom.lower())+","+str(dni)+","+str(gen)+","+str(fecha)+","+str(nm_usr)+","+str(contra)+","+str(num_t)+","+str(saldo)+","+str(bandera)+"\n"
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
        lee_aux = lee.split(',')
        if(num!=lee_aux[7]):
            aux.write(lee)
            lee=archivo.readline()
        else:
            print("Usuario encontrado")
            aux.write(str(lee_aux[0])+","+str(lee_aux[1])+","+str(lee_aux[2])+","+str(lee_aux[3])+","+str(lee_aux[4])+","+str(lee_aux[5])+","+str(lee_aux[6])+","+str(lee_aux[7])+","+str(lee_aux[8])+","+str("X")+"\n")
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
#----------------------------------------------------------------------------------------------[LISTAR]
def listar():
    archivo = open("sube_datos.txt","r")
    lee = archivo.readline()
    cont= 1
    while lee!='':
        lee_aux = lee.split(',',12)
        a=lee_aux[9]
        if(a[:-1]!='X'):
            print("*****************************************************************************************************************************************************************")
            print(cont,"-","Nombre:",str(lee_aux[0]),"| Apellido:",str(lee_aux[1]),"| DNI:",str(lee_aux[2]),"| Genero:",str(lee_aux[3]),"| Fecha de nacimiento:",str(lee_aux[4]),"| Usuario:",str(lee_aux[5]),"| Contraseña:",str(lee_aux[6]),"| Nro de tarjeta:",str(lee_aux[7]),"| Saldo:",str(lee_aux[8]))
            cont += 1
            lee = archivo.readline()
        else:
            lee = archivo.readline()
    archivo.close()
    menu()
#--------------------------------------------------------------------------------------------------------------------------------------------------[MENU]
def menu():
    print("----------[MENU]----------")
    print("ingrese una opcion")
    opc=int(input("¿que desea hacer?\n1)Alta\n2)Modifica\n3)Baja\n4)Listar\n0)Salir\n:"))
    if opc==1:
        alta()
    if opc==2:
        modifica()
    if opc==3:
        baja()
    if opc==4:
        listar()
    if opc==0:
        print("hasta luego")
menu()

#------------------------------
#--------------------------------------
#---------------------------------------------
#--------------------------------------------------
#---------------------------------------------------------
#----------------------------------------
#-------------------------------------------------------------
#---------------------------------[]
#[terminado]
#---
#-
#--
#3pro---
