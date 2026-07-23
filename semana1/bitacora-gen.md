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



## ++++++++++ serialización +++++++++