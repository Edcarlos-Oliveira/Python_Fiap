import getpass
from datetime import datetime

# Vericando o uso pelo usuario
print(f'Usuario: {getpass.getuser()}')
print(f'Data completa: {datetime.now()}')
print(f'Dia: {datetime.now().day}')
print(f'Mês: {datetime.now().month}')
print(f'Ano: {datetime.now().year}')
print(f'Hora: {datetime.now().hour}')
print(f'Minuto: {datetime.now().minute}')
print(f'Segundo: {datetime.now().second}')

# Logando usuario básico(não recomendado):
usu = input('Digite o usuário: ').upper()
senha = input('Digite a senha: ')

if usu == 'EDCARLOS' and senha == 'EstuD2023':
    print('Usuário Logado!!')
else:
    print('Usuário ou senha inválido!!')
