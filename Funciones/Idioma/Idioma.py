from Funciones.BasesDeDatos.Textos_Diccionario import Textos

# Creamos la clase Idioma
class Idioma():
    def __init__(self,idioma="es"):
        self.idioma = idioma
        self.textos = Textos[idioma]

        self.arreglo_Elementos = []
        self.callbacks = []

    
    def cambiar_Idioma(self,idioma):
        self.idioma = idioma
        self.textos = Textos[idioma]

        for elemento, clave in self.arreglo_Elementos:
            elemento.config(text=self.get(clave))

        # Para que los frames se puedan actualizar al cambiar el idioma
        for callback in self.callbacks:
            callback()
    
    def get(self,clave):
        return self.textos.get(clave, f"{clave}")
    
    def registrar_Cambio_Idioma(self,cambio):
        self.callbacks.append(cambio)
    
    
    def registrar_Clave_Boton(self,elemento,clave):
        self.arreglo_Elementos.append((elemento,clave))
        elemento.config(text=self.get(clave))
    

idioma_Global = Idioma()