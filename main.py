from flask import Flask, jsonify, request
from dotenv import load_dotenv
import os

load_dotenv()  # reads .env into os.environ

import requests
app = Flask(__name__)

WEATHER_API = os.getenv("Weather_API")

@app.route('/')
def home():
    return app.send_static_file("assignment2.html")

@app.route('/api/loc', methods=['POST','GET'])
def client_loc():
    data = request.get_json()
    coordinate = data.split(',')
    print(coordinate)
    file = get_weather(coordinate)
    return jsonify(file)

def get_weather(location):
    lat = location[0]
    lon = location[1]
    url = f"https://api.tomorrow.io/v4/timelines?location={lat},{lon}&fields=temperature&fields=temperatureApparent&fields=temperatureMin&fields=temperatureMax&fields=windSpeed&fields=humidity&fields=uvIndex&fields=weatherCode&fields=pressureSeaLevel&fields=visibility&fields=cloudCover&units=imperial&timesteps=current&timesteps=1d&timezone=America%2FLos_Angeles&apikey={WEATHER_API}"

    headers = {
        "accept": "application/json",
        "Accept-Encoding": "gzip"
    }
    response = requests.get(url, headers=headers)
    return response.json()

@app.route('/api/adv', methods=['POST'])
def client_loc2():
    data = request.get_json()
    coordinate = data.split(',')
    file = get_AdvWeather(coordinate)
    return jsonify(file)

def get_AdvWeather(location):
    lat = location[0]
    lon = location[1]
    url = f"https://api.tomorrow.io/v4/timelines?location={lat},{lon}&fields=temperature&fields=temperatureApparent&fields=temperatureMin&fields=temperatureMax&fields=windSpeed&fields=windDirection&fields=humidity&fields=pressureSeaLevel&fields=uvIndex&fields=weatherCode&fields=precipitationProbability&fields=precipitationType&fields=sunriseTime&fields=sunsetTime&fields=visibility&fields=moonPhase&fields=cloudCover&units=imperial&timesteps=current&timesteps=1d&timesteps=1h&timezone=America%2FLos_Angeles&apikey={WEATHER_API}"

    headers = {
        "accept": "application/json",
        "Accept-Encoding": "gzip"
    }
    response = requests.get(url, headers=headers)
    return response.json()

@app.route('/getWeather', methods=['GET'])
def python_get_weather():
    key = 'S7QOcQOzX6g6Q0CEhXwt0HE3X2BAtiFv'
    lat = 34
    lon = 118.3
    url = f"https://api.tomorrow.io/v4/timelines?location={lat},{lon}&fields=temperature&fields=temperatureApparent&fields=temperatureMin&fields=temperatureMax&fields=windSpeed&fields=windDirection&fields=humidity&fields=pressureSeaLevel&fields=uvIndex&fields=weatherCode&fields=precipitationProbability&fields=precipitationType&fields=sunriseTime&fields=sunsetTime&fields=visibility&fields=moonPhase&fields=cloudCover&units=imperial&timesteps=current&timesteps=1d&timesteps=1h&timezone=America%2FLos_Angeles&apikey={WEATHER_API}"

    headers = {
        "accept": "application/json",
        "Accept-Encoding": "gzip"
    }
    response = requests.get(url, headers=headers)
    return response.json()


if __name__ == '__main__':
    app.run()
