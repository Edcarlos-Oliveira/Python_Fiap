print('-'*10, 'Desafio while', '-'*10)

resposta = 'SIM'
while resposta == 'SIM':
    nivel = str(input('Digite o nível de acesso: ')).upper()
    if nivel == 'ADM' or nivel == 'USR':
        genero = str(input('Digite o gênero: ')).upper()
        if nivel == 'ADM':
            if genero == 'MASCULINO':
                print('Olá Aministrador!')
            else:
                print('Olá Administradora!')
        else:
            if genero == 'MASCULINO':
                print('Olá Usuário!')
            else:
                print('Olá Usuária!')
    elif nivel == 'GUEST':
        print('Olá Visitante!')
    else:
        print('Olá Desconhecido(a)!')

    resposta = str(input('Digite SIM para continuar: ')).upper()