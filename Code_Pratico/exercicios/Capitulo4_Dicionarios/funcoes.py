print('*'*10, 'Refazendo o Manager com Funções', '*'*10)
print()

def perguntar():
    resp = input("[I] - Para Inserir Usuário"+
           "\n[P] - Para Pesquisar Usuário"+
           "\n[E] - Para Excluir Usuário"+
           "\n[L] - Para Listar Usuário"+
           "\n[F] - Para Finalizar"+
           "\nO que você deseja realizar? ").upper()
    return(resp)

def inserir(dicionario):
    chave = input('Digite o Login: ').upper()
    dicionario[chave] = [input('Digite o nome: ').upper(),
                        input('Data último acesso: '),
                        input('Última estação acessada: ').upper()]

def pesquisar(dicionario, chave):
    lista = dicionario.get(chave)
    if lista != None:
        print(f'Nome: {lista[0]}')
        print(f'Último Acesso: {lista[1]}')
        print(f'Última Estação: {lista[2]}')

def excluir(dicionario, chave):
    if dicionario.get(chave) != None:
        del dicionario[chave]
    print('Objeto Excluído!')

def listar(dicionario):
    for chave, valor in dicionario.items():
        print('Objeto: ')
        print(f'Login: {chave}')
        print(f'Dados: {valor}')