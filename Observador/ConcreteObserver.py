from IObservador import Suscriptor

# Observador Concreto
class Usuario(Suscriptor):
    def __init__(self, nombre: str):
        self.nombre = nombre

    def actualizar(self, clave: str):
        print(f"{self.nombre}: ¡Nueva clave generada! -> {clave}")