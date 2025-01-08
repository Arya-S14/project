import requests # type: ignore

def get_weather_data(city):
    api_key="8f487b13a2f243e4611a8ce0464f4680"
    url="https://api.openweathermap.org/data/2.5/weather"
    params={
        "q": city,
        "APPID": api_key,
        "units": "metric"
    }
    response= requests.get(url,params=params)
    if(response.status_code==200):
        return response.json()
    else:
        return None
