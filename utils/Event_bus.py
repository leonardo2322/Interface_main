class EventBus:
    def __init__(self):
        self.suscriptores = {}  # {"nombre_evento": [func1, func2]}

    def suscribir(self, evento, callback):
        if evento not in self.suscriptores:
            self.suscriptores[evento] = []
        self.suscriptores[evento].append(callback)

    def emitir(self, evento, data=None):
        if evento in self.suscriptores:
            for callback in self.suscriptores[evento]:
                callback(data)