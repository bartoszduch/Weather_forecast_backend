import unittest
from unittest.mock import patch, MagicMock
from app import app, get_weather_data

class TestWeatherApp(unittest.TestCase):
    def test_get_weather_data_valid_input(self):
        # Test dla poprawnych danych wejściowych
        latitude = 40.7128
        longitude = -74.0060
        response = get_weather_data(latitude, longitude)
        self.assertNotIn('error', response)
        self.assertIsInstance(response, list)
        self.assertGreater(len(response), 0)

    def test_get_weather_data_invalid_input(self):
        # Test dla niepoprawnych danych wejściowych
        latitude = 100.0
        longitude = -200.0
        response = get_weather_data(latitude, longitude)
        self.assertIn('error', response)
        self.assertEqual(response['error'], 'Invalid latitude or longitude values. Latitude must be between -90 and 90. Longitude must be between -180 and 180.')

    def test_weather_endpoint_valid_request(self):
        # Test dla poprawnego żądania do endpointu
        tester = app.test_client(self)
        response = tester.get('/weather?latitude=40.7128&longitude=-74.0060')
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertNotIn('error', data)
        self.assertIsInstance(data, list)
        self.assertGreater(len(data), 0)

    def test_weather_endpoint_missing_parameters(self):
        # Test dla braku parametrów w żądaniu do endpointu
        tester = app.test_client(self)
        response = tester.get('/weather')
        self.assertEqual(response.status_code, 400)
        data = response.get_json()
        self.assertIn('error', data)
        self.assertEqual(data['error'], 'Latitude and longitude parameters are required.')

if __name__ == '__main__':
    unittest.main()
