#!/usr/bin/env python3

import requests
import json
import time
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# OpenWeatherMap API configuration
api_key = os.getenv("API_KEY")
city = "London"
api_url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

# Function to fetch weather data
def fetch_weather_data():
    response = requests.get(api_url)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error fetching data: {response.status_code}")
        return None

# Main script to fetch and send weather data
# Main script for Splunk
def main():
    weather_data = fetch_weather_data()
    if weather_data:
        # Format the data as JSON and print it to stdout
        output = {
            "city": weather_data["name"],
            "temperature": weather_data["main"]["temp"],
            "humidity": weather_data["main"]["humidity"],
            "wind_speed": weather_data["wind"]["speed"],
            "weather_condition": weather_data["weather"][0]["description"],
            "timestamp": weather_data["dt"]
        }
        # Print the data in JSON format (Splunk will read this as input)
        print(json.dumps(output))

if __name__ == "__main__":
    main()