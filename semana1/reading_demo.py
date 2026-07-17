## Día 1: funciones puras y lectura de sensores

"""
funcion pura de la temp, humedad y verificacioens de lectura
## Convertir C a F

def cel_fahr(celsius: float) -> float: # indica que la funcion recibe un float y devuelve un float (se prepara para una variable de tipo float)
       return (celsius * 9 / 5) + 32 # Es la formula para la convercion de C a F

## convertir F a C

def fahr_cel(fahrenheit: float) -> float: # indica que la funcion recibe un float y devuelve un float (se prepara para una variable de tipo float)
        return (fahrenheit - 32) * 5 / 9 # Es la formula para la convercion de F a C

## Cheacr temp alta

def temp_High(temperatura: float, limite: float = 35.0) -> bool:# Indica que la funcion devolverá True o False, dependiendo de si la temperatura es mayor al limite (35.0 por defecto)
       return temperatura > limite # al resolver la comparacion se devolverá un T o F dependiendo de si la temperatura es mayor al limite o no 

## Cheacar Humedad alta

def hum_High(humedad: float, limite: float = 80.0) -> bool: # Indica que la funcion devolverá True o False, dependiendo de si la humedad es mayor al limite (80.0 por defecto)
       return humedad > limite # al resolver la comparacion se devolverá un T o F dependiendo de si la humedad es mayor al limite o no

## Verificacion de lectura

def verificacion_lect(temperatura: float, humedad: float) -> bool: # Indica que la funcion devolverá True o False, dependiendo de si los valores estan dentro de un rango razonable
        return -50 <= temperatura <= 100 and 0 <= humedad <= 100    # solo si ambas condiciones se cumplen devolverá True, de lo contrario devolverá False
    
"""

from dataclasses import dataclass  # Permite crear clases para almacenar datos sin escribir manualmente el constructor.
from enum import Enum, auto  # Enum sirve para crear enumeraciones o agrupar valores relacionados.
from typing import Protocol  # Protocol permite definir interfaces sin necesidad de herencia.
import json  # Se importa json para convertir objetos a formato JSON.


class SensorType(Enum):  # Define una enumeración para representar los diferentes tipos de sensores.

    TEMPERATURE = auto()  # Crea el tipo TEMPERATURE y le asigna automáticamente un valor.

    HUMIDITY = auto()  # Crea el tipo HUMIDITY y le asigna automáticamente un valor.


@dataclass(frozen=True)  # Crea automáticamente el constructor y hace que el objeto sea inmutable.

class Reading:  # Define una clase para almacenar la información de una lectura del sensor.

    sensor_id: str  # Guarda el identificador del sensor.

    value: float  # Guarda el valor medido por el sensor.

    sensor_type: SensorType  # Guarda el tipo de sensor.


class Transport(Protocol):  # Define una interfaz para cualquier medio de transporte de datos.

    def send(self, payload: bytes) -> None:

        ...


def to_frame(reading: Reading) -> bytes:  # Convierte un objeto Reading a un arreglo de bytes.

    return f"{reading.sensor_id}:{reading.value:.2f}".encode()


# integracion de las funciones puras

## Convertir C a F

def cel_fahr(reading: Reading) -> Reading:
    # Indica que la función recibe un objeto Reading y devuelve un nuevo objeto Reading

    nuevo_valor = (reading.value * 9 / 5) + 32  # Aplica la fórmula para convertir de Celsius a Fahrenheit

    return Reading(  # Devuelve un nuevo objeto Reading sin modificar el original

        sensor_id=reading.sensor_id,

        value=nuevo_valor,

        sensor_type=reading.sensor_type

    )


## Convertir F a C

def fahr_cel(reading: Reading) -> Reading:
    # Indica que la función recibe un objeto Reading y devuelve un nuevo objeto Reading

    nuevo_valor = (reading.value - 32) * 5 / 9  # Aplica la fórmula para convertir de Fahrenheit a Celsius

    return Reading(

        sensor_id=reading.sensor_id,

        value=nuevo_valor,

        sensor_type=reading.sensor_type

    )


## Checar temperatura alta

def temp_High(reading: Reading, limite: float = 35.0) -> bool:
    # Indica que la función devolverá True o False dependiendo de si la temperatura supera el límite

    return reading.value > limite


## Checar humedad alta

def hum_High(reading: Reading, limite: float = 80.0) -> bool:
    # Indica que la función devolverá True o False dependiendo de si la humedad supera el límite

    return reading.value > limite


## Verificación de lectura

def verificacion_lect(temperatura: float, humedad: float) -> bool:
    # Indica que la función devolverá True o False dependiendo de si los valores están dentro de un rango razonable

    return -50 <= temperatura <= 100 and 0 <= humedad <= 100


## Serializar lectura a diccionario

def reading_dict(reading: Reading) -> dict:
    # Convierte un objeto Reading en un diccionario

    return {

        "sensor_id": reading.sensor_id,

        "value": reading.value,

        "sensor_type": reading.sensor_type.name

    }


## lectura de JSON serializado 

def reading_json(reading: Reading) -> str:
    # Convierte un objeto Reading en una cadena con formato JSON

    return json.dumps(reading_dict(reading))


# ejemplo

temperatura = Reading(

    sensor_id="TEMP01",

    value=27.0,

    sensor_type=SensorType.TEMPERATURE

)

humedad = Reading(

    sensor_id="HUM01",

    value=85.0,

    sensor_type=SensorType.HUMIDITY

)

# print(cel_fahr(temperatura), fahr_cel(cel_fahr(temperatura)), temp_High(temperatura), hum_High(humedad), verificacion_lect(temperatura.value, humedad.value), reading_dict(temperatura), reading_json(temperatura), to_frame(temperatura), sep="\n")

print(cel_fahr(temperatura))

print(fahr_cel(cel_fahr(temperatura)))

print(temp_High(temperatura))

print(hum_High(humedad))

print(verificacion_lect(temperatura.value, humedad.value))

print(reading_dict(temperatura))

print(reading_json(temperatura))

print(to_frame(temperatura))