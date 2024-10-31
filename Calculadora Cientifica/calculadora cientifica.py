
class Calculadora:
    tipo = 'cientifica'
    
    def __init__(self,operando1, operando2 , operacion= None):
        self.operando1= operando1
        self.operando2 = operando2
        if operacion is  None:
            self.operacion=operacion 
            if operacion == '+':
                print(self.suma())
            elif operacion == '-':
                print(self.resta())
            elif operacion == '*':
                print(self.multiplicacion())
            elif operacion == '/':
                print(self.division())
                
    def __srt__(self):
        return str(self.operando1) + self.operacion+str(self.operando2)
    
    def suma(self, operando1 = None, operando2 = None):
        if operando1 is not None and operando2 is not None:
            self.operando1=operando1
            self.operando2=operando2
        return self.operando1 +self.operando2
    def resta (self,operando1 = None, operando2 = None):
        if operando1 is not None and operando2 is not None:
            self.operando1=operando1
            self.operando2=operando2
        return self.operando1 - self.operando2
    def multiplicacion (self,operando1 = None, operando2 = None):
        if operando1 is not None and operando2 is not None:
            self.operando1=operando1
            self.operando2=operando2
        return self.operando1 * self.operando2
    def division (self,operando1 = None, operando2 = None):
        if operando1 is not None and operando2 is not None:
            self.operando1=operando1
            self.operando2=operando2
        
        try:
            return self.operando1 / self.operando2
        except ZeroDivisionError as err:
            print('Gestion de exepciones: ', err)
            return "Valor no definido"
while True:      
    print("-----------------CALCULADORA------------------------\n")      
    print("Ingrese dos numeros")
    num1 = int(input("Primer numero: "))
    num2 = int(input("segundo numero: "))


    operacion = int(input("ingrese 1 para sumar, 2 para restar, 3 para multiplicar, 4 para dividir: "))



    while operacion > 4:
        print("la opcion es incorrecta")
        operacion = int(input("ingrese 1 para sumar, 2 para restar, 3 para multiplicar, 4 para dividir: "))
        
    if operacion == 1:
        objeto1 = Calculadora(num1,num2)
        resultado = objeto1.suma()
        print(f"El resultado de la suma es: {resultado}")
        
    elif operacion == 2:
        objeto2 = Calculadora(num1,num2)
        resultado2= objeto2.resta()
        print(f"El resultado de la resta es: {resultado2}")
        
    elif operacion == 3:
        objeto3 = Calculadora(num1,num2)
        resultado3= objeto3.multiplicacion()
        print(f"El resultado de la multiplicacion es: {resultado3}")
    elif operacion == 4:
        objeto4 = Calculadora(num1,num2)
        reusultado4= objeto4.division()
        print(f"El resultado de la division: {reusultado4}")
    else:
        print("Error")







