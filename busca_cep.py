import requests
import json


class Busca_cep():
    def __init__(self, codigo_postal):
        self._codigo_postal = codigo_postal    

    def requisicao_api(self):
        resultado = requests.get('https://viacep.com.br/ws/{}/json/'.format(self._codigo_postal))
        if resultado.status_code == 200:
            return resultado.json()
        else:
            print('pagina não acessivel')
            return resultado.status_code
    
    def imprime_cep(self):
        dados_api = self.requisicao_api()
        if dados_api is not int:
            for (k, v) in dados_api.items():
                print(f'{k}: {v}')
        else:
            print(dados_api)

mostra_cep = Busca_cep(13207210)
print(mostra_cep.imprime_cep())