# Dia 5: Tests de device.py

import pytest

from uart_driver.config import UartConfig

from uart_driver.device import UartDevice

from uart_driver.parsers import ModbusParser


def test_connected_device():  # Comprueba que un dispositivo conectado pueda analizar datos.

    config = UartConfig(

        9600,

        "N",

        1,

        1.0

    )

    parser = ModbusParser()

    device = UartDevice(

        config,

        parser

    )

    device.connect()

    resultado = device.read_and_parse(

        b"\x01\x03\x00\x01"

    )

    assert resultado["protocol"] == "Modbus"


def test_disconnected_device():  # Comprueba que un dispositivo desconectado produzca un error.

    config = UartConfig(

        9600,

        "N",

        1,

        1.0

    )

    parser = ModbusParser()

    device = UartDevice(

        config,

        parser

    )

    with pytest.raises(ConnectionError):

        device.read_and_parse(

            b"\x01\x03\x00\x01"

        )


def test_invalid_frame():  # Comprueba que un frame inválido produzca un error.

    config = UartConfig(

        9600,

        "N",

        1,

        1.0

    )

    parser = ModbusParser()

    device = UartDevice(

        config,

        parser

    )

    device.connect()

    with pytest.raises(ValueError):

        device.read_and_parse(

            b"\x01"

        )