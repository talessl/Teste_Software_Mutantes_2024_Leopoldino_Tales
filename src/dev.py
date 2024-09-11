def dev_fun(a: int, b: int) -> int:
    return a / b


def dev_redundent(a: int, b: int) -> int:
    c = a + b
    c2 = a - b
    c3 = a / b
    return (c3, c, c2)