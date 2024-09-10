<<<<<<< HEAD
from src.sqrt import redundant_sqrt, sqrt_fun

def test_sqrt_fun():
    
    assert sqrt_fun(4) == 2
    assert sqrt_fun(9) == 3
    assert sqrt_fun(15) == 3  
    assert sqrt_fun(16) == 4
    assert sqrt_fun(25) == 5

def test_redundant_sqrt():

    assert redundant_sqrt(3, 4) == 7
    assert redundant_sqrt(10, 5) == 15
    assert redundant_sqrt(0, 0) == 0
    assert redundant_sqrt(-3, -4) == -7
    assert redundant_sqrt(7, -3) == 4

    assert redundant_sqrt(3, 4) == 7 
=======
from src.sqrt import redundant_sqrt, sqrt_fun

def test_sqrt_fun():
    
    assert sqrt_fun(4) == 2
    assert sqrt_fun(9) == 3
    assert sqrt_fun(15) == 3  
    assert sqrt_fun(16) == 4
    assert sqrt_fun(25) == 5

def test_redundant_sqrt():

    assert redundant_sqrt(3, 4) == 7
    assert redundant_sqrt(10, 5) == 15
    assert redundant_sqrt(0, 0) == 0
    assert redundant_sqrt(-3, -4) == -7
    assert redundant_sqrt(7, -3) == 4

    assert redundant_sqrt(3, 4) == 7 
>>>>>>> 3cd855890a236904c98c62c751d0fcb16af8fe9b
