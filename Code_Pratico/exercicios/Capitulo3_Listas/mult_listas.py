print('='*10, 'Criando Listas Multiplas', '='*10)

equip = list()
vl = list()
nSerial = list()
dep = list()
resp = 'S'

while resp == 'S':
    equip.append(str(input('Equipamento: ')))
    vl.append(float(input('Valor: ')))
    nSerial.append(int(input('Numero Serial ')))
    dep.append(str(input('Departamento: ')))
    
    resp = str(input('Digite [S] para continuar: ')).upper()

# Percorrendo Lista especifica
for v in nSerial:
    print(v)

# Percorrendo a Lista pelos indices
for i in range(0, len(equip)):
    print(f'Equipamento: {i + 1}') # Inicia como 'Equipamento 1'
    print(f'Nome: {equip[i]}')
    print(f'Valor: {vl[i]}')
    print(f'Serial: {nSerial[i]}')
    print(f'Departamento: {dep[i]}')

# Buscando determinado item
busca = str(input('Nome do equipamento que deseja buscar: '))
for i2 in range(0, len(equip)):
    if busca == equip[i2]:
        print(f'Valor: {vl[i2]}')
        print(f'Serial: {nSerial[i2]}')

# Aplicando depreciação(10%) em determinado item
deprec = input('Nome do equipamento para depreciar: ')
for i3 in range(0, len(equip)):
    if deprec == equip[i3]:
        print(f'Valor antigo: {equip[i3]}')
        vl[i3] = vl[i3] * 0.9
        print(f'Novo Valor: {vl[i3]}')

# Excluindo um item(serial)
excluir = int(input('Numero do serial para excluir: '))
for i4 in range(0, len(equip)):
    if nSerial[i4] == excluir:
        del dep[i4]
        del equip[i4]
        del nSerial[i4]
        del vl[i4]
        break

for i4 in range(0, len(equip)):
    print(f'Equipamento: {i4 + 1}')
    print(f'Nome: {equip[i4]}')
    print(f'Valor: {vl[i4]}')
    print(f'Serial: {nSerial[i4]}')
    print(f'Departamento: {dep[i4]}')





