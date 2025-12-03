import tkinter as tk
import random

from Funciones.Idioma.Idioma import idioma_Global

from Funciones.Estadísticas.Ranking import Estadisticas

from Funciones.Estadísticas.Usuario import Apodo

class SopaDeLetras(tk.Frame):
    def __init__(self,ventana_Padre,controlador,filas,col,cantidad_Palabras,texto_Tipo_Juego,texto_dificultad):
        super().__init__(ventana_Padre)
        # Atributo del controlador de los frames
        self.controlador = controlador
        
        # Atributo que recibe la cantidad de filas
        self.filas = filas
        # Atributo que recibe la cantidad de columnas
        self.col = col
        # Atributo que recibe la cantidad de palabras
        self.cantidad_Palabras = cantidad_Palabras
        # Atributo que recibe el texto tipo de juego
        self.texto_Tipo_Juego = texto_Tipo_Juego
        # Atributo que recibe el texto de la dificultad
        self.texto_dificultad = texto_dificultad
        # Atributo que recibe el idioma del juego
        self.idioma = idioma_Global

        self.jugador_actual = "A"
        self.tiempo_A = [0, 0]   # [minutos, segundos]
        self.tiempo_B = [0, 0]

        self.timer_A = None
        self.timer_B = None
        
        # Creamos el atributo casillas vacio
        self.casillas = []
        # Creamos el atributo hitboxes  vacio
        self.hitboxes = []
        # Creamos el atributo palabra_seleccionada como cadena de texto
        self.palabra_seleccionada = ""
        # Creamos el atributo casillas_seleccionadas vacio
        self.casillas_seleccionadas = []
        # Creamos el atributo arreglo_Letras vacio
        self.arreglo_Letras = []
        # Creamos el atributo canvas_info como diccionario
        self.canvas_info = {}
        # Creamos el atributo primero_seleccionado como cadena de texto
        self.primero_seleccionado = ""
        # Creamos el atributo tamaño que va ser igual a las filas
        self.tamaño = self.filas
        # Creamos el atributo size para cada celda
        self.size = 30
        # Creamos el atributo cords_palabras vacio
        self.cords_palabras = []
        # Creamos el atributo cords_encontradas vacio
        self.cords_encontradas = []
        # Creamos el atributo color como cadena de texto 
        self.color = ""
        # Creamos el atributo abecedario que tendra todas las letras
        self.abecedario = "abcdefghijklmnñopqrstuvwxyz"
        # Creamos el atributo primer_x inicializado en 0
        self.primer_x = 0
        # Creamos el atributo primer_y inicializado en 0
        self.primer_y = 0
        # Creamos el atributo direccion vacio
        self.direccion = []
        # Creamos el atributo valores_Hex con todos los valores de los colores Hex
        self.valores_Hex = "ABCDEF0123456789"
        # Creamos el atributo minutos inicializado en 0
        self.minutos = 0
        # Creamos el atributo segundos inicializado en 0
        self.segundos = 0
        # Creamos el atributo y_Mostrar inicializado en 35
        self.y_Mostrar = 35

        # Llamamos al método de la interfaz de la sopa
        self.interfaz_Sopa()
        # Llamamos al método para interfaz del tipo de sopa
        self.tipo_Sopa()
        # Llamamos al método para mostrar las palabras que se utilizarán en la sopa
        self.mostrarPalabra()

    #E: Recibe el atributo self
    #S: Mostrar la interfaz del juego de la sopa
    #R: Solo recibe ltras
    # Método para crear la interfaz
    def interfaz_Sopa(self):
        # Bucle para configurar las columnas y filas de la ventana
        for i in range(5):
            self.columnconfigure(i,weight=1)
            self.rowconfigure(i,weight=1)

        # Configuramos el fondo de la ventana
        self.fondo = self.config(bg="#3CC183")
        # Creamos el canvas donde vamos a mostrar el contenido
        self.canvas = tk.Canvas(self,width=self.col*self.size,height=self.filas*self.size)
        # Centramos el juego
        self.canvas.grid(column=2,row=2)
        # Creamos el fondo de las palabras
        self.canvas_Palabras = tk.Canvas(self,width=200,height=400,bg="#000C3D")
        # Lo posicionamos a la derecha
        self.canvas_Palabras.grid(row=2,column=4)
        # Creamos el titulo de las palabras
        self.Palabras = self.canvas_Palabras.create_text(100,15,text=self.idioma.get("Palabras"),font=("Arial",20,"bold"),fill="#49FDA9")
        
        # Creamos una barra lateral por si las palabras sobrepasan el alto
        self.Barra_Lateral = tk.Scrollbar(self.canvas_Palabras,orient="vertical",command=self.canvas_Palabras.yview)
        # Configuramos la barra lateral
        self.Barra_Lateral.bind("<Configure>",lambda e: self.canvas_Palabras.configure(scrollregion=self.canvas_Palabras.bbox("all")))
        # Mostramos la barra lateral en el canvas de las palabras
        self.canvas_Palabras.create_window((0,0),window=self.Barra_Lateral,anchor="nw")
        # Configuramos el canvas
        self.canvas_Palabras.config(yscrollcommand=self.Barra_Lateral.set)
        # Lo mostramos para que sea verticalmente
        self.Barra_Lateral.pack(side="right",fill="y")

        # Llamamos al método de dibujar
        self.dibujar()
        # Llamamos la método para colocar las palabras
        self.colocar_palabras()

        #Controles del mouse
        self.canvas.bind("<Button-1>", self.iniciar_seleccion) #  Precionar 
        self.canvas.bind("<B1-Motion>", self.seleccionar) #Manterner precionado
        self.canvas.bind("<ButtonRelease-1>", self.soltar) #Soltar click


    def volver_Inicio(self):
        self.controlador.mostrar_frame("Menu")

    #E: Atributos para crear la visualización del crónometro
    #S: El tiempo del crónometro o un temporizador dependiendo del tipo de juego
    #R: Es llamada solamente una vez
    # Método para crear un crónometro dependiendo de si el tipo es distinto del Tradicional
    def tipo_Sopa(self):
        # Condición para saber si el modo no es el Tradicional
        if(self.texto_Tipo_Juego != "Tradicional"):
            # Creamos el cronometro
            self.fondo_cronometro = tk.Canvas(self,width=100,height=40,bg="#000C3D")
            self.fondo_cronometro.grid(row=2,column=1)
            self.texto_Tiempo = self.fondo_cronometro.create_text(50,20,text=f"{self.minutos}:{self.segundos:02d}",font=("Arial",20,"bold"),fill="#49FDA9")
            # Validamos que tipo de juego no sea contratiempo para crear un cronometro
            if(self.texto_Tipo_Juego == "Tradicional con Tiempo"):
                self.incrementar_Cronometro()
            elif(self.texto_Tipo_Juego == "Contratiempo"):
                self.tiempo_del_Temporizador()
            elif(self.texto_Tipo_Juego == "Versus"):
                self.crear_modo_versus()
    

        self.boton_Abandonar_Juego = tk.Button(self,width=13,text=self.idioma.get("boton_Abandonar"),fg="#49FDA9",bg="#000C3D",font=("Arial",18,"bold"),
                                               command=lambda:self.abandonar_Juego())
        self.idioma.registrar_Clave_Boton(self.boton_Abandonar_Juego,"boton_Abandonar")
        self.boton_Abandonar_Juego.grid(row=3,column=4)
        # Creamos el boton para mostrar la solucion
        self.boton_Mostrar = tk.Button(self,width=13,text=self.idioma.get("boton_Mostrar_Solucion"),fg="#49FDA9",bg="#000C3D",font=("Arial",18,"bold"),
                                               command=lambda:self.mostrar_Solucion())
        self.idioma.registrar_Clave_Boton(self.boton_Mostrar,"boton_Mostrar_Solucion")
        self.boton_Mostrar.grid(row=4,column=4)


    # E: Atributo self
    # S: Las palabras que se utilizarán en la sopa
    # R: Solo puede recibir el atributo self

    # Método que mostrará las palabras en el juego
    def mostrarPalabra(self):
        # Creamos el arrego vacio
        self.palabras_Arreglo = []
        # Validamos si es ingles o español
        if(self.idioma.get("Palabras") == "Palabras"):
            # Utilizamos el archivo txt en español
            with open("Palabras_es.txt","r") as archivo:
                # Obtenemos las lineas de texto
                self.palabras = archivo.readlines()
                # Cada linea va a ser agregado en nuestro arreglo de palabras
                for palabra in range(self.cantidad_Palabras):
                    self.palabras_Arreglo.append(self.palabras[palabra])
        else:
            # Utilizamos el txt en ingles
            with open("Palabras_en.txt","r") as archivo:
                # Obtenemos las lineas de texto
                self.palabras = archivo.readlines()
                # Cada linea va a ser agregado en nuestro arreglo de palabras
                for palabra in range(self.cantidad_Palabras):
                    self.palabras_Arreglo.append(self.palabras[palabra])

        # Cada palabra en nuestro arreglo de palabras va a mostrarse en el canvas de palabras
        for palabra_Arreglo in self.palabras_Arreglo:
            # Modificamos el valor de y_Mostrar para que cada palabra tendrá un distancia de 40 en y
            self.y_Mostrar += 40
            # Agregamos la palabra al canvas
            self.palabra_Arreglo = self.canvas_Palabras.create_text(100,self.y_Mostrar,text=palabra_Arreglo,font=("Arial",18),fill="#49FDA9")

    
    def crear_modo_versus(self):
        # Marco de jugador A
        self.frame_A = tk.Frame(self, bg="#000C3D")
        self.frame_A.grid(row=1, column=2)

        tk.Label(self.frame_A, text="Jugador A",
                font=("Arial", 18, "bold"), fg="#49FDA9", bg="#000C3D").pack()

        self.crono_A = tk.Label(self.frame_A, text="0:00",
                                font=("Arial", 18, "bold"), fg="#49FDA9", bg="#000C3D")
        self.crono_A.pack()

        # Marco de jugador B
        self.frame_B = tk.Frame(self, bg="#000C3D")
        self.frame_B.grid(row=3, column=2)

        tk.Label(self.frame_B, text="Jugador B",
                font=("Arial", 18, "bold"), fg="#49FDA9", bg="#000C3D").pack()

        self.crono_B = tk.Label(self.frame_B, text="0:00",
                                font=("Arial", 18, "bold"), fg="#49FDA9", bg="#000C3D")
        self.crono_B.pack()

        # Inicia jugador A
        self.iniciar_timer_A()

            
    def incrementar_Cronometro(self):
        if(self.segundos == 60):
            self.minutos += 1
            self.segundos = 0
            
        else:
            self.fondo_cronometro.itemconfigure(self.texto_Tiempo,text=(f"{self.minutos}:{self.segundos:02d}"))
            self.segundos += 1
        self.timer_id = self.fondo_cronometro.after(1000,self.incrementar_Cronometro)

    def tiempo_del_Temporizador(self):
        self.segundos = 0
        if(self.texto_dificultad == "Principiante"):
            self.minutos = 1
            self.decrementar_Temporizador()
        elif(self.texto_dificultad == "Intermedia"):
            self.minutos = 2
            self.decrementar_Temporizador()
        elif(self.texto_dificultad == "Avanzada"):
            self.minutos = 3
            self.decrementar_Temporizador()
    
    def ventana_Perder_Juego(self):
        self.fondo_Texto_Perder = tk.Canvas(self,width=400,height=300,bg="#000C3D")

        self.fondo_Texto_Perder.grid(row=2,column=2)

        self.texto_Perder = self.fondo_Texto_Perder.create_text(200,100,fill="#49FDA9",text=self.idioma.get("Perdiste"),font=("Arial",14,"bold"))

        self.boton_Inicio = tk.Button(self.fondo_Texto_Perder,width=18,bg="#49FDA9",fg="#000C3D", command=lambda: self.volver_Inicio(),
                                      text=self.idioma.get("Volver_al_Inicio"))
        
        self.boton_Reintentar = tk.Button(self.fondo_Texto_Perder,width=18,bg="#49FDA9",fg="#000C3D",text=self.idioma.get("Reintentar"),
                                          command=lambda:self.reintentar())

        self.fondo_Texto_Perder.create_window(115,150,window=self.boton_Inicio, anchor="nw")

        self.fondo_Texto_Perder.create_window(115,200,window=self.boton_Reintentar, anchor="nw")

        
    def decrementar_Temporizador(self):
        if(self.minutos == 0 and self.segundos == 0):
            return self.ventana_Perder_Juego()
        elif(self.segundos == 0):
            self.minutos -= 1
            self.segundos = 60
        else:
            self.segundos -= 1
            self.fondo_cronometro.itemconfig(self.texto_Tiempo,text=(f"{self.minutos}:{self.segundos:02d}"))
        
        self.timer_id = self.fondo_cronometro.after(1000,self.decrementar_Temporizador)

    
    # Método que nos permitirá reintentar la sopa
    def reintentar(self):
        self.controlador.iniciar_Sopa(
            self.filas,
            self.col,
            self.cantidad_Palabras,
            self.texto_Tipo_Juego,
            self.texto_dificultad
        )
    
    # Método que mostrará una ventana de si desea abandonar el juego o no
    def abandonar_Juego(self):
        # Llamamos al método para dentener el tiempo
        self.detener_tiempo()
        # Mostramos la ventana de abandonar juego
        self.ventana_Abandonar = tk.Canvas(self,width=420,height=200,bg="#000C3D")
        self.ventana_Abandonar.grid(row=2,column=2)
        self.texto_Abandonar = self.ventana_Abandonar.create_text(210,35,width=400,text=self.idioma.get("Abandonar"),fill="#49FDA9",font=("Arial",20,"bold"))
        self.boton_Opcion_Si = tk.Button(self,width=10,fg="#000C3D",bg="#49FDA9",text=self.idioma.get("Opcion_Si"),font=("Arial",16,"bold"),
                                         command=lambda: self.controlador.mostrar_frame("Menu"))
        self.boton_Opcion_No = tk.Button(self,width=10,fg="#000C3D",bg="#49FDA9",text=self.idioma.get("Opcion_No"),font=("Arial",16,"bold"),
                                         command=lambda: self.no_Abandonar())
        
        self.ventana_Abandonar.create_window(140,80,window=self.boton_Opcion_Si,anchor="nw")
        self.ventana_Abandonar.create_window(140,140,window=self.boton_Opcion_No,anchor="nw")

    # Método para saber si no quiso abandonar el juego y continuar
    def no_Abandonar(self):
        if(self.texto_Tipo_Juego != self.idioma.get("Tradicional")):
            if(self.texto_Tipo_Juego != self.idioma.get("Contratiempo")):
                self.incrementar_Cronometro()
            else:
                self.decrementar_Temporizador()
        self.ventana_Abandonar.destroy()
    
    def iniciar_timer_A(self):
        if self.timer_B: 
            self.after_cancel(self.timer_B)

        self.actualizar_timer_A()

    def iniciar_timer_B(self):
        if self.timer_A:
            self.after_cancel(self.timer_A)

        self.actualizar_timer_B()


    def actualizar_timer_A(self):
        minA, segA = self.tiempo_A
        segA += 1
        if segA == 60:
            minA += 1
            segA = 0
        self.tiempo_A = [minA, segA]

        self.crono_A.config(text=f"{minA}:{segA:02d}")
        self.timer_A = self.after(1000, self.actualizar_timer_A)


    def actualizar_timer_B(self):
        minB, segB = self.tiempo_B
        segB += 1
        if segB == 60:
            minB += 1
            segB = 0
        self.tiempo_B = [minB, segB]

        self.crono_B.config(text=f"{minB}:{segB:02d}")
        self.timer_B = self.after(1000, self.actualizar_timer_B)


    # Método que crear un ventana cuando el jugador gane al sopa
    def ventana_Ganador(self):
        # Detener cronómetro / temporizador
        self.detener_tiempo()
        # Creamos el canvas de la ventana
        self.canvas_Ganador = tk.Canvas(self,width=600,height=400,bg="#000C3D")
        self.canvas_Ganador.grid(row=2,column=2)
        # Mostramos el mensaje de que gano
        self.texto_Ganador = self.canvas_Ganador.create_text(
            300,100,
            width=550,
            text="¡Felicidades! Ganaste, introduce tu usuario:",
            font=("Arial",16,"bold"),
            fill="#49FDA9"
        )
        # Solicitamos que ingrese su usuario
        self.Ingresar_Nombre = tk.Entry(self,width=28,bg="#ffffff",fg="#000C3D")
        self.canvas_Ganador.create_window(170,200,window=self.Ingresar_Nombre,anchor="nw")
        # Creamos el boton para enviar los datos del usuario
        self.boton_Enviar_Ganador = tk.Button(
            self,
            width=20,
            bg="#49FDA9",
            fg="#000C3D",
            font=("Arial",16,"bold"),
            text="Enviar",
            command=lambda: self.enviar_registro()
        )

        self.canvas_Ganador.create_window(150,300,window=self.boton_Enviar_Ganador,anchor="nw")

    # Método para enviar el registro de la persona
    def enviar_registro(self):
        # Obtenemos el usuario ingresado
        nombre = self.Ingresar_Nombre.get().strip()

        # No registrar si está vacío
        if nombre == "":
            return  

        # Si el usuario ya existe, pedir otro
        if Apodo.existe_Apodo(nombre):
            self.canvas_Ganador.create_text(
                300, 250,
                text="Ese usuario ya existe, intenta otro.",
                font=("Arial", 14, "bold"),
                fill="red"
            )
            return

        Apodo.registrar_Apodo(nombre.upper())

        # Registrar estadísticas
        Estadisticas.registrar_Estadisticas_Todo(
            self,
            nombre.upper(),
            self.minutos,
            self.segundos,
            self.texto_Tipo_Juego,
            self.texto_dificultad
        )

        # Volver al menú
        self.controlador.mostrar_frame("Menu")
    
    # Método para 
    def dibujar(self):
        y = 0
        x = 0
        for i in range(self.tamaño):
            x = 0
            for j in range(self.tamaño):
                letra = random.choice(self.abecedario)
                casilla = self.canvas.create_rectangle(x,y,x+26.5,y+26.5, fill="white")
                casilla_texto = self.canvas.create_text(x+13,y+13, text= letra, font=("Arial",12))
                hitbox = self.canvas.create_rectangle(x+5,y+5,x+22,y+22,outline="")
                self.hitboxes.append(hitbox)
                self.casillas.append(casilla)
                self.canvas_info[casilla] = {
                                                        "x": j,
                                                        "y": i,
                                                        "letra": letra,
                                                        "casilla_texto":casilla_texto}
                x += 30
            y += 30


    def detener_tiempo(self):
        try:
            self.fondo_cronometro.after_cancel(self.timer_id)
        except:
            pass

        try:
            if self.timer_A:
                self.after_cancel(self.timer_A)
            if self.timer_B:
                self.after_cancel(self.timer_B)
        except:
            pass



    def seleccionar(self,event):
        objetos = self.canvas.find_overlapping(event.x -2 , event.y -2, event.x +2, event.y +2)
        #Find_overlapping hace que se obtengan todos los objetos en un radio determinado
        #de esos objetos voy a fitrar si se encuentra el rectangulo "hitbox" para en base a eso seleccionar las letras
        hay_hitbox = False
        for i in objetos:
            if i in self.casillas:
                casilla = i
            if i in self.hitboxes:
                hay_hitbox = True
        if hay_hitbox:
            pass
        else:
            return
        

        nuevo_x = self.canvas_info[casilla]["x"]
        nuevo_y = self.canvas_info[casilla]["y"]
        se_mueve = False
        if casilla in self.casillas:
            #print(casilla)
            if casilla not in self.casillas_seleccionadas:
                #Limita la direccion de seleccion
                if self.direccion == []:
                    if nuevo_x > self.primer_x:
                        self.direccion.append("derecha")
                    elif nuevo_x < self.primer_x:
                        self.direccion.append("izquierda")
                    if nuevo_y > self.primer_y:
                        self.direccion.append("abajo")
                    elif nuevo_y < self.primer_y:
                        self.direccion.append("arriba")

                if "arriba" in self.direccion and "derecha" in self.direccion:
                    if nuevo_x == self.primer_x +1 and nuevo_y == self.primer_y -1:
                        self.primer_x = nuevo_x
                        self.primer_y = nuevo_y
                        se_mueve = True
                elif "arriba" in self.direccion and "izquierda" in self.direccion:
                    if nuevo_x == self.primer_x -1 and nuevo_y == self.primer_y -1:
                        self.primer_x = nuevo_x
                        self.primer_y = nuevo_y
                        se_mueve = True

                elif "abajo" in self.direccion and "derecha" in self.direccion:
                    if nuevo_x == self.primer_x +1 and nuevo_y == self.primer_y +1:
                        self.primer_x = nuevo_x
                        self.primer_y = nuevo_y
                        se_mueve = True

                elif "abajo" in self.direccion and "izquierda" in self.direccion:
                    if nuevo_x == self.primer_x -1 and nuevo_y == self.primer_y +1:
                        self.primer_x = nuevo_x
                        self.primer_y = nuevo_y
                        se_mueve = True

                else:
                    if self.direccion == ["abajo"]:
                        if nuevo_y == self.primer_y +1 and nuevo_x == self.primer_x:
                            self.primer_y = nuevo_y
                            se_mueve = True
                    elif self.direccion == ["arriba"]:
                        if nuevo_y == self.primer_y -1 and nuevo_x == self.primer_x:
                            self.primer_y = nuevo_y
                            se_mueve = True
                    elif self.direccion == ["derecha"] :
                        if nuevo_x == self.primer_x +1 and nuevo_y == self.primer_y:
                            self.primer_x = nuevo_x
                            se_mueve = True
                    elif self.direccion == ["izquierda"]:
                        if nuevo_x == self.primer_x -1 and nuevo_y == self.primer_y:
                            self.primer_x = nuevo_x
                            se_mueve = True
                if se_mueve:
                    if [self.canvas_info[casilla]["x"],self.canvas_info[casilla]["y"]] not in self.cords_encontradas:
                        self.canvas.itemconfig(casilla, fill=self.color)
                        self.palabra_seleccionada += self.canvas_info[casilla]["letra"]
                        self.casillas_seleccionadas.append(casilla)

    def colocar_palabras(self):
        if(self.idioma.get("Palabras") == "Palabras"):
            contador = 0
            self.arreglo_Letras_es = self.arreglo_Letras
            with open("Palabras_es.txt","r") as archivo:
                palabras = archivo.readlines()
                for palabra in palabras:
                        if(contador != self.cantidad_Palabras):
                            self.arreglo_Letras_es.append(palabra.strip().upper())
                            contador+=1
                        else:
                            break
        else:
            contador = 0
            self.arreglo_Letras_es = self.arreglo_Letras
            with open("Palabras_en.txt","r") as archivo:
                palabras = archivo.readlines()
                for palabra in palabras:
                        if(contador != self.cantidad_Palabras):
                            self.arreglo_Letras_es.append(palabra.strip().upper())
                            contador+=1
                        else:
                            break

        for i in self.arreglo_Letras_es:
            largo = len(i)
            if largo <= self.tamaño:
                while True:
                    # ,"Arriba_der","Arriba_izq","Abajo_der","Abajo_izq"
                    direccion = random.choice(["derecha","izquierda","arriba","abajo","Arriba_der","Arriba_izq","Abajo_der","Abajo_izq"])
                    x = random.choice(range(self.tamaño))
                    y = random.choice(range(self.tamaño))
                    while True:
                        puede = True
                        while True:
                            movimiento = [0,0]
                            if direccion == "derecha":
                                if largo <= self.tamaño-x-1:
                                    movimiento[0] = 1
                                    break
                                else:
                                    puede = False
                            if direccion == "izquierda":
                                if x - largo >= 0:
                                    movimiento[0] = -1
                                    break
                                else:
                                    puede = False
                            if direccion == "arriba":
                                if y - largo >= 0:
                                    movimiento[1] = -1
                                    break
                                else:
                                    puede = False
                            if direccion == "abajo":
                                if y + largo <= self.tamaño-1:
                                    movimiento[1] = 1
                                    break
                                else:
                                    puede = False

                            
                            if direccion == "Abajo_der":
                                if y + largo <= self.tamaño-1 and largo <= self.tamaño-x-1:
                                    movimiento = [1,1]
                                    break
                                else:
                                    puede = False
                            if direccion == "Abajo_izq":
                                if y + largo <= self.tamaño-1 and x - largo >= 0:
                                    movimiento = [-1,1]
                                    break
                                else:
                                    puede = False
                            if direccion == "Arriba_der":
                                if y - largo >= 0 and largo <= self.tamaño-x-1:
                                    movimiento = [1,-1]
                                    break
                                else:
                                    puede = False
                            if direccion == "Arriba_izq":
                                if y - largo >= 0 and x - largo >= 0:
                                    movimiento = [-1,-1]
                                    break
                                else:
                                    puede = False
                            if not puede:
                                #print("Reintentar: ",i)
                                #print(direccion)
                                #print("x:",x)
                                #print("y:",y)
                                x = random.choice(range(self.tamaño))
                                y = random.choice(range(self.tamaño))
                                
                        x_temporal = x
                        y_temporal = y
                        for r in range(largo+1):
                            if [x_temporal, y_temporal] in self.cords_palabras:
                                puede = False
                            if [x_temporal+movimiento[0],y_temporal+movimiento[1]] in self.cords_palabras:
                                puede = False
                            else:
                                x_temporal+= movimiento[0]
                                y_temporal+= movimiento[1]
                        if puede:
                            break
                        else:
                            x = random.choice(range(self.tamaño))
                            y = random.choice(range(self.tamaño))
                    if puede:
                        break
                for k in range(largo):
                    letra = i[k]
                    for j in self.casillas:
                        if self.canvas_info[j]["x"] == x and self.canvas_info[j]["y"] == y:
                            self.canvas_info[j]["letra"] = letra
                            self.canvas.itemconfig(self.canvas_info[j]["casilla_texto"],text=letra)
                            self.cords_palabras.append([x,y])
                            x += movimiento[0]
                            y += movimiento[1]
                            break
    def mostrar_Solucion(self):
        for casilla in self.casillas:
            x = self.canvas_info[casilla]["x"]
            y = self.canvas_info[casilla]["y"]

            if [x, y] in self.cords_palabras:
                self.canvas.itemconfig(casilla, fill="cyan")

        self.canvas.after(2000,self.ventana_Perder_Juego)

    def iniciar_seleccion(self,event):
        self.color = "#" + "".join(random.choice(self.valores_Hex) for _ in range(6))
        objetos = self.canvas.find_overlapping(event.x -5 , event.y -5,event.x +5, event.y +5)
        hay_hitbox = False
        for i in objetos:
            if i in self.casillas:
                casilla = i
            if i in self.hitboxes:
                hay_hitbox = True
        if hay_hitbox:
            pass
        else:
            return
        if casilla in self.casillas:
            if [self.canvas_info[casilla]["x"],self.canvas_info[casilla]["y"]] not in self.cords_encontradas:
                self.primero_seleccionado = casilla
                self.casillas_seleccionadas += [self.primero_seleccionado]
                self.primer_x = self.canvas_info[self.primero_seleccionado]["x"]
                self.primer_y = self.canvas_info[self.primero_seleccionado]["y"]

                self.canvas.itemconfig(casilla, fill=self.color)
                self.palabra_seleccionada += self.canvas_info[casilla]["letra"]
                self.casillas_seleccionadas.append(casilla)

    #Funcionalidad: Ver si las letras seleccionadas generan una de las palabras
    #E: lista de letras seleccionadas y lista de palabras
    #S: Cambia el color de los cuadros si no esta la palabra y restablece valores a vacios
    def soltar(self,event):
        if self.palabra_seleccionada not in self.arreglo_Letras:
            for i in self.casillas_seleccionadas:
                if [self.canvas_info[i]["x"],self.canvas_info[i]["y"]] not in self.cords_encontradas:
                    self.canvas.itemconfig(i, fill="white")
        else:
            self.arreglo_Letras.remove(self.palabra_seleccionada)
            # CAMBIO DE TURNO EN MODO VERSUS
            if self.texto_Tipo_Juego == "Versus":
                if self.jugador_actual == "A":
                    self.jugador_actual = "B"
                    self.iniciar_timer_B()
                else:
                    self.jugador_actual = "A"
                    self.iniciar_timer_A()

            for i in self.casillas_seleccionadas:
                self.cords_encontradas.append([self.canvas_info[i]["x"],self.canvas_info[i]["y"]])
        self.palabra_seleccionada = ""
        self.casillas_seleccionadas = []
        self.primero_seleccionado = ""
        self.direccion = []
        #print(self.lista_palabras)
        if self.arreglo_Letras == []:
            self.ventana_Ganador()

