# Dia 5: Configuración del Driver UART

from dataclasses import dataclass  # Permite crear clases para almacenar datos automáticamente.


@dataclass(frozen=True)  # Hace que la configuración sea inmutable.

class UartConfig:  # Define la configuración del puerto UART.

    baudrate: int  # Guarda la velocidad de comunicación.

    parity: str  # Guarda el tipo de paridad.

    stop_bits: int  # Guarda la cantidad de bits de parada.

    timeout: float  # Guarda el tiempo de espera.


    def __post_init__(self):  # Se ejecuta automáticamente después del constructor.

        # Comprueba que el baudrate sea válido.

        if self.baudrate <= 0:

            raise ValueError("El baudrate debe ser mayor a cero.")


        # Comprueba que la paridad sea válida.

        if self.parity not in ("N", "E", "O"):

            raise ValueError("La paridad debe ser N, E u O.")


        # Comprueba que los bits de parada sean válidos.

        if self.stop_bits not in (1, 2):

            raise ValueError("Los bits de parada deben ser 1 o 2.")


        # Comprueba que el timeout no sea negativo.

        if self.timeout < 0:

            raise ValueError("El timeout no puede ser negativo.")