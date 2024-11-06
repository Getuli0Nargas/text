import pytest 
import request 
from unittest.mock import magicMock


class BancoDeDados:
    def buscar_usuario(self,user_id):
        raise NotmplementedError

    def obter_dados_adicionais(user_id):
        resposta = request.get(f"http://api.exemplo.com/dados/{user_id}")
        return resposta.json()

    def sistema_principal(user_id, banco):
        usuario = banco.buscar_usuario(user_id)
        dados_iniciais = obter_dados_adicionais(user_id)
        usuario.update(dados_adicionais)
        return usuario


@pytest. fixture