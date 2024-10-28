import math
# Função para Calcular a Área de um Círculo
def area_circulo(raio):
    if raio < 0:
        return "Erro: o raio não pode ser negativo."
    return math.pi * (raio ** 2)

# Função para Calcular a Área de um Retângulo
def area_retangulo(largura, altura):
    if largura < 0 or altura < 0:
        return "Erro: largura e altura devem ser não-negativos."
    return largura * altura

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
