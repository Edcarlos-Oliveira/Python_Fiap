from geopy.geocoders import Nominatim
from funcoes_json import verificar, salvar

geolocator = Nominatim(user_agent='app_local')

dicionario = verificar('entrada.json')

lista = dicionario['endereco']

endereco = (f'{lista[0]}, {lista[1]} {lista[2]} {lista[3]}')

location = geolocator.geocode(endereco)

saida = {'coordenadas': (location.latitude, location.longitude)}

salvar(saida, 'saida.json')

