class ServicioExistente:
    def peticion_especial(self):
        return "Respuesta del servicio existente"

class Adaptador:
    def __init__(self, servicio):
        self.servicio = servicio

    def solicitar(self):
        return self.servicio.peticion_especial()


servicio = ServicioExistente()
adaptador = Adaptador(servicio)

print("Cliente:", adaptador.solicitar())
