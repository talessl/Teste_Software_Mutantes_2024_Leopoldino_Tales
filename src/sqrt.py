from math import sqrt


def sqrt_fun(a: int) -> int:
    b = sqrt(a)
    c = int(b)
    return c


def redundant_sqrt(a: int, b: int) -> int:
    c = a+b
    return c

