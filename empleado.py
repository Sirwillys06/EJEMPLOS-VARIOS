#-----------------Problema N°1------------------#
class Empleado:
#---------------Atributos--------------------#
    def __init__(self, emp_id, emp_name, emp_salary, emp_departament):
        self.emp_id = emp_id
        self.emp_name = emp_name
        self.emp_salary = emp_salary
        self.emp_departament= emp_departament
        
#-----------------Metodos--------------------#  
    
    def calcular_emp_salary(self, hours_worked):
        if hours_worked > 50:
            horas_extras = hours_worked-50
            extra_pay = (horas_extras * (self.emp_salary / 50))
            total_salary= self.emp_salary + extra_pay
            return total_salary
        else:
            return self.emp_salary
    
    def assing_departament(self, nuevo_dpto):
        self.assing_departament=nuevo_dpto
        
    def print_employee_details(self):
        print(f"El Nombre del empleado es: {self.emp_name}")
        print(f"El Id del empleado es: {self.emp_id}")
        print(f"El departamento del empleado es: {self.emp_departament}")
        print(f"EL salario dle empleado es: {self.emp_salary}")
#---------------------------Objetos------------------------------------#       
empleado1 = Empleado("E7876", "ADAMS", 50000, "CONTABILIDAD")
empleado2 = Empleado("E7499","JONES",45000, "INVESTIGACIÓN")
empleado3 = Empleado ("E7900", "MARTIN",50000, "VENTAS" )
empleado4= Empleado("E7698" ,"SMITH", 55000, "OPERACIONES")

print("#-------------------EMPLEADO 1---------------#\n")
empleado1.print_employee_details()
print(" ")
print("#-------------------EMPLEADO 2---------------#\n")
print(" ")
empleado2.print_employee_details()
print(" ")
print("#-------------------EMPLEADO 3---------------#\n")

empleado3.print_employee_details()
print(" ")
print("#-------------------EMPLEADO 4---------------#\n")
empleado4.print_employee_details()
print(" ")
print("#-----------------Calculo de salario de los empleados---------------#")
salario_empleado1 = empleado1.calcular_emp_salary(55)
print(f"El salario total de {empleado1.emp_name} es {salario_empleado1}")
print(" ")
salario_empleado2 = empleado2.calcular_emp_salary(92)
print(f"El salario total de {empleado2.emp_name} es {salario_empleado2}")
print(" ")
salario_empleado3 = empleado3.calcular_emp_salary(63)
print(f"El salario total de {empleado3.emp_name} es {salario_empleado3}")
print(" ")
salario_empleado4 = empleado4.calcular_emp_salary(55)
print(f"El salario total de {empleado4.emp_name} es {salario_empleado4}")



