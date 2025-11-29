# Importamos la interfaz gráfica
import tkinter as tk
# Importamos la biblioteca random
import random


class LetraCelda:
    def __init__(self,canvas,fila,col,size,letra):
        super().__init__()
        self.canvas = canvas
        self.fila = fila
        self.col = col
        self.size = size
        self.letra = letra
        self.seleccionada = False
        

        x1 =  col * size
        y1 = fila *  size
        x2 = x1 + size
        y2 = y1 + size
        


        self.rectangulo = canvas.create_rectangle(x1,y1,x2,y2,fill="white",outline="black")

        self.texto = canvas.create_text(x1 + size/2, y1 + size/2,text=letra,font=("Arial",int(size/2)))

    
    def seleccionar(self):
        self.seleccionada = not self.seleccionada

        if(self.seleccionada):
            self.canvas.itemconfig(self.rectangulo, fill="yellow")
        else:
            self.canvas.itemconfig(self.rectangulo, fill="white")
    



#E: Recibe como herencia las propiedades de tk
#S: La sección del juego de la sopa de letras en la cual se podrán encontrar las palabras
#R: Solo debe crear la interfaz visual del juego
# Clase de la sopa de letras que hereda Tk
class Sopa_De_Letras(tk.Tk):
    def __init__(self,filas,col,cantidad_Palabras,texto_Tipo_Juego,texto_dificultad):
        super().__init__()

        # Bucle para configurar las columnas y filas de la ventana
        for i in range(5):
            self.columnconfigure(i,weight=1)
            self.rowconfigure(i,weight=1)

        # Definimos las medidas de la ventana del juego
        self.tamaño = self.geometry("800x600")
        # Definimos el nombre de la ventana
        self.nombre_Ventana = self.title("Sopa de Letras")
        # Configuramos el fondo de la ventana
        self.fondo = self.config(bg="#3CC183")

        # Creamos el atributo "y", inicializandolo
        self.y = 35
        # Creamos la propiedad self.filas que recibe la cantidad de filas
        self.filas = filas
        # Creamos la propiedad self.col que recibe la cantidad de columnas
        self.col = col
        self.size = 30
        self.celdas = []
        # Creamos la propiedad cantidad_Palabras que recibe la cantidad de palabras
        self.cantidad_Palabras = cantidad_Palabras
        self.abecedario = "ABCDEFGHIJKLMNÑOPQRSTUVXYZ"
        # Creamos la propiedad self.texto_Tipo_Juego que recibe el texto con el tipo de juego que se va a jugar
        self.texto_Tipo_Juego = texto_Tipo_Juego
        # Creamos las propiedades minutos y segundos para el crónometro
        self.minutos = 0
        self.segundos = 0
        # Creamos la propiedad que recibe el texto de las dificultades para el modo contratiempo
        self.texto_dificultad = texto_dificultad


        self.canvas = tk.Canvas(self,width=self.col*self.size,height=self.filas*self.size)
        self.canvas.grid(column=2,row=2)

        self.canvas_Palabras = tk.Canvas(self,width=200,height=400,bg="#000C3D")
        self.canvas_Palabras.grid(row=2,column=4)
        self.Palabras = self.canvas_Palabras.create_text(100,15,text="Palabras: ",font=("Arial",20,"bold"))
        self.canvas_Palabras.itemconfig(self.Palabras,fill="#49FDA9")

        self.Barra_Lateral = tk.Scrollbar(self.canvas_Palabras,orient="vertical",command=self.canvas_Palabras.yview)

        self.Barra_Lateral.bind("<Configure>",lambda e: self.canvas_Palabras.configure(scrollregion=self.canvas_Palabras.bbox("all")))

        self.canvas_Palabras.create_window((0,0),window=self.Barra_Lateral,anchor="nw")
        self.canvas_Palabras.config(yscrollcommand=self.Barra_Lateral.set)
        self.Barra_Lateral.pack(side="right",fill="y")

        

        
        self.tipo_Sopa()
        self.mostrarPalabra()
        self.crearTablero()
        self.canvas.bind("<Button-1>", self.click_celda)

    def crearTablero(self):
        for fila in range(self.filas):
            fila_celda = []
            for col in range(self.col):
                letra = random.choice(self.abecedario)
                celda =  LetraCelda(self.canvas,fila,col,self.size,letra)
                fila_celda.append(celda)
            
            self.celdas.append(fila_celda)
        


    def click_celda(self,evento):
        fila = evento.y // self.size
        col = evento.x // self.size

        if not(0 <= fila < self.filas and 0 <= col < self.col):
            return
        
        celda = self.celdas[fila][col]
        celda.seleccionar()


    #E: Atributo de palabras restantes
    #S: Mostramos en la interfaz la cantidad de palabras a encontrar en la sopa
    #R: Solamente debe crear la parte de las palabras escogidas aleatoriamente en el txt

    # Creamos el método para mostrar las palabras en la ventana de canvas
    def mostrarPalabra(self):
        self.palabras_Arreglo = []
        with open("Palabras.txt","r") as archivo:
            self.palabras = archivo.readlines()
            for palabra in range(self.cantidad_Palabras):
                self.palabras_Arreglo.append(self.palabras[palabra])
                
        # Dentro de nuestro método mostrarPalabras llamamos al método para saber las palabras restantes
        self.palabras_Restantes()
        # Bucle para cambiar el color de fondo de la ventana de palabras
        for palabra_Arreglo in self.palabras_Arreglo:
            self.y += 40
            self.palabra_Arreglo = self.canvas_Palabras.create_text(100,self.y,text=palabra_Arreglo,font=("Arial",18))
            self.canvas_Palabras.itemconfig(self.palabra_Arreglo,fill="#49FDA9")

    #E: El atributo de las palabras del arreglo
    #S: Devuelve la cantidad de palabras que se deben encontrar en la sopa
    #R: Debe recibir solamente números enteros
    # Creamos el método para saber la cantidad de palabras restantes    
    def palabras_Restantes(self):
        self.cantidad_Palabras = len(self.palabras_Arreglo)
    
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
            
    def incrementar_Cronometro(self):
        if(self.segundos == 60):
            self.minutos += 1
            self.segundos = 0
            
        else:
            self.fondo_cronometro.itemconfigure(self.texto_Tiempo,text=(f"{self.minutos}:{self.segundos:02d}"))
            self.segundos += 1
        self.fondo_cronometro.after(1000,self.incrementar_Cronometro)

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
        self.texto_Perder = self.fondo_Texto_Perder.create_text(200,100,fill="#49FDA9",text="Se te acabo el tiempo, has perdido.",font=("Arial",14,"bold"))
        self.boton_Inicio = tk.Button(self.fondo_Texto_Perder,width=18,bg="#49FDA9",fg="#000C3D", command=lambda: self.volver_Inicio(),text="Volver al Inicio")
        self.boton_Reintentar = tk.Button(self.fondo_Texto_Perder,width=18,bg="#49FDA9",fg="#000C3D",text="Reintentar")
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
        
        self.fondo_cronometro.after(1000,self.decrementar_Temporizador)

    def volver_Inicio(self):
        self.destroy()
        import MenuDeInicio
        MenuDeInicio
    