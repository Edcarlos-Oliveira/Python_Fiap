import json
import os
print('X'*10, 'Manipulando JSON', 'X'*10)

# Verificando se o arquivo existe
if os.path.exists('inventario_json.json'):
    # Criando o dicionario direto para evitar subescrever
    with open('inventario_json.json', 'r') as arq_json:
        inventario = json.load(arq_json)
else:
    inventario = dict()
        
op = int(input('[1] - Registrar Ativos'
           '\n[2] - Exibir Ativos'
           '\n[3] - Encerrar'
           '\nDigite: '))

while op > 0 and op < 4:
    if op == 1:
        resp = 'S'
        while resp == 'S':
            inventario[int(input('Número de Patrimônio: '))] = [
                        int(input('Data última atualização: ')),
                        input('Descrição: '),
                        input('Departamento: ')]
            resp = input('Digite [S] para continuar: ').upper()
        
        with open('inventario_json.json', 'w') as arq_json:
            json.dump(inventario, arq_json)
        print('JSON gerado!!!')

    elif op == 2:
            for ch, vl in inventario.items():
                print(f'Data: {vl[0]}')
                print(f'Descrição: {vl[1]}')
                print(f'Departamento: {vl[2]}')
    else:
        if op == 3:
            print('Sistema Encerrado!!!')
            break

    op = int(input('\n[1] - Regitrar Ativo: '
           '\n[2] - Exibir Ativos: '
           '\n[3] - Encerrar'
           '\nDigite: '))

