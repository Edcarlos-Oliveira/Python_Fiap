print('='*10, 'Manipulando Arquivos Externos', '='*10)

# Criando a ferramenta de verificação
with open('economic-indicators.csv', 'r') as boston:
    tot_voo = 0
    maior = 0
    tot_passgeiro = 0
    maior_m_diaria = 0
    mes_maior_diaria = 0

    ano_escolhido = int(input('Qual ano pesquisar? '))
    for linha in boston.readlines()[1:-1]:
        lista = linha.split(',')
        tot_voo = tot_voo + float(lista[3])

        if float(lista[2]) > float(maior):
            maior = lista[2]
            ano = lista[0]
            mes = lista[1]

        if ano_escolhido == lista[0]:
            tot_passgeiro = tot_passgeiro + float(lista[2])
            if float(lista[5] > float(maior_m_diaria)):
                maior_m_diaria = lista[5]
                mes_maior_diaria = lista[1]
       
    print(f'O total de voos é: {tot_voo}')
    print(f'Mês/Ano de maior movimento: {mes}/{ano}')
    print(f'Total de Passageiros no ano: {ano_escolhido} foi de: {tot_passgeiro}')
    print(f'O mês do ano {ano_escolhido} com maior média diária de hospedagem: {mes_maior_diaria}')
