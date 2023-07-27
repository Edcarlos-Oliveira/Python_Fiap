print('x'*10, 'Desafio Tabuada', 'x'*10)

'''tabuada = int(input('Digite um número para exibir a tabuada: '))

for num in range(0, 11):
    result = num * tabuada
    print(f'A tabuada de {num} X {tabuada} = {result}')'''

# Codigo reduzido
tabuada = int(input('Digite um número para exibir a tabuada: '))
print(f'A tabuada do número {tabuada}:')

for valor in range(1, 11, 1):
    print(f'{tabuada} X {valor} = {tabuada * valor}')

    