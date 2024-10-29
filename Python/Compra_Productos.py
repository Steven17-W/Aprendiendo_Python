def calculadora_compras():
    """
    Calcula el total de una compra, aplica un descuento y divide el costo.
    Utiliza funciones predefinidas para las operaciones básicas.
    """

    # Obtener datos del usuario
    producto1 = input("Ingrese el nombre del primer producto: ")
    precio1 = float(input(f"Ingrese el precio de {producto1}: "))
    cantidad1 = int(input(f"Ingrese la cantidad de {producto1}: "))

    producto2 = input("Ingrese el nombre del segundo producto: ")
    precio2 = float(input(f"Ingrese el precio de {producto2}: "))
    cantidad2 = int(input(f"Ingrese la cantidad de {producto2}: "))

    # Calcular el costo total de cada producto
    costo_producto1 = (precio1, cantidad1)
    costo_producto2 = (precio2, cantidad2)

    # Calcular el costo total de la compra
    costo_total = (costo_producto1, costo_producto2)
    print(f"El costo total de la compra es: {costo_total}")

    # Aplicar descuento (Puedes ajustar el porcentaje del descuento)
    descuento = 0.1  # 10% de descuento
    costo_con_descuento = (costo_total, (1 - descuento))
    print(f"El costo total con descuento es: {costo_con_descuento}")

    # Dividir el costo entre personas
    num_personas = int(input("Ingrese el número de personas: "))
    costo_por_persona = (costo_con_descuento, num_personas)
    if costo_por_persona is not None:  # Verificar si la división se realizó correctamente
        print(f"Cada persona debe pagar: {costo_por_persona}")

# Llamada a la función principal
calculadora_compras()