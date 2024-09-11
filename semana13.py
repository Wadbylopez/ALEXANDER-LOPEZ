def calcular_temperatura_promedio(ciudades_temperaturas):
    """
    Función para calcular la temperatura promedio de varias ciudades durante un período de tiempo.

    Parámetros:
    ciudades_temperaturas (dict): Un diccionario donde la clave es el nombre de la ciudad y el valor es una lista de temperaturas.

    Retorna:
    dict: Un diccionario con el nombre de la ciudad y su temperatura promedio.
    """
    promedios = {}

    for ciudad, temperaturas in ciudades_temperaturas.items():
        promedio = sum(temperaturas) / len(temperaturas)
        promedios[ciudad] = promedio

    return promedios


# Ejemplo de uso:
ciudades_temperaturas = {
    "PUYO": [31, 30, 29, 30],  # Semana 1 a 4
    "ORELLANA": [27, 29, 25, 23],
    "AMBATO ": [28, 23, 19, 28]
}

promedios = calcular_temperatura_promedio(ciudades_temperaturas)
for ciudad, promedio in promedios.items():
    print(f"Temperatura promedio en {ciudad}: {promedio:.2f}°C")
