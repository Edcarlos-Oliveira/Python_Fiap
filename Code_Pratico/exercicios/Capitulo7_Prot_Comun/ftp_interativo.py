import os
from ftplib import *

ftp_ativo = False
ftp = FTP(input('Digite o FTP que deseja conectar: '))
print(ftp.getwelcome())
usu = input('Digite o usuário: ')
senha = input('Digite a senha: ')
ftp.login(usu, senha)
print('Conexão bem sucedida. Diretório atual de trabalho: ',ftp.pwd())
menu = '1'
while menu == '1' or menu == '2' or menu == '3':
    menu = input('[1] - Para listar arquivos: '
                '\n[2] - Para definir um diretorio: '
                '\n[3] - Para baixar um arquivo: '
                '\nEscolha uma opção: ')

    if menu == '1':
        print(ftp.dir())
    elif menu == '2':
        ftp.cwd(input('Digite o diretorio que deseja entrar: '))
        print('Diretório corrente é: ', ftp.pwd())
    elif menu == '3':
        tipo = input('Digite [B] para arquivo binário ou qualquer letra ASCII: ').upper()
        if tipo == 'B':
            with open(input('Digite o nome do arquivo destino: '), 'wb') as arq:
                ftp.retrbinary('RETR' + input("Arquivo de origem: "), arq.write)
        else:
            with open(input('Digite o nome do arquivo destino: '), 'w') as arq:
                def escrever_linha(data):
                    arq.write(data)
                    arq.write(os.linesep)
                ftr.retrlines('RETR' + input("Arquivo de origem: "), escrever_linha)
        print('Arquivo baixado com sucesso!!!')
ftp.quit()