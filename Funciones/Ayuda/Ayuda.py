# Importamos tkinter
import tkinter as tk


#E: Recibe el atributo self y hereda tk
#S: Debe devolver la ventana donde muestra la información de ayuda
#R: Solo debe mostrar información.

# Creamos la clase Ayuda que hereda tkinter
class Ayuda(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry("800x600")
        self.canvas = tk.Canvas(self,width=800,height=600,bg="#000C3D")
        