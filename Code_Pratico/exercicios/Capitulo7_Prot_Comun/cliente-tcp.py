from socket import *

servidor = '127.0.0.1'
porta = 43210

msg = bytes(input('Digite algo: '), 'utf-8') 
obj_socket = socket(AF_INET, SOCK_STREAM)
obj_socket.connect((servidor, porta))
obj_socket.send(msg)
resp = obj_socket.recv(1024)
print(f'Recebemos: {resp}')
obj_socket.close()
