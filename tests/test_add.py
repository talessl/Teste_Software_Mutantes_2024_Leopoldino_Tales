from src.add import add_fun
from src.multi import multi_fun
from src.add import redundant_add

def test_add_fun():
    assert add_fun(1, 4) == 5
    assert add_fun(2, 4) == 6
    assert add_fun(3, 4) == 7
    assert add_fun(6, 4) == 10


def test_add_fun2():
    assert add_fun(5, 5) == 10
    assert add_fun(2, 4) == 6
    assert add_fun(3, 4) == 7
    assert add_fun(6, 12) == 18


def test_multi_fun():
    assert multi_fun(1, 4) == 4
    assert multi_fun(2, 4) == 8
    assert multi_fun(3, 4) == 12
    assert multi_fun(6, 4) == 24

def test_redundant_add():
    assert redundant_add(2, 3) == 5  # Este deve passar
    assert redundant_add(-1, 1) == 0  # Este deve passar
    assert redundant_add(0, 0) == 0  # Este deve passar
    assert redundant_add(1, 2) == 3  # Adicionando mais casos
    assert redundant_add(-3, -2) == -5  # Números negativos
    assert redundant_add(10, -10) == 0  # Positivo e negativo
    assert redundant_add(1000, 500) == 1500  # Números grandes
    assert redundant_add(7, 5) == 12  # Mais casos

    # Adicionando casos extremos
    assert redundant_add(1, 1) == 2  # Caso simples
    assert redundant_add(-1, -1) == -2  # Caso simples negativos
    assert redundant_add(0, 1) == 1  # Zero e positivo
    assert redundant_add(1, 0) == 1  # Positivo e zero