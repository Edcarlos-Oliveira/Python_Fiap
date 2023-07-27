# Aprimorando Inventário com Funções

# Função para escolher
def opcoes():
    op = int(input('[1] - Registrar Ativo'
                '\n[2] - Persistir em Arquivo'
                '\n[3] - Exibir Ativos'
                '\n[4] - Encerrar'
                '\nDigite: '))
    return(op)

# Função inserir
def registrar(dicionario):
    resp = 'S'
    while resp == 'S':
        dicionario[ input('Número de Patrimônio: ')] = [
                    input('Data última atualização: '),
                    input('Descrição: '),
                    input('Departamento: ')]
        resp = input('Digite [S] para continuar: ').upper()

# Função criar
def persistir(dicionario):
        with open('inventario.csv', 'a') as inv:
            for ch, vl in dicionario.items():
                inv.write(f'{ch} ; {vl[0]} ; {vl[1]} ; {vl[2]}\n')
        return('Persistido com Sucesso...')

# Função exibir
def exibir():
    with open('inventario.csv', 'r') as inv:
        return(inv.readlines()) # 'readlines()' quebra um arquivo de texto em partes

