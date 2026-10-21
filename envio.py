def calcular_envio(peso: float, tipo: str) -> float:
    if peso <= 5 and tipo == "estandar":
        return 50

    if peso > 5 and tipo == "estandar":
        excedente = peso - 5

        return 50 + excedente * 10

    raise NotImplementedError
