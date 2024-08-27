def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


def ordenar_fila(matriz, fila_a_ordenar):
    # Copiar la fila que queremos ordenar
    fila = matriz[fila_a_ordenar]

    # Ordenar la fila usando Bubble Sort
    bubble_sort(fila)

    # Asignar la fila ordenada de nuevo a la matriz
    matriz[fila_a_ordenar] = fila


# Definir la matriz bidimensional
matriz = [
    [6, 4, 3],
    [5, 2, 9],
    [1, 8, 7]
]

# Mostrar la matriz original
print("Matriz original:")
for fila in matriz:
    print(fila)

# Definir la fila que queremos ordenar (por ejemplo, la tercera fila)
fila_a_ordenar = 2

# Ordenar la fila especificada
ordenar_fila(matriz, fila_a_ordenar)

# Mostrar la matriz con la fila ordenada
print("\nMatriz con la fila ordenada:")
for fila in matriz:
    print(fila)
