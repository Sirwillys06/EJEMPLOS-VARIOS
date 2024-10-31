print("Bienvenido a SERVIAPP\n")


#---------------------------------menu de opciones---------------------------------#
print("MENU DE OPCIONES:\n")

print("INGRESA OPCION 1 PARA: REGISTRAR UN USUARIO")
print("INGRESA OPCION 2 PARA: REGISTRAR UN SERVICIO")
print("INGESA OPCION 3 PARA : ALERTA DE PAGOS")
print("INGESA OPCION 4 PARA : CALIFICAR SERVICIO")
print("INGESA OPCION 5 PARA : CONTROL DE GASTOS")
opcion = int(input("Ingresa una opcion: "))
#----------------------------------Definir variables y Bucle para opciones---------------------------------#
regis_usua = "si"
regis_servi = "si"
regis_alerta = "si"


while opcion > 5 :
    print("La opcion ingresada es incorrrecta.")
    opcion = int(input("Ingresa una opcion: "))
    
if opcion == 1:
    
    #----------------------------Uso de librerias--------------------------------------#
        from tkinter import Entry, Button, Label, Tk, Text, StringVar, Frame
        from tkinter import messagebox
        import pandas as pd

    #------------------------------------Almacenamiento de datos-------------------------#
        def enviarDatos():
    
            nombre = nombre_usuario.get()
            numero_identificacion = numero_id.get()
            correo_electronico = cor_ref.get()
            numero_telefono = cel_ref.get()
            datos_usuario = {
            "Nombre": [nombre],
            "Número de identificación": [numero_identificacion],
            "Correo electrónico": [correo_electronico],
            "Número de teléfono": [numero_telefono]
            }
            df = pd.DataFrame(datos_usuario)
            df.to_excel("D:/backup\Escritorio\Base de datos ServiApp.xlsx", index=False)
            messagebox.showinfo("Información", "Datos guardados")
    #-----------------------------ventana de registro-------------------------------------#
        ventana= Tk()
        ventana.title("Serviapp Registro")
        ventana.geometry("700x500")
    #----------------------------frames(bordes)-------------------------------#
        miframe = Frame(ventana)
        miframe.grid()
    #----------------------------texto(color,fuente,dirrecion)-------------------------------#
        Label(miframe, text="ServiApp " , fg="blue" , font= ("Poppins", 22)).grid(row=0, column=0, sticky="w", padx=5, pady=1)
        Label(miframe, text="Registrate Ahora  " , fg="black" , font= ("Poppins", 15)).grid(row=1, column=0, sticky="w", padx=5, pady=1)
        Label(miframe, text="Nombre Completo :" , fg="gray" , font= ("Poppins", 12)).grid(row=3, column=0, sticky="w", padx=5, pady=1)
        Label(miframe, text="C.C :" , fg="gray" , font= ("Poppins", 12)).grid(row=5, column=0, sticky="w", padx=5, pady=1)
        Label(miframe, text="Contraseña:" , fg="gray" , font= ("Poppins", 12)).grid(row=7, column=0, sticky="w", padx=5, pady=1)
        Label(miframe, text="CEL :" , fg="gray", font= ("poppins", 12)).grid(row=11, column=0,sticky="w", padx=5, pady=1)
        Label(miframe, text=" CORREO : " , fg="gray" , font= ("Poppins", 12)).grid(row=15, column=0, sticky="w", padx=5, pady=1)
    #----------------------------texto(tamaño y ancho)-------------------------------#
        mensajeTxt = Text(miframe, width=30, height=0)
        mensajeTxt.grid(row=4, column=0, padx=10, pady=1)
    #----------------------------variable texto y nombre user-------------------------------#
        mensaje_nombre = StringVar()
        nombre_usuario = Entry(miframe, textvariable=mensaje_nombre)
        nombre_usuario.grid(row=4, column=0, sticky='nsew', padx=10, pady=1 )

        mensaje_CC = StringVar()
        numero_id = Entry(miframe, textvariable=mensaje_CC)
        numero_id.grid(row=6, column=0, sticky='nsew', padx=10, pady=1 )

        mensaje_contra= StringVar()
        numero = Entry(miframe, textvariable=mensaje_contra) 
        numero.grid(row=8, column=0, sticky='nsew', padx=10, pady=1 )

        mensaje_cel = StringVar()
        cel_ref = Entry(miframe, textvariable= mensaje_cel)
        cel_ref.grid(row=14, column=0,sticky='nsew',padx=10, pady=1 )

        correo_w = StringVar()
        cor_ref = Entry(miframe, textvariable= correo_w)
        cor_ref.grid(row=16, column=0,sticky='nsew',padx=10, pady=1 )
        #-----------------------------boton-------------------------------------#

        boton_regi = Button(miframe, text="Registro", fg="black", font=("Poppins", 12), command=enviarDatos )
        boton_regi.grid(row=18, column=0, padx=5, pady=10)

        ventana.mainloop()
    
    
