import math
import pytest

@pytest.fixture
def lista_simples():
    return[1,2,3,4,5]

def soma (a,b):
    return a + b

def subtracao(a,b):
    return a - b

def multiplicacao(a,b):
    return a * b

def divisao(a,b):
    if(b == 0):
        return "não é possivel dividir"
    else:
        return a / b

