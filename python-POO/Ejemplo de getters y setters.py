class Equipo_futbol:
    
    def __init__ (self, name, country, technical_director, games_winners, game_lost):
        self.__name = name
        self.__country = country
        self.__technical_director = technical_director
        self.__games_winners = games_winners
        self.__games_lost = game_lost
        
        

    def get_name (self):
        return self.__name 
    def get_country (self):
        return self.__country
    def get_technical (self):
        return self.__technical_director
    def get_games_winners (self):
        return self.__games_winners
    def get_games_lost (self):
        return self.__games_lost
        
    def set_games_winners(self, games_winners):
            self.__games_winners = games_winners 
            
    def set_games_lost(self, games_lost):
            self.__games_lost = games_lost 
    def print_details (self):
          print(f"el nombre del equipo es {objeto1.get_name()}")  
          print(f"el nombre del equipo es {objeto1.get_country()}") 
                 
objeto1= Equipo_futbol("¡CORRE MARCELA! 🏃‍♀️", "Afganistan", "El juanchito", 0, 12)

print("Informacion del equipo:\n")

def print_details ():
        print(f"El nombre del equipo es:  {objeto1.get_name()}")  
        print(f"El pais es:  {objeto1.get_country()}" )
        print(f"El Director tecnico es: {objeto1.get_technical()}")
        print(f"Los partidos ganados por el equipo {objeto1.get_name()} son de {objeto1.get_games_winners()} partidos ganados")
        print(f"Los partidos perdidos por el equipo {objeto1.get_name()} son de {objeto1.get_games_lost()} partidos perdidos \n")

def menu_options():

    print("Menu de opciones: \n")

    print("1. para imprimir los detalles")
    print("2. para modificar la cantidad de los partidos ganados")
    print("3. para modificar la cantidad de los partidos perdidos")

    print("4. salir")


    opcion = int(input("Ingrese la opcion deseada: "))

    while opcion > 5:
        print("Opcion incorrecta.")
        opcion = int(input("Ingrese la opcion deseada: ")) 
        
    if opcion == 1: 
        print_details()
        
    elif opcion ==2:
        ganan = int(input("Ingresa la cantidad de partidos ganados: "))
        
        objeto1.set_games_winners(ganan)
        print_details()
    elif opcion==3:
       
        pierden = int(input("Ingresa la cantidad de partidos perdidos: "))
        
        objeto1.set_games_lost(pierden)
        print_details()
    elif opcion == 4:
        exit()
    else:
        pass
    menu_options()
menu_options()