print('-'*10, 'Lendo arquivos', '-'*10)

with open('teste.txt', 'r') as arquivo:
    conteudo = arquivo.read()
print(f'Tipo de dado da variável: {type(conteudo)}')
print(f'Conteudo do arquivo: {conteudo}')