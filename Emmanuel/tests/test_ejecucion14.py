import sys
from pathlib import Path
from unittest.mock import Mock

# Agregar la ruta raíz del proyecto al path
sys.path.insert(0, str(Path(__file__).parent.parent))
from src.ejecucion14 import Logger, Servicio

class LoggerMock:

    def info(self, mensaje):
        print(f"INFO: {mensaje}")


def test_servicio():
    mock_logger = Mock()

    service = Servicio(logger=mock_logger)
    service.procesar_data()

    mock_logger.info.assert_called_once_with("Procesando datos..")
