import os
from google.oauth2.credentials import Credentials
from google.auth.transport.requests import Request  # Corrigido aqui
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.http import MediaIoBaseDownload
import io

# Se modificar os escopos, exclua o arquivo token.json.
SCOPES = ['https://www.googleapis.com/auth/drive']

def authenticate():
    """Autentica e retorna o serviço da API Google Drive."""
    print("Iniciando autenticação...")  # Print para verificar se chegou aqui
    creds = None
    # O arquivo token.json armazena os tokens de acesso e atualização do usuário.
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
        print("Credenciais encontradas.")  # Se o token existir
    else:
        print("Nenhum token encontrado. Iniciando nova autenticação...")

    # Se não houver credenciais (ou se as credenciais expiraram), faz a autenticação.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            print("Credenciais expiradas. Tentando renovar...")
            creds.refresh(Request())  # Agora está usando o Request correto
        else:
            print("Autenticação necessária...")
            flow = InstalledAppFlow.from_client_secrets_file(
                r'C:\Users\gui\PycharmProjects\FLASK\Game_Center\json_credencial_google\credencials.json', SCOPES)  # Caminho completo
            creds = flow.run_local_server(port=0)

        # Salva as credenciais para a próxima execução.
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

        # Verificando se a autenticação foi bem-sucedida
        if creds.valid:
            print("Autenticação bem-sucedida!")
        else:
            print("Falha na autenticação!")

    service = build('drive', 'v3', credentials=creds)
    return service


if __name__ == '__main__':
    service = authenticate()  # Certifique-se de chamar a função
