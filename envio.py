from enum import StrEnum

PESO_INCLUIDO = 5
TARIFA_BASE = 50
COSTO_KILO_EXCEDENTE = 10


class TipoEnvio(StrEnum):
    ESTANDAR = "estandar"
    EXPRESS = "express"

    @property
    def multiplicador(self) -> int:
        match self:
            case TipoEnvio.ESTANDAR:
                return 1
            case TipoEnvio.EXPRESS:
                return 2


def calcular_envio(peso: float, tipo: str) -> float:
    if peso <= 0:
        raise ValueError("El peso debe ser positivo.")

    try:
        servicio = TipoEnvio(tipo)
    except ValueError:
        raise ValueError(f"Tipo de envio invalido: {tipo!r}")

    excedente = max(peso - PESO_INCLUIDO, 0)
    return (TARIFA_BASE + excedente * COSTO_KILO_EXCEDENTE) * servicio.multiplicador
