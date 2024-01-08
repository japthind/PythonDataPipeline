from dotenv import load_dotenv
import os
import requests
import json


def fetch_current_weather_data(city):
    # This will fetch the weather data by city
    load_dotenv()
    json_data = requests.get(
        "http://api.openweathermap.org/data/2.5/weather?q="+city+"&appid="+os.environ.get("api-token")).json()
    print("Fetching weather data",json_data)
    return json_data


def create_json(json_data):
    #Save current weather data to a json file.
    print("Writing Json Data to file")
    name = 'data' + str(json_data['dt'])
    print("name",name)
    filename = r"data_loc/%s.json" % name
    print("**** Filename ",os.path.abspath(filename))
    with open(filename, 'w') as f:
        json.dump(json_data, f)
    return filename