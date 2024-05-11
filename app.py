from flask import Flask, jsonify, request
from get_weather import get_weather_data
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/weather', methods=['GET'])
def weather():
    # Pobranie parametrów latitude i longitude z zapytania GET
    latitude = request.args.get('latitude')
    longitude = request.args.get('longitude')

    # Sprawdzenie poprawności parametrów
    if latitude is None or longitude is None:
        return jsonify({'error': 'Latitude and longitude parameters are required.'}), 400

    try:
        # Konwersja parametrów na float
        latitude = float(latitude)
        longitude = float(longitude)
    except ValueError:
        return jsonify({'error': 'Latitude and longitude must be float values.'}), 400

    # Pobranie danych pogodowych
    response = get_weather_data(latitude, longitude)


    if 'error' in response:
        return jsonify(response), 500
    else:
        return jsonify(response), 200

if __name__ == '__main__':
    app.run(debug=True)
