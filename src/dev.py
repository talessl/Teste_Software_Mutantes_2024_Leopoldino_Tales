<<<<<<< HEAD
def dev_fun(a: int, b: int) -> int:
    return a / b


def dev_redundent(a: int, b: int) -> int:
    c = a + b
    c2 = a - b
    c3 = a / b
=======
def dev_fun(a: int, b: int) -> int:
    return a / b


def dev_redundent(a: int, b: int) -> int:
    c = a + b
    c2 = a - b
    c3 = a / b
>>>>>>> 3cd855890a236904c98c62c751d0fcb16af8fe9b
    return (c3, c, c2)