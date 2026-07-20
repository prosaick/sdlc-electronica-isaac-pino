# Dia 5: Parsers

from abc import ABC, abstractmethod  # Permite crear clases abstractas.


class MessageParser(ABC):  # Define una clase base para todos los parsers.

    @abstractmethod

    def can_parse(self, frame: bytes) -> bool:

        pass


    @abstractmethod

    def parse(self, frame: bytes) -> dict:

        pass


class ModbusParser(MessageParser):  # Implementa un parser para Modbus RTU.

    def can_parse(self, frame: bytes) -> bool:

        return len(frame) >= 4


    def parse(self, frame: bytes) -> dict:

        return {

            "protocol": "Modbus",

            "raw": frame.hex()

        }


class NMEAParser(MessageParser):  # Implementa un parser para mensajes NMEA.

    def can_parse(self, frame: bytes) -> bool:

        return frame.startswith(b"$GPGGA")


    def parse(self, frame: bytes) -> dict:

        return {

            "protocol": "NMEA",

            "sentence": frame.decode()

        }