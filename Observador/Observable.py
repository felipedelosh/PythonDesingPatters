from IObservador import Suscriptor
import random

# Sujeto (Observable)
class GeneradorDeClaves:
    def __init__(self):
        self._suscriptores = []
        self._clave_actual = None

    def agregar_suscriptor(self, suscriptor: Suscriptor):
        self._suscriptores.append(suscriptor)

    def quitar_suscriptor(self, suscriptor: Suscriptor):
        self._suscriptores.remove(suscriptor)

    def generar_clave(self):
        self._clave_actual = "".join(random.choices("0123456789", k=3))
        self._notificar()

    def _notificar(self):
        for suscriptor in self._suscriptores:
            suscriptor.actualizar(self._clave_actual)
