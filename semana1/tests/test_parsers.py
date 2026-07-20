# Dia 5: Tests de parsers.py

from uart_driver.parsers import ModbusParser, NMEAParser


def test_modbus_valid_frame():  # Comprueba que un frame Modbus válido pueda analizarse.

    parser = ModbusParser()

    frame = b"\x01\x03\x00\x01"

    assert parser.can_parse(frame)


def test_modbus_invalid_frame():  # Comprueba que un frame Modbus inválido sea rechazado.

    parser = ModbusParser()

    frame = b"\x01"

    assert not parser.can_parse(frame)


def test_nmea_valid_frame():  # Comprueba que una sentencia NMEA válida pueda analizarse.

    parser = NMEAParser()

    frame = b"$GPGGA,123456"

    assert parser.can_parse(frame)


def test_nmea_invalid_frame():  # Comprueba que una sentencia inválida sea rechazada.

    parser = NMEAParser()

    frame = b"Hola Mundo"

    assert not parser.can_parse(frame)