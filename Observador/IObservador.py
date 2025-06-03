from abc import ABC, abstractmethod

# Interfaz Observador
class Suscriptor(ABC):
    @abstractmethod
    def actualizar(self, clave: str):
        pass
