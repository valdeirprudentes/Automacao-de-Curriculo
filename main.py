from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
import os.path

# Define o escopo da API (apenas leitura e gravação)
SCOPES = ['https://www.googleapis.com/auth/drive']

# Nome do arquivo JSON com as credenciais
CLIENT_SECRET_FILE = 'C:/Users/User/Desktop/Valdeir/Projeto Python/Automação de um Currículo/credenciais.json'

# Nome do arquivo no Google Drive
DRIVE_FILE_NAME = 'CV_BI - Valdeir Prudente.doc'

# ID do arquivo no Google Drive
DRIVE_FILE_ID = '1nCrjYlPN0YoToakeGh91_pOPFv-hVjy9'

# Função para autenticar e construir o serviço
def authenticate_and_build_service():
    creds = None

    # Carrega as credenciais do arquivo JSON se existirem
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json')

    # Se não houver credenciais válidas, solicita autorização do usuário
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(CLIENT_SECRET_FILE, SCOPES)
            creds = flow.run_local_server(port=0)

        # Salva as credenciais para uso futuro
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    # Constrói o serviço do Google Drive
    service = build('drive', 'v3', credentials=creds)
    return service

# Função para fazer o upload de um arquivo para o Google Drive
def upload_file(service, file_path):
    file_metadata = {'name': DRIVE_FILE_NAME}
    """media = MediaFileUpload(file_path, mimetype='application/msword')
    file = service.files().update(fileId=DRIVE_FILE_ID, body=file_metadata, media_body=media).execute()
    print('Arquivo atualizado:', file.get('name'))"""

# Autentica e constrói o serviço
drive_service = authenticate_and_build_service()

# Caminho para o arquivo do currículo localmente
curr_resume_file_path = 'C:/Users/User/Desktop/Valdeir/Projeto Python/Automação de um Currículo/CV_BI - Valdeir Prudente.doc'

# Faz o upload do arquivo
upload_file(drive_service, curr_resume_file_path)