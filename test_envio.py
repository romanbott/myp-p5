from envio import calcular_envio


def test_envio_estandar_hasta_5k():
    assert calcular_envio(3, "estandar") == 50


def test_envio_estandar_5k():
    assert calcular_envio(5, "estandar") == 50


def test_envio_estandar_1k_excedente():
    assert calcular_envio(6, "estandar") == 60


def test_envio_estandar_2k_excedente():
    assert calcular_envio(7, "estandar") == 70


def test_envio_express_hasta_5k():
    assert calcular_envio(3, "express") == 100


def test_envio_express_2k_excedente():
    assert calcular_envio(7, "express") == 140
