# Importamos la clase de sopa de letras
from Funciones.Dificultades.Dificultades import DificultadesFrame
# Importamos tkinter
import tkinter as tk
from PIL import Image, ImageTk

from Funciones.Idioma.Idioma import idioma_Global

from Funciones.Estadísticas.Ranking import Estadisticas

# Creamos la clase para tipos de juegos que hereda tk
class TiposDeJuegosFrame(tk.Frame):
    def __init__(self,ventana_Padre,controlador):
        super().__init__(ventana_Padre)
        self.controlador = controlador
        self.idioma = idioma_Global
        self.idioma.registrar_Cambio_Idioma(self.actualizar_Idioma)


        # Ejecutamos el metodo abrir_Ventana
        self.abrir_Ventana()



    # Metódo para ejecutar la ventana en bucle
    def abrir_Ventana(self):


        # Configuramos las filas y columnas de la ventana
        for i in range(5):
            self.rowconfigure(i,weight=1)
            self.columnconfigure(i,weight=1)


        # Creamos un canvas para esta seccion
        self.canvas = tk.Canvas(self,width=800,height=600)

        # Posicionamos el canvas en el medio
        self.canvas.grid(row=2,column=2)

        # Definimos la coordenada y 
        self.y = 180
        
        # Llamamos al método para crear y mostrar el fondo
        self.crear_Fondo()

        # Llamamos al método para crear los botones y mostrarlos
        self.crear_Botones()
        
        

    # Método para crear los botones
    def crear_Botones(self):
        # Creamos los botones de cada tipo de juego
        self.botones = [
            ("Tradicional",self.tipo_Seleccionado),
            ("Tradicional_Con_Tiempo",self.tipo_Seleccionado),
            ("Contratiempo",self.tipo_Seleccionado),
            ("Versus",self.tipo_Seleccionado)
        ]

        
        # Realizamos un bucle por cada elemento de la tupla de self.botones 
        for clave_Tipo_Juego,ejecutar_Funcion in self.botones:
            texto_Boton_Tipo_Juego = self.idioma.get(clave_Tipo_Juego)
            # Creamos un boton por cada iteracion
            nuevo_boton = tk.Button(self,text=texto_Boton_Tipo_Juego,font=("Arial",18,"bold"),width=20,
                                    command=lambda texto=texto_Boton_Tipo_Juego:ejecutar_Funcion(texto),bg="#000C3D",fg="#49FDA9")
            self.idioma.registrar_Clave_Boton(nuevo_boton,clave_Tipo_Juego)
            # Creamos y mostramos en la ventana cada boton de la tupla
            self.canvas.create_window(250, self.y,anchor="nw",window=nuevo_boton)
            # Cambiamos el valor de la coordenada "y"
            self.y+=80

        # Creamos el boton regresar
        self.boton_Regresar = tk.Button(self,width=20,text="Regresar",font=("Arial",18,"bold"),bg="#000C3D",fg="#49FDA9",
                                        command=lambda: self.regresar_Tipo_Juego())
        self.idioma.registrar_Clave_Boton(self.boton_Regresar,"Regresar") 
        
        self.canvas.create_window(250,self.y,anchor="nw",window=self.boton_Regresar)


    # Metódo que llamará cada boton al ser presionado    
    def tipo_Seleccionado(self,texto_Tipo_Juego):
        self.controlador.actualizar_Dificultad(texto_Tipo_Juego)
        self.controlador.mostrar_frame("Dificultades")
    
    # Método para crear el fondo de la interfaz
    def crear_Fondo(self):
        # Creamos el fondo
        try:
            ruta = self.idioma.get("Selecciona_Juego")
            self.imagen_Fondo = Image.open(ruta)
            self.imagen_tk = ImageTk.PhotoImage(self.imagen_Fondo)
        except FileNotFoundError as e:
            print(f"Error: no se encontró el archivo de imagen. {e}")
            return
        # Creamos la imagen en el canvas
        self.fondo = self.canvas.create_image(0,0,anchor="nw",image=self.imagen_tk)
        # Tomamos la referencia del fondo de la imagen
        self.canvas.image = self.imagen_tk 

    def actualizar_Idioma(self):
        self.crear_Fondo()
        self.canvas.create_image(0,0,anchor="nw",image=self.imagen_tk)
    
    # Método para regresar al menú de inicio
    def regresar_Tipo_Juego(self):
        self.controlador.mostrar_frame("Menu")
        