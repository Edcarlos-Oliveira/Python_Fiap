print('='*10, 'Criando arquivos', '='*10)

# Criando arquivo html
with open('pag.html', 'w') as pg:
    pg.write('<body><h1> Este é um teste para páginas WEB</h1>')
    pg.write('<br><h2> Abaixo segue alguns nomes importantes para o projeto: </h2>')
    pg.write('<h3>')

    nome = ''

    while nome != 'SAIR':
        nome = input('Digite um nome ou [SAIR]: ').upper()
        if nome != 'SAIR':
            pg.write(f'<br> {nome}')
    pg.write('</h3></body>')