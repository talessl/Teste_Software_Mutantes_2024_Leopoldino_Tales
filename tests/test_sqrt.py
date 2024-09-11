from src.sqrt import sqrt_fun


def test_sqrt_fun():
    assert sqrt_fun(4) == 2
    assert sqrt_fun(8) == 2
    assert sqrt_fun(6) == 2
    assert sqrt_fun(10) == 3