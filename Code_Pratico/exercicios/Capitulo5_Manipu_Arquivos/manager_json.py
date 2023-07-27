from funcoes_json import *
print('='*10, 'Funções com JSON', '='*10)

inventario = verificar('inventario_json.json')

#Menu de opções
op = opcoes()

# Criando as condições
while op > 0 and op < 4:
    if op == 1:
        print(registrar(inventario, 'inventario_json.json'))

    elif op == 2:
        exibir('inventario_json.json')
    else:
        if op == 3:
            print('Encerrado com Suecesso!!!')
            break
    op = opcoes()

