# Importamos tk para la interfaz gráfica
import tkinter as tk
# Importamos la funcion tipo de juego para ir a la seccion de la selección del tipo de juego
from Funciones.TiposDeJuegos.TiposDeJuegos import Tipos_De_Juegos
# Importamos PIL para mostrar las imagenes como fondo
from PIL import Image, ImageTk

#E: La clase menu de inicio hereda tk
#S: Muestra la interfaz del menu de inicio con sus respectivos botones
#R: Solo hereda las propiedades de la interfaz gráfica

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
        self.crear_Fondo()
        
        self.fondo = self.canvas.create_image(20,20,anchor="nw",image=self.imagen_tk)
        self.botones_Menu_Inicio()
        
        self.mainloop()
    
    # Metodo que nos dirige a la siguiente seccion para jugar
    def mostrar_Tipos_Juegos(self):
        self.destroy()
        Tipos_De_Juegos()

    def botones_Menu_Inicio(self):
        # Creamos el boton para jugar
        self.boton_Jugar = tk.Button(self,width=20,text="Iniciar Juego",font=("Arial",20,"bold"),bg="#000C3D",fg="#49FDA9",
                                     command=lambda:self.mostrar_Tipos_Juegos())
        
        # Creamos el boton del ranking
        self.boton_Ranking = tk.Button(self,width=20,text="Ver Ranking",font=("Arial",20,"bold"), bg="#000C3D",fg="#49FDA9",),
        #command=lambda:self.ver_Ranking)

        # Creamos el boton de ayuda
        self.boton_Ayuda = tk.Button(self,width=20,text="Ayuda",font=("Arial",20,"bold"), bg="#000C3D",fg="#49FDA9",)#command=lambda: 

        # Creamos el boton para salir
        self.boton_Salir = tk.Button(self,width=20,text="Salir",font=("Arial",20,"bold"), bg="#000C3D",fg="#49FDA9",command=lambda: self.salir_Del_Juego())
        # Mostramos el de iniciar juego en la ventana del canvas
        self.canvas.create_window(240,200,anchor="nw",window=self.boton_Jugar)
        # Mostramos el boton del ranking en el canvas
        self.canvas.create_window(240,300,anchor="nw",window=self.boton_Ranking)
        # Mostramos el boton de ayuda en la ventana del canvas
        self.canvas.create_window(240,400,anchor="nw",window=self.boton_Ayuda)
        # Mostramos el boton de salir en la ventana del canvas
        self.canvas.create_window(240,500,anchor="nw",window=self.boton_Salir)
        

    #E: Recibe el atributo self
    #S: Devuelve la imagen como fondo de la interfaz
    #R: Solo recibe el atributo self 
    # Creamos el método para mostrar el fondo como imagem
    def crear_Fondo(self):
        # Creamos el fondo
        try:
            self.imagen_Fondo = Image.open("Imagenes/Inicio/Frame.png")
            self.imagen_tk = ImageTk.PhotoImage(self.imagen_Fondo)
        except FileNotFoundError as e:
            print(f"Error: no se encontró el archivo de imagen. {e}")
        self.canvas.image = self.imagen_tk 
    
    def salir_Del_Juego(self):
        self.destroy()
    
MenuInicio()