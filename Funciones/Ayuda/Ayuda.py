# Importamos tkinter
import tkinter as tk

from Funciones.Idioma.Idioma import idioma_Global

from PIL import Image,ImageTk

#E: Recibe el atributo self y hereda tk
#S: Debe devolver la ventana donde muestra la información de ayuda
#R: Solo debe mostrar información.

# Creamos la clase Ayuda que hereda tkinter
class AyudaFrame(tk.Frame):
    def __init__(self,ventana_Padre,controlador):
        super().__init__(ventana_Padre)
        self.controlador = controlador
        # Guardamos la clase Idioma en un atributo
        self.idioma = idioma_Global
        self.idioma.registrar_Cambio_Idioma(self.actualizar_Idioma)
        # Definimos el atributo y
        self. y = 150
        self.arreglo_Botones = {}
        # Llamamos al método que crea la seccion de ayuda
        self.crear_Interfaz_Ayuda()
        # Llamamos al método que crea los botones de la seccion de ayuda
        self.crear_Botones_Ayuda()

    
    # Método para crear y configurar la sección de ayuda
    def crear_Interfaz_Ayuda(self):
        # Utilizamos el for para configurar las columnas y filas
        for i in range(5):
            self.rowconfigure(i,weight=1)
            self.columnconfigure(i,weight=1)

        self.configure(bg="#000C3D")
       
        
        # Creamos el canvas donde va ir nuestro contenido
        self.canvas = tk.Canvas(self,width=600,height=500)

        # Posicionamos el canvas en el centro
        self.canvas.grid(row=2,column=2)

        # Creamos el fondo
        self.crear_Fondo_Ayuda()

        
        
        

        

        


    # Método para crear los botones de la sección de ayuda
    def crear_Botones_Ayuda(self):
            # Creamos una tupla con el nombre de los botones y la función que se debe ejecutar
            self.botones = [
                ("boton_Caracteristicas",self.mostrar_Ayuda),
                ("boton_Funcionalidades",self.mostrar_Ayuda),
                ("boton_Reglas",self.mostrar_Ayuda),
            ]
            
            # Realizamos un bucle para crear cada boton con su respectivo texto y función
            for clave_Boton,funcion_Ejecutar in self.botones:
                texto_Boton = self.idioma.get(clave_Boton)
                self.nuevo_Boton = tk.Button(self,width=16,bg="#000C3D",fg="#49FDA9",font=("Arial",20,"bold"),text=texto_Boton,
                                            command=lambda texto=texto_Boton:funcion_Ejecutar(texto))
                
                self.arreglo_Botones[clave_Boton] = self.nuevo_Boton
                self.idioma.registrar_Clave_Boton(self.nuevo_Boton,clave_Boton)
                self.canvas.create_window(165,self.y,window=self.nuevo_Boton,anchor="nw")
                self.y += 80
            
            
            self.boton_Regresar_Inicio = tk.Button(self,width=16,text="Regresar",bg="#000C3D",fg="#49FDA9",font=("Arial",20,"bold"),
                                               command=lambda:self.regresar_Inicio())
            self.canvas.create_window(165,self.y,window=self.boton_Regresar_Inicio,anchor="nw")
            self.arreglo_Botones["Regresar"] = self.boton_Regresar_Inicio
            self.idioma.registrar_Clave_Boton(self.boton_Regresar_Inicio,"Regresar")
        
    
    # Método para la ventana de cada seccion a consultar
    def mostrar_Ventana(self,nombre_Clave):
        self.nueva_Ventana = tk.Canvas(self,width=650,height=500)
        self.nueva_Ventana.grid(row=2,column=2)
        self.crear_Fondo_Consulta()


        self.nuevo_Texto = self.nueva_Ventana.create_text(10,20,width=600,text=self.idioma.get(nombre_Clave),
                                                                              fill="#000C3D",anchor="nw",font=("Arial",16,"bold"))
        
    
    # Método para saber cual sección es la que el usuario o jugador desea consultar
    def mostrar_Ayuda(self,texto_Boton):
        if(texto_Boton == "Características" or texto_Boton == "Characteristics"):
            return self.mostrar_Caracteristicas()
        elif(texto_Boton == "Funcionalidades" or texto_Boton == "Funcionality"):
            return self.mostrar_Funcionalidades()
        elif(texto_Boton == "Reglas del Juego" or texto_Boton == "Game rules"):
            return self.mostrar_Reglas()
        elif(texto_Boton == "Regresar" or texto_Boton == "Back"):
            self.regresar_Inicio()

    
    # Método que me muestra las características del juego que consulta el jugador o usuario
    def mostrar_Caracteristicas(self):
        self.mostrar_Ventana("Caracteristicas")
        
        
        # Utilizamos el método que crea al botón para regresar al aréa de consultar de ayuda
        self.boton_Seccion_Ayuda(self.nueva_Ventana)
        
    
    # Método que me muestra las funcionalidades del juego que consulta el jugador o usuario
    def mostrar_Funcionalidades(self):
        self.mostrar_Ventana("Funcionalidades")
        
        # Utilizamos el método que crea al botón para regresar al aréa de consultar de ayuda
        self.boton_Seccion_Ayuda(self.nueva_Ventana)

    # Método que me muestra las reglas del juego que consulta el jugador o usuario
    def mostrar_Reglas(self):
        self.mostrar_Ventana("Reglas del Juego")
        
        # Utilizamos el método que crea al botón para regresar al aréa de consultar de ayuda
        self.boton_Seccion_Ayuda(self.nueva_Ventana)


    # Creamos el método para crear el boton de regreso al aréa de consultas
    def boton_Seccion_Ayuda(self,ventana):
        self.boton_Regresar_Seccion_Ayuda = tk.Button(self,width=20,text="Regresar",command=lambda:self.regresar_Seccion_Ayuda(),font=("Arial",18,"bold"),
                                        fg="#49FDA9",bg="#000C3D")
        ventana.create_window(190,430,window=self.boton_Regresar_Seccion_Ayuda,anchor="nw")
        self.arreglo_Botones["Regresar"] = self.boton_Regresar_Seccion_Ayuda
        self.idioma.registrar_Clave_Boton(self.boton_Regresar_Seccion_Ayuda,"Regresar")


    # Creamos el método para regresar a la sección de ayuda
    def regresar_Seccion_Ayuda(self):
        self.nueva_Ventana.grid_forget()

    # Creamos el métodos para regresar al menú de inicio
    def regresar_Inicio(self):
        self.controlador.mostrar_frame("Menu")

    def crear_Fondo_Ayuda(self):
        # Creamos el fondo
        try:
            self.fondo_Ayuda = Image.open(self.idioma.get("Ayuda"))
            self.imagen_Ayuda = ImageTk.PhotoImage(self.fondo_Ayuda)
        except FileNotFoundError as e:
            print(f"Error: no se encontró el archivo de imagen. {e}")
        self.canvas.image = self.imagen_Ayuda
        self.canvas.create_image(0,0,anchor="nw",image=self.imagen_Ayuda)

    def crear_Fondo_Consulta(self):
        # Creamos el fondo
        try:
            self.fondo_Consulta = Image.open(self.idioma.get("Consulta"))
            self.imagen_Consulta = ImageTk.PhotoImage(self.fondo_Consulta)
        except FileNotFoundError as e:
            print(f"Error: no se encontró el archivo de imagen. {e}")
        self.nueva_Ventana.image = self.imagen_Consulta
        self.nueva_Ventana.create_image(0,0,anchor="nw",image=self.imagen_Consulta)

    def actualizar_Idioma(self):
        self.crear_Fondo_Ayuda()
        self.canvas.create_image(0,0,anchor="nw",image=self.imagen_Ayuda)
