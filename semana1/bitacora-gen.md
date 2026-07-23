# Día 1/Semana1

## ++++++++ Enum/SensorType +++++++

La práctica consta en generar una lectura a travéz de un sensor.
Para esto necesitamos generar algunos componentes fundamentales como:

"SensorType"
"Readig"
"Transport"

Y algunos otros más.

Utilizamos la libreria "Enum" la cual nos ayuda a crear un conjunto de constantes con nombre, es decirnos ayudan a representar constantes con nombre más claros

la manera enq ue se usó el Enum en nuestro código fue la sigueinte:

<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>

class SensorType(Enum):  # Define una enumeración para representar los diferentes tipos de sensores.

    TEMPERATURE = auto()  # Crea el tipo TEMPERATURE y le asigna automáticamente un valor.

    HUMIDITY = auto()  # Crea el tipo HUMIDITY y le asigna automáticamente un valor.

<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>

Al asignarlos de esta manera podemos evitar errores como recibir solo

<<<<<<<>>>>>>>

sensor = 15
<<<<<<<>>>>>>>

por que el resultaado esperado es 

<<<<<<<<<<<>>>>>>>>>>>>

SensorType.TEMPERATURE

<<<<<<<<<<<>>>>>>>>>>>

Y no cualquier dato entero.

Aparte de que la libreria nos ayuda a hacer un poco más legible el script 

## +++++++ Reading ++++++++

creamos una clase llamada reading como la siguiente

<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>
    /# @dataclass es un constructor para el SensorType

@dataclass(frozen=True)   #indica que el parametro (frozen=True) no podrán ser modificados 
class Reading:      # indicac el nombre de la clase (la clase es todo lo de abajo)
    sensor_id: str  # crea un atributo con un resultado tipo string (cadena de texto)
    value: float    # se espera recibir un dato tipo float
    sensor_type: SensorType    # espera recibir datos del atributo SensorType a travez de las enumeraciones del SensoorType

<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>

## +++++++ Protocolo de transporte +++++++++

Creamos un protocolo de transporte como el siguiente

<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>

class Transport(Protocol):  # Define una interfaz para cualquier medio de transporte de datos.

    def send(self, payload: bytes) -> None:  # define un método que debe ser implementado por cualquier clase que herede de Transport.

        ... 

<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>

Aquí definimos una nueva clase llamada transport  de la libreria Protocol y esto hace referencia al medio por que cual se cargarán y recibirán datos.
siendo pyload el indicativo de enviar datos
y ":bytes" la manera de enviar los datos que es este caso fueron binario y con none indicamos que no necesitamos recibir datos o valores, solo realizar la acción.

los "..." solo dicen que no hay implementación del método pero que  tiene que existir, tambien puede  indicar que un método acepta otros argumentos adicionales que se han omitido para simplificar la lectura

## +++++++++ Funciones Puras ++++++++

Tuvimos que desarrollar 5 funciones puras relacionnadas con la funcón "Reading" por ejemplo:

<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>
def cel_fahr(reading: Reading) -> Reading:
    # Indica que la función recibe un objeto Reading y devuelve un nuevo objeto tipo Reading 

    nuevo_valor = (reading.value * 9 / 5) + 32  # Aplica la fórmula para convertir de Celsius a Fahrenheit

    return Reading(  # Devuelve un nuevo objeto Reading sin modificar el original 

        sensor_id=reading.sensor_id, #indica que el valor del lado derecho se almacenará en el iszquierdo

        value=nuevo_valor,

        sensor_type=reading.sensor_type

    )
<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>

Estas funciones tenian que cumplir con el hecho de que:
1.- Siempre deberían producir la misma salida para la misma entrada, es decir, tomando el ejemplo anterior:
{

cel-fahr(20)
= 68

}

2.- No modificar nada externo, es decir, solo dedicarse a lo que es, calcular.

Principalmente lo hemos hecho con el fin de practicar el Reading, ya que  las funciones generadas reciben el dato y generan un resultado sin la necesidad de modificar la lectura.

## +++++++++++ type hints ++++++++++++

Otra cosa que estuvimos utilizando fueron los Type Hints.

