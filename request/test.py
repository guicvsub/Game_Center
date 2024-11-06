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

# Função para obter a capa do jogo
'''def obter_capa_jogo(access_token, game_title):
    headers = {
        'Client-ID': client_id,
        'Authorization': f'Bearer {access_token}'
    }
    data = f"fields name, cover; search \"{game_title}\";"

    print(f"Buscando capa do jogo: {game_title}")  # Debug: buscando capa

    start_time = time.time()  # Início da medição do tempo
    response = requests.post(igdb_url, headers=headers, data=data)
    end_time = time.time()  # Fim da medição do tempo

    tempo_resposta = end_time - start_time  # Calculando o tempo de resposta
    print(f'Tempo de resposta da API (capa do jogo): {tempo_resposta:.2f} segundos')

    print("Resposta da API:", response.json())  # Imprimir a resposta completa para análise

    if response.status_code == 200:
        games = response.json()
        if games and isinstance(games, list) and len(games) > 0:
            game = games[0]  # Pega o primeiro jogo da lista
            cover_id = game['cover']  # Pega o ID da capa

            # Buscar a URL da capa com o ID
            start_time_cover = time.time()  # Início da medição do tempo para a capa
            cover_response = requests.post(igdb_cover_url, headers=headers, data=f"fields url; where id = {cover_id};")
            end_time_cover = time.time()  # Fim da medição do tempo para a capa

            tempo_resposta_cover = end_time_cover - start_time_cover  # Calculando o tempo de resposta da capa
            print(f'Tempo de resposta da API (capa com ID): {tempo_resposta_cover:.2f} segundos')

            if cover_response.status_code == 200:
                cover_data = cover_response.json()
                if cover_data and isinstance(cover_data, list) and len(cover_data) > 0:
                    cover_image_url = f"https:{cover_data[0]['url']}"  # Formatar URL da capa
                    return cover_image_url
                else:
                    print("Capa não encontrada com o ID fornecido.")
            else:
                print(f'Erro ao buscar a capa com o ID: {cover_response.status_code}')
        else:
            print("Nenhum jogo encontrado.")
    else:
        print(f'Erro ao buscar a capa do jogo: {response.status_code}')  # Debug: erro na busca
    return None

# Função para baixar a imagem
def baixar_imagem(url, nome_arquivo):
    print(f"Baixando imagem de: {url}")  # Debug: URL da imagem
    image_response = requests.get(url)
    if image_response.status_code == 200:
        with open(nome_arquivo, 'wb') as file:
            file.write(image_response.content)
        print(f'Imagem salva como {nome_arquivo}')
    else:
        print('Erro ao baixar a imagem.')

# Função principal
def main():
    start_time = time.time()  # Início da medição do tempo total de execução

    access_token = obter_token_oauth(client_id, client_secret)
    if access_token:
        game_title = 'Grand Theft Auto V'  # Novo título do jogo
        cover_url = obter_capa_jogo(access_token, game_title)

        if cover_url:
            baixar_imagem(cover_url, 'capa_gta_v.jpg')
        else:
            print('Nenhuma capa encontrada para o jogo.')
    else:
        print("Falha ao obter o token.")

    end_time = time.time()  # Fim da medição do tempo total de execução
    tempo_total = end_time - start_time
    print(f'Tempo total de execução: {tempo_total:.2f} segundos')

# Executar a função principal
main()
'''