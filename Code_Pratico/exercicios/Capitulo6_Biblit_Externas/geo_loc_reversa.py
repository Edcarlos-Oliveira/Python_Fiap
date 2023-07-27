from geopy.geocoders import Nominatim

geolocator = Nominatim(user_agent='app_local')

print('Utilize como teste as coordenadas, Lat[-23.5740406] e Long[-46.623408900000015]')
latitude = float(input('Digite a Latitude: '))
longitude = float(input('Digite a Longitude: '))

result = str(geolocator.reverse(f'{latitude}, {longitude}')).split(',')

if result[0] != 'None':
    print(f'Endereço completo: {result}')
    print(f'Dado 1: {result[0]}')
    print(f'Dado 2: {result[1]}')
    print(f'Dado 3: {result[2]}')