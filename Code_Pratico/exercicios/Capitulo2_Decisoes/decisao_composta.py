print('-'*10, 'Decisão Composta com if, else', '-'*10)

nome = str(input('Digite o nome: '))
idade = int(input('Digite a idade: '))

if idade >= 65:
    print(f'O(a) paciente {nome} POSSUI atendimento prioritário!')
else:
    print(f'O(a) paciente {nome} NÃO POSSUI atendimento prioritário!')
print()

print('-'*10, 'Aprimorando a decisão composta com elif', '-'*10)
nome2 = str(input('Digite o nome: '))
idade2 = int(input('Digite a idade: '))
doenca_infect = str(input('Possui doença infectocontagiosa: ')).upper()

if idade2 >= 65:
    print(f'O(a) paciente {nome2} POSSUI atendimento prioritário!')
elif doenca_infect == 'SIM':
    print(f'O(a) paciente {nome2} DEVE ser direcionado à sala reservada!')
else:
    print(f'O(a) paciente {nome2} NÃO POSSUI atendimento prioritário!')

print()
print('-'*10, 'Aprimorando a decisão composta com mais elif', '-'*10)
nome3 = str(input('Digite o nome: '))
idade3 = int(input('Digite a idade: '))
doenca_infect3 = str(input('Possui doença infectocontagiosa: ')).upper()

if idade3 >= 65 and doenca_infect3 == 'SIM':
    print(f'O(a) paciente {nome3} direcionado a sala AMARELA COM prioridade!')
elif idade3 < 65 and doenca_infect3 == 'SIM':
    print(f'O(a) paciente {nome3} direcionado a sala AMARELA SEM prioridade!')
elif idade3 >= 65 and doenca_infect3 == 'NAO':
    print(f'O(a) paciente {nome3} direcionado a sala BRANCA COM prioridade!')
elif idade3 < 65 and doenca_infect3 == 'NAO':
    print(f'O(a) paciente {nome3} direcionado a sala BRANCA SEM prioridade!')
else:
    print('Responda a suspeita de doença infectocontagiosa com SIM ou NAO')


