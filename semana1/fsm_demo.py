## Día 2: FSM (Finite State Machine) para un semáforo


from enum import Enum, auto  # Enum sirve para crear enumeraciones o agrupar valores relacionados.



class TrafficLightState(Enum):  # Define una clase Enum para representar los posibles estados del semáforo.

    RED = auto()  # Crea el estado RED y le asigna automáticamente un valor interno.

    YELLOW = auto()  # Crea el estado YELLOW y le asigna automáticamente un valor interno.

    GREEN = auto()  # Crea el estado GREEN y le asigna automáticamente un valor interno.



class TrafficLightFSM:  # Define una clase que representa la máquina de estados del semáforo.

    def __init__(self) -> None:  # Se ejecuta automáticamente al crear un nuevo objeto.

        self._state = TrafficLightState.RED  # Establece el estado inicial del semáforo en rojo.

        self._cycle_count = 0  # Inicializa el contador de transiciones en cero.



    @property  # Permite acceder al método como si fuera un atributo.

    def state(self) -> TrafficLightState:  # Devuelve el estado actual del semáforo.

        return self._state


    @property  # Permite acceder al método como si fuera un atributo.

    def cycle_count(self) -> int:  # Devuelve la cantidad de transiciones realizadas.

        return self._cycle_count



    def transition(self) -> TrafficLightState:  # Cambia el estado actual del semáforo.

        if self._state == TrafficLightState.RED:  # Comprueba si el estado actual es RED.

            self._state = TrafficLightState.GREEN  # Cambia el estado a GREEN.

        elif self._state == TrafficLightState.GREEN:  # Comprueba si el estado actual es GREEN.

            self._state = TrafficLightState.YELLOW  # Cambia el estado a YELLOW.

        else:  # Si no es RED ni GREEN, solamente puede ser YELLOW.

            self._state = TrafficLightState.RED  # Cambia nuevamente al estado RED.

        self._cycle_count += 1  # Incrementa el contador cada vez que ocurre una transición.

        return self._state  # Devuelve el nuevo estado del semáforo.