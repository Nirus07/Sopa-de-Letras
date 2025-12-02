# Importamos tkinter
import tkinter as tk
# Importamos la biblioteca PIL para utilizarlo con las imagenes
from PIL import Image, ImageTk

from Funciones.Idioma.Idioma import idioma_Global

from Funciones.Rutas import Rutas

import os

# E: Hereda el frame de la ventana principal
# S: Muestra otra seccion donde estarán los botones para cada ranking
# R: No puede modificar la geometria ni el titulo de la ventana
#  Clases del ranking
class Estadisticas(tk.Frame):
    def __init__(self,ventana_Padre,controlador):
        super().__init__(ventana_Padre)
        self.controlador = controlador
        self.idioma = idioma_Global
        self.id = 1
        self.minutos_Menor = 1000
        self.segundos_Menor = 1000

        self.mapa_dificultad = {
            "Principiante": 5,
            "Intermedia": 6,
            "Avanzada": 7
        }
        self.mapa_dificultad_inverso = {
            "5": "Principiante",
            "6": "Intermedia",
            "7": "Avanzada"
        }

        self.ventana_Estadisticas()

    def ventana_Estadisticas(self):

        # Configuramos las filas y columnas de la ventana
        for i in range(5):
            self.rowconfigure(i,weight=1)
            self.columnconfigure(i,weight=1)

        self.y = 160
        


        self.contenido_Estadisticas = tk.Canvas(self,width=800,height=600)
        self.contenido_Estadisticas.grid(row=2,column=2)
        self.crear_Fondo(self.contenido_Estadisticas,"Ranking")
        # Creamos la imagen en el canvas

        self.crear_Botones_Estadisticas()


    def crear_Botones_Estadisticas(self):
        self.botones_Estadisticas_Arreglo = [
            ("Tradicional_Tiempo_Estadisticas",lambda: self.seleccionar_modo("Tradicional")),
            ("Contra_Reloj_Estadisticas",lambda: self.seleccionar_modo("Contratiempo")),
            ("Versus_Estadisticas",lambda: self.seleccionar_modo("Versus")),
            ("Juegos_Generales",self.estadisticas_Todos)
        ]

        for clave_Boton,funcion_Boton in self.botones_Estadisticas_Arreglo:
            texto_Boton = self.idioma.get(clave_Boton)
            self.nuevo_Boton_Estadisticas = tk.Button(self,width=20,bg="#000C3D",fg="#49FDA9",text=texto_Boton, font=("Arial",16,"bold"),
                                                      command=funcion_Boton)
            self.idioma.registrar_Clave_Boton(self.nuevo_Boton_Estadisticas,clave_Boton)
            self.contenido_Estadisticas.create_window(270,self.y,window=self.nuevo_Boton_Estadisticas,anchor="nw")
            self.y+= 90

        self.boton_Regresar_Menu = tk.Button(self,width=20,bg="#000C3D",fg="#49FDA9",text=self.idioma.get("Regresar"),font=("Arial",16,"bold"),
                                             command=lambda:self.volver_Menu())
        self.contenido_Estadisticas.create_window(270,self.y,window=self.boton_Regresar_Menu,anchor="nw")

    def seleccionar_modo(self, modo):
        self.modo_seleccionado = modo
        self.dificultades()

    def dificultades(self):
        self.y = 180

        self.canvas = tk.Canvas(self,width=800,height=600,bg="#000C3D")
        self.canvas.grid(row=2,column=2)
        


        self.botones = ["Principiante","Intermedia","Avanzada"]
        # Creamos un arreglo vació para cada boton presionado
        # Realizamos un for para la tupla de self.botones 
        for clave_Dificultad in self.botones:
            texto_Boton_Dificultad = self.idioma.get(clave_Dificultad)
            # Creamos cada boton con el texto de cada dificultad
            self.boton_Dificultad = tk.Button(self,text=texto_Boton_Dificultad,width=18,bg="#49FDA9",fg="#000C3D",
                                              command=lambda texto=texto_Boton_Dificultad:self.mostrar_ranking(texto),font=("Arial",20,"bold"))
            
            self.idioma.registrar_Clave_Boton(self.boton_Dificultad,clave_Dificultad)
            
            # Creamos la ventana donde mostraremos cada boton
            self.canvas.create_window(260,self.y,anchor="nw",window=self.boton_Dificultad)


            # Modificamos el valor de "y"
            self.y+=80
        

        # Creamos el boton para regresar
        self.boton_Regresar = tk.Button(self,width=18,text="Regresar",font=("Arial",20,"bold"),bg="#49FDA9",fg="#000C3D",
                                        command=lambda: self.volver_Estadisticas())
        
        self.idioma.registrar_Clave_Boton(self.boton_Regresar,"Regresar")
        # Mostramos el boton de regresar en el canvas
        self.canvas.create_window(260,self.y,anchor="nw",window=self.boton_Regresar)

    def obtener_ruta_archivo(self, modo, dificultad):

        if(modo == "Tradicional"):
            if(dificultad == "Principiante"):
                return Rutas.Estadisticas_Tradicional_Tiempo_Principiantes_txt
            if(dificultad == "Intermedia"):
                return Rutas.Estadisticas_Tradicional_Tiempo_Intermedios_txt
            return Rutas.Estadisticas_Tradicional_Avanzados_txt

        if(modo == "Contratiempo"):
            if(dificultad == "Principiante"):
                return Rutas.Estadisticas_Contratiempo_Principiante_txt
            if(dificultad == "Intermedia"):
                return Rutas.Estadisticas_Contratiempo_Intermedio_txt
            return Rutas.Estadisticas_Contratiempo_Avanzado_txt

        if(modo == "Versus"):
            if(dificultad == "Principiante"):
                return Rutas.Estadisticas_Versus_Principiante_txt
            if(dificultad == "Intermedia"):
                return Rutas.Estadisticas_Versus_Intermedio_txt
            return Rutas.Estadisticas_Versus_Avanzado_txt
    
    # # Metodo para mostrar las estadisticas del juego segun la dificultad
    # def seleccion_Dificultad(self,texto_dificultad):
    #     self.estadisticas_Tradicional_Tiempo(texto_dificultad)
    
    def estadisticas_Tradicional_Tiempo(self, dificultad):
        self.canvas = tk.Canvas(self, width=800, height=600, bg="#000C3D")
        self.canvas.grid(row=2, column=2)

        titulo = f"Ranking Tradicional con Tiempo - {dificultad}"
        self.canvas.create_text(400, 40, text=titulo,
                                font=("Arial", 20, "bold"), fill="#49FDA9")

        boton_regresar = tk.Button(
            self, text="Regresar", width=20,
            bg="#49FDA9", fg="#000C3D",
            font=("Arial", 16, "bold"),
            command=self.dificultades
        )
        self.canvas.create_window(400, 550, window=boton_regresar)

        self.mostrar_top3(self.canvas, dificultad)

   
    

    def registrar_Estadisticas_Todo(self,jugador_Nombre,minutos,segundos,tipo_Juego,dificultad):

        with open(Rutas.Registro_Todo,"a", encoding="utf-8") as archivo:
            archivo.write(f"Jugador: {jugador_Nombre}, Tiempo: {minutos}:{segundos}, Tipo de Juego: {tipo_Juego}, Dificultad: {dificultad}\n")
        
        # Inicializamos la ruta con None por defecto
        ruta = None
        # Verificamos si el tipo de modo es tradicional
        print(tipo_Juego)
        if(tipo_Juego == "Tradicional con Tiempo"):
            if(dificultad == "Principiante"):
                ruta = Rutas.Estadisticas_Tradicional_Tiempo_Principiante_txt
            elif(dificultad == "Intermedia"):
                ruta = Rutas.Estadisticas_Tradicional_Tiempo_Intermedio_txt
            elif(dificultad == "Avanzada"):
                ruta = Rutas.Estadisticas_Tradicional_Avanzado_txt

        # Verificamos si el tipo de modo es contratiempo
        elif(tipo_Juego == "Contratiempo"):
            
            if(dificultad == "Principiante"):
                ruta = Rutas.Estadisticas_Contratiempo_Principiante_txt
            elif(dificultad == "Intermedia"):
                ruta = Rutas.Estadisticas_Contratiempo_Intermedio_txt
            elif(dificultad == "Avanzada"):
                ruta = Rutas.Estadisticas_Contratiempo_Avanzado_txt

        # Verificamos si el tipo de modo es modo versus
        elif(tipo_Juego == "Versus"):
            if(dificultad == "Principiante"):
                ruta = Rutas.Estadisticas_Versus_Principiante_txt
            elif(dificultad == "Intermedia"):
                ruta = Rutas.Estadisticas_Versus_Intermedio_txt
            elif(dificultad == "Avanzada"):
                ruta = Rutas.Estadisticas_Versus_Avanzado_txt

        # Si la ruta esta bien, se coloca en el txt del top correspondiente
        if(ruta):
            with open(ruta, "a", encoding="utf-8") as archivo_modo:
                archivo_modo.write(f"Jugador: {jugador_Nombre}, Tiempo: {minutos}:{segundos:02d}\n")
        


    def estadisticas_Tradicional_Tiempo(self):
        self.fondo_estadisticas_Tradicional = tk.Canvas(self,width=800,height=600,bg="#000C3D")
        self.fondo_estadisticas_Tradicional.grid(row=2,column=2)
        self.titulo_Estadisticas_Tradicional = self.fondo_estadisticas_Tradicional.create_text(400,30,text="Estadísticas Tradicional con Tiempo",
                                                                                               font=("Arial",20,"bold"),fill="#49FDA9")

        

        self.boton_Regresar_Estadisticas = tk.Button(self,width=20,bg="#49FDA9",fg="#000C3D",text=self.idioma.get("Regresar"),font=("Arial",16,"bold"),
                                             command=lambda:self.volver_Estadisticas())
        self.contenido_Estadisticas.create_window(270,self.y,window=self.boton_Regresar_Estadisticas,anchor="nw")
        self.crear_Fondo_Jugadores(self.fondo_estadisticas_Tradicional)

        self.leer_Estadisticas("Tradicional con Tiempo",usuario="Rodrigo")


    def crear_Fondo_Jugadores(self,ventana):
        self.y_Jugador = 100
        self.y_Texto = 105
        self.fondo_Estadistica_Jugador_Tradicional = tk.Frame(self,bg="#49FDA9",width=600,height=40)
        ventana.create_window(100,self.y_Jugador,window=self.fondo_Estadistica_Jugador_Tradicional,anchor="nw")
        self.texto = tk.Label(self,text="1. Rodrigo, 10:00, Tradicional con Tiempo, Avanzada",font=("Arial",16,"bold"),fg="#000000",bg="#49FDA9")
        ventana.create_window(100,self.y_Texto,window=self.texto,anchor="nw")

    def estadisticas_Todos(self):
        self.fondo_Estadisticas_Todos = tk.Canvas(self,width=800,height=600,bg="#000C3D")
        self.fondo_Estadisticas_Todos.grid(row=2,column=2)
        self.titulo_Estadisticas_Todos = self.fondo_Estadisticas_Todos.create_text(400,30,text="Estadísticas Generales",
                                                                                               font=("Arial",20,"bold"),fill="#49FDA9")

        

        self.boton_Regresar_Estadisticas = tk.Button(self,width=20,bg="#49FDA9",fg="#000C3D",text=self.idioma.get("Regresar"),font=("Arial",16,"bold"),
                                             command=lambda:self.volver_Estadisticas())
        self.contenido_Estadisticas.create_window(270,self.y,window=self.boton_Regresar_Estadisticas,anchor="nw")
        
        self.crear_Fondo_Jugadores(self.fondo_Estadisticas_Todos)


    def leer_jugadores(self, modo, dificultad):

        archivo = self.obtener_ruta_archivo(modo, dificultad)
        lista_Archivos_Temp = []

        try:
            with open(archivo, "r") as f:
                lineas = f.readlines()
        except FileNotFoundError:
            return []

        for linea in lineas:
            linea_Lectura = linea.strip().split()

            if len(linea_Lectura) < 3:
                continue

            nombre = linea_Lectura[1]

            # MODO TRADICIONAL Y CONTRATIEMPO === tiempo MM:SS
            if modo in ("Tradicional", "Contratiempo"):
                tiempo = linea_Lectura[2]
                if ":" in tiempo:
                    m, s = tiempo.split(":")
                    total = int(m) * 60 + int(s)
                else:
                    continue  
            # MODO VERSUS === puntaje simple
            else:
                tiempo = linea_Lectura[2]
                total = int(tiempo)

            lista_Archivos_Temp.append((nombre, tiempo, total))

        lista_Archivos_Temp.sort(key=lambda x: x[2])
        return lista_Archivos_Temp[:3]


    def mostrar_ranking(self, dificultad):

        self.canvas = tk.Canvas(self, width=800, height=600, bg="#000C3D")
        self.canvas.grid(row=2, column=2)

        titulo = f"Ranking {self.modo_seleccionado} - {dificultad}"
        self.canvas.create_text(400, 40, text=titulo,
                                fill="#49FDA9", font=("Arial", 20, "bold"))

        top_3 = self.leer_jugadores(self.modo_seleccionado, dificultad)

        if(not top_3):
            self.canvas.create_text(400, 250, text="No hay registros",
                                    fill="#49FDA9", font=("Arial", 18, "bold"))
        else:
            y = 160
            pos = 1
            for nombre, tiempo, _ in top_3:
                txt = f"{pos}. {nombre} - {tiempo} - {dificultad}"
                self.canvas.create_text(400, y, text=txt,
                                        fill="#49FDA9", font=("Arial", 18, "bold"))
                y += 60
                pos += 1

        self.boton_regresar = tk.Button(self, text="Regresar",
                                   width=20, bg="#49FDA9", fg="#000C3D",
                                   font=("Arial", 16, "bold"),
                                   command=self.dificultades)
        self.canvas.create_window(400, 550, window=self.boton_regresar)
    
    def estadisticas_Todos(self):

        self.canvas = tk.Canvas(self, width=800, height=600, bg="#000C3D")
        self.canvas.grid(row=2, column=2)

        self.canvas.create_text(400, 40, text="Historial de Juegos",
                                fill="#49FDA9", font=("Arial", 20, "bold"))

        try:
            with open(Rutas.Registro_Todo, "r") as f:
                lineas = f.readlines()
        except FileNotFoundError:
            lineas = []

        y = 120

        if(not lineas):
            self.canvas.create_text(400, 200, text="No hay registros",
                                    fill="#49FDA9", font=("Arial", 18, "bold"))
        else:
            for linea in lineas[-10:]:
                self.canvas.create_text(400, y, text=linea.strip(),
                                        fill="#49FDA9", font=("Arial", 14))
                y += 40

        boton_regresar = tk.Button(self, text="Regresar", width=20,
                                   bg="#49FDA9", fg="#000C3D",
                                   font=("Arial", 16, "bold"),
                                   command=self.ventana_Estadisticas)
        self.canvas.create_window(400, 550, window=boton_regresar)

    # Método para regresar a la pantalla anterior 
    def regresar_Dificultades(self):
        # Regresamos a la selección de tipos de juegos
        self.dificultades()


    def volver_Estadisticas(self):
        self.ventana_Estadisticas()
    
    def volver_Menu(self):
        self.controlador.mostrar_frame("Menu")

    # Metodo para crear el fondo(imagen) del canvas
    def crear_Fondo(self,contenido_Estadisticas,Ranking):
        # Creamos el fondo para la imagen
        try:
            ruta = self.idioma.get(Ranking)
            imagen_Fondo = Image.open(ruta)
            imagen_tk = ImageTk.PhotoImage(imagen_Fondo)
            contenido_Estadisticas.create_image(0,0,anchor="nw",image=imagen_tk)
            contenido_Estadisticas.image = imagen_tk 
        except FileNotFoundError as e:
            print(f"Error: no se encontró el archivo de imagen. {e}")

        # Tomamos la referencia del fondo de la imagen
    
    def crear_Fondo_Consultar_Ranking(self,canvas):
        # Creamos el fondo para la imagen
        try:
            ruta = self.idioma.get("Dificultad")
            self.imagen_Fondo = Image.open(ruta)
            fondo_tk = ImageTk.PhotoImage(self.imagen_Fondo)
            # Tomamos la referencia del fondo de la imagen
            canvas.image = fondo_tk 
            canvas.create_image(0,0,image=fondo_tk,anchor="nw")
        except FileNotFoundError as e:
            print(f"Error: no se encontró el archivo de imagen. {e}")

        




    # def validar_Tiempo(self,minutos=5,segundos=5):
    #     self.arreglo_Letras_Jugadores_Tradicional_Tiempo = []
    #     for jugador_Tradicional in self.jugadores_Arreglo_Tradicional_Tiempo:
    #         letras_Jugador_Tradicional_Tiempo = []
    #         for letras in jugador_Tradicional[2]:
    #             if(letras != ":"):
    #                 letras_Jugador_Tradicional_Tiempo.append(letras)
    #         self.arreglo_Letras_Jugadores_Tradicional_Tiempo.append(letras_Jugador_Tradicional_Tiempo)

    #     self.arreglo_Tiempo_Tradicional = []
    #     for letras_Jugadores in self.arreglo_Letras_Jugadores_Tradicional_Tiempo:
    #         letras_Jugadores[0] = minutos 
    #         segundos = f"{letras_Jugadores[1]}{letras_Jugadores[2]}"

    #         if(minutos < self.minutos_Menor and int(segundos) < self.segundos_Menor):
    #             self.minutos_Menor = minutos
    #             self.segundos_Menor = segundos
    #             self.tiempo_Menor = f"{self.minutos_Menor}:{self.segundos_Menor}"
    #             self.arreglo_Tiempo_Tradicional.append(self.tiempo_Menor)
                

    #         else:
    #             self.tiempo = f"{minutos}:{segundos}"
    #             self.arreglo_Tiempo_Tradicional.append(self.tiempo)

    #     return self.arreglo_Tiempo_Tradicional


    # def leer_Estadisticas(self,tipo_Juego,usuario="Rodrigo",minutos=5,segundos=5,dificultad="Avanzada"):
    #     self.minutos_Menor = 1000
    #     self.segundos_Menor = 1000
    #     if(tipo_Juego != "Tradicional"):
    #         if(tipo_Juego == "Tradicional con Tiempo"):
    #             self.jugadores_Arreglo_Tradicional_Tiempo = []
    #             with open(Rutas.Estadisticas_Tradicional_Tiempo_txt,"r") as archivo:
    #                 Jugadores = archivo.readlines()
    #                 for jugador in Jugadores:
    #                     posicion_Jugador_Tradicional = jugador.strip().split()
    #                     self.jugadores_Arreglo_Tradicional_Tiempo.append(posicion_Jugador_Tradicional)
                    
    #                 self.tiempos_Arreglos = self.validar_Tiempo()
                    
                        

    #         elif(tipo_Juego == "Contratiempo"):
    #             with open(Rutas.Estadisticas_Contratiempo_txt,"r") as archivo:
    #                 Jugadores = archivo.readlines()
    #                 for jugador in Jugadores:
    #                     posicion_Jugador = jugador.strip().split()
    #                     if(posicion_Jugador[1] == "Rodrigo"):
    #                         print("hola")

    #         else:
    #             with open(Rutas.Estadisticas_Versus_txt,"r") as archivo:
    #                 Jugadores = archivo.readlines()
    #                 for jugador in Jugadores:
    #                     posicion_Jugador = jugador.strip().split()
    #                     if(posicion_Jugador[1] == "Rodrigo"):
    #                         print("hola")
    #  def tipo_De_Ranking(self, texto):
    #     if texto == "Tradicional con Tiempo":
    #         self.dificultades()
    #     else:
    #         print("Modo aún no implementado:", texto)