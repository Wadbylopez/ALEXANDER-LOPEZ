# Escritura de Archivo de Texto
# Abre (o crea) un nuevo archivo llamado my_notes.txt en modo de escritura
# 'w' significa que se abrirá el archivo para escritura
with open('my_notes.txt', 'w') as file:
    # Escribimos cuatro líneas de notas personales en el archivo
    file.write("Nota 1: El viernes tengo partido de futbol.\n")  # Primera nota
    file.write("Nota 2: Llegar temprano a casa.\n")            # Segunda nota
    file.write("Nota 3: Terminar los deberes hasta el domingo.\n")  # Tercera nota
    file.write("Nota 4: Falta una semana para acabar el semestre.\n")   # Cuarta nota

# Lectura de Archivo de Texto
# Abrimos el archivo my_notes.txt en modo de lectura
# 'r' significa que se abrirá el archivo para lectura
with open('my_notes.txt', 'r') as file:
    # Leemos el contenido del archivo línea por línea
    # Usamos un bucle para leer cada línea
    for line in file:
        # Muestra cada línea leída en la consola
        # .strip() elimina los saltos de línea al final
        print(line.strip())

# Cierre de Archivos
# Los archivos se cierran automáticamente al salir del bloque 'with'.
