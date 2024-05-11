import requests
from datetime import datetime

def get_weather_data(lati, longi):
    if not (-90 <= lati <= 90) or not (-180 <= longi <= 180):
        return {'error': "Invalid latitude or longitude values. Latitude must be between -90 and 90. Longitude must be between -180 and 180."}

    # Endpoint API z danymi pogodowymi
    endpoint = f"https://api.open-meteo.com/v1/forecast?latitude={lati}&longitude={longi}&daily=weather_code,temperature_2m_max,temperature_2m_min,sunshine_duration"
    print(endpoint)
    try:
        # Wykonanie zapytania GET do API
        response = requests.get(endpoint)
        data = response.json()

        # Przetwarzanie danych z API
        weather_data = []

        for i in range(len(data["daily"]["time"])):
            sunshine_duration=data["daily"]["sunshine_duration"][i]
            energy=2.5*0.2*sunshine_duration
            weather_data.append({
                'date': data["daily"]["time"][i],
                'weather_code': data["daily"]["weather_code"][i],
                'temperature_min': data["daily"]["temperature_2m_min"][i],
                'temperature_max': data["daily"]["temperature_2m_max"][i],
                'sunshine_duration': data["daily"]["sunshine_duration"][i],#I'm not sure if I chose the sunlight time parameter correctly
                'energy': energy,
            })

        return weather_data

    except Exception as e:
        # Obsługa błędów zapytania do API
        return {'error': str(e)}


