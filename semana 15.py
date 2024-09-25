# Crear el diccionario llamado 'informacion_personal' con datos ficticios
informacion_personal = {
    "nombre": "Alexander lopez",
    "edad": 22,
    "ciudad": "Puyo",
    "profesion": "Ingeniero"
}

# Acceder al valor de la clave "ciudad" y modificarlo
# Aquí se accede a la ciudad actual y luego se cambia
print(f"Ciudad actual: {informacion_personal['ciudad']}")  # Mostrar la ciudad actual
informacion_personal["ciudad"] = "Ambato"  # Cambiar la ciudad
print(f"Ciudad modificada: {informacion_personal['ciudad']}")  # Mostrar la ciudad modificada

# Agregar una nueva clave-valor para la profesión (aunque ya existe, la cambiaremos por otra)
informacion_personal["profesion"] = "Desarrollador de Software"  # Cambiar la profesión

# Verificar si la clave "telefono" existe en el diccionario
# Si no existe, se agrega un número de teléfono ficticio
if "telefono" not in informacion_personal:
    informacion_personal["telefono"] = "0984321167"  # Agregar número de teléfono ficticio

# Eliminar la clave "edad" porque no es necesaria
del informacion_personal["edad"]

# Imprimir el diccionario final después de las modificaciones
print("Diccionario final:", informacion_personal)
