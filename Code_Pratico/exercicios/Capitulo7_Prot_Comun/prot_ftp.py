from ftplib import *

ftp_ativo = False                                   # Armazena somente os valores True ou False
ftp = FTP('ftp.ibiblio.org')                        # Cria o objeto
print(ftp.getwelcome())

usu = input('Digite o usuário: ')
senha = input('Digite a senha: ')
ftp.login(usu, senha)                               # Estabelece a conexão com o servidor
print(f'Diretório atual do trabalho: {ftp.pwd()}')  # 'pwd' => Retorna o endereço atual do trabalho
ftp.cwd('pub')                                      # 'cwd' => Deslocamento entre os diretórios
print(f'Diretório corrente: {ftp.pwd()}')
print(ftp.retrlines('LIST'))                        # 'retrlines' => Lista os arquivos encontrados
ftp.quit()
