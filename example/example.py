""""""
#!/usr/bin/env python
# -*- coding: utf-8 -*-

try:
    from pyScenicWeather import Scenic
except ModuleNotFoundError as exception:
    print(exception)

def main():
    """"""
    weatherBy = Scenic('your-API-key')  # You MUST provide a valid API key

    # Search for current weather in Toronto (Canada)
    # Defaults to current weather measurement
    current_weather = weatherBy.city(city='Toronto', country='CA')  

    print(current_weather)

    # Weather details
    print(f"Temperature = {current_weather.temperature}")
    print(f"Humidity = {current_weather.humidity}")
    print(f"Wind Speed = {current_weather.wind.speed}")
    print(f"Wind Direction = {current_weather.wind.direction}")

    print(current_weather.__readings__)

    # Get the current weather at lat=43.65N, lon=79.38W (Toronto, Canada)
    observation = weatherBy.lat_lon(latitude=43.65, longitude=-79.38,
                                    metric_units=False).forecast(plus_hour=1)
    print(observation)

if __name__ == '__main__':
    main()