Los Type Hints son una forma de decirle a python que tipo de dato esperamos recibir y que tipo de dato esperamos devolver.

Por ejemplo:

<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>

def cel_fahr(reading: Reading) -> Reading:

<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>

Aquí podemos ver que la función espera recibir un dato tipo Reading y tambien devolverá un dato tipo Reading.

Otro ejemplo es:

<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>

def temp_High(temperatura: float, limite: float = 35.0) -> bool:

<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>

En este caso esperamos recibir dos datos tipo float y devolver un dato tipo bool (True o False).

Esto ayuda principalmente a evitar errores al momento de programar y tambien hace que el código sea más facil de entender para otra persona.

Los Type Hints no obligan a python a usar esos tipos de datos, solamente sirven como ayuda para el programador y para herramientas como mypy.


## ++++++++++ Serialización +++++++++

Otro de los ejercicios consistió en serializar la información de una lectura.

La serialización consiste en convertir un objeto a un formato que pueda almacenarse o enviarse por algun medio de comunicación.

Por ejemplo, si tenemos una lectura como la siguiente:

<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>

Reading(

sensor_id="TEMP-01",

value=25.5,

sensor_type=SensorType.TEMPERATURE

)

<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>

Podemos convertirla a un diccionario.

<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>

{

"sensor_id":"TEMP-01",

"value":25.5,

"sensor_type":"TEMPERATURE"

}

<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>

O incluso convertirla a formato JSON.

Esto es muy util cuando se necesita guardar información en archivos o enviarla por internet utilizando protocolos como HTTP o MQTT.


## +++++++++++++ to_frame() +++++++++++++

Tambien utilizamos la función to_frame().

Esta función recibe un objeto Reading y lo convierte en una cadena de bytes para poder ser enviada mediante algun protocolo de comunicación.

La función quedó de la siguiente manera.

<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>

def to_frame(r: Reading) -> bytes:

    return f"{r.sensor_id}:{r.value:.2f}".encode()

<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>

Lo que hace primero es formar una cadena con el id del sensor y el valor de la lectura.

Por ejemplo:

TEMP-01:25.50

Despues utiliza ".encode()" para convertir esa cadena en bytes.

El resultado final sería algo parecido a:

b'TEMP-01:25.50'

Esto es importante ya que la mayoria de protocolos de comunicación transmiten bytes y no objetos de Python.


## +++++++++++++ mypy y ruff +++++++++++++

Como parte de la actividad tambien investigamos dos herramientas llamadas mypy y ruff.

mypy sirve para revisar los Type Hints del programa y detectar errores relacionados con los tipos de datos antes de ejecutar el programa.

Por otro lado ruff sirve para revisar el estilo del código.

Esta herramienta ayuda a detectar variables que no se utilizan, imports innecesarios, errores de formato y algunas malas practicas al momento de programar.

Aunque en un principio tuve algunos problemas para ejecutarlos porque no estaban instalados en el entorno virtual, entendí que ambas herramientas ayudan a mejorar la calidad del código antes de entregar un proyecto.


## +++++++++++++ Conclusiones +++++++++++++

Durante este primer día comprendí que Python no solamente consiste en aprender una nueva sintaxis.

Tambien existen herramientas y formas de programar que ayudan a que el código sea más ordenado, más facil de mantener y más sencillo de probar.

Aprendí el uso de Enum, dataclass, Protocol, funciones puras, Type Hints y serialización, además de conocer herramientas como mypy y ruff para revisar el código.

Aunque algunos conceptos fueron nuevos para mi, pude relacionarlos con conocimientos que ya tenia de programación en C y de sistemas embebidos, por lo que fue más facil comprender para que sirven dentro de un proyecto más grande.

## +++++++++ Dificultades encontradas +++++++++

- Al principio no entendía la diferencia entre una función pura y una función normal.
- Tuve problemas para instalar ruff y mypy dentro del entorno virtual.
- Me costó comprender el uso de Protocol porque nunca había trabajado con interfaces en Python.


# Día 2/Semana1

## +++++++++ Máquina de Estados Finitos (FSM) +++++++++

