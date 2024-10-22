import sqlite3

class Cuenta:
    def __init__(self):
        self.conexion_db = sqlite3.connect("cuenta.db")
        self.inicializar_db()

    def inicializar_db(self):
        cursor = self.conexion_db.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS cuenta (saldo REAL)")
        cursor.execute("INSERT INTO cuenta (saldo) VALUES (0) ON CONFLICT DO NOTHING")
        self.conexion_db.commit()

        cursor.execute("SELECT saldo FROM cuenta")
        resultado = cursor.fetchone()
        self.saldo = resultado[0] if resultado else 0

    def actualizar_saldo(self):
        cursor = self.conexion_db.cursor()
        cursor.execute("UPDATE cuenta SET saldo = ?", (self.saldo,))
        self.conexion_db.commit()

    def ingresar(self, cantidad):
        self.saldo += cantidad
        self.actualizar_saldo()
        print(f"Se han ingresado {cantidad} pesos. Saldo actual: {self.saldo} pesos")

    def retirar(self, cantidad):
        if cantidad > self.saldo:
            print("Error: Saldo insuficiente.")
        else:
            self.saldo -= cantidad
            self.actualizar_saldo()
            print(f"Se han retirado {cantidad} pesos. Saldo actual: {self.saldo}pesos")

    def pagar(self, cantidad):
        if cantidad > self.saldo:
            print("Error: Saldo insuficiente para realizar el pago.")
        else:
            self.saldo -= cantidad
            self.actualizar_saldo()
            print(f"Se ha realizado un pago de {cantidad} unidades. Saldo actual: {self.saldo}")

    def ver_saldo(self):
        print(f"Saldo actual: {self.saldo}")



cuenta_usuario = Cuenta()

saldo = float(input("Cuánto saldo deseas ingresar: "))
cuenta_usuario.ingresar(saldo)

cuenta_usuario.conexion_db.close()  
