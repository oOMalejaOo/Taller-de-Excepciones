#Programa de inventario de zapatos que valide si una talla, color, tipo de zapatos está disponible.

inventario = {
    "tenis": {
        "talla": [35, 36, 37, 38, 39, 40],
        "color": ["rojo", "azul", "negro", "blanco"]
    },
    "tacones": {
        "talla": [36, 38, 40],
        "color": ["rojo", "negro", "café"],
        "tipo": ["alto", "bajo"]
    }
}

def validar_inventario(tipo, talla, color, inventario, tipo_tacon=None):

    if tipo not in inventario:
        raise ValueError("El tipo de zapato no existe")

    datos = inventario[tipo]

    if color not in datos["color"]:
        raise ValueError("Color no disponible")

    if talla not in datos["talla"]:
        raise ValueError("Talla no disponible")

    if tipo == "tacones":
        if tipo_tacon not in datos["tipo"]:
            raise ValueError("Tipo de tacón no disponible")

    return True


try:
    tipo = input("Ingrese el tipo de zapato (Tenis y Tacones): ").lower()
    talla = int(input("Ingrese la talla: "))
    color = input("Ingrese el color: ").lower()

    tipo_tacon = None
    if tipo == "tacones":
        tipo_tacon = input("Ingrese el tipo de tacón (alto/bajo): ").lower()

    validar_inventario(tipo, talla, color, inventario, tipo_tacon)

    print("Zapato disponible :)")

except ValueError as e:
    print(f"Error: {e} X")

except Exception:
    print("Entrada inválida :(")