Durante este segundo día el objetivo fue volver a realizar una Máquina de Estados Finitos (FSM), pero ahora utilizando Programación Orientada a Objetos (POO) en lugar de hacerlo de manera procedural como normalmente se hace en C.

En esta ocasión el ejemplo utilizado fue un semáforo.

Los estados posibles fueron:

<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>

RED

YELLOW

GREEN

<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>

Cada uno de ellos se creó utilizando una enumeración.

<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>

class TrafficLightState(Enum):

    RED = auto()

    YELLOW = auto()

    GREEN = auto()

<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>

Con esto evitamos utilizar números como 0,1 y 2 para representar los estados del semáforo, haciendo el código más legible.

## +++++++++ Clase TrafficLightFSM +++++++++

Posteriormente se creó una clase llamada TrafficLightFSM.

Esta clase representa completamente al semáforo y es donde vive toda la información relacionada con él.

Al crear un objeto de esta clase automáticamente se ejecuta el método __init__().

<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>

def __init__(self):

    self._state = TrafficLightState.RED

    self._cycle_count = 0

<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>

Aquí se inicializa el semáforo en color rojo y además se crea un contador para registrar cuántas veces cambia de estado.

Aprendí que el prefijo "_" delante del nombre de una variable indica que esa variable no debería modificarse directamente desde fuera de la clase.

## +++++++++ @property +++++++++

También utilizamos el decorador @property.

Este decorador permite consultar una variable privada como si fuera un atributo normal.

Por ejemplo:

<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>

@property

def state(self):

    return self._state

<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>

Gracias a esto podemos escribir:

<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>

fsm.state

<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>

En lugar de escribir algo como:

<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>

fsm.get_state()

<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>

Esto hace que el código sea un poco más limpio y fácil de leer.

## +++++++++ Método transition() +++++++++

El método transition() es el encargado de cambiar el estado del semáforo.

La lógica consiste en revisar el estado actual y cambiarlo por el siguiente.

<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>

RED

↓

GREEN

↓

YELLOW

↓

RED

<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>

Cada vez que ocurre una transición también aumenta el contador de ciclos.

<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>

self._cycle_count += 1

<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>

Finalmente el método devuelve el nuevo estado del semáforo.

## +++++++++ Programación Orientada a Objetos +++++++++

Durante este ejercicio pude notar varias diferencias respecto a como normalmente programaba en C.

Anteriormente era común utilizar variables globales para guardar el estado del sistema.

Ahora el estado pertenece al objeto.

Esto permite que puedan existir varios semáforos funcionando al mismo tiempo sin interferir unos con otros.

Cada objeto mantiene su propio estado y su propio contador.

Esto hace que el programa sea mucho más ordenado.

## +++++++++ Tests con Pytest +++++++++

Otra parte importante del día consistió en crear pruebas automáticas utilizando pytest.

Se realizaron cuatro pruebas.

1.- Verificar que el estado inicial sea RED.

2.- Verificar la transición de RED a GREEN.

3.- Verificar que después de un ciclo completo vuelva nuevamente a RED.

4.- Verificar que el contador de ciclos aumente correctamente.

Cada prueba comprueba solamente una parte específica del programa.

Esto permite detectar rápidamente si algún cambio rompe el funcionamiento del código.

## +++++++++ ¿Qué aprendí de los tests? +++++++++

Antes normalmente ejecutaba el programa para ver si aparentemente funcionaba.

Con pytest aprendí que es posible comprobar automáticamente si una función hace exactamente lo que esperamos.

De esta forma si en un futuro modificamos el código podremos saber inmediatamente si algo dejó de funcionar.

Esto hace que sea mucho más seguro realizar cambios.

## +++++++++ Conclusiones +++++++++

Durante este segundo día comprendí mejor el funcionamiento de la Programación Orientada a Objetos.

Aprendí a utilizar clases, objetos, atributos privados, propiedades y métodos.

También comprendí que una Máquina de Estados puede implementarse de una forma mucho más organizada utilizando objetos.

Finalmente conocí pytest y la importancia de crear pruebas automáticas para verificar el funcionamiento del programa sin tener que hacerlo manualmente cada vez que se modifica el código.

# Día 3/Semana1

## +++++++++ Principios SOLID +++++++++

