import requests
import subprocess

# URL do arquivo ZIP
url = "https://github.com/CVEProject/cvelistV5/archive/refs/heads/main.zip"

# Nome do arquivo local
local_filename = "main.zip"

# Faça o download do arquivo
response = requests.get(url)
with open(local_filename, 'wb') as f:
    f.write(response.content)

# Execute o comando 'unzip'
try:
    subprocess.run(["unzip", local_filename])
    print("Arquivo descompactado com sucesso!")
except Exception as e:
    print(f"Erro ao descompactar o arquivo: {str(e)}")
