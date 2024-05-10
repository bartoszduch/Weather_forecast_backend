import requests
from datetime import datetime

def get_weather_data(lati, longi):
    if not (-90 <= latitude <= 90) or not (-180 <= longitude <= 180):
        raise ValueError("Invalid latitude or longitude values. Latitude must be between -90 and 90. Longitude must be between -180 and 180.")

    # Endpoint API z danymi pogodowymi
    endpoint = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&daily=weather_code,temperature_2m_max,temperature_2m_min,sunshine_duration"
    print(endpoint)
    try:
        # Wykonanie zapytania GET do API
        response = requests.get(endpoint)
        data = response.json()

        # Przetwarzanie danych z API
        weather_data = []

        for i in range(len(data["daily"]["time"])):
            weather_data.append({
                'date': data["daily"]["time"][i],
                'weather_code': data["daily"]["weather_code"][i],
                'temperature_min': data["daily"]["temperature_2m_min"][i],
                'temperature_max': data["daily"]["temperature_2m_max"][i],
                'sunshine_duration': data["daily"]["sunshine_duration"][i],#I'm not sure if I chose the sunlight time parameter correctly
            })

        return weather_data

    except Exception as e:
        # Obsługa błędów zapytania do API
        return {'error': str(e)}


def count_energy(resp):
    energy_data=[]
    for i in range(len(response)):
        energy=2.5*0.2*response[i].get('sunshine_duration')
        energy_data.append(energy)
    return energy_data

print("Enter latitude")
latitude=float(input())
print("Enter longitude")
longitude=float(input())
if not (-90 <=latitude<=90) or not (-180 <= longitude <= 180):
    print("Latitude must be between -90 and 90. Longitude must be between -180 and 180")

response = get_weather_data(latitude, longitude)
energy=count_energy(response)
print(energy)
for i in range(len(response)):
    print(response[i])

for i in range(len(energy)):
    print("Generated energy in day "+str(response[i].get('date')+":"+str(energy[i])))


