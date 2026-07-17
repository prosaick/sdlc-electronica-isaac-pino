# Dia 4: Principios SOLID (ISP y DIP)

from dataclasses import dataclass  # Permite crear clases para almacenar datos automáticamente.

from enum import Enum, auto  # Enum sirve para crear enumeraciones.

from typing import Protocol  # Protocol permite crear interfaces sin necesidad de herencia.



class SensorType(Enum):  # Define los diferentes tipos de sensores.

    TEMPERATURE = auto()  # Crea el tipo TEMPERATURE.

    HUMIDITY = auto()  # Crea el tipo HUMIDITY.



@dataclass(frozen=True)  # Crea una clase inmutable para almacenar una lectura.

class SensorReading:

    sensor_id: str  # Guarda el identificador del sensor.

    value: float  # Guarda el valor medido.

    sensor_type: SensorType  # Guarda el tipo de sensor.


# ISP (Interface Segregation Principle o Principio de Segregación de Interfaces)

### esta mal

class SensorDevice:
    # Esta interfaz obliga a implementar métodos que algunos sensores no necesitan.

    def read(self):

        pass

    def write(self):

        pass

    def calibrate(self):

        pass

    def reset(self):

        pass



### esta corecto

class Readable(Protocol):
    # Define una interfaz solamente para leer información.

    def read(self) -> SensorReading:

        ...



class Writable(Protocol):
    # Define una interfaz solamente para escribir información.

    def write(self, data: SensorReading) -> None:

        ...



class Calibratable(Protocol):
    # Define una interfaz solamente para calibrar un dispositivo.

    def calibrate(self) -> None:

        ...



class TemperatureSensor:
    # Implementa únicamente la interfaz que realmente necesita.

    def read(self) -> SensorReading:

        return SensorReading(

            "TEMP01",

            25.8,

            SensorType.TEMPERATURE

        )



# DIP - Dependency Inversion Principle

class DataRepository(Protocol):
    # Define la interfaz que utilizarán los repositorios.

    def save(self, reading: SensorReading) -> None:

        ...

    def get_latest(self, sensor_id: str) -> SensorReading | None:

        ...



class InMemoryRepository:
    # Guarda las lecturas utilizando un diccionario en memoria.

    def __init__(self):

        self._storage = {}



    def save(self, reading: SensorReading) -> None:

        self._storage[reading.sensor_id] = reading



    def get_latest(self, sensor_id: str) -> SensorReading | None:

        return self._storage.get(sensor_id)



class DataProcessor:
    # Esta clase depende de una abstracción y no de un repositorio específico.

    def __init__(self, repository: DataRepository):

        self._repo = repository



    def process(self, reading: SensorReading):

        # Guarda la lectura utilizando el repositorio recibido.

        self._repo.save(reading)



    def latest(self, sensor_id: str):

        # Devuelve la última lectura almacenada.

        return self._repo.get_latest(sensor_id)