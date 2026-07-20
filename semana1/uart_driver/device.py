# Dia 5: Dispositivo UART

from uart_driver.config import UartConfig  # Importa la configuración.

from uart_driver.parsers import MessageParser  # Importa la clase base de los parsers.



class UartDevice:  # Representa un dispositivo UART.

    def __init__(self, config: UartConfig, parser: MessageParser):

        self._config = config  # Guarda la configuración.

        self._parser = parser  # Guarda el parser.

        self._connected = False  # Indica si el dispositivo está conectado.



    def connect(self):  # Conecta el dispositivo.

        self._connected = True



    def disconnect(self):  # Desconecta el dispositivo.

        self._connected = False



    def read_and_parse(self, frame: bytes):

        # Comprueba que el dispositivo esté conectado.

        if not self._connected:

            raise ConnectionError("El dispositivo no está conectado.")


        # Comprueba si el parser puede interpretar el mensaje.

        if not self._parser.can_parse(frame):

            raise ValueError("Frame inválido.")


        # Devuelve la información parseada.

        return self._parser.parse(frame)