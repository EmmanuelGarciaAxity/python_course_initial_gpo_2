'''
Inyeccion manual
'''


class Contenedor:
    def __init__(self):
        self.registro = {}

    def registrar(self, nombre, provedor):
        self.registro[nombre] = provedor

    def resolver(self, nombre):
        return self.registro[nombre]()

class Logger:
    def info(self, mensaje):
        print(f"INFO: {mensaje}")

class Servicio:
    def __init__(self, logger):
        self.logger = logger

    def procesar_data(self):
        self.logger.info("Procesando datos..")

contenedor = Contenedor()

contenedor.registrar("logger", Logger)
contenedor.registrar("servicio", lambda: Servicio(contenedor.resolver("logger")))

servicio = contenedor.resolver("servicio")
servicio.procesar_data()