def m_saldo(usu,con):
    archivo = open("sube_datos.txt","r")
    lee = archivo.readline()
    while(lee != ""):  
        lee2 = lee.split(",",12)
        if(str(usu) == str(lee2[5]) and str(con) == str(lee2[6])):
            print("Su saldo es de",float(lee2[8]))
        lee = archivo.readline()
    archivo.close()
    menu(usu,con)
def modifica(usu,con):
    archivo2 = open("temp.txt","w")
    archivo = open("sube_datos.txt","r")
    lee=archivo.readline()

    while(lee!=''):
        aux=lee.split(',',12)
        aux2=str(aux[5])
        aux3=str(aux[6])
        if(aux2!=usu and aux3 != con):
            archivo2.write(lee)
        else:
            nuevo_usu = input("Ingrese nuevo numero de usuario: ")
            ocu = veri(nuevo_usu)
            while(ocu):
                    print("ERROR\nUsuario ya existente")
                    print("***************************************************************")
                    nuevo_usu = input("Ingrese nuevo numero de usuario: ")
                    ocu = veri(nuevo_usu)
            nueva_contra = input("Ingrese su nuevo numero de contraseña : ")
            aux[5]= nuevo_usu
            aux[6]= nueva_contra
            aux=str(aux[0])+","+str(aux[1])+","+str(aux[2])+","+str(aux[3])+","+str(aux[4])+","+str(aux[5])+","+str(aux[6])+","+str(aux[7])+","+str(aux[8])+","+str(aux[9])
            archivo2.write(aux)

        lee=archivo.readline()
    archivo.close()
    archivo2.close()
    archivo2 = open ("temp.txt","r")
    archivo = open ("sube_datos.txt","w")
    aux = archivo2.readline()
    while(aux != ""):
        archivo.write(aux)
        aux = archivo2.readline()
    archivo.close()
    archivo2.close()
    print("cambios hechos!!")
    login()

def veri(usu):
    archivo=open("sube_datos.txt","a")
    archivo.close()
    archivo=open("sube_datos.txt","r")
    lee=archivo.readline()

    while (lee!=""):
        aux=lee.split(",",10)
        if (str(aux[5]) == str(usu)):
            return(True)
        lee=archivo.readline()

def cargasaldo(usu,con):
    verificar = True
    archivo = open("sube_datos.txt","r")
    aux = open("cliente_aux.txt","w")
    lee = archivo.readline()
    while lee != '':
        lee_aux = lee.split(',')
        if str(lee_aux[5]) != str(usu) and str(lee_aux[6]) != str(con):
            aux.write(lee)
            lee=archivo.readline()
        elif lee_aux[5] == usu and lee_aux[6] == con:
            num = float(lee_aux[8])
            suma=float(input("Ingrese un numero de valor menor o igual a 1000$ para cargar:"))
            while(suma>=1000):
                print("ERROR ingrese un valor dentro del rango permitido")
                suma=float(input("Ingrese un numero de valor menor o igual a 1000$ para cargar:"))
            if(suma+num)<=3000:    
                num+=suma
                lee_aux[8]=str(num)
                print("Tu nuevo saldo es de",lee_aux[8],'pesos')
                aux.write(str(lee_aux[0])+","+str(lee_aux[1])+","+str(lee_aux[2])+","+str(lee_aux[3])+","+str(lee_aux[4])+","+str(lee_aux[5])+","+str(lee_aux[6])+","+str(lee_aux[7])+","+str(lee_aux[8])+","+str(lee_aux[9]))
            else:
                verificar  = False
                print("NO se puede ingresar, se pasa el valor")
                
                aux.write(lee)
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
    if(verificar == True):
        archivo2 = open("movimientos.txt","a")
        archivo = open("sube_datos.txt","r")
        lee = archivo.readline()
        while lee != '':
            lee_aux = lee.split(',',12)
            if str(lee_aux[5]) == str(usu) and str(lee_aux[6]) == str(con):
                auxiliar = lee_aux[7]+","+"Cargo de saldo"+","+"Carga: $"+str(suma)+","+"Saldo: $"+str(num)+","+str("")+","+str("")+"\n"
                archivo2.write(auxiliar)
            lee = archivo.readline()
        archivo.close()
        archivo2.close()
    menu(usu,con)   

