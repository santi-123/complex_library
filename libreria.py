import math


def suma(c1, c2):
    a = c1[0] + c2[0]
    b = c1[1] + c2[1]
    return a, b


def producto(c1, c2):
    a = (c1[0] * c2[0]) - (c1[1] * c2[1])
    b = (c1[0] * c2[1]) + (c1[1] * c2[0])
    return a, b


def resta(c1, c2):
    a = c1[0] - c2[0]
    b = c1[1] - c2[1]
    return a, b


def division(c1, c2):
    denominador = c2[0] ** 2 + c2[1] ** 2
    if denominador != 0:
        a = ((c1[0] * c2[0]) + (c1[1] * c2[1])) / denominador
        b = ((c1[1] * c2[0]) - (c1[0] * c2[1])) / denominador
        return a, b
    return "El divisor es cero"


def modulo(c1):
    resultado = (c1[0] ** 2 + c1[1] ** 2) ** (1 / 2)
    return resultado


def conjugado(c1):
    return c1[0], -1 * c1[1]


def car_pol(c1):
    return modulo(c1), math.atan2(c1[1], c1[0])


def pol_car(c1):
    return c1[0]*math.cos(c1[1]), c1[0]*math.sin(c1[1])


def fase(c1):
    return math.atan2(c1[1], c1[0])
