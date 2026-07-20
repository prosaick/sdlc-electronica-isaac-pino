## Dia 2: FSM (Finite State Machine) para un semáforo


from fsm_demo import TrafficLightFSM, TrafficLightState  # Importa la clase del semáforo y la enumeración de estados.



def test_initial_state():  # Comprueba que el estado inicial sea RED.

    semaforo = TrafficLightFSM()  # Crea un nuevo semáforo.

    assert semaforo.state == TrafficLightState.RED  # Verifica que el estado inicial sea RED.



def test_red_to_green():  # Comprueba la transición de RED a GREEN.

    semaforo = TrafficLightFSM()  # Crea un nuevo semáforo.

    semaforo.transition()  # Realiza una transición.

    assert semaforo.state == TrafficLightState.GREEN  # Verifica que el estado ahora sea GREEN.



def test_complete_cycle():  # Comprueba que un ciclo completo regrese al estado RED.

    semaforo = TrafficLightFSM()  # Crea un nuevo semáforo.

    semaforo.transition()  # RED -> GREEN.

    semaforo.transition()  # GREEN -> YELLOW.

    semaforo.transition()  # YELLOW -> RED.

    assert semaforo.state == TrafficLightState.RED  # Comprueba que regresó a RED.



def test_cycle_counter():  # Comprueba que el contador aumente después de las transiciones.

    semaforo = TrafficLightFSM()  # Crea un nuevo semáforo.

    semaforo.transition()  # Primera transición.

    semaforo.transition()  # Segunda transición.

    semaforo.transition()  # Tercera transición.

    assert semaforo.cycle_count == 3  # Verifica que se realizaron tres transiciones.