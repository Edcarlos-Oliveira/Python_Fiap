print('='*10, 'Criando Tuplas', '='*10)

ips = dict()
resp = 'S'

while resp == 'S':
    ips[(input('Primeiros octetos: '), input('Últimos octetos: '))] = input('Nome da máquina: ')
    resp = input('Digite [S] para continuar: ').upper

print('Exibindo ips: ')
for ip in ips.keys():
    print(f'{ip[0]}.{ip[1]}')

print('Exibindo a máquina com o mesmo endereço: ')
busca = input('Digite os dois últimos octetos: ')

for ip, nome in ips.items():
    print('Máquinas no mesmo endereço (redes diferentes)')
    if (ip[1] == busca):
        print(nome)

print('Exibindo as máquinas que compõem uma mesma rede: ')
rede = input('Digite os dois primeiros octetos: ')
for ip, nome in ips.items():
    if ip[0] == rede:
        print(nome)



