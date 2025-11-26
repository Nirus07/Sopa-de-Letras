# Importamos la interfaz gráfica
import tkinter as tk
import random


class LetraCelda:
    def __init__(self,canvas,fila,col,size,letra):
        super().__init__()
        self.canvas = canvas
        self.fila = fila
        self.col = col
        self.size = size
        self.letra = letra

        x1 =  col * size
        y1 = fila *  size
        x2 = x1 + size
        y2 = y1 + size

        self.rectangulo = canvas.create_rectangle(x1,y1,x2,y2,fill="white",outline="black")

        self.texto = canvas.create_text(x1 + size/2, y1 + size/2,text=letra,font=("Arial",int(size/2)))




class Sopa_De_Letras(tk.Tk):
    def __init__(self,filas,col):
        super().__init__()

        for i in range(5):
            self.columnconfigure(i,weight=1)

        for i in range(5):
            self.rowconfigure(i,weight=1)

        self.tamaño = self.geometry("800x600")
        self.nombre_Ventana = self.title("Sopa de Letras")
        self.fondo = self.config(bg="#49FDA9")

        self.y = 15
        self.filas = filas
        self.col = col
        self.size = 30
        self.abecedario = "ABCDEFGHIJKLMNÑOPQRSTUVXYZ"


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
        

        self.celdas = []
        
        self.mostrarPalabra()
        self.crearTablero()

    def crearTablero(self):
        for fila in range(self.filas):
            fila_celda = []
            for col in range(self.col):
                letra = random.choice(self.abecedario)
                celda =  LetraCelda(self.canvas,fila,col,self.size,letra)
                fila_celda.append(celda)
            
            self.celdas.append(fila_celda)

    def mostrarPalabra(self):
        self.palabras_Arreglo = []
        with open("Palabras.txt","r") as archivo:
            self.palabras = archivo.readlines()
            for arreglo_Palabras in self.palabras:
                palabra_Split = arreglo_Palabras.split()
                self.palabras_Arreglo.append(palabra_Split)
        self.palabras_Restantes()
        
        for palabra_Arreglo in self.palabras_Arreglo:
            self.y += 35
            self.palabra_Arreglo = self.canvas_Palabras.create_text(100,self.y,text=palabra_Arreglo,font=("Arial",18))
            self.canvas_Palabras.itemconfig(self.palabra_Arreglo,fill="#49FDA9")

        
    
    def palabras_Restantes(self):
        self.cantidad_Palabras = len(self.palabras_Arreglo)
            
