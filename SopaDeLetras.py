# Importamos la interfaz gráfica
import tkinter as tk

class SopaDeLetras(tk.Tk):
    def __init__(self):
        super().__init__()

        self.frame = tk.Frame(self,width=100,height=50)


        self.tamaño = self.geometry("800x600")
        self.nombre_Ventana = self.title("Sopa de Letras")
        self.boton = tk.Button

        # Se inicia el juego
        self.Iniciar_Juego()

    def Iniciar_Juego(self):
        self.mainloop()


SopaDeLetras()