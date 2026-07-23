# Product Backlog

#       <<<<<<<< User Story 1 >>>>>>>>

## US-01: Registrar un sensor

Story Points: 2

Como operador de planta,

quiero registrar un sensor en el sistema mediante un identificador único,

para poder almacenar posteriormente sus lecturas.

### Escenario: Registrar un sensor válido

*Dado* que el sistema no contiene un sensor con id "TEMP-01"

*Cuando* registro un sensor con id "TEMP-01"

*Entonces* el sensor queda almacenado en el sistema

*Y* aparece en la lista de sensores registrados

### Escenario: Registrar un sensor duplicado

*Dado* que ya existe un sensor con id "TEMP-01"

*Cuando* intento registrar nuevamente el mismo sensor

*Entonces* el sistema responde con un error indicando que el sensor ya existe

#           <<<<<<<< User Story 2 >>>>>>>>

## US-02: Registrar una lectura de un sensor

Story Points: 3

Como operador de planta,

quiero registrar una lectura de temperatura de un sensor existente,

para mantener un historial de las mediciones realizadas.

### Escenario: Registrar una lectura válida

*Dado* que existe un sensor con id "TEMP-01"

*Cuando* registro una lectura de 24.5 °C

*Entonces* la lectura queda almacenada con estado *"OK"*

*Y* puedo consultarla posteriormente

### Escenario: Registrar una lectura para un sensor inexistente

*Dado* que no existe un sensor con id "TEMP-99"

*Cuando* intento registrar una lectura de 24.5 °C

*Entonces* el sistema responde con un error indicando que el sensor no existe


#       <<<<<<<< User Story 3 >>>>>>>>

## US-03: Consultar el historial de lecturas

Story Points: 5

Como operador de planta,

quiero consultar el historial de lecturas de un sensor,

para revisar su comportamiento a lo largo del tiempo.

### Escenario: Consultar un historial existente

*Dado* que el sensor **"TEMP-01"** tiene lecturas registradas

*Cuando* solicito el historial del sensor

*Entonces* el sistema muestra todas las lecturas almacenadas

*Y* las presenta ordenadas por fecha de registro

### Escenario: Consultar un sensor sin historial

*Dado* que el sensor **"TEMP-02"** no tiene lecturas registradas

*Cuando* solicito su historial

*Entonces* el sistema informa que no existen lecturas disponibles