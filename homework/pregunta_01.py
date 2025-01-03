# pylint: disable=import-outside-toplevel
# pylint: disable=line-too-long
# flake8: noqa
"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta.
"""


import zipfile
import os
import glob
import fileinput
import pandas as pd


def pregunta_01():
    """
    La información requerida para este laboratio esta almacenada en el
    archivo "files/input.zip" ubicado en la carpeta raíz.
    Descomprima este archivo.

    Como resultado se creara la carpeta "input" en la raiz del
    repositorio, la cual contiene la siguiente estructura de archivos:


    ```
    train/
        negative/
            0000.txt
            0001.txt
            ...
        positive/
            0000.txt
            0001.txt
            ...
        neutral/
            0000.txt
            0001.txt
            ...
    test/
        negative/
            0000.txt
            0001.txt
            ...
        positive/
            0000.txt
            0001.txt
            ...
        neutral/
            0000.txt
            0001.txt
            ...
    ```

    A partir de esta informacion escriba el código que permita generar
    dos archivos llamados "train_dataset.csv" y "test_dataset.csv". Estos
    archivos deben estar ubicados en la carpeta "output" ubicada en la raiz
    del repositorio.

    Estos archivos deben tener la siguiente estructura:

    * phrase: Texto de la frase. hay una frase por cada archivo de texto.
    * sentiment: Sentimiento de la frase. Puede ser "positive", "negative"
      o "neutral". Este corresponde al nombre del directorio donde se
      encuentra ubicado el archivo.

    Cada archivo tendria una estructura similar a la siguiente:

    ```
    |    | phrase                                                                                                                                                                 | target   |
    |---:|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|
    |  0 | Cardona slowed her vehicle , turned around and returned to the intersection , where she called 911                                                                     | neutral  |
    |  1 | Market data and analytics are derived from primary and secondary research                                                                                              | neutral  |
    |  2 | Exel is headquartered in Mantyharju in Finland                                                                                                                         | neutral  |
    |  3 | Both operating profit and net sales for the three-month period increased , respectively from EUR16 .0 m and EUR139m , as compared to the corresponding quarter in 2006 | positive |
    |  4 | Tampere Science Parks is a Finnish company that owns , leases and builds office properties and it specialises in facilities for technology-oriented businesses         | neutral  |
    ```


    """
    zip_path = "files/input.zip"
    descomprimir_tarea(zip_path)
    directory_test = "files/input/input/test"
    directory_train = "files/input/input/train"
    test = iterar_en_carpetas(directory_test)
    train = iterar_en_carpetas(directory_train)
    # Crear la carpeta output si no existe
    output_dir = "files/output"
    os.makedirs(output_dir, exist_ok=True)

    # Rutas de los archivos CSV
    test_csv = os.path.join(output_dir, "test_dataset.csv")
    train_csv = os.path.join(output_dir, "train_dataset.csv")

    # Guardar los DataFrames como archivos CSV
    test.to_csv(test_csv, index=False)
    train.to_csv(train_csv, index=False)

    # Confirmar y devolver las rutas de los archivos generados
    print(f"Archivos generados:\nTest: {test_csv}\nTrain: {train_csv}")
    return test_csv, train_csv


def descomprimir_tarea(zip_path):
    if not os.path.exists(zip_path):
        print(f"El archivo {zip_path} no existe.")
        return
    
    extract_path = os.path.splitext(zip_path)[0]
    
    try:
        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            zip_ref.extractall(extract_path)
        print(f"Archivo descomprimido en: {extract_path}")
    except zipfile.BadZipFile:
        print(f"El archivo {zip_path} no es un archivo ZIP válido.")

def iterar_en_carpetas(directory):
    sequences = []
    files = [f for f in glob.glob(f"{directory}/**", recursive=True) if os.path.isfile(f)]
    
    if not files:
        return sequences
    
    with fileinput.input(files=files) as file:
        for line in file:
            folder_name = os.path.basename(os.path.dirname(fileinput.filename()))
            sequences.append((folder_name, line.strip())) 
    df1 = pd.DataFrame(sequences, columns=["target", "phrase"])
    df = df1[['phrase', 'target']]

    return df

if __name__ == "__main__":
    pregunta_01()
