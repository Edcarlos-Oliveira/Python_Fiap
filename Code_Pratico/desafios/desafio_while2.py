print('-'*10, 'Decisões Encandeadas 2', '-'*10)

nome = str(input('Digite o nome: '))
idade = int(input('Digite a idade: '))
doenc_infect = str(input('Suspeita de doença infectocontagiosa? ')).upper()

# PRIMEIRAS CONDIÇÕES
while doenc_infect != 'SIM' and doenc_infect != 'NAO':
    print('Digite SIM ou NAO')
    doenc_infect = str(input('Suspeita de doença infectocontagiosa? ')).upper()
    
if doenc_infect == 'SIM':
    print(f'Encaminhe o(a) paciente {nome} à sala AMARELA')
else:
    print(f'Encaminhe o(a) paciente {nome} à sala BRANCA')

# SEGUNDA CONDIÇÕES
if idade >= 65:
    print(f'Paciente {nome} COM prioridade')
else:
    genero = str(input('Digite o gênero do paciente: ')).upper()
    if genero == 'FEMININO' and idade > 10:
        gravidez = str(input(f'A paciente {nome} está grávida? ')).upper()
        if gravidez == 'SIM':
            print(f'Paciente {nome} COM prioridade')
        else:
            print(f'Paciente {nome} SEM prioridade')
    else:
        print(f'Paciente {nome} SEM prioridade')

    
    
