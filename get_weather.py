import requests
from datetime import datetime

def get_weather_data(latitude, longitude):
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
                'sunshine_duration': data["daily"]["sunshine_duration"][i],
            })

        return weather_data

    except Exception as e:
        # Obsługa błędów zapytania do API
        return {'error': str(e)}

# Wywołanie funkcji z odpowiednimi parametrami
latitude = '30'
longitude = '10'
response = get_weather_data(latitude, longitude)

# Wypisanie odpowiedzi
for i in range(0,7):
    print(response[i])


