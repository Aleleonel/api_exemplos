import requests 
import json

token = '45c658001518a012c21b84925fd00221'
city = input("Digite uma Cidade: ")

class BuscaClima():

    def __init__(self, cidade, chave):
        
        self._cidade = cidade
        self._chave = chave


    def requisicao_api(self):

        resposta = requests.get("http://apiadvisor.climatempo.com.br/api/v1/locale/city?name={}&token={}"
        .format(self._cidade, self._chave ))

        if resposta.status_code == 200:
            # retorno =json.loads(resposta.text)            

            return resposta.json()
        else:
            return resposta.status_code
    
    def imprime_api(self):

        dados_api = self.requisicao_api()

        if type(dados_api) is not int:
            
           for ichave in dados_api:

                iid = ichave['id']
                inome = ichave['name']
                iuf = ichave['state']
                icountry = ichave['country']

                print( "id: " + str(iid), 
                "Cidade: "    + str(inome) + 
                " Estado: "   + str(iuf) +
                " country: "  + str(icountry))
        else:
            print(dados_api)



clima = BuscaClima(city, token )
print(clima.imprime_api())