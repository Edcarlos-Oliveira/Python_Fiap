print('='*10, 'Gravando arquivos', '='*10)


# Criando arquivo
with open('teste.txt', 'w') as arquivo:
    arquivo.write('Nunca foi tão fácil criar um arquivo!!!')

# Nesse caso o 'a' cria o append no arquivo teste.txt, não subescrevendo o primeiro.
with open('teste.txt', 'a') as arquivo:
    arquivo.write('\nContinuação do texto...')