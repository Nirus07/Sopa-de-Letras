from Funciones.Rutas import Rutas

class Apodo:
    def __init__(self,nuevo_Apodo):
        self.apodos = []
        self.apodos_Repetidos(nuevo_Apodo)


    def apodos_Repetidos(self,nuevo_Apodo):
        if(self.apodos == []):
            return False
        else:
            self.leer_Base_De_Datos(nuevo_Apodo)
            
    def base_De_Datos_Usuarios(self):
        with open("BaseDeDatos/Jugadores.txt","a") as archivo:
            for apodo in self.apodos:
                archivo.write(f"{apodo}\n")
    
    def leer_Base_De_Datos(self,nuevo_Apodo):
        with open("BaseDeDatos/Jugadores.txt","r") as archivo:
            usuarios =archivo.readlines()
            for usuario in usuarios:
                apodo = usuario.strip()
                if(apodo == nuevo_Apodo):
                    return True
                else:
                    return False