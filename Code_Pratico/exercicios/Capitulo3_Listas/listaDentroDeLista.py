print('='*10, 'Criando Listas Dentro de Listas', '='*10)

inv = []
resp = 'S'

while resp == 'S':
    equip = [input('Equipamento:'),
            float(input('Valor: ')),
            int(input('Serial: ')),
            input('Departamento: ')]

    inv.append(equip)
    resp = input('Digite [S] para continuar: ').upper()

for elem in inv:
    print(f'Nome: {elem[0]}')
    print(f'Valor: {elem[1]}')
    print(f'Serial: {elem[2]}')
    print(f'Departamento: {elem[3]}')

# Criando uma busca
busca = input('Nome do equipamento: ')

for item in inv:
    if busca == item[0]:
        print(f'Valor: {item[1]}')
        print(f'Serial: {item[2]}')

# Criando depreciação de um item
deprec = input('Nome do item a depreciar: ')
for dpr in inv:
    if deprec == dpr[0]:
        print(f'Valor antigo: {dpr[1]}')
        dpr[1] = dpr[1] * 0.9
        print(f'Novo valor: {dpr[1]}')  

# Excluindo um item
serial = int(input('Serial que será excluido: '))
for ser in inv:
    if ser[2] == serial:
        inv.remove(ser)

for ser in inv:
    print(f'Nome: {ser[0]}')
    print(f'Valor: {ser[1]}')
    print(f'Serial: {ser[2]}')
    print(f'Dep: {ser[3]}')

# Trabalhando com valores
valores = []

for v in inv:
    valores.append(v[1])
if len(valores) > 0:
    print(f'O equipamento mais caro: {max(valores)}')
    print(f'Equipamento mais barato: {min(valores)}')
    print(f'Total dos equipamentos: {sum(valores)}')

