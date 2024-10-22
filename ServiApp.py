from os import system
system('cls')
print("BIENVENIDO A SERVIAPP 💡\n")
print("Por favor completa el siguiente formulario para que te puedas registar y acceder a las funciones. \n")

#-------------------------Crear listas----------------------------#
usuarios=[]
lista_servicios=[]


#------------------------------Registro de usuario-------------------------------#
def registar_usuario():
    name = input("Nombre completo: ")
    email = input("Correo electrónico: ")
    user = input("Usuario: ")
    password = input("Contraseña segura: ")
    while True:
        Num_tel = input("Número de teléfono: ")
        if Num_tel.isdigit():
            break
        else:
            print("Por favor ingresa solo números.")
    ti_id = input("Tipo de identificación: ")
    while True:
        Num_id = input("Número de identificación: ")
        if Num_id.isdigit():
            break
        else:
            print("Por favor ingresa solo números.")
    departament = input("Departamento: ")
    city = input("Ciudad: ")
    direction = input("Direccion de recidencia: ")
    date_N = input("Fecha de Nacimiento: \n ")
#---------------------------Almacenamiento de datos en listas----------------------------#
    usuarios.append({
                      
        'Nombre': name,
        'Correo Electronico': email,
        'Contraseña': password,
        'usuario' : user,
        'numerotel': Num_tel,
        'tipo de identificación': ti_id,
        'numero ID': Num_id,
        'Departamento': departament,
        'Ciudad': city,
        'Dirección': direction,
        'Fecha Nacimiento': date_N,
        'Recordatorios':[]
        })
    print(f"Listo {name.title()} te has registrado exitosamente\n")

registar_usuario()

#-----------------------------------Inicio de sesion-----------------------------#
def inicio_sesion():
    print("Inicia sesión para acceder a las demas opciones: ")
    correo = input("Ingresa tu usuario: ")
    contraseña = input("Ingresa tu Contraseña: ")
#--------------------------------Condiciones de inicio de secion-----------------------#
    usuario_encontrado = False

    for usuario in usuarios :
        if usuario['usuario'] == correo and usuario['Contraseña'] == contraseña:
            print(f"\nBienvenido {usuario['Nombre']}!\n")
            usuario_encontrado = True
        else:
            print("Los datos ingresados son incorrectos.")
        while usuario_encontrado == False:
           correo = input("Ingresa tu usuario: ")
           contraseña = input("Ingresa tu Contraseña: ") 
           if usuario['usuario'] == correo and usuario['Contraseña'] == contraseña:
                print(f"\nBienvenido {usuario['Nombre']}!\n")
                usuario_encontrado = True
           else:
               print("Los datos ingresados son incorrectos")

#---------------------------Menu de opciones para usuarios registrados-------------------------------#   
        while True:
            print("Menú de opciones: \n")
            
            print("1. Registrar un servicio")
            print("2. Mostrar los servicios registrados")
            print("3. Agregar recordatorio" )
            print("4. Editar recordatorio")
            print("5. Eliminar recordatorios")
            print("6. Mostar mi recordatorio")
            print("7. Pagar la factura de mi servicio público") 
            print("8. Calificar un servicio")
            print("9. Calcula cuanto deberas pagar por concepto de servicios publicos al mes.")
            print("10. Reportar una emergencia")
            print("11. Mostrar el perfil del usuario registrado ")
            print("12. Salir\n")
            opcion = int(input("Ingresa el número de la opción que deseas escoger: "))
            
            while opcion >12:
                print("Opción incorrecta")
                opcion = int(input("Ingresa el número de la opción que deseas escoger: "))
