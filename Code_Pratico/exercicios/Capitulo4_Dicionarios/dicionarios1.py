print('+'*10, 'Criando Dicionários', '+'*10)

usuarios = {}

usu = {'Chaves': ['Chaves Silva', '17/06/2017', 'Recep_01'],
       'Quico': ['Enrico Flores', '03/06/2017', 'Raiox_02'],
       'Quico': ['Erico Flores', '03/06/1976', 'Raiox_03']}

# Adicionando um item
usu['Florinda'] = ['Florinda', '26/11/2017', 'Recep_01']
usu['Florinda'] = ['Florinda', '26/11/2016', 'Recep_01']

# Retornando os dados de várias maneiras
print(usu)
print('='*100)
print(f'Dados: {usu.get("Chaves")}')
print('#'*100)
print(usu['Quico'])
print(usu['Florinda'])