import os
import json

# Diretório raiz
diretorio_raiz = '/home/kali/cve/cvelistV5-main/cves'

# Função para buscar arquivos .json recursivamente
def buscar_arquivos_json(diretorio):
    arquivos_json = []
    for diretorio_atual, _, arquivos in os.walk(diretorio):
        for nome_arquivo in arquivos:
            if nome_arquivo.endswith('.json'):
                arquivos_json.append(os.path.join(diretorio_atual, nome_arquivo))
    return arquivos_json

# Função para acessar os parâmetros solicitados em cada arquivo JSON
def acessar_informacoes(arquivo_json):
    with open(arquivo_json, 'r') as arquivo:
        dados = json.load(arquivo)
        if 'containers' in dados and 'cna' in dados['containers']:
            cna = dados['containers']['cna']
            if 'affected' in cna:
                for item in cna['affected']:
                    product = item.get('product', 'N/A')
                    version = item.get('versions', [{}])[0]
                    less_than = version.get('lessThan', 'N/A')
                    value = version.get('version', 'N/A')
                    availability_impact = cna.get('metrics', [{}])[0].get('cvssV3_0', {}).get('availabilityImpact', 'N/A')
                    base_score = cna.get('metrics', [{}])[0].get('cvssV3_0', {}).get('baseScore', 'N/A')
                    return product, less_than, value, availability_impact, base_score

    return 'N/A', 'N/A', 'N/A', 'N/A', 'N/A'

# Solicite uma palavra-chave ao usuário
palavra_chave = input('Digite uma palavra-chave para pesquisa nos arquivos JSON: ')

# Busque todos os arquivos .json no diretório e subdiretórios
arquivos_json = buscar_arquivos_json(diretorio_raiz)

# Acesse e imprima as informações solicitadas em cada arquivo JSON que contenha a palavra-chave
for arquivo_json in arquivos_json:
    product, less_than, value, availability_impact, base_score = acessar_informacoes(arquivo_json)
    if palavra_chave.lower() in f"{product} {less_than} {value} {availability_impact} {base_score}".lower():
        print(f'No arquivo {arquivo_json}:')
        print(f'  - Product: {product}')
        print(f'  - Less Than: {less_than}')
        print(f'  - Version: {value}')
        print(f'  - Availability Impact: {availability_impact}')
        print(f'  - Base Score: {base_score}')
        print()
