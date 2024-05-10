from get_weather import get_weather_data, count_energy
from datetime import datetime

def get_float_input():
    while True:
        try:
            value = float(input())
            return value
        except ValueError:
            print("Enter float number.")

print("Enter latitude")
while True:
    latitude = get_float_input()
    if -90<=latitude<=90:
        break
    else:
        print("Latitude must be between -90 and 90")
print("Enter longitude")
while True:
    longitude = get_float_input()
    if -180<=longitude<=180:
        break
    else:
        print("Longitute must be between -180 and 180")

response = get_weather_data(latitude, longitude)

if 'error' in response:
    print(response['error'])
else:
    print("Weather forecast:")
    for data in response:
        print(f"Date: {data['date']}, Weather Code: {data['weather_code']}, Min Temp: {data['temperature_min']}, Max Temp: {data['temperature_max']}, Sunshine Duration: {data['sunshine_duration']}")

    energy = count_energy(response)
    print("\nGenerated energy:")
    for i in range(len(energy)):
        print(f"Date: {response[i]['date']}, Energy: {energy[i]}")
