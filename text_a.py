from codigo2_a import *

def test_area_retangulo():
    assert area_retangulo(3,4) == 12
    assert area_retangulo(-1,4) == "Erro: largura e altura devem ser não-negativos."
    assert area_retangulo(3,-2) == "Erro: largura e altura devem ser não-negativo."

def test_area_circulo():
    assert  area_circulo(3) == math.pi * 9
    assert  area_circulo(-1) == "Erro: p raio não pode ser negativo."

