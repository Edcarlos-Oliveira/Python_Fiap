print('-'*10, 'Decisões Encandeadas', '-'*10)

nome = str(input('Digite o nome: '))
idade = int(input('Digite a idade: '))
doen_infecto = str(input('Suspeita de doença infectocontagiosa? ')).upper()

if idade >= 65:
    print(f'Paciente {nome} COM prioridade!')
    if doen_infecto == 'SIM':
        print(f'Encaminhe o paciente {nome} para a sala AMARELA!')
    elif doen_infecto == 'NAO':
        print(f'Encaminhe o paciente {nome} para a sala BRANCA!')
    else:
        print('Responda a suspeita de doença SIM ou NAO!')

else:
    print(f'Paciente {nome} SEM prioridade!')
    if doen_infecto == 'SIM':
        print(f'Encaminhe o paciente {nome} para a sala AMARELA!')
    elif doen_infecto == 'NAO':
        print(f'Encaminhe o paciente {nome} para a sala BRANCA!')
    else:
        print('Responda a suspeita de doença SIM ou NAO!')


