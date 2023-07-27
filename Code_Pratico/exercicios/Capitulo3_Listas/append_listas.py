print('='*10, 'Criando Listas Append', '='*10)

inv = []
resp = 'S'

while resp == 'S':
    inv.append(str(input('Equipamento: ')))
    inv.append(float(input('Valor: ')))
    inv.append(int(input('Número serial: ')))
    inv.append(str(input('Departamento: ')))
    resp = str(input('Digite [S] para continuar: ')).upper()

# Percorrendo a lista com FOR
for elemento in inv:
    print(elemento)

    