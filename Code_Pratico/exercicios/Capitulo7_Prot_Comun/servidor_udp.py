from socket import *

servidor = '127.0.0.1'
porta = 43210
obj_socket = socket(AF_INET, SOCK_DGRAM)    #'SOCK_DEGRAM' => indica que o protocolo é UDP
obj_socket.bind((servidor, porta))

print('Servidor Pronto...')

while True:
    dados, origem = obj_socket.recvfrom(65535) # '65535'=> Tamanho dos dados do cliente
    print(f'Origem: {origem}')
    print(f'Dados recebidos: {dados.decode()}') # 'decode()' exibe os dados bytes em strings(pode usar no TCP)
    resp = input('Digite a resposta: ')
    obj_socket.sendto(resp.encode(), origem)
obj_socket.close()