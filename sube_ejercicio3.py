#Diseñar un programa que permita:
#1) Dar de alta un usuario solicitando lo sientes datos:
#Apellido
#Nombres
#DNI
#Genero (M-Masculino; F-Femenino; X-No Binario)
#Fecha de Nacimiento
#Nombre de usuario (inicialmente será su nro de DNI)
#contraseña (inicialmente será su nro de DNI)
#luego genera automáticamente los siguientes datos:
#Nro tarjeta: 16 digitos. Los primeros 8 son los siguientes: 6061 2682 xxxx xxxx
#Saldo
#Debe generar un registro en el archivo “cliente_sube.txt” con los datos anteriores.
#2) Modificación de un usuario
#Debe permitir modificar los datos de un usuario solicitando nro de tarjeta
#3) Baja de usuario
#Debe permitir baja los datos de un usuario solicitando nro de tarjeta. La baja se hara por bandera
#4) Listar Usuarios
#0) Salir de programa

def menu():
    año_nacimiento_maximo=int(1923)
    año_nacimiento_minimo=int(2015)
    opc=int(input("1) Dar de alta un usuario\n2) Modificar un usuario\n3) Dar de baja un usuario\n4) Listar usuarios\n0) Salir\nIngrese una opcion: "))
    while opc!=1 and opc!=2 and opc!=3 and opc!=4 and opc!=0:
        opc=int(input("Ingrese una opcion valida: "))
    if opc==1:
        apellido=input("Ingrese su/s apellido/s: ")
        nombre=input("Ingrese su/s nombre/s: ")
        documento=input("Ingrese su DNI sin puntos: ")
        verif=verificar_dni(documento)
        while len(documento)>9 or len(documento)<7 or verif==True:
            documento=input("El DNI es incorrecto o ya esta registrado, Ingrese un DNI valido: ")
            verif=verificar_dni(documento)
        genero=input("M) Masculino\nF) Femenino\nX) No binario\nIngrese su genero: ")
        genero=genero.lower()
        while genero!="m" and genero!="f" and genero!="x":
            genero=input("Ingrese una opcion valida: ")
        if genero=="m":
            genero="Masculino"
        elif genero=="f":
            genero="Femenino"
        elif genero=="x":
            genero="No Binario"
        fecha_nacimiento=""
        meses=[31,28,31,30,31,30,31,31,30,31,30,31]
        año=int(input("Ingrese el año de su nacimiento: "))
        while año<año_nacimiento_maximo or año>año_nacimiento_minimo:
            año=int(input("Ingrese un valor valido: "))
        mes=input("Ingrese su mes de nacimiento (en numeros): ")
        while int(mes)>12 or int(mes)<1:
            mes=input("Ingrese un mes valido: ")
        dia=input("Ingrese su dia de nacimiento: ")
        while int(dia)<1 or int(dia)>meses[int(mes)-1]:
            dia=input("Ingrese un dia valido: ")
        fecha_nacimiento=dia+"/"+mes+"/"+str(año)
        nombre_usuario=documento
        contraseña=documento
        archivo=open("clientes_sube.txt", "a", encoding="utf-8")
        estado="a"
        archivo.write(documento+","+nombre+","+apellido+","+genero+","+fecha_nacimiento+","+nombre_usuario+","+contraseña+","+estado+"\n")
        archivo.close()
        archivo=open("datos_tarjetas.txt","a",encoding="utf-8")
        tarjeta="60612682"+documento
        saldo=int(0)
        archivo.write(documento+","+tarjeta+","+str(saldo)+"\n")
        archivo.close()
        menu()
    elif opc==2:
        modif=input("Ingrese su numero de tarjeta: ")
        while len(modif)!=16:
            modif=input("Ingrese un numero de tarjeta valido: ")
        cadena=""
        for h in range(8,16):
            cadena+=modif[h]
        aux=verificar_tarjeta(modif)
        while aux!=True:
            modif=input("Ingrese un numero de tarjeta valido: ")
            aux=verificar_tarjeta(modif)
        archivo=open("clientes_sube.txt","r",encoding="utf-8")
        lectura=archivo.readline()
        vec=[]
        datos_usuario=[]
        while lectura!="":
            vec=lectura.split(",",8)
            if vec[0]==cadena:
                datos_usuario=vec
            lectura=archivo.readline()
        opciones=int(input("Que quiere modificar?\n1) DNI\n2) Nombre\n3) Apellido\n4) Genero\n5) Fecha de nacimiento\n6) Usuario\n7) Contraseña\nIngrese una opcion: "))
        while opciones!=1 and opciones!=2 and opciones!=3 and opciones!=4 and opciones!=5 and opciones!=6 and opciones!=7:
            opciones=int(input("Ingrese una opcion valida: "))
        if opciones==1:
            documento=input("Ingrese su DNI sin puntos: ")
            verif=verificar_dni(documento)
            while len(documento)>9 or len(documento)<7 or verif==True:
                documento=input("El DNI es incorrecto o ya esta registrado, Ingrese un DNI valido: ")
                verif=verificar_dni(documento)
            datos_usuario[0]=documento
            modificacion(datos_usuario)
        elif opciones==2:
            nombre=input("Ingrese su/s nombre/s: ")
        elif opciones==3:
            apellido=input("Ingrese su/s apellido/s: ")
        elif opciones==4:
            genero=input("M) Masculino\nF) Femenino\nX) No binario\nIngrese su genero: ")
            genero=genero.lower()
            while genero!="m" and genero!="f" and genero!="x":
                genero=input("Ingrese una opcion valida: ")
            if genero=="m":
                genero="Masculino"
            elif genero=="f":
                genero="Femenino"
            elif genero=="x":
                genero="No Binario"
        elif opciones==5:    
            fecha_nacimiento=""
            meses=[31,28,31,30,31,30,31,31,30,31,30,31]
            año=int(input("Ingrese el año de su nacimiento: "))
            while año<año_nacimiento_maximo or año>año_nacimiento_minimo:
                año=int(input("Ingrese un valor valido: "))
            mes=input("Ingrese su mes de nacimiento (en numeros): ")
            while int(mes)>12 or int(mes)<1:
                mes=input("Ingrese un mes valido: ")
            dia=input("Ingrese su dia de nacimiento: ")
            while int(dia)<1 or int(dia)>meses[int(mes)-1]:
                dia=input("Ingrese un dia valido: ")
            fecha_nacimiento=dia+"/"+mes+"/"+str(año)
        elif opciones==6:
            nombre_usuario=input("Ingrese nuevo nombre de usuario: ")
        elif opciones==7:
            contraseña=input("Ingrese su nueva contraseña: ")
        menu()
    elif opc==3:
        pass
    elif opc==4:
        pass
    
