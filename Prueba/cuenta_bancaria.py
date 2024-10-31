class Cuenta_Bancaria: 
    
    def __init__(self, numero_cuenta, saldo, fecha_apertura, nombre_cliente):
        self.numero_cuenta = numero_cuenta
        self.saldo = saldo
        self.fecha_apertura= fecha_apertura
        self.nombre_cliente = nombre_cliente
        
    def retirar(self):
        valor = float(input("Ingrese el valor a retirar: "))
        while valor > self.saldo:
            print("El valor ingresado supera el valor en tu cuenta")
            valor = float(input("Ingrese el valor a retirar: "))
        if valor > 0:
            descuento = self.saldo-valor
            print (f"Usted ha retirado de la cuenta N° {self.numero_cuenta} a nombre de {self.nombre_cliente} un valor de {valor} y quedo un saldo de {descuento}")
        else:
            print(f"No se hicieron retiros de la cuenta {self.numero_cuenta}")
          
    def depositar(self):
        depo = float(input("Ingrese un valor a depositar:  "))
        if depo > 0:
            saldo = depo + self.saldo
            print (f"Usted ha depositado en la cuneta N° {self.numero_cuenta} a nombre de {self.nombre_cliente} un valor de {depo} y quedo un saldo de {saldo}") 
        else:
            print(f"No se hizo deposito en la cuenta N° {self.numero_cuenta}")
    
    


print("BIENVENIDO A BANCO DE CARTAGENA")

nombre = input ("ingrese su nombre: ")
numerodecuenta = input ("ingrese su numero de cuenta: ")
fapertura = input ("ingrese su fecha de apertura: ")
saldoinicial= float (input ("ingrese su saldo inicial: "))
print(" ")
print ("escoja su metodo de deposito\n")
print ("1. efectivo")
print ("2. Transferencia")
print ("3. PSE")
metodepo = input(" ingrese la opcion que corresponda a su metodo de retiro: ")

objeto1 = Cuenta_Bancaria(numerodecuenta, saldoinicial,fapertura, nombre)

def opciones():
    opcion = int(input("ingrese 1 para retirar, ingrese 2 para depositar, ingrese 3 para salir: "))
        
    while opcion > 3:
        print("opcion incorrecta, intente nuevamente.")
        opcion = int(input("ingrese 1 para retirar, ingrese 2 para depositar: "))
    
    
    if opcion == 1:
        objeto1.retirar()
    elif opcion ==2:
        objeto1.depositar()
    elif opcion == 3:
        exit()
    opciones()
opciones()


