# Importamos tkinter
import tkinter as tk
# Importamos la Sopa de Letras
from Funciones.SopaDeLetras.SopaDeLetras import Sopa_De_Letras
# Importamos la biblioteca PIL para mostrar el fondo como imagen
from PIL import Image,ImageTk

# Importamos el archivo de idioma para cambiarlo dinamicamente
from Funciones.Idioma.Idioma import idioma_Global


#E: Hereda las propiedades de tk y el texto del tipo de juego
#S: Devuelve la interfaz donde se va a seleccionar la dificultad del juego con sus respectivos botones
#R: Debe recibir el texto del tipo de juego

# Creamos la clase que maneja las dificultades
class DificultadesFrame(tk.Frame):
    def __init__(self,ventana_Padre,controlador,texto_Tipo_Juego):
        super().__init__(ventana_Padre)
        self.controlador = controlador
        self.texto_Tipo_Juego = texto_Tipo_Juego
        self.idioma = idioma_Global
        self.abrir_Ventana()


    def abrir_Ventana(self):
        self.y = 180

        for i in range(5):
            self.rowconfigure(i,weight=1)
            self.columnconfigure(i,weight=1)

        self.canvas = tk.Canvas(self,width=800,height=600)
        self.canvas.grid(row=2,column=2)
        self.crear_Fondo()

        self.botones = [
            ("Principiante",self.seleccion_Dificultad),
            ("Intermedia",self.seleccion_Dificultad),
            ("Avanzada",self.seleccion_Dificultad)
        ]
        # Creamos un arreglo vació para cada boton presionado
        self.botones_Dificultades = []
        # Realizamos un for para la tupla de self.botones 
        for clave_Dificultad,metodo_Dificultad in self.botones:
            texto_Boton_Dificultad = self.idioma.get(clave_Dificultad)
            # Creamos cada boton con el texto de cada dificultad
            self.boton_Dificultad = tk.Button(self,text=texto_Boton_Dificultad,width=18,bg="#000C3D",fg="#49FDA9",
                                              command=lambda texto=texto_Boton_Dificultad: metodo_Dificultad(texto),font=("Arial",20,"bold"))
            
            self.idioma.registrar_Clave_Boton(self.boton_Dificultad,clave_Dificultad)
            
            # Creamos la ventana donde mostraremos cada boton
            self.canvas.create_window(240,self.y,anchor="nw",window=self.boton_Dificultad)

            # Modificamos el valor de "y"
            self.y+=80

            # Añadimos cada boton a nuestro arreglo
            self.botones_Dificultades.append(self.boton_Dificultad)

        # Creamos el boton para regresar
        self.boton_Regresar = tk.Button(self,width=18,text="Regresar",font=("Arial",20,"bold"),bg="#000C3D",fg="#49FDA9",
                                        command=lambda: self.regresar_Tipo_Juego())
        
        self.idioma.registrar_Clave_Boton(self.boton_Regresar,"Regresar")
        # Mostramos el boton de regresar en el canvas
        self.canvas.create_window(240,self.y,anchor="nw",window=self.boton_Regresar)


    # Metodo para crear el fondo(imagen) del canvas
    def crear_Fondo(self):
        # Creamos el fondo para la imagen
        try:
            self.imagen_Fondo = Image.open("Imagenes/Dificultad/Frame.png")
            self.imagen_tk = ImageTk.PhotoImage(self.imagen_Fondo)
        except FileNotFoundError as e:
            print(f"Error: no se encontró el archivo de imagen. {e}")

        # Creamos la imagen en el canvas
        self.fondo = self.canvas.create_image(0,0,anchor="nw",image=self.imagen_tk)
        # Tomamos la referencia del fondo de la imagen
        self.canvas.image = self.imagen_tk 


    def actualizar_Tipo_Juego(self, texto):
        self.texto_Tipo_Juego = texto

    
    # Metodo para iniciar el juego segun la dificultad
    def seleccion_Dificultad(self,texto_dificultad):
        if(texto_dificultad == "Principiante"):
            self.controlador.iniciar_Sopa(filas=12,col=12,cant=6,tipo=self.texto_Tipo_Juego,dificultad=texto_dificultad)
        elif(texto_dificultad == "Intermedia"):
            self.controlador.iniciar_Sopa(filas=20,col=20,cant=10,tipo=self.texto_Tipo_Juego,dificultad=texto_dificultad)
        elif(texto_dificultad == "Avanzada"):
            self.controlador.iniciar_Sopa(filas=28,col=28,cant=14,tipo=self.texto_Tipo_Juego,dificultad=texto_dificultad)

    # Método para regresar a la pantalla anterior 
    def regresar_Tipo_Juego(self):
        # Regresamos a la selección de tipos de juegos
        self.controlador.mostrar_frame("Tipos")