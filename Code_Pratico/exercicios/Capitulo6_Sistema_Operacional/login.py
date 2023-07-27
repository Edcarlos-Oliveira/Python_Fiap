import getpass
 
usu = input('Digite o usuário: ').upper()
senha = getpass.getpass('Digite a senha: ')

if usu == 'EDCARLOS' and senha == 'EstuD2023':
    print('Logado!!')
else:
    print('Usuário ou senha errada!!')

