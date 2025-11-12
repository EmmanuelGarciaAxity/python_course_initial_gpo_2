import sys
from pathlib import Path

# Agregar la ruta raíz del proyecto al path
sys.path.insert(0, str(Path(__file__).parent.parent))
from src.ejecucion11 import Notificacion

def test_enviar_mensaje():
    notificacion = Notificacion()
    msj = notificacion.enviar_mensaje("Hola")
    assert "Enviando mensaje: Hola" in msj

def test_cancelar_mensaje():
    notificacion = Notificacion()
    msj = notificacion.cancelar_mensaje("Hola")
    assert "Cancelando mensaje: Hola" in msj