def verificar_dni(documento):
    archivo=open("datos_tarjetas.txt","a",encoding="utf-8")
    archivo.close()
    archivo=open("datos_tarjetas.txt","r",encoding="utf-8")
    aux=archivo.readline()

    while aux!="":
        vec=aux.split(",",8)
        if vec[0]==documento:
            return(True)
        aux=archivo.readline()

def verificar_tarjeta(modif):
    archivo=open("datos_tarjetas.txt","a",encoding="utf-8")
    archivo.close()
    archivo=open("datos_tarjetas.txt","r",encoding="utf-8")
    aux=archivo.readline()

    while aux!="":
        vec=aux.split(",",8)
        if vec[1]==modif:
            return(True)
        aux=archivo.readline()

"""def modificacion(datos_usuario):
    archivo_escribir=open("clientes_sube_aux.txt","w",encoding="utf-8")
    archivo_leer=open("clientes_sube.txt","r",encoding="utf-8")
    aux=archivo_leer.readline()

    while aux!="":
        vec=aux.split(",",8)
        if vec[0]!=datos_usuario[0]:
            archivo_escribir.write(aux)
        elif vec[0]==datos_usuario[0]:
            for i in range (len(datos_usuario)):
                archivo_escribir.write(str(datos_usuario[i])+",")
            archivo_escribir.write("\n")
        aux=archivo_leer.readline()
    archivo_escribir.close()
    archivo_leer.close()"""


menu()
