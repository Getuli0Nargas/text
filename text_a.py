from codigo2_a import *

def test_area_retangulo():
    assert area_retangulo(3,4) == 12
    assert area_retangulo(-1,4) == "Erro: largura e altura devem ser não-negativos."
    assert area_retangulo(3,-2) == "Erro: largura e altura devem ser não-negativo."

def test_area_circulo():
    assert  area_circulo(3) == math.pi * 9
    assert  area_circulo(-1) == "Erro: p raio não pode ser negativo."


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

