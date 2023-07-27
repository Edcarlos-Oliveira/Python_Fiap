print('-'*10, 'Decisão Simples com if', '-'*10)

nome = str(input('Digite o nome: '))
idade = int(input('Digite a idade: '))
prioridade = 'NÃO'

if idade >= 65:
    prioridade = 'SIM'

print(f'O(a) paciente {nome} possui atendimento prioritário? {prioridade}')


