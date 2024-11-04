from codigo import *

def test_fixture(lista_simples):
    assert sum(lista_simples) == 15
    assert (lista_simples[4]) == 5
    assert len(lista_simples) == 5

def test_se_a_mais_b():
    assert soma (8,9) == 17
    assert soma (10,5) == 15
    assert soma (8,5) == 13

def test_subtracao_():
    assert subtracao(5,3) == 2
    assert subtracao(3,3) == 0
    assert subtracao(5,4) == 1

def test_multiplicacao_():
    assert multiplicacao(5,3) == 15
    assert multiplicacao(3,3) == 9
    assert multiplicacao(5,4) == 20


def test_divisao_():
    assert divisao(5,5) == 1
    assert divisao(3,3) == 1
    assert divisao(8,0) == "não é possivel dividir"

def test_dividir_4_por_2_resulatdo_2():
    assert divisao (4,2) == 2

def test_divisao_por_zero():
    assert dividir (4,0) == "não é possivel dividir"