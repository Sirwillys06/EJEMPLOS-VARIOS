empresa= input("Ingresa la empresa prestadora del servicio: ")
numero =int(input("Ingresa cuantos meses vas a promediar: "))


    



if numero == 1:
    
    for i in range (1,numero ):
     mes=  float (input(f"ingresa el valor del {i} mes: "))
     
elif  numero == 2:
    
    for i in range (1,numero ):
     mes=  float (input(f"ingresa el valor del {i} mes: "))
     
elif  numero == 3:
    
    for i in range (1,numero ):
     mes=  float (input(f"ingresa el valor del {i} mes: "))
     
elif  numero == 4:
    
    for i in range (1,numero ):
     mes=  float (input(f"ingresa el valor del {i} mes: "))

elif  numero == 5:
    
    for i in range (1,numero ):
     mes=  float (input(f"ingresa el valor del {i} mes: "))
elif  numero == 6:
    
    for i in range (1,numero ):
     mes=  float (input(f"ingresa el valor del {i} mes: "))
else: 
    print("error")
   


#Calcular promedio:

promedio = (mes+i)/numero

print (promedio)