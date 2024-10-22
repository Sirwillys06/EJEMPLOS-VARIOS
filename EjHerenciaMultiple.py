class Persona:
    def __init__ (self,nombre, edad):
        self.nombre= nombre
        self.edad=edad
    
    def datos(self):
        print(f"Nombre: {self.nombre}, edad: {self.edad}")
        
class Estudiante(Persona):
    def __init__(self, nombre, edad,grado):
        super().__init__(nombre, edad)
        self.grado = grado
        
    def Grado(self):
        print(self.grado)
        

Objeto = Estudiante("Juan", 12, "Sexto")

Objeto.datos()
Objeto.Grado()

