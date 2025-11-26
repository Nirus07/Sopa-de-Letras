from email.mime import image
import tkinter as tk
from Funciones.TiposDeJuegos.TiposDeJuegos import Tipos_De_Juegos
from PIL import Image, ImageTk

# Clase del mnu de inicio que hereda tk
class MenuInicio(tk.Tk):
    def __init__(self):
        super().__init__()
        # Llamamos la metodo del menu
        self.Menu()


    # Metodo para mostrar el menu
    def Menu(self):
        # Definimos el tamaño
        self.geometry("800x600")
        
        # Configuramos las filas y columnas de la ventana
        for i in range(5):
            self.rowconfigure(i,weight=1)
            self.columnconfigure(i,weight=1)
        # Creamos un canvas
        self.canvas = tk.Canvas(self,width=800,height=600)
        # Posicionamos el canvas en el medio de la ventana
        self.canvas.grid(row=2,column=2)
        # Creamos el fondo
        try:
            self.imagen_Fondo = Image.open("Imagenes/Inicio/Frame.png")
            self.imagen_tk = ImageTk.PhotoImage(self.imagen_Fondo)
        except FileNotFoundError as e:
            print(f"Error: no se encontró el archivo de imagen. {e}")
        
        self.fondo = self.canvas.create_image(20,20,anchor="nw",image=self.imagen_tk)
        # Creamos el boton para jugar
        self.boton_Jugar = tk.Button(self,width=20,text="Iniciar Juego",font=("Arial",20,"bold"),bg="#000C3D",fg="#49FDA9",activebackground=None,command=lambda:self.mostrar_Tipos_Juegos())
        # Mostramos el boton en la ventana de canvas
        self.canvas.create_window(230,200,anchor="nw",window=self.boton_Jugar)
        # Creamos el boton del ranking
        self.boton_ranking = tk.Button(self,width=20,text="Ranking",font=("Arial",20,"bold"), bg="#000C3D",fg="#49FDA9",activebackground=None),#command=lambda:self.ver_Ranking)
        # Mostramos el boton del ranking en el canvas
        self.canvas.create_window(230,300,anchor="nw",window=self.boton_ranking)
        self.canvas.image = self.imagen_tk 
        self.mainloop()
    
    # Metodo que nos dirige a la siguiente seccion para jugar
    def mostrar_Tipos_Juegos(self):
        self.destroy()
        Tipos_De_Juegos()
    
MenuInicio()