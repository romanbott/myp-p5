def calcular_envio(peso: float, tipo: str) -> float:

    if peso <= 0:
        raise ValueError("El pso debe ser positivo.")

    if peso <= 5:
        costo_base = 50
    else:
        excedente = peso - 5
        costo_base = 50 + excedente * 10

    if tipo == "estandar":
        return costo_base
    return 2 * costo_base
