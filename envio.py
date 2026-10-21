def calcular_envio(peso: float, tipo: str) -> float:

    if peso <= 0:
        raise ValueError("El peso debe ser positivo.")

    if tipo not in ["estandar", "express"]:
        raise ValueError("El tipo debe ser 'estandar' o 'express'")

    if peso <= 5:
        costo_base = 50
    else:
        excedente = peso - 5
        costo_base = 50 + excedente * 10

    if tipo == "estandar":
        return costo_base
    return 2 * costo_base