Durante este día comenzamos a trabajar con los principios SOLID.

Estos principios son una serie de recomendaciones que ayudan a desarrollar programas más organizados, fáciles de mantener y de modificar en el futuro.

En esta práctica solamente trabajamos con los tres primeros principios:

S = Single Responsibility Principle.

O = Open Closed Principle.

L = Liskov Substitution Principle.

Cada uno fue implementado utilizando el dominio de sensores que hemos estado utilizando desde el inicio de la semana.

## +++++++++ S (Single Responsibility Principle) +++++++++

El primer principio indica que una clase solamente debe tener una responsabilidad.

Al inicio realizamos un ejemplo incorrecto donde una sola clase hacía varias cosas.

<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>

class SensorManager:

    def read_sensor(...)

    def save(...)

<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>

Esta clase se encargaba tanto de leer el sensor como de guardar la información.

Si en algún momento cambia la forma de leer el sensor o cambia la forma de guardar los datos, tendríamos que modificar la misma clase.

Posteriormente se realizó la forma correcta.

<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>

class SensorReader

class DataLogger

<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>

Ahora cada clase tiene solamente una responsabilidad.

SensorReader únicamente obtiene la lectura.

DataLogger únicamente guarda la información.

Esto hace que el código sea más fácil de modificar y mantener.

## +++++++++ O (Open Closed Principle) +++++++++

El segundo principio establece que una clase debe estar abierta para extenderse pero cerrada para modificarse.

Para esto utilizamos una clase abstracta llamada AlertStrategy.

<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>

class AlertStrategy(ABC)

<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>

Después se crearon diferentes formas de enviar una alerta.

ConsoleAlert.

FileAlert.

EmailAlert.

Cada una implementa el método send().

<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>

def send(self, message):

<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>

La ventaja es que si mañana se desea agregar otro tipo de alerta, solamente será necesario crear una nueva clase.

No será necesario modificar el código existente.

Esto reduce el riesgo de introducir nuevos errores.

## +++++++++ Clases Abstractas (ABC) +++++++++

Durante este ejercicio también conocimos las clases abstractas.

Estas sirven para definir una estructura que otras clases deberán seguir.

Una clase abstracta no se utiliza directamente.

Su función principal es indicar qué métodos deberán implementar las clases que hereden de ella.

Gracias a esto todas las estrategias de alerta funcionan de la misma manera.

## +++++++++ L (Liskov Substitution Principle) +++++++++

El tercer principio indica que una clase hija debe poder reemplazar a su clase padre sin alterar el funcionamiento del programa.

Para demostrarlo se creó una clase base llamada BaseSensor.

<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>

class BaseSensor(ABC)

<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>

Después se implementaron dos sensores.

TemperatureSensor.

HumiditySensor.

Ambos implementan el método read().

Posteriormente se creó la función.

<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>

process_sensor(sensor)

<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>

Esta función recibe cualquier objeto que herede de BaseSensor.

Sin importar si es un sensor de temperatura o uno de humedad, el programa funciona exactamente igual.

Esto demuestra que ambas clases son intercambiables.

## +++++++++ Pruebas realizadas +++++++++

Después de implementar los principios SOLID también se desarrollaron pruebas utilizando pytest.

Las pruebas verificaron que:

SensorReader devuelve correctamente una lectura.

DataLogger puede guardar una lectura.

ConsoleAlert funciona correctamente.

EmailAlert también funciona correctamente.

TemperatureSensor devuelve una lectura de temperatura.

HumiditySensor devuelve una lectura de humedad.

Cada prueba verifica únicamente una pequeña parte del programa.

Esto facilita encontrar errores cuando el proyecto crece.

## +++++++++ Relación con sistemas embebidos +++++++++

Durante esta práctica pude relacionar estos principios con proyectos de electrónica.

Anteriormente era común escribir una sola función donde se leía un sensor, se procesaban los datos y además se enviaban por UART.

Con SOLID aprendí que es mejor dividir esas responsabilidades.

De esta forma si cambia el sensor solamente se modifica la clase correspondiente.

Si cambia el medio de almacenamiento únicamente cambia DataLogger.

