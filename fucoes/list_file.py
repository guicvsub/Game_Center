from request.request_api_google import authenticate

def list_files_in_folder(service, folder_id):
    """Lista os arquivos de uma pasta específica no Google Drive."""
    query = f"'{folder_id}' in parents"  # Filtra arquivos dentro da pasta com o ID fornecido
    results = service.files().list(q=query, spaces='drive', fields="files(id, name)").execute()
    items = results.get('files', [])

    if not items:
        print('Nenhum arquivo encontrado na pasta.')
    else:
        print('Arquivos encontrados:')
        for item in items:
            print(f"{item['name']} (ID: {item['id']})")

if __name__ == '__main__':
    # Autentica o serviço
    service = authenticate()

    # ID da pasta no Google Drive
    folder_id = '1Jmwq9dl3VhfwqSubvjgoIa49aA82URW7'

    # Chama a função para listar arquivos na pasta especificada
    list_files_in_folder(service, folder_id)
