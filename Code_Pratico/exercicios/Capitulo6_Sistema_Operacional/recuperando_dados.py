import platform

# Verificando informações da máquina:
print(f'Distribuição do SO: {platform.platform()}')
print(f'Nome SO: {platform.system()}')
print(f'Versão SO: {platform.release()}')
print(f'Arquitetura: {platform.architecture()}')
print(f'Nome Computador: {platform.node()}')
print(f'Tipo Máquina: {platform.machine()}')
print(f'Processador: {platform.processor()}')
print(f'Versão Python: {platform.python_version()}')