Y si cambia la forma de enviar alertas solamente se crea una nueva estrategia.

El resto del programa continúa funcionando igual.

## +++++++++ Dificultades encontradas +++++++++

Al principio me costó entender para qué servían realmente los principios SOLID.

Parecía que solamente hacían que hubiera más clases y más archivos.

Después de realizar los ejemplos pude comprender que la intención es que el código sea más fácil de modificar conforme el proyecto crece.

También tuve algunas dudas con las clases abstractas porque nunca las había utilizado en Python.

Otra dificultad fue comprender la diferencia entre herencia y sustitución, ya que al principio pensaba que eran exactamente lo mismo.

Después de realizar varios ejemplos quedó más claro cómo funciona el principio de Liskov.

---

## +++++++++ Conclusiones +++++++++

Durante este tercer día comprendí que los principios SOLID no buscan hacer el código más complicado.

Su objetivo principal es organizar mejor un proyecto para facilitar su mantenimiento.

Aprendí que una clase debe tener una sola responsabilidad, que es posible agregar nuevas funcionalidades sin modificar el código existente y que las clases derivadas deben poder sustituir a su clase base sin afectar el funcionamiento del programa.

También comprendí que estos principios son muy utilizados en proyectos grandes porque ayudan a reducir errores cuando el software comienza a crecer.


# Día 4/Semana1

## +++++++++ Principios SOLID (ISP y DIP) +++++++++

Durante este cuarto día terminamos de estudiar los principios SOLID.

En esta ocasión trabajamos con los dos principios restantes.

I = Interface Segregation Principle.

D = Dependency Inversion Principle.

Para esto desarrollamos un nuevo archivo llamado "solid_isp_dip.py" donde implementamos ambos principios utilizando nuevamente el ejemplo de sensores.

## +++++++++ ISP (Interface Segregation Principle) +++++++++

El principio ISP indica que una clase no debe estar obligada a implementar métodos que realmente no necesita.

Al principio se mostró un ejemplo donde existía una interfaz muy grande.

<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>

read()

write()

calibrate()

reset()

<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>

El problema de este diseño es que algunos dispositivos solamente necesitan leer datos, mientras que otros solamente necesitan escribir.

Si todos heredan de la misma interfaz, terminarán implementando funciones que nunca utilizarán.

La solución fue dividir esa interfaz en varias interfaces más pequeñas.

Readable.

Writable.

Calibratable.

Cada dispositivo solamente implementa la interfaz que realmente necesita.

Esto hace que el código sea más limpio y evita implementar funciones innecesarias.

## +++++++++ Protocol +++++++++

Para este ejercicio también utilizamos nuevamente la librería Protocol.

<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>

class DataRepository(Protocol)

<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>

Protocol funciona como una interfaz.

Su función es indicar qué métodos debe tener cualquier clase que quiera comportarse como un repositorio.

En este caso se definieron dos métodos.

save()

get_latest()

De esta manera cualquier repositorio podrá ser utilizado mientras implemente esos métodos.

## +++++++++ DIP (Dependency Inversion Principle) +++++++++

El último principio fue DIP.

Este principio indica que las clases no deben depender directamente de otras clases concretas.

En lugar de eso deben depender de una abstracción.

Para esto se creó la clase DataProcessor.

<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>

class DataProcessor:

    def __init__(self, repository: DataRepository)

<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>

Aquí podemos observar que DataProcessor no recibe un tipo específico de repositorio.

Únicamente recibe cualquier objeto que cumpla con la interfaz DataRepository.

Esto hace que el programa sea mucho más flexible.

## +++++++++ Inyección de Dependencias +++++++++

Durante este ejercicio también aprendimos el concepto de Inyección de Dependencias.

Consiste en entregar un objeto ya creado a otra clase mediante el constructor.

Por ejemplo.

<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>

repo = InMemoryRepository()

procesador = DataProcessor(repo)

<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>

Aquí DataProcessor recibe el repositorio desde el exterior.

No lo crea por sí mismo.

Gracias a esto podemos cambiar fácilmente el tipo de repositorio sin modificar DataProcessor.

Por ejemplo podríamos utilizar.

InMemoryRepository.

JsonRepository.

PostgreSQLRepository.

