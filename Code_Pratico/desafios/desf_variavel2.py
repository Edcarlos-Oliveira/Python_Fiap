print('-=-'*5, 'Desafio Variável 2', '-=-'*5)

chefe = str(input('Digite o nome do chefe: '))
func = str(input('Digite o nome do funcionário: '))
evento = str(input('Digite o nome do evento: '))
gasto = float(input(f'Digite o valor gasto por {func} R$: '))

print(f'"Declaro para o senhor {chefe} que o senhor {func} esteve presente no evento {evento} e gastou o valor de R$ {gasto :.2f} com entrada."')
