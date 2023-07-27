print('x'*10, 'Criando Variáveis', 'x'*10)

aluno = 'Edcarlos Oliveira'
instituicao = 'FIAP' 
qtde_funcionarios = 500
mediaMensalidade = 856.50

# Mostrando o resultado
print(f'{aluno} fazendo o curso de Python na {instituicao}.')
print(f'A {instituicao} possui {qtde_funcionarios} funcionários.')
print(f'A média da mensalidade é de R$ {mediaMensalidade :.2f}')
print()

print('-'*10, 'Criando as variáveis com inputs', '-'*10)

aluno = str(input('Digite seu nome: '))
instituicao = str(input('Digite a Instituição: '))
qtd_func = int(input('Digite a quantidade de funcionários: '))
med_mens = float(input('Digite a média de mensalidade: R$ '))

# Mostrando o resultado:
print(f'{aluno} fazendo o curso de Python na {instituicao}.')
print(f'A {instituicao} possui {qtd_func} funcionários.')
print(f'A média da mensalidade é de R$ {med_mens :.2f}')

print('='*10, 'Verificando o tipo dos dados', '='*10)
print()
print(f'A variável [aluno] é do tipo: {type(aluno)}')
print(f'A variável [instituicao] é do tipo: {type(instituicao)}')
print(f'A variável [qtd_func] é do tipo: {type(qtd_func)}')
print(f'A variável [med_mens] é do tipo: {type(med_mens)}')

