def calcular_envio(peso: float, tipo: str) -> float:

    if peso <= 5 and tipo == "estandar":
        return 50

    raise NotImplementedError
