# Importamos tk para la interfaz gráfica
import tkinter as tk
# Importamos la funcion tipo de juego para ir a la seccion de la selección del tipo de juego
from Funciones.TiposDeJuegos.TiposDeJuegos import TiposDeJuegosFrame
# Importamos PIL para mostrar las imagenes como fondo
from PIL import Image, ImageTk
# Importamos la clase ayuda para ir a la seccion de ayuda
from Funciones.Ayuda.Ayuda import AyudaFrame

from Funciones.Idioma.Idioma import idioma_Global

from Funciones.Dificultades.Dificultades import DificultadesFrame

from Funciones.SopaDeLetras.SopaDeLetras import Sopa_De_Letras

#E: La clase menu de inicio hereda tk
#S: Muestra la interfaz del menu de inicio con sus respectivos botones
#R: Solo hereda las propiedades de la interfaz gráfica

# Clase del mnu de inicio que hereda tk
class MenuInicioFrame(tk.Frame):
    def __init__(self,ventana_Padre,controlador):
        super().__init__(ventana_Padre)
        self.controlador = controlador
        self.idioma = idioma_Global
        self.botones_arreglo = {}
        # Llamamos la metodo del menu
        self.Menu()


    # Metodo para mostrar el menu
    def Menu(self):
        # Definimos el tamaño
        self.y = 180
        self.x = 680
        
        
        # Configuramos las filas y columnas de la ventana
        for i in range(5):
            self.rowconfigure(i,weight=1)
            self.columnconfigure(i,weight=1)
        # Creamos un canvas
        self.canvas = tk.Canvas(self,width=800,height=600)
        # Posicionamos el canvas en el medio de la ventana
        self.canvas.grid(row=2,column=2)
        self.crear_Fondo()
        
        self.canvas.create_image(0,0,anchor="nw",image=self.imagen_tk)
        self.botones_Menu_Inicio()

        self.botones_Idioma()

            
    # Metodo que nos dirige a la siguiente seccion para jugar
    def mostrar_Tipos_Juegos(self):
        self.controlador.mostrar_frame("Tipos")

    def botones_Menu_Inicio(self):
        self.botones = [
            "boton_Jugar",
            "boton_Ranking",
            "boton_Ayuda",
            "boton_Salir"
        ]


        for clave_Boton in self.botones:
            texto_boton = self.idioma.get(clave_Boton)
            self.nuevo_Boton = tk.Button(self,width=20,text=texto_boton,font=("Arial",20,"bold"),bg="#000C3D",fg="#49FDA9",
                                     command=lambda texto=texto_boton:self.seccion_Botones(texto))  
            
            self.botones_arreglo[clave_Boton] = self.nuevo_Boton
            self.idioma.registrar_Clave_Boton(self.nuevo_Boton,clave_Boton)
            self.ventana_Botones(self.nuevo_Boton)
            self.y+=100
            

    
    def ventana_Botones(self,boton):
        self.canvas.create_window(240,self.y,anchor="nw",window=boton)

    def seccion_Botones(self,texto_boton):
        if(texto_boton == "Iniciar Juego" or texto_boton == "Start Game"):
            self.mostrar_Tipos_Juegos()
        elif(texto_boton == "Ver Ranking" or texto_boton == "Ranking"):
            print("Ranking")
        elif(texto_boton == "Ayuda" or texto_boton == "Help"):
            self.seccion_Ayuda()
        elif(texto_boton == "Salir" or texto_boton == "Exit"):
            self.salir_Del_Juego()
        

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


    def botones_Idioma(self):
        self.idiomas = [
            "es",
            "en"
        ]

        for idioma in self.idiomas:
            self.nuevo_Boton_Idioma = tk.Button(self,width=2,height=1,bg="#000C3D",fg="#49FDA9",font=("Arial",16,"bold"),
                                                text=idioma,command=lambda i=idioma:self.idioma.cambiar_Idioma(i))
            self.canvas.create_window(self.x,530,window=self.nuevo_Boton_Idioma,anchor="nw")
            self.x += 52



    def seccion_Ayuda(self):
        self.controlador.mostrar_frame("Ayuda")
    
    def salir_Del_Juego(self):
        self.controlador.destroy()



class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Juego")
        self.geometry("800x600")

        self.frame_Contenedor = tk.Frame(self)
        self.frame_Contenedor.pack(fill="both", expand=True)

        self.frames = {}

        self.frames["Menu"] = MenuInicioFrame(self.frame_Contenedor, self)
        self.frames["Tipos"] = TiposDeJuegosFrame(self.frame_Contenedor, self)
        self.frames["Ayuda"] = AyudaFrame(self.frame_Contenedor, self)
        self.frames["Dificultades"] = DificultadesFrame(self.frame_Contenedor, self, "Vacio")
        self.frames["Sopa"] = tk.Frame(self.frame_Contenedor)

        for frame in self.frames.values():
            frame.place(relwidth=1, relheight=1)

        self.mostrar_frame("Menu")

    def actualizar_Dificultad(self, tipo_Juego):
        self.texto_tipo_actual = tipo_Juego
        frame = self.frames["Dificultades"]
        frame.actualizar_Tipo_Juego(tipo_Juego)

    def mostrar_frame(self, nombre):
        self.frames[nombre].tkraise()


    def iniciar_Sopa(self, filas, col, cant, tipo, dificultad):

        # Limpiar el frame anterior de la sopa
        for widget in self.frames["Sopa"].winfo_children():
            widget.destroy()

        # Crear una nueva sopa con tus parámetros
        Sopa = Sopa_De_Letras(
            ventana_Padre=self.frames["Sopa"],
            controlador=self,
            filas=filas,
            col=col,
            cantidad_Palabras=cant,
            texto_Tipo_Juego=tipo,
            texto_dificultad=dificultad
        )

        Sopa.pack(fill="both",expand=True)


        # Mostrarla
        self.mostrar_frame("Sopa")

App().mainloop()