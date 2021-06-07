""""""
#!/usr/bin/env python
# -*- coding: utf-8 -*-

from scenic import Scenic as weatherBy

NowDawn('your-API-key')  # You MUST provide a valid API key

# Search for current weather in San Francisco (United States)
current_weather = weatherBy.city(city='Toronto', country='CA')  # Defaults to current weather measurement
print(current_weather)

# Weather details
current_weather.temperature     # 9
current_weather.humidity        # 87
current_weather.wind            # 4
current_weather.wind.direction  # 180

print(current_weather.__readings__)

# Get the current weather at lat=43.65N, lon=79.38W (Toronto, Canada)
observation = weatherBy.lat_lon(lat=43.65, lon=-79.38,
                               metric_units=False).forecast(plus_hour=1)
print(observation)