class Persona:
    
    def __init__(self, nombre, edad, profesion):
        self.nombre = nombre
        self.edad = edad 
        self.profesion = profesion
        
    def hablar(self):
        print("Estoy hablando") 

class Artista:
    
    def __init__(self, habilidad):
        self.habilidad = habilidad
        
    def mostrar_habilidad(self):
        return f"Mi habilidad es {self.habilidad}"

class EmpleadoArtista(Persona, Artista):
    
    def __init__(self, nombre, edad, profesion, habilidad, salario, empresa):
        Persona.__init__(self, nombre, edad, profesion)
        Artista.__init__(self, habilidad)
        self.salario = salario
        self.empresa = empresa
        
    def presentarse(self):
        print(f"Hola, soy {self.nombre}, {self.mostrar_habilidad()} y trabajo en {self.empresa}")

objeto = EmpleadoArtista("Juan", 45, "Programador", "Saltar", 100000, "SpaceX")
objeto.presentarse()