def movimientos(usu,con):
    cont = 0
    cont2 = 0
    cont3 = 0
    archivo3 = open("movimientos.txt","a")
    archivo3.close()
    archivo = open("sube_datos.txt","a")
    archivo.close()
    archivo = open("sube_datos.txt","r")
    lee=archivo.readline()
    while(lee!=''):
        aux=lee.split(',',12)
        aux2=str(aux[5])
        aux3=str(aux[6])
        cont+=1
        if(aux2 == usu and aux3 == con):
            num_t = int(aux[7])
        lee=archivo.readline()
    archivo.close()
    archivo3 = open("movimientos.txt","r")
    lee=archivo3.readline()
    while(lee!=''):
        aux = lee.split(",",10)
        aux2 = int(aux[0])
        cont2+=1
        if(aux2 == num_t):
            cont3+=1
            print("**********************************************************************************")
            print("Numero de tarjeta: ",str(aux[0])+"|"+str(aux[1])+"|"+str(aux[2])+"|"+str(aux[3])+str(aux[4])+"|"+str(aux[5]))
        lee=archivo3.readline()
    if(cont == 0 and cont2 == 0):
        print("No hay ningun dato")
    if(cont3 == 0):
        print("No existe ningun movimiento")
    menu(usu,con)

#------------------------------------------------------------[tren]
def menuviaje(lineas,lsm,luq,lsa,lM1,lM2,lM3,lBN,lBS1,lBS2,lR1,lR2,lR3,usu,con):
    archivo = open("sube_datos.txt", "r")
    lee = archivo.readline()
    while lee != '':
        lee_aux = lee.split(',')
        if lee_aux[5] == usu and lee_aux[6] == con:
            saldo = lee_aux[8]
            lee = archivo.readline()
        else:
            lee = archivo.readline()

    if float(saldo) >= 100:

        opc = -1
        cont = int(1)
        for i in range(len(lineas)):
            print(cont,lineas[i])
            cont+=1
        print("0 Salir")
        opc = int(input("Indique en que linea viajara: "))
        if opc == 1:
            estacion(lsm,usu,con,opc-1,lineas)
        if opc == 2:
            estacion(luq,usu,con,opc-1,lineas)
        if opc == 3:
            estacion(lsa,usu,con,opc-1,lineas)
        if opc == 4:
            print("1 Ramal Tigre (Retiro - Tigre)\n2 Ramal Suarez (Retiro - José León Suarez)\n3 Ramal Mitre (Retiro - Mitre)\n4 Salir")
            opc2 = int(input("En que ramal de la linea Mitre viajara: "))
            if opc2 == 1:
                estacion(lM1,usu,con,opc-1,lineas)
            if opc2 == 2:
                estacion(lM2,usu,con,opc-1,lineas)
            if opc2 == 3:
                estacion(lM3,usu,con,opc-1,lineas)
            if opc2 == 0 or opc2 >= 4:
                print("")
        if opc == 5:
            estacion(lBN,usu,con,opc-1,lineas)
        if opc == 6:
            print("1 Ramal Catan (Constitución - Gonzalez Catan)\n2 Ramal Cro Gral Belgrano (Constitución - Marineros Crucero grl Belgrano)\3 Salir")
            opc2 = int(input("En que ramal de la linea Belgrano Sur viajara: "))
            if opc2 == 1:
                estacion(lBS1,usu,con,opc-1,lineas)
            if opc2 == 2:
                estacion(lBS2,usu,con,opc-1,lineas)
            if opc2 == 0 or opc2 >= 3:
                print()
        if opc == 7:
            print("1 Ramal la Plata (Constitución - La plata)\n2 Ramal Bosques (Constitución - Bosques)\n3 Ramal Cañuelas (Ezeiza - Cañuelas)Cañuelas (Ezeiza - Cañuelas)\n4 Salir")
            opc2 = int(input("En que ramal de la linea Roca viajara: "))
            if opc2 == 1:
                estacion(lR1,usu,con,opc-1,lineas)
            if opc2 == 2:
                estacion(lR2,usu,con,opc-1,lineas)
            if opc2 == 3:
                estacion(lR3,usu,con,opc-1,lineas)
            if opc2 == 0 or opc2 >= 4:
                print("")
        if opc == "0":
            print("")
    else:
        print("El saldo minimo para realizar un viaje es $100")

def estacion(est,usu,con,opc,lineas):
    estacion_f = lineas[opc]
    cont = 1
    for i in range(len(est)):
        print(cont,est[i])
        cont+=1
    sube = int(input("Indique en que numero de estacion se sube: "))
    while sube > len(est) or sube < 1:
        print("No existe, vuelva a ingresarlo")
        sube = int(input("Indique en que numero de estacion se sube: "))
    print("Sube en la estacion",est[sube-1])
    baja = int(input("Indique en que numero de estacion se baja: "))
    while baja > len(est) or baja < 1:
        print("No existe, vuelva a ingresarlo")
        baja = int(input("Indique en que numero de estacion se baja: "))
    print("Baja en la estacion",est[baja-1])

    cobro(sube,baja,usu,con,estacion_f)

