from Funciones.Rutas import Rutas

class Apodo:
    # Archivo donde se guardan los usuarios
    ruta = Rutas.Jugadores 

    # Método estático para saber si el apodo existe
    @staticmethod
    def existe_Apodo(nuevo_Apodo):
        # Devuelve True si el apodo esta registrado
        try:
            with open(Apodo.ruta, "r", encoding="utf-8") as archivo:
                for linea in archivo:
                    if linea.strip().lower() == nuevo_Apodo.lower():
                        return True
        except FileNotFoundError:
            return False
        return False

    # Método estático para reistrar
    @staticmethod
    def registrar_Apodo(nuevo_Apodo):
        """Registra un apodo nuevo"""
        with open(Apodo.ruta, "a", encoding="utf-8") as archivo:
            archivo.write(nuevo_Apodo + "\n")