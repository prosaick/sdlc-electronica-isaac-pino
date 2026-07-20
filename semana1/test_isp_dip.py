# Dia 4: Tests ISP y DIP

from solid_isp_dip import (

    TemperatureSensor,

    SensorReading,

    SensorType,

    InMemoryRepository,

    DataProcessor

)

# ISP (Interface Segregation Principle o Principio de Segregación de Interfaces)


def test_temperature_sensor():

    # Crea un sensor de temperatura.

    sensor = TemperatureSensor()

    # Obtiene una lectura del sensor.

    lectura = sensor.read()

    # Comprueba que el tipo del sensor sea TEMPERATURE.

    assert lectura.sensor_type == SensorType.TEMPERATURE



def test_sensor_id():

    # Crea un sensor de temperatura.

    sensor = TemperatureSensor()

    # Obtiene una lectura.

    lectura = sensor.read()

    # Comprueba que el identificador sea TEMP01.

    assert lectura.sensor_id == "TEMP01"



# DIP (Dependency Inversion Principle o Principio de Inversión de Dependencias)


def test_save_reading():

    # Crea un repositorio en memoria.

    repo = InMemoryRepository()

    # Crea el procesador utilizando inyección de dependencias.

    processor = DataProcessor(repo)

    # Crea una lectura de prueba.

    lectura = SensorReading(

        "TEMP01",

        30,

        SensorType.TEMPERATURE

    )

    # Guarda la lectura.

    processor.process(lectura)

    # Comprueba que la lectura fue almacenada.

    assert repo.get_latest("TEMP01") == lectura



def test_latest_reading():

    # Crea un repositorio en memoria.

    repo = InMemoryRepository()

    # Crea el procesador.

    processor = DataProcessor(repo)

    # Crea una lectura.

    lectura = SensorReading(

        "TEMP01",

        28,

        SensorType.TEMPERATURE

    )

    # Guarda la lectura.

    processor.process(lectura)

    # Comprueba que latest() devuelve la lectura correcta.

    assert processor.latest("TEMP01") == lectura