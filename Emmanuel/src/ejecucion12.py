from abc import ABC, abstractmethod

'''
Inyección de dependencias
'''

#Inyeccion de dependencias por constructor
class ServiceEmail:
    def enviar_email(self, mensaje:str):
        print(f"Enviando email: {mensaje}")


class Notificador:
    def set_email_service(self, service_email:ServiceEmail):
        self.service_email = service_email

    def notificar(self, mensaje:str):
        self.service_email.enviar_email(mensaje)


service_email = ServiceEmail()
notificador = Notificador()
notificador.set_email_service(service_email)
notificador.notificar("Buenas tardes")



class MotorBase(ABC):
    @abstractmethod
    def encender(self):
        pass


class MotorElectrico(MotorBase):
    def encender(self):
        print("Encendiendo motor eléctrico")

class MotorCombustion(MotorBase):
    def encender(self):
        print("Encendiendo motor de combustión")

class Auto:
    def __init__(self, motor_base:MotorBase):
        self.motor = motor_base

    def arrancar(self):
        self.motor.encender()


auto_electrico = Auto(MotorElectrico())
auto_combustion = Auto(MotorCombustion())

auto_electrico.arrancar()
auto_combustion.arrancar()