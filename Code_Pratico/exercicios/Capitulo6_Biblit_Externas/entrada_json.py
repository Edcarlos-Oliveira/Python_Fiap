import json
# Criando o arquivo json
dicionario = {'endereco':['Avenida Sapopemba', '5000', 'Sapopemba', 'Sao Paulo', 'Sp']}
with open('entrada.json', 'w') as arq_json:
    json.dump(dicionario, arq_json)
