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

## Ciclo 2 - Verde

```
============================= test session starts ==============================
collected 4 items

test_envio.py ....                                                       [100%]

============================== 4 passed in 0.01s ===============================
```

## Ciclo 3 - Rojo

```
============================= test session starts ==============================
collected 6 items

test_envio.py ....FF                                                     [100%]

=================================== FAILURES ===================================
_________________________ test_envio_express_hasta_5k __________________________

    def test_envio_express_hasta_5k():
>       assert calcular_envio(3, "express") == 100
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^

test_envio.py:21:
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _

peso = 3, tipo = 'express'

    def calcular_envio(peso: float, tipo: str) -> float:
        if peso <= 5 and tipo == "estandar":
            return 50

        if peso > 5 and tipo == "estandar":
            excedente = peso - 5

            return 50 + excedente * 10

>       raise NotImplementedError
E       NotImplementedError

envio.py:10: NotImplementedError
_______________________ test_envio_express_2k_excedente ________________________

    def test_envio_express_2k_excedente():
>       assert calcular_envio(7, "express") == 140
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^

test_envio.py:25:
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _

peso = 7, tipo = 'express'

    def calcular_envio(peso: float, tipo: str) -> float:
        if peso <= 5 and tipo == "estandar":
            return 50

        if peso > 5 and tipo == "estandar":
            excedente = peso - 5

            return 50 + excedente * 10

>       raise NotImplementedError
E       NotImplementedError

envio.py:10: NotImplementedError
=========================== short test summary info ============================
FAILED test_envio.py::test_envio_express_hasta_5k - NotImplementedError
FAILED test_envio.py::test_envio_express_2k_excedente - NotImplementedError
========================= 2 failed, 4 passed in 0.03s ==========================
```

## Ciclo 3 - Verde

```
============================= test session starts ==============================
collected 6 items

test_envio.py ......                                                     [100%]

============================== 6 passed in 0.01s ===============================
```

## Ciclo 4 - Rojo

```
============================= test session starts ==============================
collected 8 items

test_envio.py ......FF                                                   [100%]

=================================== FAILURES ===================================
__________________________ test_peso_cero_es_invalido __________________________

    def test_peso_cero_es_invalido():
>       with pytest.raises(ValueError):
             ^^^^^^^^^^^^^^^^^^^^^^^^^
E       Failed: DID NOT RAISE ValueError

test_envio.py:31: Failed
________________________ test_peso_negativo_es_invalido ________________________

    def test_peso_negativo_es_invalido():
>       with pytest.raises(ValueError):
             ^^^^^^^^^^^^^^^^^^^^^^^^^
E       Failed: DID NOT RAISE ValueError

test_envio.py:36: Failed
=========================== short test summary info ============================
FAILED test_envio.py::test_peso_cero_es_invalido - Failed: DID NOT RAISE Valu...
FAILED test_envio.py::test_peso_negativo_es_invalido - Failed: DID NOT RAISE ...
========================= 2 failed, 6 passed in 0.03s ==========================
```

## Ciclo 4 - Verde

```
============================= test session starts ==============================
collected 8 items

test_envio.py ........                                                   [100%]

============================== 8 passed in 0.01s ===============================
```

## Ciclo 5 - Rojo

```
============================= test session starts ==============================
collected 9 items

test_envio.py ........F                                                  [100%]

=================================== FAILURES ===================================
______________________________ test_tipo_invalido ______________________________

    def test_tipo_invalido():
>       with pytest.raises(ValueError):
             ^^^^^^^^^^^^^^^^^^^^^^^^^
E       Failed: DID NOT RAISE ValueError

test_envio.py:41: Failed
=========================== short test summary info ============================
FAILED test_envio.py::test_tipo_invalido - Failed: DID NOT RAISE ValueError
========================= 1 failed, 8 passed in 0.02s ==========================
```

## Ciclo 5 - Verde

```
============================= test session starts ==============================
collected 9 items

test_envio.py .........                                                  [100%]

============================== 9 passed in 0.01s ===============================
```
