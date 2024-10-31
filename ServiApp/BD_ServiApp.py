import tkinter as tk
import sqlite3
from tkinter import messagebox
import sqlite3

class Ventana_registro:
    
    def __init__(self,ventana):
        self.ventana= ventana
        self.ventana.title ("Registro ServiApp")
        self.ventana.geometry ("1000x1000")
        
        self.label = tk.Label (ventana, text= "Nombre de usuario", )
        self.label.grid(row=4,column=0, sticky='nsew', padx=10, pady=1)
        self.label.pack()
        
    
    
    
    
    
        
        
if __name__ == "__main__":
    ventana = tk.Tk()
    app = Ventana_registro(ventana)
    ventana.mainloop() 