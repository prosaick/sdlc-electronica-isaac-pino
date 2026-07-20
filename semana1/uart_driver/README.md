# Driver UART Modernizado

## Descripción

Este proyecto consiste en la implementación de un driver UART utilizando Python y aplicando los principios SOLID.

El objetivo es reemplazar un diseño tradicional basado en variables globales y funciones independientes por una arquitectura orientada a objetos, donde cada clase tiene una responsabilidad específica y puede reutilizarse fácilmente.

El proyecto incluye:

- Configuración del puerto UART.
- Parsers para diferentes protocolos.
- Dispositivo UART.
- Registro de información en formato JSON Lines.
- Pruebas unitarias utilizando pytest.


# Estructura del proyecto

uart_driver/
│
├── __init__.py
├── config.py
├── parsers.py
├── device.py
├── recorder.py
├── README.md
│
└── tests/
    ├── test_config.py
    ├── test_parsers.py
    ├── test_device.py
    └── test_recorder.py


# Instalación

1. Clonar el repositorio.

```bash
git clone <URL_DEL_REPOSITORIO_propio.>
```

2. Entrar a la carpeta del proyecto.

```bash
cd semana1
```

3. Instalar pytest (si aún no está instalado).

```bash
pip install pytest
```

---

# Ejecutar los tests

Desde la carpeta principal ejecutar:

```bash
pytest uart_driver/tests -v
```

Si todo funciona correctamente aparecerán todos los tests como aprobados.

---

# Principios SOLID aplicados

## SRP (Single Responsibility Principle)

Cada clase tiene una única responsabilidad.

Ejemplos:

- UartConfig solamente almacena la configuración.
- DataRecorder solamente guarda información.
- UartDevice solamente administra la comunicación UART.

---

## OCP (Open Closed Principle)

Los parsers pueden ampliarse agregando nuevas clases sin modificar el código existente.

Ejemplo:

- ModbusParser
- NMEAParser

En el futuro podría agregarse un parser CAN o SPI creando una nueva clase.

---

## LSP (Liskov Substitution Principle)

Todos los parsers pueden utilizarse de la misma manera porque implementan la misma interfaz.

Esto permite intercambiarlos sin modificar el resto del programa.

---

## ISP (Interface Segregation Principle)

Las interfaces fueron separadas para que cada clase implemente únicamente los métodos que necesita.

Esto evita obligar a una clase a implementar funciones innecesarias.

---

## DIP (Dependency Inversion Principle)

UartDevice depende de la abstracción MessageParser y no de una implementación específica.

Gracias a esto es posible utilizar distintos parsers sin modificar la clase UartDevice.

---

# Reflexión

Aplicar los principios SOLID permitió dividir el proyecto en componentes pequeños y fáciles de mantener.

Cada clase realiza una tarea específica, lo que facilita la reutilización del código y la realización de pruebas unitarias.

Además, la utilización de inyección de dependencias permite cambiar implementaciones sin afectar el funcionamiento del programa.

En comparación con un driver tradicional desarrollado en C utilizando variables globales, esta implementación resulta más modular, escalable y sencilla de probar.

### Glosario de conceptos Semana 1 (palabras clave)

### Python
Lenguaje de programación de alto nivel utilizado para desarrollar todo el proyecto.

### Dataclass
Clase especial de Python que permite crear objetos para almacenar datos sin escribir manualmente el constructor.

### Frozen Dataclass
Dataclass cuyos atributos no pueden modificarse después de crear el objeto.

### Enum
Tipo de dato que permite agrupar constantes relacionadas bajo un mismo nombre.

### auto()
Función que asigna automáticamente un valor a cada elemento de una enumeración.

### Type Hint
Anotación que indica el tipo de dato que recibe o devuelve una variable o función.

### Protocol
Interfaz de Python que define qué métodos debe tener una clase, sin obligarla a heredar de otra.

### ABC (Abstract Base Class)
Clase abstracta que sirve como base para que otras clases implementen métodos obligatorios.

### Método Abstracto
Método declarado en una clase abstracta que debe implementarse en las clases hijas.

### Función pura
Función que siempre devuelve el mismo resultado para las mismas entradas y no modifica variables externas.

### JSON
Formato de texto utilizado para almacenar e intercambiar información estructurada.

### JSON Lines (.jsonl)
Archivo donde cada línea contiene un objeto JSON independiente.

### Parser
Componente encargado de interpretar un mensaje o trama y convertirlo en información útil.

### Frame
Conjunto de bytes recibido durante una comunicación serial.

### UART
Protocolo de comunicación serial asíncrona ampliamente utilizado en sistemas embebidos.

### Máquina de Estados Finitos (FSM)
Modelo que cambia entre diferentes estados según determinadas condiciones o eventos.

### Test Unitario
Prueba que verifica el correcto funcionamiento de una parte específica del programa.

### pytest
Biblioteca de Python utilizada para ejecutar pruebas unitarias.

### SRP (Single Responsibility Principle)
Principio SOLID que indica que una clase debe tener una única responsabilidad.

### OCP (Open/Closed Principle)
Principio SOLID que establece que una clase debe poder extenderse sin modificar su código existente.

### LSP (Liskov Substitution Principle)
Principio SOLID que indica que una clase hija debe poder sustituir a su clase base sin alterar el funcionamiento del programa.

### ISP (Interface Segregation Principle)
Principio SOLID que recomienda dividir interfaces grandes en varias más pequeñas y específicas.

### DIP (Dependency Inversion Principle)
Principio SOLID que indica que las clases deben depender de abstracciones y no de implementaciones concretas.

### Inyección de Dependencias
Técnica que consiste en proporcionar los objetos que una clase necesita desde el exterior, en lugar de crearlos internamente.

### Repositorio (Repository)
Clase encargada de almacenar y recuperar información.

### Inmutabilidad
Propiedad de un objeto cuyos datos no pueden modificarse después de haber sido creado.

### Commit
Registro de un conjunto de cambios realizados en un proyecto utilizando Git.

### Ruff
Herramienta que analiza el código para detectar errores de estilo y posibles problemas.

### mypy
Herramienta que verifica que los type hints sean correctos sin ejecutar el programa.