if opcion == 2:
    print("REGISTRA UN SERVICIO \n")
    
    while regis_servi == "si":
        print("Servicios Disponibles: \n")
        print("Servicio de Energia")
        print("Servicio de Agua")
        print("Servicio de Gas")
    
        servicio = input("Porfavor ingresa el servicio que quieres registar: ")
        print(f"Ok, el servicio que elegiste fue {servicio}, porfavor diligencia este formulario: \n")
    
        empresa = input("Ingres el nombre de la empresa prestadora del servicio: ")
        id= int(input("Ingresa el numero de NIC o Contrato del servicio: "))
        fcort= input("Ingresa la fecha de corte de tu servicio: ")
    
        regis_servi= input("Si desea registrar otro servicio digite si, de lo contrario digite no: ")
    print("Ok, Tu servio quedo regsitrado")
    
if opcion == 3:
    print("REVISA SI ES HORA DE PAGAR TU SERVICIO:\n")
    
    regis_alerta = input("¿Quieres verificar si es hora de pagar tu servicio? Ingresa 'si' o 'no': ")
    
    while regis_alerta == "si":
        fechau = input("Ingresa la última fecha de pago: ")
        fecha_actual = input("Ingresa la fecha actual: ")
        
        from datetime import datetime, timedelta
        
        fecha_actual = datetime.now()
        fechau = fecha_actual - timedelta(days=30)
        
        mes = (fecha_actual - fechau).days

        if mes >= 30:
            print("Es hora de pagar tu servicio.")
        else:
            print("Aún no es hora de pagar tu servicio.")
        
        regis_alerta = input("¿Quieres verificar si es hora de pagar tu servicio? Ingresa 'si' o 'no': ")
    print("Ok esta bien😁!")

if opcion == 4:
    print ("CALIFICA EL SERVICIO ⭐")

    servp = input ("Que servicio fue prestado?:   ")

    print (f"Califica tu servicio de {servp} de 1 a 10 estrellas")

    calif = int(input("Cual es la calificacion que das al servicio prestado?:⭐ "))

    while calif <0 or calif >10 :
        print("calficacion invalida")

        calif= int(input("ingrese nuevamente su calificacion:⭐ "))

    if calif >0 and calif <=5:
        print("No estas satisfecho en el servicio")
    elif calif >=6 and calif <=7:
        print("El servicio te parecio regular, Que podemos mejorar del servicio?")
    elif calif >=8 and calif <= 10:
        print("El servicio fue satisfactorio")
    
if opcion == 5:
    print ("CONTROL DE GASTOS")
    print("Conoceras el gasto total del mes en servicios publicos")
    mes = input ("De que mes deseas conocer tus gastos?")
    print (f"el mes que elegiste fue {mes}")

    energia = float (input ("ingrese el valor se su factura de energia: "))
    agua = float (input ("ingrese el valor se su factura de agua: "))
    gas  = float (input ("ingrese el valor se su factura de gas: "))

    gatotal = energia + agua + gas 

    print (f"el gasto total en recibos publicos en el mes de {mes} fue de {gatotal}")

    # print ("{:3f}". format (gatotal)) OTRA FORMA POR LO DE LOS PUNTOS
    