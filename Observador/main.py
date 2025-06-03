from Observable import GeneradorDeClaves
from ConcreteObserver import Usuario

generador = GeneradorDeClaves()

suscriptor1 = Usuario("Ana")
suscriptor2 = Usuario("Luis")

generador.agregar_suscriptor(suscriptor1)
generador.agregar_suscriptor(suscriptor2)

print("Generando claves aleatorias:")
generador.generar_clave()  # Ejemplo: "Ana: ¡Nueva clave generada! -> ???"
generador.generar_clave()  # Ejemplo: "Luis: ¡Nueva clave generada! -> ???"