Todos funcionarían exactamente igual siempre que respeten la interfaz.

## +++++++++ Ventajas para realizar pruebas +++++++++

Una de las principales ventajas del principio DIP es que facilita mucho las pruebas.

Durante los tests no es necesario utilizar una base de datos real.

Basta con crear un repositorio en memoria.

De esta manera las pruebas son más rápidas y no dependen de archivos ni bases de datos externas.

Esto también hace que los errores sean más fáciles de detectar.

## +++++++++ Relación con proyectos de electrónica +++++++++

Pude relacionar este principio con proyectos de microcontroladores.

Por ejemplo, si un programa obtiene datos mediante UART y posteriormente deseo cambiar a SPI o I2C, el programa principal no debería cambiar.

Únicamente debería cambiar la clase encargada de la comunicación.

Mientras todas respeten la misma interfaz el resto del programa continuará funcionando normalmente.

Esto permite reutilizar gran parte del código.

## +++++++++ Pruebas realizadas +++++++++

Durante esta práctica también desarrollamos pruebas utilizando pytest.

Las pruebas verificaron que.

Las clases implementaran correctamente sus interfaces.

DataProcessor pudiera guardar correctamente una lectura.

El repositorio devolviera la última lectura almacenada.

Las pruebas también permitieron comprobar que el programa funciona correctamente utilizando diferentes implementaciones del repositorio.

## +++++++++ Dificultades encontradas +++++++++

Al principio me costó comprender la diferencia entre Protocol y una clase abstracta.

Pensaba que ambos hacían exactamente lo mismo.

Después entendí que Protocol solamente define qué métodos debe tener una clase, mientras que una clase abstracta además puede contener parte de la implementación.

También me tomó algo de tiempo comprender la Inyección de Dependencias.

Al principio parecía más sencillo crear directamente el repositorio dentro de la clase.

Después comprendí que recibir el repositorio desde fuera hace que el código sea más flexible y mucho más sencillo de probar.

## +++++++++ Conclusiones +++++++++

Durante este cuarto día terminé de estudiar los principios SOLID.

Aprendí que las interfaces deben ser pequeñas y específicas para cada necesidad.

También comprendí la importancia de depender de abstracciones en lugar de implementaciones concretas.

Finalmente entendí que la Inyección de Dependencias es una técnica que facilita las pruebas, permite reutilizar código y hace que el programa sea mucho más fácil de modificar cuando el proyecto crece.


# Día 5/Semana1

## +++++++++ Driver Modernizado +++++++++

Durante este quinto día realizamos un ejercicio integrador llamado "Driver Modernizado".

El objetivo fue tomar la idea de un driver UART desarrollado de manera tradicional en C y reestructurarlo utilizando Python moderno y los principios SOLID.

El problema del driver original era que utilizaba variables globales, mezclaba la comunicación con el procesamiento de datos y era muy complicado realizar pruebas o utilizar más de un dispositivo al mismo tiempo.

La solución consistió en dividir todo el proyecto en diferentes archivos, donde cada uno tuviera una única responsabilidad.

## +++++++++ Organización del proyecto +++++++++

El proyecto quedó organizado de la siguiente manera.

<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>

uart_driver/

config.py

parsers.py

device.py

recorder.py

__init__.py

tests/

README.md

<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>

Cada archivo cumple una función diferente.

Esto hace que el proyecto sea mucho más fácil de entender y mantener.

## +++++++++ config.py +++++++++

En este archivo desarrollamos la clase UartConfig.

La clase fue creada utilizando @dataclass junto con el parámetro frozen=True.

Esto hace que la configuración no pueda modificarse después de crear el objeto.

Dentro de esta clase almacenamos parámetros como.

Baudrate.

Paridad.

Bits de parada.

Timeout.

También agregamos una validación para comprobar que el baudrate sea mayor que cero.

Si el valor no es válido se genera una excepción.

De esta forma evitamos crear configuraciones incorrectas.

## +++++++++ parsers.py +++++++++

En este archivo desarrollamos los analizadores de mensajes.

Primero se creó una clase abstracta llamada MessageParser.

<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>

class MessageParser(ABC)

<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>