def cobro(sube,baja,usu,con,estacion_f):
    minimo = float(17.50)
    maximo = float(100.00)
    aumento = float(7.50)
    total = float(0.00)
    cobro = float(0.00)
    sald = (0)
    if baja > sube:
        estaciones = baja-sube
        for i in range(estaciones):
            if (i+1)%5 == 0:
                total+=aumento
        cobro = total+minimo

    else:
        estaciones = sube-baja
        for i in range(estaciones):
            if (i+1)%5 == 0:
                total+=aumento
        cobro = total+minimo
    print("El valor del boleto es de",cobro,"pesos.")
#---------------------------------------------------------------resta
    archivo = open("sube_datos.txt","r")
    le = archivo.readline()
    while le != "":
        le_aux = le.split(",")
        if le_aux[5] == usu and le_aux[6] == con:
            sald = le_aux[8]
            
        le = archivo.readline()
    archivo.close()
    saldo =float(float(sald)-float(cobro))
    print("El saldo es: "+str(saldo))

#---------------------------------------------------------datos al movimiento

    arch_m = open("movimientos.txt", "a")
    archivo = open("sube_datos.txt", "r")
    lee = archivo.readline()
    while lee != '':
        lee_aux = lee.split(',')
        if lee_aux[5] == usu and lee_aux[6] == con:
            auxiliar = lee_aux[7]+","+estacion_f+","+"Gasto: $"+str(cobro)+","+"Saldo: $"+str(saldo)+","+"Cobro Total: $"+str(maximo)+","+"Devuelve: $"+str(maximo-cobro)+"\n"
            arch_m.write(auxiliar)

        lee=archivo.readline()
    arch_m.close()
    archivo.close()


#--------------------------------------------------------------------------------------------[valor del saldo al txt principal]
    archivo = open('sube_datos.txt','r')
    aux = open("cliente_aux.txt","w")
    lee = archivo.readline()
    while lee!= "":
        lee_aux = lee.split(",")
        if lee_aux[5] == usu and lee_aux[6] == con:
            lee_aux[8] = str(saldo)
            aux.write(lee_aux[0]+","+lee_aux[1]+","+lee_aux[2]+","+lee_aux[3]+","+lee_aux[4]+","+lee_aux[5]+","+lee_aux[6]+","+lee_aux[7]+","+lee_aux[8]+","+lee_aux[9])            
        else:
            aux.write(lee)
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

