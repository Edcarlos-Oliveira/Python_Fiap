import socket

resp = 'S'

while resp == 'S':
    url = input('Digite uma url: ')
    ip = socket.gethostbyname(url)
    print(f'O IP da url digitada é: {ip}')
    resp = input('Digite [S] para continuar: ').upper()
