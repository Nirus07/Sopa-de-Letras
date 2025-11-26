class Apodo:
    def __init__(self):
        self.apodos = []

    def agregar_Apodo(self,nuevo_Apodo):
        if(self.apodos_Repetidos(nuevo_Apodo)):
            print("Este apodo ya existe, introduce otro apodo.")
            # Volver a solicitar apodo
        else:
            self.apodos.append(nuevo_Apodo)
            self.base_De_Datos_Usuarios()

    def apodos_Repetidos(self,nuevo_Apodo):
        if(self.apodos == []):
            return False
        else:
            for apodo in self.apodos:
                if(apodo == nuevo_Apodo):
                    return True
                else:
                    return False
            
    def base_De_Datos_Usuarios(self):
        with open("Base De Datos/Usuarios.txt","a") as archivo:
            for apodo in self.apodos:
                archivo.write(f"{apodo}\n")