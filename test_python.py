from python import *

def teste_email_valido():
    assert email_valido("teste@example.com") == True
    assert email_valido("teste.com") == False

def teste_eh_par():
    assert eh_par(4) == True
    assert eh_par(5) == False

def teste_fatorial():
    assert fatorial(5) == 120
    assert fatorial(0) == 1

def teste_qudrado():
    assert quadrado(3) == 9
    assert quadrado(5) == 25

def teste_eh_positivo():
    assert eh_positivo(3) == True
    assert eh_positivo(-1) == False

def teste_verificar_maioridade():
    assert verificar_maioridade(17) == "menor de idade"
    assert verificar_maioridade(40) == "maior de idade" 

def teste_classificar_temperatura():
    assert classificar_temperatura(-2) == "frio"
    assert classificar_temperatura(19) == "moderado"
    assert classificar_temperatura(33) == "quente"

def teste_avaliar_nota():
    assert avaliar_nota(8) == "aprovado"
    assert avaliar_nota(6) == "recuperacao"
    assert avaliar_nota(3) == "reprovado"

def teste_pode_votar():
    assert pode_votar(29) == "voto obrigatório"
    assert pode_votar(17) == "voto facultativo"
    assert pode_votar(11) == "não pode votar"

def teste_avaliar_produto():
    assert avaliar_produto(5) == "excelente"
    assert avaliar_produto(4) == "bom"
    assert avaliar_produto(3) == "regular"
    assert avaliar_produto(2) == "ruim"
    assert avaliar_produto(1) == "péssimo"
    assert avaliar_produto(0) == "valor inválido"