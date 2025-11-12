from dependency_injector import containers, providers


class Logger:
    def info(self, mensaje):
        print(f"INFO: {mensaje}")

class Servicio:
    def __init__(self, logger):
        self.logger = logger

    def procesar_data(self):
        self.logger.info("Procesando datos..")

class Contenedor(containers.DeclarativeContainer):
    logger = providers.Singleton(Logger)
    servicio = providers.Factory(Servicio, logger=logger)

contenedor = Contenedor()
servicio = contenedor.servicio()
servicio.procesar_data()

