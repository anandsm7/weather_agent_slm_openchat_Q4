import requests
import config as cfg

def get_weather(city: str) -> str:
    API_KEY = cfg.WEATHER_KEY
    url = f"http://api.weatherapi.com/v1/current.json?key={API_KEY}&q={city}&aqi=no"
    try:
        r = requests.get(url)
        if r.status_code == 200:
            data = r.json()
            region = data['location']['region']
            country = data['location']['country']
            temp = data['current']['temp_c']
            return f"The weather in {city} located in {region}, {country} with a temperature of {temp}°C."
        else:
            return f"Could not fetch weather for {city}."
    except Exception as e:
        pass


if __name__ == "__main__":
    result = get_weather("kochi")
    print(result)