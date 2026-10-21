# Práctica 5: desarrollo de una funcionalidad siguiendo TDD

Modelado y Programación

Implementación de `calcular_envio(peso, tipo)`, que calcula el costo de envío de
un paquete según su peso en kilogramos y el tipo de servicio (`estandar` o
`express`). El desarrollo se hizo en ciclos ROJO → VERDE → refactorización y la
evidencia de cada ciclo está en `evidencia.md`.

## Registro de ciclos

Cada ciclo comenzó con una prueba en ROJO; la salida de pytest de cada estado
está en `evidencia.md`.

| Ciclo           | Prueba agregada                                                                                 | Cambio realizado                                                                             | Resultado                             |
| --------------- | ----------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | ------------------------------------- |
| 1               | `test_envio_estandar_hasta_5k` (3 kg -> $50)                                                    | `return 50` fijo                                                                             | ROJO (`NotImplementedError`) -> VERDE |
| 2               | `test_envio_estandar_1k_excedente` (6 kg -> $60), más los casos límite de 5 kg y 7 kg           | costo base más $10 por cada kilo excedente                                                   | ROJO -> VERDE                         |
| 3               | `test_envio_express_hasta_5k` (3 kg -> $100) y `test_envio_express_2k_excedente` (7 kg -> $140) | cálculo de un costo base que después se multiplica según el tipo                             | ROJO -> VERDE                         |
| 4               | `test_peso_cero_es_invalido` y `test_peso_negativo_es_invalido`                                 | `ValueError` si el peso no es positivo, antes de calcular                                    | ROJO (`DID NOT RAISE`) -> VERDE       |
| 5               | `test_tipo_invalido` ("urgente")                                                                | `ValueError` si el tipo de envío no era válido                                               | ROJO (`DID NOT RAISE`) -> VERDE       |
| Refactorización | —                                                                                               | constantes con nombre, `max()` para el excedente, `StrEnum` con su multiplicador, docstrings | 9 pruebas en VERDE                    |

## Cómo ejecutar

Con uv:

```bash
uv sync
uv run pytest -v
```

Con Python y pytest ya instalados:

```bash
python -m pytest -v
```

El código usa `StrEnum`, así que requiere Python 3.11 o superior.

## Reflexión final

La prueba de envío express fue la que me obligó a cambiar el diseño:
en lugar de repetir la fórmula del peso para cada tipo, fue mejor primero calcular un costo base y luego multiplicarlo por dos para el caso de envíos express.

Refactorizar sin romper el funcionamiento del código fue muy sencillo gracias a los tests ya implementados.

Lo más difícil fue aceptar que una implementación incompleta, como la primera versión de la función era el paso correcto, en vez de adelantar todos los requisitos desde el inicio.
