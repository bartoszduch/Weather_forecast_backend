from get_weather import get_weather_data, count_energy

print("Enter latitude")
latitude = float(input())
print("Enter longitude")
longitude = float(input())

if not (-90 <= latitude <= 90) or not (-180 <= longitude <= 180):
    print("Latitude must be between -90 and 90. Longitude must be between -180 and 180")
    exit()

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
