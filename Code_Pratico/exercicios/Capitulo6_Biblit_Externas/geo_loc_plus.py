from geopy.geocoders import Nominatim

# Localização recebendo do input
geolocator = Nominatim(user_agent='app_local')

endereco = input('Digite um endereço com número e cidade. [Exemplo: avenida paulista, 100 São Paulo]: ')

result = str(geolocator.geocode(endereco)).split(',')

if result[0] != 'None':
    print(f'Endereço: {result}')
    print(f'Bairro: {result[1]}')
    print(f'Cidade : {result[2]}')
    print(f'Região: {result[3]}')
