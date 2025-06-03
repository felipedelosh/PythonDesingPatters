# Observer

Es un patrón comportamental el cual establece una relación de UNO a MUCHOS. En esta relación existe un objeto el cual se le suscriben muchos otros para conocer su estado en tiempo real. En caso ed que el objeto cambie todos sus suscriptores son notificados.

Se basa en una clase principal que tiene una lista de suscriptores y si el estado del observable cambia la lista de suscriptores va a ser modificada mediante un ciclo.

ConcreteObserser: Son las clases que implementarán el contrato.
<br>
IObservador: Se encarga de generar un contrato de suscripción para actualización (Informar el cambio).
<br>
Observable: Es la clase en donde existira una lista de usuarios los cuales se notificara con un ciclo en caso de exitir un cambio.
