import requests
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime

@csrf_exempt
def get_weather_data(request):
    if request.method == 'POST':
        latitude = request.POST.get('latitude')
        longitude = request.POST.get('longitude')

        # Sprawdzenie, czy szerokość i długość geograficzna zostały przekazane
        if not latitude or not longitude:
            return JsonResponse({'error': 'Wymagane są parametry latitude i longitude'}, status=400)

        # Endpoint strony z danymi pogodowymi
        endpoint = 'https://open-meteo.com/en/docs'  # Zastąp 'https://example.com/weather' odpowiednim adresem URL

        # Parametry do zapytania
        params = {
            'latitude': latitude,
            'longitude': longitude,
            'current_weather': 'true',
        }

        try:
            # Wykonanie zapytania GET do strony z danymi pogodowymi
            response = requests.get(endpoint, params=params)
            data = response.json()

            # Przetwarzanie danych z API
            weather_data = {
                'data': datetime.fromtimestamp(data['current_weather']['timestamp']).strftime('%Y-%m-%d %H:%M:%S'),
                'weather_code': data['current_weather']['weathercode'],
                'temperature_min': data['current_weather']['temperature']['min'],
                'temperature_max': data['current_weather']['temperature']['max'],
                # Tutaj możesz obliczyć szacowaną wartość wygenerowanej energii na podstawie otrzymanych danych pogodowych
                'estimated_energy_production': calculate_energy_production(data),
            }

            # Zwrócenie danych w formie JSON
            return JsonResponse(weather_data)

        except Exception as e:
            # Obsługa błędów zapytania do strony z danymi pogodowymi
            return JsonResponse({'error': str(e)}, status=500)

    else:
        return JsonResponse({'error': 'Metoda GET nie jest obsługiwana'}, status=405)


def calculate_energy_production(weather_data):
    # Tutaj obliczysz produkcję energii na podstawie danych pogodowych
    # Zgodnie z podanym wzorem
    # Przykładowa implementacja:
    solar_panel_power = 2.5  # kW
    sunlight_exposure = weather_data['current_weather'][
        'solar_exposure']  # czas ekspozycji na światło słoneczne w godzinach
    panel_efficiency = 0.2
    energy_production = solar_panel_power * sunlight_exposure * panel_efficiency
    return energy_production
