# pyScenicWeather

![Windows Build Status](https://github.com/ScenicWeather/pyScenicWeather/workflows/Windows/badge.svg)
![Linux Build Status](https://github.com/ScenicWeather/pyScenicWeather/workflows/Linux/badge.svg)
![MIT License](https://img.shields.io/github/license/ScenicWeather/pyScenicWeather)

## Open Source Python library for interfacing with the Scenic API

## What is it?

PyScenicWeather is a client Python wrapper library for Scenic REST APIs. It allows quick and easy consumption of NowDawn data by Python applications.

## Get started

### API key

As Scenic Weather APIs require a valid API key to allow responses, *pyScenicWeather will not work without one*.
You can get a free API key [on the Scenic website](https://scenicdata.com/register)
Do note that free API subscription plans are subject to requests throttling.

### Example

With a free NowDawn API Key:

```python
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
```

##  Installation

Install with `pip` for your ease:

```shell
$ pip install pyScenicWeather
```

## Documentation

The library software API documentation is available on [Read the Docs](https://api.scenicdata.com/docs).
