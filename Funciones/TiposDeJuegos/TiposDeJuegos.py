# Importamos la clase de sopa de letras
from Funciones.Dificultades.Dificultades import Dificultades
# Importamos tkinter
import tkinter as tk
from PIL import Image, ImageTk

# Creamos la clase para tipos de juegos que hereda tk
class Tipos_De_Juegos(tk.Tk):
    def __init__(self):
        super().__init__()

        # Ejecutamos el metodo abrir_Ventana
        self.abrir_Ventana()


    # Metódo para ejecutar la ventana en bucle
    def abrir_Ventana(self):

        # Configuramos las filas y columnas de la ventana
        for i in range(5):
            self.rowconfigure(i,weight=1)
            self.columnconfigure(i,weight=1)

        # Definimos las medidas
        self.geometry("800x600")

        # Creamos un canvas para esta seccion
        self.canvas = tk.Canvas(self,width=800,height=600)
        self.canvas.grid(row=2,column=2)
        self.crear_Fondo()

        # Creamos los botones de cada tipo de juego
        self.botones = [
            ("Tradicional",self.seleccionar_Dificultad),
            ("Tradicional con Tiempo",self.seleccionar_Dificultad),
            ("Contratiempo",self.seleccionar_Dificultad),
            ("Versus",self.seleccionar_Dificultad)
        ]

        # Definimos la coordenada y 
        self.y = 180
        # Realizamos un bucle por cada elemento de la tupla de self.botones 
        for texto_boton,ejecutar_Funcion in self.botones:
            # Creamos un boton por cada iteracion
            nuevo_boton = tk.Button(self,text=texto_boton,font=("Arial",18,"bold"),width=20,command=lambda:ejecutar_Funcion(),bg="#000C3D",fg="#49FDA9")
            # Creamos y mostramos en la ventana cada boton de la tupla
            self.ventana = self.canvas.create_window(270, self.y,anchor="nw",window=nuevo_boton)
            # Cambiamos el valor de la coordenada "y"
            self.y+=80

        # Creamos el boton regresar
        self.boton_Regresar = tk.Button(self,width=20,text="Regresar",font=("Arial",18,"bold"),bg="#000C3D",fg="#49FDA9",
                                        command=lambda: self.regresar_Tipo_Juego())
        self.canvas.create_window(270,self.y,anchor="nw",window=self.boton_Regresar)
        
        self.mainloop()
        

    # Metódo que llamará cada boton al ser presionado    
    def seleccionar_Dificultad(self):
        self.destroy()
        Dificultades()

    def crear_Fondo(self):
        # Creamos el fondo
        try:
            self.imagen_Fondo = Image.open("Imagenes/Selecciona_Juego/Frame.png")
            self.imagen_tk = ImageTk.PhotoImage(self.imagen_Fondo)
        except FileNotFoundError as e:
            print(f"Error: no se encontró el archivo de imagen. {e}")
        # Creamos la imagen en el canvas
        self.fondo = self.canvas.create_image(20,20,anchor="nw",image=self.imagen_tk)
        # Tomamos la referencia del fondo de la imagen
        self.canvas.image = self.imagen_tk 

    def regresar_Tipo_Juego(self):
        self.destroy()
        import MenuDeInicio
        MenuDeInicio()
        