Esta clase obliga a que todos los analizadores implementen dos métodos.

can_parse()

parse()

Posteriormente se desarrollaron dos analizadores.

ModbusParser.

NMEAParser.

Cada uno solamente reconoce el protocolo que le corresponde.

Esto permite agregar nuevos protocolos sin modificar el código existente.

## +++++++++ device.py +++++++++

En este archivo desarrollamos la clase UartDevice.

Esta clase representa al dispositivo UART.

Recibe dos objetos importantes.

La configuración.

El parser.

Ambos son recibidos mediante Inyección de Dependencias.

Gracias a esto el dispositivo puede trabajar con cualquier parser que implemente la interfaz correspondiente.

También se implementaron los métodos.

connect()

disconnect()

read_and_parse()

Con estos métodos el dispositivo puede conectarse, desconectarse y analizar la información recibida.

## +++++++++ recorder.py +++++++++

Este archivo contiene la clase DataRecorder.

Su única responsabilidad consiste en guardar la información procesada.

Los datos se almacenan utilizando el formato JSON Lines.

Cada lectura se guarda en una línea independiente.

Esto facilita leer posteriormente la información sin necesidad de cargar todo el archivo.

Aquí también se aplica el principio SRP ya que solamente se encarga del almacenamiento.

## +++++++++ Tests +++++++++

Después de desarrollar todas las clases también realizamos pruebas utilizando pytest.

Las pruebas verificaron diferentes situaciones.

Configuraciones válidas.

Configuraciones inválidas.

Inmutabilidad del objeto UartConfig.

Frames Modbus válidos.

Frames Modbus inválidos.

Frames NMEA válidos.

Frames NMEA inválidos.

Dispositivo desconectado.

Guardado correcto de archivos JSON.

Cada prueba verifica solamente una parte específica del proyecto.

De esta forma resulta más sencillo localizar errores.

## +++++++++ README +++++++++

También elaboramos un archivo README.

En él agregamos una descripción general del proyecto.

La estructura de carpetas.

Cómo instalar las dependencias.

Cómo ejecutar las pruebas.

Una pequeña reflexión sobre los principios SOLID utilizados durante el desarrollo.

Además agregamos una lista de palabras clave para facilitar el estudio del proyecto.

## +++++++++ Relación con proyectos reales +++++++++

Este ejercicio fue el que más relación encontré con la programación de sistemas embebidos.

Anteriormente hubiera desarrollado todo dentro de un solo archivo.

Ahora comprendí que dividir el proyecto en varios módulos hace que el mantenimiento sea mucho más sencillo.

También entendí que utilizando diferentes clases es posible reutilizar gran parte del código sin necesidad de volver a escribir todo desde cero.

## +++++++++ Dificultades encontradas +++++++++

Este fue el ejercicio que más tiempo me tomó durante toda la semana.

Al principio me costó organizar correctamente todos los archivos del proyecto porque no estaba acostumbrado a dividir un programa en tantos módulos.

También tuve algunas dudas sobre cuándo utilizar una clase abstracta y cuándo utilizar un Protocol.

Otra dificultad fue comprender completamente la Inyección de Dependencias, ya que al principio parecía innecesario recibir objetos desde el exterior.

Después de realizar las pruebas comprendí que esto facilita mucho cambiar componentes y realizar tests.

También tuve algunos problemas ejecutando pytest, ruff y mypy porque algunas herramientas no estaban instaladas dentro del entorno virtual.

## +++++++++ Conclusiones +++++++++

Durante este quinto día pude integrar prácticamente todo lo aprendido durante la primera semana.

Comprendí que un proyecto profesional no consiste únicamente en que el programa funcione.

También debe ser fácil de mantener, probar y ampliar en el futuro.

Aprendí a organizar un proyecto en diferentes módulos, utilizar principios SOLID, realizar pruebas automáticas, escribir documentación y comprender mejor cómo se estructura un proyecto de software de tamaño mediano.

Considero que este ejercicio fue el que mejor resume todo lo aprendido durante la primera semana.


# Día 6/Semana1

## +++++++++ Cierre de la Semana +++++++++

Durante este último día el objetivo principal fue revisar que todas las actividades realizadas durante la semana funcionaran correctamente.

