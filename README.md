# FelipedelosH

# Patrones de diseño:


# Factory:

Sirve para tener una fabrica de objetos de muchas subclases (Hijos)... No se involucra al padre... Solo se involucra a la fabrica.

# Singleton:

Sirve para que un objeto que se instancia en muchas partes solo se cree una vez... No hay que crear el objeto muchas veces.
Solo se crea muchas veces pero se instancia 1 sola vez.


# Decorator:

Añade funcionalidad a un método sin necesidad de modificarlo, o sea simplemente se llama a otra función antes de que el método
se ejecute para hacer algo en otra función.

# Adapter

Conecta clases incompatibles para trabajar. Osea si tengo 2 clases que no están hechas para trabajar juntas se hace 
una clase adaptadora la cual tendra un metodo que las pondrá a trabajar en conjunto.

# Observer

En caso de necesitar que varias clases se enteren en tiempo real del estado de un Objeto, se puede crear una colección de suscriptores y notificar del cambio.
