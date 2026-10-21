from envio import calcular_envio


def test_envio_estandar_hasta_5k():
    assert calcular_envio(3, "estandar") == 50
