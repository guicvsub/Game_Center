import requests
import os
from dotenv import load_dotenv
import time

# Carregar as variáveis do arquivo .env
load_dotenv()

# Acessar CLIENT_ID e CLIENT_SECRET
client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET")

# URLs
oauth_url = 'https://id.twitch.tv/oauth2/token'
igdb_url = 'https://api.igdb.com/v4/games'
igdb_cover_url = 'https://api.igdb.com/v4/covers'  # Nova URL para buscar as capas

# Função para obter o token de acesso usando OAuth
def obter_token_oauth(client_id, client_secret):
    payload = {
        'client_id': client_id,
        'client_secret': client_secret,
        'grant_type': 'client_credentials'
    }
    print("Iniciando a requisição OAuth...")  # Debug: começando a requisição

    response = requests.post(oauth_url, data=payload)
    if response.status_code == 200:
        print("Token obtido com sucesso!")  # Debug: token obtido
        return response.json()['access_token']
    else:
        print(f'Erro ao obter token: {response.status_code}')  # Debug: erro na requisição
        return None