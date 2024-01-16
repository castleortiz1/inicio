import geopy
from geopy.geocoders import Nominatim

# Introducir la dirección IP
ip = "8.8.8.8"

# Crear el objeto geocoder
geolocator = Nominatim(user_agent="geoapiExercises")

# Obtener la ubicación
location = geolocator.geocode(ip)

# Imprimir la información
print("Dirección:", location.address)
print("Latitud:", location.latitude)
print("Longitud:", location.longitude)
