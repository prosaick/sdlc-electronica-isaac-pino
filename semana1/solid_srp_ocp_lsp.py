# Dia 3: Principios SOLID

from abc import ABC, abstractmethod  # Permite crear clases abstractas y métodos obligatorios.

from dataclasses import dataclass  # Permite crear clases para almacenar datos automáticamente.

from enum import Enum, auto  # Enum sirve para crear enumeraciones o agrupar valores relacionados.



class SensorType(Enum):  # Define los diferentes tipos de sensores.

    TEMPERATURE = auto()  # Crea el tipo TEMPERATURE.

    HUMIDITY = auto()  # Crea el tipo HUMIDITY.



@dataclass(frozen=True)  # Crea una clase inmutable para almacenar una lectura.

class SensorReading:

    sensor_id: str  # Guarda el identificador del sensor.

    value: float  # Guarda el valor medido.

    sensor_type: SensorType  # Guarda el tipo de sensor.



# ===================================================
# S - Single Responsibility Principle
# ===================================================

# ---------- MAL ----------

class SensorManager:  # Esta clase tiene más de una responsabilidad.

    def read_sensor(self) -> SensorReading:  # Lee un sensor.

        return SensorReading(

            "TEMP01",

            25.5,

            SensorType.TEMPERATURE

        )

    def save(self, reading: SensorReading):  # También guarda información.

        print(f"Guardando {reading}")



# ---------- BIEN ----------

class SensorReader:  # Esta clase solamente se encarga de leer sensores.

    def read(self) -> SensorReading:  # Devuelve una lectura del sensor.

        return SensorReading(

            "TEMP01",

            25.5,

            SensorType.TEMPERATURE

        )



class DataLogger:  # Esta clase solamente se encarga de guardar información.

    def save(self, reading: SensorReading):  # Guarda la lectura recibida.

        print(f"Guardando {reading}")



# ===================================================
# O - Open Closed Principle
# ===================================================

class AlertStrategy(ABC):  # Define una estrategia base para enviar alertas.

    @abstractmethod

    def send(self, message: str) -> None:  # Obliga a las clases hijas a implementar send().

        pass



class ConsoleAlert(AlertStrategy):  # Envía la alerta por consola.

    def send(self, message: str) -> None:

        print(message)



class FileAlert(AlertStrategy):  # Simula guardar la alerta en un archivo.

    def send(self, message: str) -> None:

        print(f"Archivo: {message}")



class EmailAlert(AlertStrategy):  # Agrega una nueva estrategia sin modificar las existentes.

    def send(self, message: str) -> None:

        print(f"Email: {message}")



class AnomalyDetector:  # Detecta anomalías utilizando cualquier estrategia de alerta.

    def __init__(self, alert: AlertStrategy, threshold: float):  # Inicializa la estrategia y el umbral.

        self._alert = alert

        self._threshold = threshold

    def check(self, reading: SensorReading):  # Comprueba si la lectura supera el umbral.

        if reading.value > self._threshold:

            self._alert.send(

                f"Anomalía en {reading.sensor_id}"

            )



# ===================================================
# L - Liskov Substitution Principle
# ===================================================

class BaseSensor(ABC):  # Define una clase base para cualquier tipo de sensor.

    @abstractmethod

    def read(self) -> SensorReading:  # Obliga a implementar el método read().

        pass



class TemperatureSensor(BaseSensor):  # Implementa un sensor de temperatura.

    def read(self):

        return SensorReading(

            "TEMP01",

            30,

            SensorType.TEMPERATURE

        )



class HumiditySensor(BaseSensor):  # Implementa un sensor de humedad.

    def read(self):

        return SensorReading(

            "HUM01",

            75,

            SensorType.HUMIDITY

        )



def process_sensor(sensor: BaseSensor):  # Recibe cualquier objeto que herede de BaseSensor.

    lectura = sensor.read()  # Obtiene la lectura del sensor recibido.

    print(lectura)  # Muestra la lectura obtenida.