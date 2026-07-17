# Dia 5: Registro de datos

import json  # Permite trabajar con formato JSON.



class DataRecorder:  # Guarda los datos parseados en formato JSON Lines.

    def __init__(self, filename: str):

        self._filename = filename  # Guarda el nombre del archivo.



    def save(self, data: dict):

        # Abre el archivo en modo agregar.

        with open(self._filename, "a", encoding="utf-8") as file:

            # Guarda un objeto JSON por línea.

            json.dump(data, file)

            file.write("\n")