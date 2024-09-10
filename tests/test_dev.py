<<<<<<< HEAD
from src.dev import dev_fun
from src.dev import dev_redundent


def test_add_fun():
    assert dev_fun(4, 4) == 1
    assert dev_fun(8, 4) == 2
    assert dev_fun(6, 2) == 3
    assert dev_fun(10, 5) == 2

def test_dev_redundent():
    
    result = dev_redundent(4, 2)
    assert result[0] == 2.0  # Esperado: 4 / 2 = 2.0
    assert result[1] == 6    # Esperado: 4 + 2 = 6
    assert result[2] == 2    # Esperado: 4 - 2 = 2

    result = dev_redundent(8, 4)
    assert result[0] == 2.0  # Esperado: 8 / 4 = 2.0
    assert result[1] == 12   # Esperado: 8 + 4 = 12
    assert result[2] == 4    # Esperado: 8 - 4 = 4

    result = dev_redundent(6, 2)
    assert result[0] == 3.0  # Esperado: 6 / 2 = 3.0
    assert result[1] == 8    # Esperado: 6 + 2 = 8
    assert result[2] == 4    # Esperado: 6 - 2 = 4

    result = dev_redundent(10, 5)
    assert result[0] == 2.0  # Esperado: 10 / 5 = 2.0
    assert result[1] == 15   # Esperado: 10 + 5 = 15
    assert result[2] == 5    # Esperado: 10 - 5 = 5

    # Testes adicionais para garantir cobertura completa
    result = dev_redundent(10, 2)
    assert result[0] == 5.0  # Esperado: 10 / 2 = 5.0
    assert result[1] == 12   # Esperado: 10 + 2 = 12
    assert result[2] == 8    # Esperado: 10 - 2 = 8

    result = dev_redundent(20, 4)
    assert result[0] == 5.0  # Esperado: 20 / 4 = 5.0
    assert result[1] == 24   # Esperado: 20 + 4 = 24
    assert result[2] == 16   # Esperado: 20 - 4 = 16

    result = dev_redundent(5, 1)
    assert result[0] == 5.0  # Esperado: 5 / 1 = 5.0
    assert result[1] == 6    # Esperado: 5 + 1 = 6
    assert result[2] == 4    # Esperado: 5 - 1 = 4

    result = dev_redundent(15, 3)
    assert result[0] == 5.0  # Esperado: 15 / 3 = 5.0
    assert result[1] == 18   # Esperado: 15 + 3 = 18
    assert result[2] == 12   # Esperado: 15 - 3 = 12

    # Testes com números decimais
    result = dev_redundent(10, 3)
    assert result[0] == 3.3333333333333335  # Esperado: 10 / 3 ≈ 3.333...
    assert result[1] == 13   # Esperado: 10 + 3 = 13
    assert result[2] == 7    # Esperado: 10 - 3 = 7

    # Teste para verificar tratamento de divisão por zero
    try:
        dev_redundent(1, 0)
    except ZeroDivisionError:
        pass  # Esperado: ZeroDivisionError
    else:
        assert False, "Expected ZeroDivisionError"

    # Testes para verificar alterações em c = a + b e c2
    result = dev_redundent(6, 3)
    assert result[0] == 2.0  # Para verificar c = a / b
    assert result[1] == 9    # Esperado: 6 + 3 = 9
    assert result[2] == 3    # Esperado: 6 - 3 = 3

    result = dev_redundent(7, 2)
    assert result[0] == 3.5  # Para verificar c = a / b
    assert result[1] == 9    # Esperado: 7 + 2 = 9
    assert result[2] == 5    # Esperado: 7 - 2 = 5

    result = dev_redundent(3, 1)
    assert result[0] == 3.0  # Para verificar c = a / b
    assert result[1] == 4    # Esperado: 3 + 1 = 4
=======
from src.dev import dev_fun
from src.dev import dev_redundent


def test_add_fun():
    assert dev_fun(4, 4) == 1
    assert dev_fun(8, 4) == 2
    assert dev_fun(6, 2) == 3
    assert dev_fun(10, 5) == 2

def test_dev_redundent():
    
    result = dev_redundent(4, 2)
    assert result[0] == 2.0  # Esperado: 4 / 2 = 2.0
    assert result[1] == 6    # Esperado: 4 + 2 = 6
    assert result[2] == 2    # Esperado: 4 - 2 = 2

    result = dev_redundent(8, 4)
    assert result[0] == 2.0  # Esperado: 8 / 4 = 2.0
    assert result[1] == 12   # Esperado: 8 + 4 = 12
    assert result[2] == 4    # Esperado: 8 - 4 = 4

    result = dev_redundent(6, 2)
    assert result[0] == 3.0  # Esperado: 6 / 2 = 3.0
    assert result[1] == 8    # Esperado: 6 + 2 = 8
    assert result[2] == 4    # Esperado: 6 - 2 = 4

    result = dev_redundent(10, 5)
    assert result[0] == 2.0  # Esperado: 10 / 5 = 2.0
    assert result[1] == 15   # Esperado: 10 + 5 = 15
    assert result[2] == 5    # Esperado: 10 - 5 = 5

    # Testes adicionais para garantir cobertura completa
    result = dev_redundent(10, 2)
    assert result[0] == 5.0  # Esperado: 10 / 2 = 5.0
    assert result[1] == 12   # Esperado: 10 + 2 = 12
    assert result[2] == 8    # Esperado: 10 - 2 = 8

    result = dev_redundent(20, 4)
    assert result[0] == 5.0  # Esperado: 20 / 4 = 5.0
    assert result[1] == 24   # Esperado: 20 + 4 = 24
    assert result[2] == 16   # Esperado: 20 - 4 = 16

    result = dev_redundent(5, 1)
    assert result[0] == 5.0  # Esperado: 5 / 1 = 5.0
    assert result[1] == 6    # Esperado: 5 + 1 = 6
    assert result[2] == 4    # Esperado: 5 - 1 = 4

    result = dev_redundent(15, 3)
    assert result[0] == 5.0  # Esperado: 15 / 3 = 5.0
    assert result[1] == 18   # Esperado: 15 + 3 = 18
    assert result[2] == 12   # Esperado: 15 - 3 = 12

    # Testes com números decimais
    result = dev_redundent(10, 3)
    assert result[0] == 3.3333333333333335  # Esperado: 10 / 3 ≈ 3.333...
    assert result[1] == 13   # Esperado: 10 + 3 = 13
    assert result[2] == 7    # Esperado: 10 - 3 = 7

    # Teste para verificar tratamento de divisão por zero
    try:
        dev_redundent(1, 0)
    except ZeroDivisionError:
        pass  # Esperado: ZeroDivisionError
    else:
        assert False, "Expected ZeroDivisionError"

    # Testes para verificar alterações em c = a + b e c2
    result = dev_redundent(6, 3)
    assert result[0] == 2.0  # Para verificar c = a / b
    assert result[1] == 9    # Esperado: 6 + 3 = 9
    assert result[2] == 3    # Esperado: 6 - 3 = 3

    result = dev_redundent(7, 2)
    assert result[0] == 3.5  # Para verificar c = a / b
    assert result[1] == 9    # Esperado: 7 + 2 = 9
    assert result[2] == 5    # Esperado: 7 - 2 = 5

    result = dev_redundent(3, 1)
    assert result[0] == 3.0  # Para verificar c = a / b
    assert result[1] == 4    # Esperado: 3 + 1 = 4
>>>>>>> 3cd855890a236904c98c62c751d0fcb16af8fe9b
    assert result[2] == 2    # Esperado: 3 - 1 = 2