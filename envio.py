"""Calcula el costo de envio de un paquete segun su peso y tipo de servicio."""

from enum import StrEnum

PESO_INCLUIDO = 5
TARIFA_BASE = 50
COSTO_KILO_EXCEDENTE = 10


class TipoEnvio(StrEnum):
    """Tipos de envio aceptados, con su factor sobre la tarifa base."""

    ESTANDAR = "estandar"
    EXPRESS = "express"

    @property
    def multiplicador(self) -> int:
        """Factor que se aplica a la tarifa base."""
        match self:
            case TipoEnvio.ESTANDAR:
                return 1
            case TipoEnvio.EXPRESS:
                return 2


def calcular_envio(peso: float, tipo: str) -> float:
    """Calcula el costo de envio de un paquete de `peso` kg.

    Lanza ValueError si el peso no es positivo o si el tipo no es valido.
    """
    if peso <= 0:
        raise ValueError("El peso debe ser positivo.")

    try:
        servicio = TipoEnvio(tipo)
    except ValueError:
        raise ValueError(f"Tipo de envio invalido: {tipo!r}")

    excedente = max(peso - PESO_INCLUIDO, 0)
    return (TARIFA_BASE + excedente * COSTO_KILO_EXCEDENTE) * servicio.multiplicador
