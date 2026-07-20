# Dia 3: Principios SOLID

# Importa todas las clases que se utilizarán para realizar las pruebas.

from solid_srp_ocp_lsp import (

    SensorReader,

    DataLogger,

    SensorReading,

    SensorType,

    ConsoleAlert,

    EmailAlert,

    AnomalyDetector,

    TemperatureSensor,

    HumiditySensor,

)

# SRP (Principio de Responsabilidad Única)


def test_sensor_reader():  # Comprueba que la clase SensorReader pueda leer un sensor.

    reader = SensorReader()  # Crea un objeto de la clase SensorReader.

    lectura = reader.read()  # Obtiene una lectura del sensor.

    assert lectura.sensor_id == "TEMP01"  # Comprueba que el identificador del sensor sea TEMP01.



def test_data_logger():  # Comprueba que DataLogger pueda guardar una lectura.

    logger = DataLogger()  # Crea un objeto de la clase DataLogger.

    lectura = SensorReader().read()  # Obtiene una lectura utilizando SensorReader.

    assert logger.save(lectura) is None  # Comprueba que el método save() termine correctamente.



# OCP (Programación Orientada a Componentes)


def test_console_alert():  # Comprueba que ConsoleAlert funcione como estrategia de alerta.

    detector = AnomalyDetector(  # Crea un detector de anomalías.

        ConsoleAlert(),  # Utiliza ConsoleAlert como estrategia.

        20  # Establece el umbral en 20.

    )

    detector.check(  # Envía una lectura para comprobar si existe una anomalía.

        SensorReading(

            "TEMP",

            30,

            SensorType.TEMPERATURE

        )

    )

    assert True  # Si no ocurre ningún error, la prueba se considera correcta.



def test_email_alert():  # Comprueba que EmailAlert funcione sin modificar el detector.

    detector = AnomalyDetector(

        EmailAlert(),  # Utiliza EmailAlert como estrategia.

        20

    )

    detector.check(

        SensorReading(

            "TEMP",

            30,

            SensorType.TEMPERATURE

        )

    )

    assert True



# LSP (Language Server Protocol o Protocolo de Servidor de Lenguaje)

def test_temperature_sensor():  # Comprueba que TemperatureSensor pueda utilizarse correctamente.

    sensor = TemperatureSensor()  # Crea un sensor de temperatura.

    lectura = sensor.read()  # Obtiene una lectura.

    assert lectura.sensor_type == SensorType.TEMPERATURE  # Comprueba que el tipo de sensor sea TEMPERATURE.



def test_humidity_sensor():  # Comprueba que HumiditySensor pueda utilizarse correctamente.

    sensor = HumiditySensor()  # Crea un sensor de humedad.

    lectura = sensor.read()  # Obtiene una lectura.

    assert lectura.sensor_type == SensorType.HUMIDITY  # Comprueba que el tipo de sensor sea HUMIDITY.