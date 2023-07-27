print('='*10, 'Criando Rotinas de Inventário', '='*10)

inventario = dict()

op = int(input('[1] - Registrar Ativo'
               '\n[2] - Persistir em Arquivo'
               '\n[3] - Exibir Ativos'
               '\n[4] - Encerrar'
               '\nDigite: '))

while op > 0 and op < 5:
    if op == 1:
        resp = 'S'
        while resp == 'S':
            inventario[input('Número de Patrimônio: ')] = [
                       input('Data última atualização: '),
                       input('Descrição: '),
                       input('Departamento: ')]

            resp = input('Digite [S] para continuar: ').upper()
    elif op == 2:
        with open('inventario.csv', 'a') as inv:
            for ch, vl in inventario.items():
                inv.write(f'{ch} ; {vl[0]} ; {vl[1]} ; {vl[2]}\n')
                print('Persisitido com Sucesso...')

    elif op == 3:
        with open('inventario.csv', 'r') as inv:
            print(inv.readlines()) # 'readlines()' quebra um arquivo de texto em partes

    else:
        if op == 4:
            print('Encerrado com SUCESSO!')
            break

    op = int(input('[1] - Registrar Ativo'
               '\n[2] - Persistir em Arquivo'
               '\n[3] - Exibir Ativos'
               '\n[4] - Encerrar'
               '\nDigite: '))

               