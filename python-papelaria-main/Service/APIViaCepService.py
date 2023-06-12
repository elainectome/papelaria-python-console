import requests

class APIViaCepService:
    def __init__(self, cep):
        self.cep = cep
        self.base_url = 'https://viacep.com.br/ws/'

    def getLojaLocation(self):
        response = requests.get(f'{self.base_url}/{self.cep}/json/')
        response.raise_for_status()
        return response.json()