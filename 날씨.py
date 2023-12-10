import requests

def get_weather(api_key, city):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': city,
        'appid': api_key,
        'units': 'metric'  
    }

    try:
        response = requests.get(base_url, params=params)
        data = response.json()

        if response.status_code == 200:
            weather_description = data['weather'][0]['description']
            temperature = data['main']['temp']
            humidity = data['main']['humidity']
            wind_speed = data['wind']['speed']

            print(f"Weather in {city}: {weather_description}")
            print(f"Temperature: {temperature}°C")
            print(f"Humidity: {humidity}%")
            print(f"Wind Speed: {wind_speed} m/s")
        else:
            print(f"Failed to retrieve weather data. Status code: {response.status_code}")

    except Exception as e:
        print(f"An error occurred: {e}")

# 사용 예제
api_key = 'YOUR_OPENWEATHERMAP_API_KEY'
city_name = 'Seoul'  # 원하는 도시명으로 변경

get_weather(api_key, city_name)
