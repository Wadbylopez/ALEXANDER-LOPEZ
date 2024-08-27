def buscar_valor_en_matriz(matriz, valor_buscado):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] == valor_buscado:
                return (i, j)
    return None

# Definir la matriz bidimensional
matriz = [
    [4, 6, 11],
    [7, 1, 8],
    [2, 4, 5]
]

# Definir el valor que quieres buscar
valor_buscado = 11

# Llamar a la función de búsqueda
resultado = buscar_valor_en_matriz(matriz, valor_buscado)

# Mostrar el resultado
if resultado:
    print(f"Valor {valor_buscado} encontrado en la posición: {resultado}")
else:
    print(f"Valor {valor_buscado} no encontrado en la matriz.")
