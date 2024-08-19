# Librería de Operaciones con Números Complejos

Esta librería de Python brinda funciones para llevar a cabo diferentes operaciones con números complejos. Esto abarca desde operaciones simples hasta transformaciones de sus representaciones y cálculos relacionados con sus características.

## Operaciones Incluidas

La librería consta de las siguientes operaciones para números complejos, los números complejos se representan por medio de tuplas, donde la primera componente es la parte real y la segunda, la imaginaria, en caso de cordenadas polares la primer componente es el modulo y la segunda la fase:

- **Suma:** `suma(complex1, complex2)`
- **Producto:** `producto(complex1, complex2)`
- **Resta:** `resta(complex1, complex2)`
- **División:** `division(complex1, complex2)`
- **Módulo:** `modulo(complex)`
- **Conjugado:** `conjugado(complex)`
- **Conversión Polar a Cartesiano:** `pol_car(complex_polares)`
- **Conversión Cartesiano a Polar:** `car_pol(complex_cartesianas)`
- **Fase:** `fase(complex)`

## Requisitos

- [PyCharm 3.11](https://www.jetbrains.com/pycharm/)

## Uso

1. Clona este repositorio en tu máquina local.
2. Abre el proyecto en PyCharm.
3. Importa el módulo de la librería en tus scripts.
4. Utiliza las funciones de para realizar operaciones con números complejos.

## Ejemplo de Uso

```python
import math
import libreria as lc

# Suma
complex1 = (3, 5)
complex2 = (-2.6, 6.8)
result = lc.suma(complex1, complex2)
print("Suma:", result)

# Resta
complex1 = (3, 2)
complex2 = (-5, 5.2)
result = lc.resta(complex1, complex2)
print("Resta:", result)

# Multiplicación
complex1 = (2, 9)
complex2 = (4, -5)
result = lc.producto(complex1, complex2)
print("Multiplicación:", result)

# División
complex1 = (9, 5)
complex2 = (-5, 5.2)
result = lc.division(complex1, complex2)
print("División:", result)

# Módulo
complex1 = (3, 2)
result = lc.modulo(complex1)
print("Módulo:", result)

# Conjugado
complex1 = (3, 2)
result = lc.conjugado(complex1)
print("Conjugado:", result)

# Conversión cartesiano a polar
complex1 = (5, -2)
result = lc.car_pol(complex1)
print("Coordenadas polares:", result)

# Conversión polar a cartesiano
polar1 = (3, math.pi/6)
result = lc.pol_car(polar1)
print("Coordenadas cartesianas:", result)

# Fase
complex1 = (3, 2)
result = lc.fase(complex1)
print("Fase:", result)

```
## Autor
**Santiago Diaz Rojas**