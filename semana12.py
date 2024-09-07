# Crear una matriz 3D que representa ciudades, días de la semana y semanas
# Ejemplo: 2 ciudades, 7 días de la semana, 2 semanas
temperaturas = [
    [  # Ciudad 1
        [14, 16, 18, 19, 17, 20, 15],  # Semana 1 (Lunes a Domingo)
        [21, 22, 26, 24, 23, 25, 27]  # Semana 2 (Lunes a Domingo)
    ],
    [  # Ciudad 2
        [31, 32, 33, 31, 30, 32, 35],  # Semana 1 (Lunes a Domingo)
        [29, 28, 30, 31, 32, 30, 31]  # Semana 2 (Lunes a Domingo)
    ]
]

# Lista de nombres de las ciudades
ciudades = ["Ciudad 1", "Ciudad 2"]

# Calcular el promedio de temperaturas por ciudad y semana
for ciudad in range(len(temperaturas)):  # Recorrer ciudades
    print(f"\nPromedio de temperaturas para {ciudades[ciudad]}:")
    for semana in range(len(temperaturas[ciudad])):  # Recorrer semanas
        suma_temperaturas = 0
        dias_semana = len(temperaturas[ciudad][semana])  # Número de días en la semana
        for dia in range(dias_semana):  # Recorrer días de la semana
            suma_temperaturas += temperaturas[ciudad][semana][dia]

        # Calcular el promedio de la semana
        promedio_semana = suma_temperaturas / dias_semana
        print(f"Semana {semana + 1}: {promedio_semana:.2f}°C")
