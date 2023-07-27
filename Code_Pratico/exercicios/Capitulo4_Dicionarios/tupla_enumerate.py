print('='*10, 'Criando Tuplas com enumerate', '='*10)

usu = dict()
resp = 'S'
emails = list()

while resp == 'S':
    emails.append(input('Digite um email: ').lower())
    resp = input('Digite [S] para continuar: ').upper()

tupla = list(enumerate(emails))
for chave in range(0,len(tupla)):
    print(f'Email: {tupla[chave][1]}')
    usu[tupla[chave]] = [input('Digite o nome: '), input('Digite o nível: ')]

for chave, dado in usu.items():
    print(f'Usuario: {chave[0]}')
    print(f'Email: {chave[1]}')
    print(f'Nome: {dado[0]}')
    print(f'Nível: {dado[1]}')
    