import tkinter as tk
import random

from Funciones.Idioma.Idioma import idioma_Global

from Funciones.Estadísticas.Ranking import Estadisticas

class SopaDeLetras(tk.Frame):
    def __init__(self,ventana_Padre,controlador,filas,col,cantidad_Palabras,texto_Tipo_Juego,texto_dificultad):
        super().__init__(ventana_Padre)
        # Atributo del controlador de los frames
        self.controlador = controlador

        self.filas = filas
        self.col = col
        self.cantidad_Palabras = cantidad_Palabras
        self.texto_Tipo_Juego = texto_Tipo_Juego
        self.texto_dificultad = texto_dificultad
        self.idioma = idioma_Global
        
        #Datos
        self.casillas = []
        self.hitboxes = []
        self.palabra_seleccionada = ""
        self.casillas_seleccionadas = []
        self.arreglo_Letras = []
        self.canvas_info = {}
        self.primero_seleccionado = ""
        self.tamaño = self.filas
        self.size = 30
        self.cords_palabras = []
        self.cords_encontradas = []
        self.color = ""
        self.abecedario = "abcdefghijklmnñopqrstuvwxyz"
        self.primer_x = 0
        self.primer_y = 0
        self.direccion = []
        self.valores_Hex = "ABCDEF0123456789"
        self.minutos = 0
        self.segundos = 0
        self.y_Mostrar = 35


        self.interfaz_Sopa()
        self.tipo_Sopa()
        self.mostrarPalabra()

        
    
    def interfaz_Sopa(self):
        # Bucle para configurar las columnas y filas de la ventana
        for i in range(5):
            self.columnconfigure(i,weight=1)
            self.rowconfigure(i,weight=1)

        # Configuramos el fondo de la ventana
        self.fondo = self.config(bg="#3CC183")
        # Creamos el canvas donde vamos a mostrar el contenido
        self.canvas = tk.Canvas(self,width=self.col*self.size,height=self.filas*self.size)
        self.canvas.grid(column=2,row=2)

        self.canvas_Palabras = tk.Canvas(self,width=200,height=400,bg="#000C3D")
        self.canvas_Palabras.grid(row=2,column=4)
        self.Palabras = self.canvas_Palabras.create_text(100,15,text=self.idioma.get("Palabras"),font=("Arial",20,"bold"),fill="#49FDA9")

        self.Barra_Lateral = tk.Scrollbar(self.canvas_Palabras,orient="vertical",command=self.canvas_Palabras.yview)

        self.Barra_Lateral.bind("<Configure>",lambda e: self.canvas_Palabras.configure(scrollregion=self.canvas_Palabras.bbox("all")))

        self.canvas_Palabras.create_window((0,0),window=self.Barra_Lateral,anchor="nw")
        self.canvas_Palabras.config(yscrollcommand=self.Barra_Lateral.set)
        self.Barra_Lateral.pack(side="right",fill="y")

        
        self.dibujar()
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
            self.fondo_cronometro = tk.Canvas(self,width=100,height=40,bg="#000C3D")
            self.fondo_cronometro.grid(row=2,column=1)
            self.texto_Tiempo = self.fondo_cronometro.create_text(50,20,text=f"{self.minutos}:{self.segundos:02d}",font=("Arial",20,"bold"),fill="#49FDA9")
            if(self.texto_Tipo_Juego != "Tradicional" and self.texto_Tipo_Juego != "Contratiempo"):
                self.incrementar_Cronometro()
            elif(self.texto_Tipo_Juego == "Contratiempo"):
                self.tiempo_del_Temporizador()
            elif(self.texto_Tipo_Juego == "Versus"):
                print("Metodo crea 2 frames, uno para cada jugador")#########################################################################################################################
        self.boton_Abandonar_Juego = tk.Button(self,width=13,text=self.idioma.get("boton_Abandonar"),fg="#49FDA9",bg="#000C3D",font=("Arial",18,"bold"),
                                               command=lambda:self.abandonar_Juego())
        self.idioma.registrar_Clave_Boton(self.boton_Abandonar_Juego,"boton_Abandonar")
        self.boton_Abandonar_Juego.grid(row=3,column=4)

    def mostrarPalabra(self):
        self.palabras_Arreglo = []
        if(self.idioma.get("Palabras") == "Palabras"):
            with open("Palabras_es.txt","r") as archivo:
                self.palabras = archivo.readlines()
                for palabra in range(self.cantidad_Palabras):
                    self.palabras_Arreglo.append(self.palabras[palabra])
        else:
            with open("Palabras_en.txt","r") as archivo:
                self.palabras = archivo.readlines()
                for palabra in range(self.cantidad_Palabras):
                    self.palabras_Arreglo.append(self.palabras[palabra])

        for palabra_Arreglo in self.palabras_Arreglo:
            self.y_Mostrar += 40
            self.palabra_Arreglo = self.canvas_Palabras.create_text(100,self.y_Mostrar,text=palabra_Arreglo,font=("Arial",18))
            self.canvas_Palabras.itemconfig(self.palabra_Arreglo,fill="#49FDA9")
            
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

    

    def reintentar(self):
        self.controlador.iniciar_Sopa(
            self.filas,
            self.col,
            self.cantidad_Palabras,
            self.texto_Tipo_Juego,
            self.texto_dificultad
        )
    
    def abandonar_Juego(self):
        self.ventana_Abandonar = tk.Canvas(self,width=420,height=200,bg="#000C3D")
        self.ventana_Abandonar.grid(row=2,column=2)
        self.texto_Abandonar = self.ventana_Abandonar.create_text(210,35,width=400,text=self.idioma.get("Abandonar"),fill="#49FDA9",font=("Arial",20,"bold"))
        self.boton_Opcion_Si = tk.Button(self,width=10,fg="#000C3D",bg="#49FDA9",text=self.idioma.get("Opcion_Si"),font=("Arial",16,"bold"),
                                         command=lambda: self.controlador.mostrar_frame("Menu"))
        self.boton_Opcion_No = tk.Button(self,width=10,fg="#000C3D",bg="#49FDA9",text=self.idioma.get("Opcion_No"),font=("Arial",16,"bold"),
                                         command=lambda: self.ventana_Abandonar.destroy())
        
        self.ventana_Abandonar.create_window(140,80,window=self.boton_Opcion_Si,anchor="nw")
        self.ventana_Abandonar.create_window(140,140,window=self.boton_Opcion_No,anchor="nw")

    def ventana_Ganador(self):
        # Detener cronómetro / temporizador
        self.detener_tiempo()

        self.canvas_Ganador = tk.Canvas(self,width=600,height=400,bg="#000C3D")
        self.canvas_Ganador.grid(row=2,column=2)

        self.texto_Ganador = self.canvas_Ganador.create_text(
            300,100,
            width=550,
            text="¡Felicidades! Ganaste, introduce tu usuario:",
            font=("Arial",16,"bold"),
            fill="#49FDA9"
        )

        self.Ingresar_Nombre = tk.Entry(self,width=28,bg="#ffffff",fg="#000C3D")
        self.canvas_Ganador.create_window(170,200,window=self.Ingresar_Nombre,anchor="nw")

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


    def enviar_registro(self):
        nombre = self.Ingresar_Nombre.get().strip()

        if nombre == "":
            return  # No registrar si está vacío

        # Registrar en archivo Registro_Juegos.txt
        with open("Funciones/BasesDeDatos/Registro_Juegos.txt", "a", encoding="utf-8") as archivo:
            archivo.write(
                f"{nombre} | {self.minutos}:{self.segundos:02d} | {self.texto_Tipo_Juego} | {self.texto_dificultad}\n"
            )

        # Registrar también en sistema de estadísticas específico
        Estadisticas.registrar_Estadisticas_Todo(
            self,
            nombre,
            self.minutos,
            self.segundos,
            self.texto_Tipo_Juego,
            self.texto_dificultad
        )

        # Volver al menú
        self.controlador.mostrar_frame("Menu")

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
                #print(i)
                for k in range(largo):
                    letra = i[k]
                    for j in self.casillas:
                        if self.canvas_info[j]["x"] == x and self.canvas_info[j]["y"] == y:
                            self.canvas_info[j]["letra"] = letra
                            self.canvas.itemconfig(self.canvas_info[j]["casilla_texto"],text=letra)
                            self.cords_palabras.append([x,y])
                            x += movimiento[0]
                            y += movimiento[1]
                            self.canvas.itemconfig(j, fill="cyan")
                            break
                    #print(cords_palabras)

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
            for i in self.casillas_seleccionadas:
                self.cords_encontradas.append([self.canvas_info[i]["x"],self.canvas_info[i]["y"]])
        self.palabra_seleccionada = ""
        self.casillas_seleccionadas = []
        self.primero_seleccionado = ""
        self.direccion = []
        #print(self.lista_palabras)
        if self.arreglo_Letras == []:
            self.ventana_Ganador()

