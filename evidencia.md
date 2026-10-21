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
