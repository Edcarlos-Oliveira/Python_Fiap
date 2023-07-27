import json
import os

# Menu de opcoes:
def opcoes():
    op = int(input('[1] - Registrar Ativos'
           '\n[2] - Exibir Ativos'
           '\n[3] - Encerrar'
           '\nDigite: '))
    return(op)

# Verificando se arquivo existe
def verificar(arquivo):
    if os.path.exists(arquivo):
        with open(arquivo, 'r') as arq_json:
            dicionario = json.load(arq_json)
    else:
        dicionario = dict()
    return (dicionario)

# Salvando o arquivo
def salvar(dicionario, arquivo):
    with open(arquivo, 'w') as arq_json:
        json.dump(dicionario, arq_json)

# Registrar dados
def registrar(dicionario, arquivo):
    resp = 'S'
    while resp == 'S':
        dicionario[int(input('Número de Patrimônio: '))] = [
                   int(input('Data última atualização: ')),
                   input('Descrição: '),
                   input('Departamento: ')]
        resp = input('Digite [S] para continuar: ').upper()
        salvar(dicionario, arquivo)
    return('JSON gerado!!!') 
        
# Exibindo os arquivos
def exibir(arquivo):
    dicionario = verificar(arquivo)
    for ch, vl in dicionario.items():
        print(f'Data: {vl[0]}')
        print(f'Descrição: {vl[1]}')
        print(f'Departamento: {vl[2]}')