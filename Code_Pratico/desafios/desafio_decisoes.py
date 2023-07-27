print('='*10, 'Desafio Condições', '-'*10)

nivel_acesso = str(input('Digite o nível de acesso: ')).upper()

if nivel_acesso == 'ADM' or nivel_acesso == 'USR':
    genero = str(input('Digite o genero: ')).upper()
    if nivel_acesso == 'ADM':
        if genero == 'MASCULINO':
            print('Olá Administrador!')
        else:
            print('Olá Administradora!')
    else:
        if genero == 'MASCULINO':
            print('Olá Usuário!')
        else:
            print('Olá Usuária!')
elif nivel_acesso == 'GUEST':
    print('Olá Visitante!')
else:
    print('Olá Desconhecido!')
    