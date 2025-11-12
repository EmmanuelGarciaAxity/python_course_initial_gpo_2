import logging

from exceptions.exception import function_con_error

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

try:
    function_con_error(-1)
except Exception as e :
    logging.error(f"Error: {e}")
else:
    logging.info(f"Resultado correcto")

finally:
    logging.info("Fin del programa")    