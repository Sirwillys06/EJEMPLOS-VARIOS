# class Persona:
    
#     def __init__ (self, nombre, edad):
#         self._nombre = nombre
#         self._edad = edad
        
        
#     def get_nombre(self):
#         return self._nombre
    
#     def get_edad(self):
#         return self._edad
    
#     def set_nombre(self, new_name):
#         self._nombre=new_name
    
#     def set_edad(self, new_edad):
#         self._edad= new_edad

# Sir= Persona("WIllys", 18)

# nombre = Sir.get_nombre()

# print(nombre)


# Sir.set_nombre("Pedro")
# nombre = Sir.get_nombre()

# print(nombre)


#Encapsulamiento con Decoradores:
#Property es un depcorador el cual se utiliza para convertir una funcion o metodo en una propiedad.
class Persona:
    
     def __init__ (self, nombre, edad):
         self._nombre = nombre
         self._edad = edad
        
     @property   
     def nombre(self):
         return self._nombre
     @property
     def edad(self):
         return self._edad
     
     @nombre.setter
     def nombre(self, new_name):
         self._nombre=new_name
     @nombre.setter
     def edad(self, new_edad):
         self._edad= new_edad


Sir= Persona("WIllys", 18)

nombre = Sir.nombre
print(nombre)

Sir.nombre= "Juan"
nombre=Sir.nombre
print(nombre)

