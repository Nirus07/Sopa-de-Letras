from Funciones.BasesDeDatos.Textos_Diccionario import Textos

# Creamos la clase Idioma
class Idioma():
    def __init__(self,idioma="es"):
        self.idioma = idioma
        self.textos = Textos[idioma]
    

    
    def cambiar_Idioma(self,idioma):
        self.idioma = idioma
        self.textos = Textos[idioma]
    
    def get(self,clave):
        return self.textos.get(clave, f"[{clave}]")