from funcoes import *
from time import sleep
print('+'*10, 'Manipulando Dicionários', '+'*10)

usu = dict()

op = perguntar()

# Condições das opções
while op == 'I' or op == 'P' or op == 'E' or op == 'L' or op == 'F':
    if op == 'I':
        inserir(usu)
    
    if op == 'P':
        pesquisar(usu, input('Qual o login para pesquisar? '))

    if op == 'E':
        excluir(usu, input('Qual login para excluir? '))

    if op == 'L':
        listar(usu)

    if op == 'F':
        print('Aguarde, Finalizando....')
        sleep(2)
        print('Sistema Finalizado com Sucesso!!')
        break
    op = perguntar()
    