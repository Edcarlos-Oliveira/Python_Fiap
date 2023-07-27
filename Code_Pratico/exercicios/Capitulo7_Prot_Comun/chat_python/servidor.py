from socket import *

servidor = '127.0.0.1'

porta = 43210

# Criando o objeto socket(obs: Todos os dados transmitidos via socket devem ser em bytes)
obj_socket = socket(AF_INET, SOCK_STREAM)   # 'AF_INET' => Identifica o emissor/receptor 'SOCK_STREAM' => Transporte do pacote
obj_socket.bind((servidor, porta))          # Associação do servidor e porta  
obj_socket.listen(2)                        # 'listen' => Define a quantidade de clientes  

print('Aguardando cliente....')

while True:
    con, cliente = obj_socket.accept()
    print(f'Conectando com: {cliente}')
    while True:
        msg_recebida = str(con.recv(1024))
        print(f'Recebemos: {str(msg_recebida)[2:-1]}')
        msg_enviada = bytes(input('Sua Resposta: '), 'utf-8')
        con.send(msg_enviada)
        break
    con.close()
