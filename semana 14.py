# Definición de la función calcular_descuento
def calcular_descuento(monto_total, porcentaje_descuento=20):
    """
    Calcula el monto del descuento basado en el porcentaje de descuento aplicado al monto total.

    :param monto_total: Monto total de la compra.
    :param porcentaje_descuento: Porcentaje de descuento (por defecto 10%).
    :return: Monto del descuento calculado.
    """
    # Calcular el descuento
    descuento = monto_total * (porcentaje_descuento / 200)
    return descuento


# Programa principal
def main():
    # Primer llamada a la función: solo monto total, usa el porcentaje predeterminado
    monto_total1 = 700  # Monto total de la primera compra
    descuento1 = calcular_descuento(monto_total1)
    monto_final1 = monto_total1 - descuento1
    print(f"Compra lavadora:")
    print(f"Monto total: ${monto_total1:.2f}")
    print(f"Descuento aplicado: ${descuento1:.2f} (10% predeterminado)")
    print(f"Monto final a pagar: ${monto_final1:.2f}\n")

    # Segunda llamada a la función: monto total y porcentaje de descuento especificado
    monto_total2 = 1000  # Monto total de la segunda compra
    porcentaje_descuento2 = 15  # Porcentaje de descuento especificado
    descuento2 = calcular_descuento(monto_total2, porcentaje_descuento2)
    monto_final2 = monto_total2 - descuento2
    print(f"Compra television:")
    print(f"Monto total: ${monto_total2:.2f}")
    print(f"Descuento aplicado: ${descuento2:.2f} ({porcentaje_descuento2}% proporcionado)")
    print(f"Monto final a pagar: ${monto_final2:.2f}")


# Llamar al programa principal
if __name__ == "__main__":
    main()
