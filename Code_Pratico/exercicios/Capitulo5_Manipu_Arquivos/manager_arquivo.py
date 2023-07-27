from funcoes_arquivo import *
print('='*10, 'Aprimorando arquivos com funcões', '='*10)

inventario = dict()

# Chamando a função opcões
op = opcoes()

# Criando as condições:
while op > 0 and op < 5:
    if op == 1:
        registrar(inventario)

    if op == 2:
        print(persistir(inventario))

    if op == 3:
        print(exibir())

    if op == 4:
        print('Sistema Encerrado!!')
        break
    
    op = opcoes()