#---------------------------------------------Funciones de las opciones del menu-----------------------------------#               
            if opcion == 1:
                print("Registro de servicio\n")
                
                tipservi = input("ingresa el tipo de servicio que quieres registar (Agua, Electricidad, Gas): ")
                
                print("Porfavor llena este formulario para registrar tu servicio\n")
                nomempre = input("Cual es la compañia prestadora del servicio?: ")
                while True:
                        numid = input("Ingresa el número de identificacion del recibo (N° contrato, NIC etc.): ")
                        if numid.isdigit():
                            break
                        else:
                         print("Por favor ingresa solo números.")
                    
                fecorte = input("ingresa la fecha de corte de tu servicio: ")
                    
                lista_servicios.append({
                        'empresa': nomempre,
                        'ID': numid,
                        'fecha_corte': fecorte
                    })
                    
                print("Perfecto, tu servicio quedo registrado.")
             
            
            elif opcion == 2:
                print(f"los servicios guardados y sus datos son: {lista_servicios} ")
                
            elif opcion ==3 :
                print("")
                recordatorio = input("Ingrese el recordatorio: ")
                usuario['Recordatorios'].append(recordatorio)
                print("\nRecordatorio agregado con éxito!\n")
            elif opcion == 4:
                print("")
                if len(usuario['Recordatorios']) > 0:
                        print("Tus recordatorios:")
                        for i, recordatorio in enumerate(usuario['Recordatorios']):
                            print(f"{i + 1}. {recordatorio}")
                        opcion_editar = input("Ingrese el número del recordatorio que desea editar: ")
                        try:
                            opcion_editar = int(opcion_editar)
                            if 1 <= opcion_editar <= len(usuario['Recordatorios']):
                                nuevo_recordatorio = input("Ingrese el nuevo recordatorio: ")
                                usuario['Recordatorios'][opcion_editar - 1] = nuevo_recordatorio
                                print("\nEl recordatorio ha sido editado con éxito.\n")
                            else:
                                print("Opción inválida. Por favor, ingrese un número válido.")
                        except ValueError:
                            print("Opción inválida. Por favor, ingrese un número válido.")
                else:
                        print("No tienes recordatorios para editar.")  
                          
            elif opcion == 5:
                print("")
                if len(usuario['Recordatorios']) > 0:
                        print("Tus recordatorios:")
                        for i, recordatorio in enumerate(usuario['Recordatorios']):
                            print(f"{i + 1}. {recordatorio}")
                        opcion_eliminar = input("Ingrese el número del recordatorio que desea eliminar: ")
                        try:
                            opcion_eliminar = int(opcion_eliminar)
                            if 1 <= opcion_eliminar <= len(usuario['Recordatorios']):
                                recordatorio_eliminado = usuario['Recordatorios'].pop(opcion_eliminar - 1)
                                print(f"El recordatorio '{recordatorio_eliminado}' ha sido eliminado con éxito.")
                            else:
                                print("Opción inválida. Por favor, ingrese un número válido.")
                        except ValueError:
                            print("Opción inválida. Por favor, ingrese un número válido.")
                else:
                        print("No tienes recordatorios para eliminar.")   
                
            elif opcion== 6:
                 print("\nTus recordatorios:")
                 for recordatorio in usuario['Recordatorios']:
                    print(f"- {recordatorio}")
                    
            elif opcion == 7:
                print("Simulador de pago \n")
                
                pago= input("Que servicio deseas pagar? (Agua, Energia o Gas): ")
                valor= float(input("Ingresa el valor a pagar: \n"))
                print("Escoje un metodo de pago: \n")
                print("1. tarjeta debito o credito")
                print("2. Efectivo")
                print("3. Criptomonedas")
                print("4. PayPal")
                
                
                while True:
                        Tipopago= int(input("Ingresa el numero de tu metodo de pago: "))
                        if Tipopago.isdigit():
                            break
                        else:
                         print("Por favor ingresa solo números.")
                while Tipopago > 4:
                    print("ingresaste un opcion invalida, intenta de nuevo.")
                    while True:
                        Tipopago= int(input("Ingresa el numero de tu metodo de pago: "))
                        if Tipopago.isdigit():
                            break
                        else:
                         print("Por favor ingresa solo números.")
                        if Tipopago == 1:
                             titar= input("Ingres el tipo de tarjeta (Debito/Credito): ")
                    
                             Ntar= int(input("Ingresa el número de tu tarjeta:"))
                             cvc= int(input("Ingresa el CVC: "))
                       
                             Fechaex= input("Ingresa la fecha de expedicion de tu tarjeta: ")
                
                    
                print(f"Exelente tu pago con la tarjeta N°{Ntar} fue exitoso!")    
                    
                       
                  
                
            elif opcion == 8:
                servicios = ['agua', 'gas', 'energia']
                calificaciones = {1: 'muy malo', 2: 'malo', 3: 'regular', 4: 'bueno', 5: 'excelente'}

                servicio = input('¿Qué servicio deseas calificar? (agua/gas/energia): ')
                while servicio not in servicios:
                    print('Por favor ingresa un servicio válido.')
                    servicio = input('¿Qué servicio deseas calificar? (agua/gas/energia): ')

                calificacion = int(input('Ingresa tu calificación (1-5): '))
                while calificacion not in calificaciones.keys():
                    print('Por favor ingresa una calificación válida.')
                    calificacion = int(input('Ingresa tu calificación (1-5): '))

                print(f'Has calificado el servicio de {servicio} como {calificaciones[calificacion]}.')

                comentario = input('¿Deseas dejar un comentario para mejorar el servicio? (si/no): ')
                if comentario == 'si':
                    comentario_texto = input('Ingresa tu comentario: ')
                    print(f'Gracias por tu comentario: {comentario_texto}')
                else:
                     print('Ok, muchas gracias por tu mensaje.')


                        
            elif opcion == 9:
                print("Calculadora de pago\n")
                gas = float(input("Ingresa el valor que vas a pagar en tu factura de gas: "))
                energia = float(input("Ingresa el valor que vas a pagar en tu factura de energia: "))
                agua= float(input("ingresa el valor que vas a paragr en tu fcatura de agua: "))
                
                suma = (agua + energia+ agua)
                print(f"Tu saldo a pagar en el mes por concepto de factura de servicios publicos es de: {suma}")
        
            elif opcion == 10:
                    servicios = {
                                 'electricidad': '115',
                                 'agua': '116',
                                 'gas': '164',
                                 'Electricidad': '115',
                                 'Agua': '116',
                                 'Gas': '164'
                                            }
                    servicio = input('¿Qué servicio público desea reportar? (electricidad, agua, gas): ')
                    if servicio in servicios:
                        print(f'Por favor llame al número de emergencia {servicios[servicio]} para reportar un problema con el servicio de {servicio}.')
                    else:
                        print('Lo siento, no tengo información sobre ese servicio.')
            elif opcion == 11:
                print(f"los datos de tu perfil son: {usuario}")
            elif opcion == 12:
               print("MUy bien gracias por usar nuestros servicios, vuelva pronto😁")
               break
            else:
                print("error")
inicio_sesion()            
              




                
            
                    
    
            
            
            
        
         
                
              

    