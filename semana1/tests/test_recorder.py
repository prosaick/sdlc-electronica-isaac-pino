# Dia 5: Tests de recorder.py

import json

from uart_driver.recorder import DataRecorder


def test_json_line(tmp_path):  # Comprueba que DataRecorder escriba un objeto JSON por línea.

    archivo = tmp_path / "datos.jsonl"

    recorder = DataRecorder(

        str(archivo)

    )

    datos = {

        "sensor": "TEMP01",

        "value": 25.5

    }

    recorder.save(datos)

    contenido = archivo.read_text(

        encoding="utf-8"

    ).strip()

    assert json.loads(contenido) == datos


def test_multiple_lines(tmp_path):  # Comprueba que puedan guardarse varias líneas JSON.

    archivo = tmp_path / "datos.jsonl"

    recorder = DataRecorder(

        str(archivo)

    )

    recorder.save(

        {"id": 1}

    )

    recorder.save(

        {"id": 2}

    )

    lineas = archivo.read_text(

        encoding="utf-8"

    ).splitlines()

    assert len(lineas) == 2


def test_empty_file(tmp_path):  # Comprueba que el archivo exista después de guardar información.

    archivo = tmp_path / "datos.jsonl"

    recorder = DataRecorder(

        str(archivo)

    )

    recorder.save(

        {"ok": True}

    )

    assert archivo.exists()