import unittest
from get_weather import get_weather_data, count_energy

class TestWeatherApp(unittest.TestCase):

    def test_get_weather_data_valid_values(self):
        # Sprawdzenie, czy funkcja get_weather_data zwraca poprawne dane dla prawidłowych wartości szerokości i długości geograficznej
        latitude = 50
        longitude = 20
        response = get_weather_data(latitude, longitude)
        self.assertIsInstance(response, list)
        self.assertTrue(len(response) > 0)
        self.assertIsInstance(response[0], dict)
        self.assertIn('date', response[0])
        self.assertIn('weather_code', response[0])
        self.assertIn('temperature_min', response[0])
        self.assertIn('temperature_max', response[0])
        self.assertIn('sunshine_duration', response[0])

    def test_get_weather_data_invalid_values(self):
        # Sprawdzenie, czy funkcja get_weather_data zwraca błąd dla nieprawidłowych wartości szerokości i długości geograficznej
        latitude = 200
        longitude = 200
        response = get_weather_data(latitude, longitude)
        self.assertIsInstance(response, dict)
        self.assertIn('error', response)

    def test_count_energy(self):
        # Sprawdzenie, czy funkcja count_energy poprawnie oblicza energię dla danych pogodowych
        mock_weather_data = [
            {'sunshine_duration': 3600},  # 1 godzina słońca
            {'sunshine_duration': 7200},  # 2 godziny słońca
        ]
        energy = count_energy(mock_weather_data)
        print(len(energy))
        print(energy[0],energy[1])
        self.assertIsInstance(energy, list)
        self.assertEqual(len(energy), 2)
        self.assertAlmostEqual(energy[0], 2.5*0.2*3600)  # oczekiwana wartość: moc * efektywność * 1 godzina
        self.assertAlmostEqual(energy[1], 2.5*0.2*7200)  # oczekiwana wartość: moc * efektywność * 2 godziny

if __name__ == '__main__':
    unittest.main()