En lugar de desarrollar nuevas funcionalidades, el trabajo consistió en comprobar que el proyecto estuviera completo y que cumpliera con los requisitos establecidos.

También fue un día para ordenar el repositorio y preparar todo para la entrega.

## +++++++++ Revisión de los tests +++++++++

Lo primero que hice fue ejecutar nuevamente todas las pruebas desarrolladas durante la semana utilizando pytest.

El objetivo fue comprobar que todas las funciones continuaran funcionando correctamente después de los cambios realizados durante la semana.

Las pruebas abarcaron.

La Máquina de Estados Finitos.

Los principios SOLID.

El Driver Modernizado.

Con esto pude comprobar que cada módulo seguía funcionando de manera independiente.

## +++++++++ Ruff +++++++++

Otra de las herramientas utilizadas fue Ruff.

Esta herramienta analiza el estilo del código y ayuda a detectar algunos errores comunes.

Durante esta parte descubrí que Ruff no estaba instalado dentro del entorno virtual.

Por esta razón fue necesario instalarlo antes de poder ejecutar la revisión del proyecto.

Después de instalarlo fue posible revisar el código para comprobar que no existieran errores relacionados con el formato o algunas malas prácticas.

## +++++++++ mypy +++++++++

También revisamos el proyecto utilizando mypy.

Esta herramienta analiza los Type Hints utilizados durante el programa.

Su función principal consiste en detectar errores relacionados con los tipos de datos antes de ejecutar el programa.

Aunque durante esta primera semana todavía no era obligatorio, sirvió para conocer otra herramienta utilizada en proyectos profesionales.

## +++++++++ Git +++++++++

También revisé el historial de Git.

El objetivo fue comprobar que los commits realizados durante la semana fueran claros y descriptivos.

Aprendí que un commit no solamente sirve para guardar cambios.

También funciona como documentación del proyecto y permite conocer la evolución del desarrollo.

Por esta razón los mensajes deben indicar claramente qué cambio se realizó.

## +++++++++ README +++++++++

Durante este día también revisé nuevamente el archivo README.

En él verifiqué que estuvieran incluidos.

La descripción del proyecto.

La estructura de carpetas.

La forma de ejecutar los tests.

La explicación general del Driver Modernizado.

Las palabras clave aprendidas durante la semana.

Esto facilita que cualquier persona pueda entender el proyecto antes de revisar el código.

## +++++++++ Preparación para la sesión +++++++++

Una parte importante del día fue prepararme para explicar el funcionamiento del código.

El profesor indicó que durante la revisión podría preguntar cualquier línea del proyecto.

Por esta razón repasé nuevamente los archivos desarrollados durante la semana y traté de comprender el motivo por el cual cada parte del código fue escrita de esa manera.

Esto me ayudó a identificar algunos conceptos que todavía necesitaba estudiar un poco más.

## +++++++++ Dificultades encontradas +++++++++

La mayor dificultad durante este día fue configurar correctamente algunas herramientas del entorno de desarrollo.

Al ejecutar pytest aparecieron errores porque faltaba instalar el complemento pytest-cov.

También tuve problemas para ejecutar Ruff ya que no se encontraba instalado dentro del entorno virtual.

Otra dificultad fue comprender algunos mensajes de error generados por PowerShell, aunque poco a poco fui entendiendo cómo resolverlos.

Finalmente me di cuenta de que no basta con escribir código que funcione.

También es importante saber utilizar las herramientas que ayudan a comprobar la calidad del proyecto.

## +++++++++ Conclusiones +++++++++

Durante este último día comprendí que desarrollar software no consiste únicamente en escribir código.

También es necesario probarlo, documentarlo y mantenerlo organizado.

A lo largo de la semana aprendí conceptos completamente nuevos para mí como dataclass, Protocol, funciones puras, Type Hints, pruebas automáticas con pytest, principios SOLID e Inyección de Dependencias.

Aunque todavía considero que necesito practicar varios de estos temas, ahora tengo una mejor idea de cómo se organiza un proyecto de software moderno y de la importancia que tienen las pruebas y la documentación dentro del desarrollo profesional.