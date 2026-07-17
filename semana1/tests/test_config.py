# Dia 5: Tests de config.py

from dataclasses import FrozenInstanceError  # Permite comprobar que una dataclass sea inmutable.

import pytest  # Permite realizar pruebas automáticas.

from uart_driver.config import UartConfig  # Importa la configuración UART.


def test_valid_config():  # Comprueba que una configuración válida pueda crearse correctamente.

    config = UartConfig(

        baudrate=9600,

        parity="N",

        stop_bits=1,

        timeout=1.0

    )

    assert config.baudrate == 9600


def test_invalid_baudrate():  # Comprueba que un baudrate inválido produzca un error.

    with pytest.raises(ValueError):

        UartConfig(

            baudrate=0,

            parity="N",

            stop_bits=1,

            timeout=1.0

        )


def test_config_is_frozen():  # Comprueba que la configuración sea inmutable.

    config = UartConfig(

        baudrate=9600,

        parity="N",

        stop_bits=1,

        timeout=1.0

    )

    with pytest.raises(FrozenInstanceError):

        config.baudrate = 115200