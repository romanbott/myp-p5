# TDD

## Ciclo 1 - Rojo

```
============================= test session starts ==============================
collected 1 item

test_envio.py F                                                          [100%]

=================================== FAILURES ===================================
_________________________ test_envio_estandar_hasta_5k _________________________

    def test_envio_estandar_hasta_5k():
>       assert calcular_envio(3, "estandar") == 50
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

test_envio.py:5:
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _

peso = 3, tipo = 'estandar'

    def calcular_envio(peso: float, tipo: str):
>       raise NotImplementedError
E       NotImplementedError

envio.py:2: NotImplementedError
=========================== short test summary info ============================
FAILED test_envio.py::test_envio_estandar_hasta_5k - NotImplementedError
============================== 1 failed in 0.02s ===============================
```

## Ciclo 1 - Verde

```
============================= test session starts ==============================
collected 1 item

test_envio.py .                                                          [100%]

============================== 1 passed in 0.01s ===============================
```

## Ciclo 2 - Rojo

```
============================= test session starts ==============================
collected 4 items

test_envio.py ..FF                                                       [100%]

=================================== FAILURES ===================================
_______________________ test_envio_estandar_1k_excedente _______________________

    def test_envio_estandar_1k_excedente():
>       assert calcular_envio(6, "estandar") == 60
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

test_envio.py:13:
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _

peso = 6, tipo = 'estandar'

    def calcular_envio(peso: float, tipo: str) -> float:

        if peso <= 5 and tipo == "estandar":
            return 50

>       raise NotImplementedError
E       NotImplementedError

envio.py:6: NotImplementedError
_______________________ test_envio_estandar_2k_excedente _______________________

    def test_envio_estandar_2k_excedente():
>       assert calcular_envio(7, "estandar") == 70
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

test_envio.py:17:
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _

peso = 7, tipo = 'estandar'

    def calcular_envio(peso: float, tipo: str) -> float:

        if peso <= 5 and tipo == "estandar":
            return 50

>       raise NotImplementedError
E       NotImplementedError

envio.py:6: NotImplementedError
=========================== short test summary info ============================
FAILED test_envio.py::test_envio_estandar_1k_excedente - NotImplementedError
FAILED test_envio.py::test_envio_estandar_2k_excedente - NotImplementedError
========================= 2 failed, 2 passed in 0.02s ==========================
```
