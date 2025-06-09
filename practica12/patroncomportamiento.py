class Observador:
    def actualizar(self, mensaje):
        pass

class ObservadorConcreto(Observador):
    def __init__(self, nombre):
        self.nombre = nombre

    def actualizar(self, mensaje):
        print(f"{self.nombre} recibió: {mensaje}")

class Sujeto:
    def __init__(self):
        self._observadores = []

    def adjuntar(self, observador):
        self._observadores.append(observador)

    def notificar(self, mensaje):
        for obs in self._observadores:
            obs.actualizar(mensaje)

# Uso
sujeto = Sujeto()
obs1 = ObservadorConcreto("Observer A")
obs2 = ObservadorConcreto("Observer B")

sujeto.adjuntar(obs1)
sujeto.adjuntar(obs2)

sujeto.notificar("Estado actualizado")
