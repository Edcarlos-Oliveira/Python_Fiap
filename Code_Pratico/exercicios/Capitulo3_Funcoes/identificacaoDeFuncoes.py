print('='*10, 'Identificando Funções', '='*10)

# Preenchendo a lista
def preencher_inventario(lista):
    resp = 'S'
    while resp == 'S':
        equip = [input('Equipamento: '),
                float(input('Valor: ')),
                int(input('Serial: ')),
                input('Departamento: ')]
        lista.append(equip)
        resp = input('Digite [S] para continuar: ').upper()

# Exibindo o resultado
def exibir_inventario(lista):
    for elem in lista:
        print(f'Nome: {elem[0]}')
        print(f'Valor: {elem[1]}')
        print(f'Serial: {elem[2]}')
        print(f'Dep: {elem[3]}')

# Localizando um item
def localizar_nome(lista):
    localizar = input('Digite o nome: ')
    for item in lista:
        if localizar == item[0]:
            print(f'Valor: {item[1]}')
            print(f'Serial: {item[2]}')

# Depreciando(10%) um item:
def depreciar_item(lista, porc):
    deprec = input('Digite o nome do item para depreciação: ')
    for item in lista:
        if deprec == item[0]:
            print(f'Valor antigo: {item[1]}')
            item[1] = item[1] * (1 - porc/100)
            print(f'Novo valor: {item[1]}')

# Remover por serial
def remover_serial(lista):
    serial = int(input('Digite o serial: '))
    for item in lista:
        if item[2] == serial:
            lista.remove(item)
    return ('Itens excluídos!!!')

# Resumir os valores
def resumir_valores(lista):
    valores = []
    for item in lista:
        valores.append(item[1])
    if len(valores) > 0:
        print(f'Maior valor: {max(valores)}')
        print(f'Menor Valor: {min(valores)}')
        print(f'Total valores: {sum(valores)}')
    else:
        print('Valores menor que 0!')
