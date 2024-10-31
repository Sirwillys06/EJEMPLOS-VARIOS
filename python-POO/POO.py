class Estudiante:
    
    def __init__(self, Nombre, Edad, Grado):
        self.Nombre= Nombre
        self.Edad = Edad
        self.Grado = Grado
        
        
    def estudiar(self):
        print(f"El estudiante {self.Nombre} esta estudiando")
    
    def datos(self):
        print("Datados del estudiante: \n")
        
        print(f"Nombre: {self.Nombre}")
        print(f"Edad: {self.Edad}")
        print(f"Grado: {self.Grado}")
            
            


Nombre= input("Ingrese el nombre del estudiante: ")
Edad = int(input("Ingrese la edad del estudiante: "))
Grado = input("Ingrese el grado que esta cursando el estudiante: ")



Student = Estudiante(Nombre, Edad, Grado)
Student.datos()

while True:
    Study = input()

    if (Study.lower == "estudiar"):
        Student.estudiar()