def arch_m1(usu,con):
    lineas = ["Linea San Martin", "Linea Urquiza", "Linea Sarmiento", "Linea Mitre", "Línea Belgrano Norte", "Línea Belgrano Sur", "Línea Roca"]
    lsm = ["Retiro", "Palermo", "Villa Crespo", "La Paternal", "Villa del Parque", "Devoto", "Sáenz Peña", "Santos Lugares", "Caseros", "El Palomar", "Hurlingham", "William Morris", "Bella Vista", "Muñiz", "San Miguel", "José C. Paz", "Sol y Verde", "Derqui", "Villa Astolfi", "Pilar", "Manzanares", "Doctor Cabred"]
    luq = ["Federico Lacroze", "Artigas", "Arata", "Francisco Beiró", "El Libertador", "Devoto", "Lynch", "F. Moreno", "Lourdes", "Tropezón", "J.M. Bosch", "Martín Coronado", "Pablo Podestá", "Jorge Newbery", "Rubén Darío", "Ejército de los Andes", "Lasalle", "Sargento Barrufaldi", "Capitán Lozano", "Teniente Agneta", "Campo de Mayo", "Sargento Cabral", "General Lemos"]
    lsa = ['Once', 'Caballito', 'Flores', 'Floresta', 'Villa Luro', 'Liniers', 'Ciudadela', 'Ramos Mejía', 'Haedo', 'Morón', 'Castelar', 'Ituzaingó', 'San Antonio de Padua', 'Merlo', 'Paso del Rey', 'Moreno']
    lM1 = ["Retiro", "Lisandro de la Torre", "Belgrano C", "Núñez", "Rivadavia", "Vicente López", "Olivos", "La Lucila", "Martínez", "Acassuso", "San Isidro", "Beccar", "Victoria", "Virreyes", "San Fernando", "Carupá", "Tigre"]
    lM2 = ["Retiro", "3 de Febrero", "Carranza", "Colegiales", "Belgrano R", "Drago", "Urquiza", "Pueyrredón", "Miguelete", "San Martín", "San Andrés", "Malaver", "Villa Ballester", "Chilavert", "José León Suarez"]
    lM3 = ["Retiro", "3 de Febrero", "Carranza", "Colegiales", "Belgrano R", "Coghlan", "Saavedra", "J.B. Justo", "Florida", "Cetránngolo", "Mitre"]
    lBN = ["Retiro", "Saldías", "R.S.Ortíz", "A. Del Valle", "M.M Padilla", "Florida", "Munro", "Carapachay", "Villa Adelina", "Boulogne Sur Mer", "Vice. A. Montes", "Don Torcuato", "A. Sordeaux", "Villa de Mayo", "Los Polvorines", "Ing P. Nogués", "Grand Bourg", "Tierras Altas", "Tortuguitas", "Manuel Alberti","Villa Rosa"]
    lBS1 = ["Constitución", "Buenos Aires", "Dr Saenz", "Villa Soldati", "Pte Illia", "Villa Lugano", "Villa Madero", "M Del Fourner", "Tapiales", "Ing Castello", "KM 12", "Querandí", "Laferrere", "Eva Duarte", "Independencia", "Gonzales Catán"]
    lBS2 = ["Constitución", "Buenos Aires", "Dr Saenz", "Villa Soldati", "Pte Illia", "Villa Lugano", "Villa Madero", "M Del Fourner", "Tapiales", "Ing Castello", "Bonzi", "M S Mendeville", "J Ingenieros", "J Villegas", "Isidro Casanova", "R Castillo", "Merlo Gómez", "Libertad", "Marinos del Cro. General Belgrano"]
    lR1 = ["Constitución", "Sarandí", "Villa Domínico", "Wilde", "Don Bosco", "Bernal", "Quilmes", "Ezpeleta", "Berazategui", "Plátanos", "Hudson", "Pereyra", "Villa Elisa", "City Bell", "Gonnet", "Ringuelet", "Tolosa", "La Plata"]
    lR2 = ["Constitución", "Sarandí", "Villa Domínico", "Wilde", "Don Bosco", "Bernal", "Quilmes", "Ezpeleta", "Berazategui", "Villa España", "Ranelagh", "Sourigues", "Bosques"]
    lR3 = ["Ezeiza", "Unión Ferroviaria", "Tristán Suárez", "Spegazzini", "Máximo Paz", "Casares", "Petión", "Kloosterman", "Levene", "Cañuelas"]
    menuviaje(lineas,lsm,luq,lsa,lM1,lM2,lM3,lBN,lBS1,lBS2,lR1,lR2,lR3,usu,con)
#--------------------------------[menu+login]----------------------------------------------------------------------------------
def menu(usu,con):
    print ("Bienvenido, que desea hacer:")
    opc=int(input("1)Mostrar Saldo.\n2)Carga de Saldo.\n3)Movimientos del Usuario.\n4)Cobro.\n5)Modificar.\n0)Salir\n:"))
    if(opc == 1):
        m_saldo(usu,con)
    elif(opc == 2):
        cargasaldo(usu,con)
    elif(opc == 3):
        movimientos(usu,con)
    elif(opc == 4):
        arch_m1(usu,con)
    elif(opc == 5):
        modifica(usu,con)
    elif opc == 0:
        print("Fin del programa")    
def login():
    print("*******************************[Login]*******************************")
    val1 = False
    val2 = False
    verif = True
    cont1=0
    cont2=0
    archivo = open("sube_datos.txt","a")
    archivo.close()
    archivo = open("sube_datos.txt","r")
    lee=archivo.readline()
    usu = str(input("Ingrese su usuario: "))
    con = input("Ingrese su contraseña: ")
    while lee != '':
        cont1+=1
        lee2=lee.split(",",12)
        if(str(lee2[9])!='X'):
            cont2+=1
            if(str(lee2[5])==usu):
                print("usuario correcto")
                val1=True
                if(str(lee2[6])==con):
                    print("Contraseña correcta")
                    val2=True
    
        else:
            verif=False
        lee=archivo.readline()
    if(val1 and val2 ==True):
        menu(usu,con)
    if(verif==False):
        print("Usuario no encontrado")
                
            
                

       
login()


#--------------------------------------------
#---------------------
#TERMINADO[][][]
#-----
#[]
#-----terminado
