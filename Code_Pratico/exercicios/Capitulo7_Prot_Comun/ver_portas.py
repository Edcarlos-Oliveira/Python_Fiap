import socket

# Verificando portas
print(f'Dominio: {socket.gethostbyname("domain")}') # Por padrão porta 53
print(f'Http: {socket.gethostbyname("http")}')      # Por padrão porta 80
print(f'Ftp: {socket.gethostbyname("ftp")}')        # Por padrão porta 21

