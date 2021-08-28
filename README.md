# pyScenicWeather

> Open Source client wrapper in Python for interfacing with the Scenic Weather data REST API

![PyPi version: 0.0.2](https://img.shields.io/badge/pypi-v0.0.2-blue)
![Python Versions: 3.7|3.8|3.9](https://img.shields.io/badge/python-3.7%7C3.8%7C3.9-blue)
![Windows Build Status](https://github.com/ScenicWeather/pyScenicWeather/workflows/Windows/badge.svg)
![Linux Build Status](https://github.com/ScenicWeather/pyScenicWeather/workflows/Linux/badge.svg)
![MIT License](https://img.shields.io/github/license/ScenicWeather/pyScenicWeather)
[![Average time to resolve an issue](http://isitmaintained.com/badge/resolution/ScenicWeather/pyScenicWeather.svg)](http://isitmaintained.com/project/ScenicWeather/pyScenicWeather "Average time to resolve an issue")
[![Percentage of issues still open](http://isitmaintained.com/badge/open/ScenicWeather/pyScenicWeather.svg)](http://isitmaintained.com/project/ScenicWeather/pyScenicWeather "Percentage of issues still open")

## Getting started

##  Installation

Python 3.7 or higher is required.

[pyScenicWeather is available on Pypi](https://pypi.org/project/pyScenicWeather/) and can be installed with `pip`:

```shell
# Linux

pip install pyScenicWeather

```

```shell
# Windows

$ pip install pyScenicWeather
```

### Quick Example

With a free Scenic Weather API Key:

```python
from scenic import Scenic

current_weather = None
with Scenic('your-API-key') as weatherBy: # You MUST provide a valid API key
    # Search for current weather in Toronto (Canada)
    # Defaults to current weather measurement
    current_weather = weatherBy.city(city='Toronto', country='CA')  

    if current_weather is not None:
        print(current_weather)

        # Weather details
        print(f"Temperature: {current_weather.temperature}")
        print(f"Humidity: {current_weather.humidity}")
        print(f"Wind Speed: {current_weather.wind.speed}")
        print(f"Wind Direction: {current_weather.wind.direction}")

        print(current_weather.__readings__)

        # Get the current weather at lat=43.65N, lon=79.38W (Toronto, Canada)
        observation = weatherBy.lat_lon(latitude=43.65, longitude=-79.38, metric_units=False).forecast(plus_hour=1)
        print(observation)
```

You can find more examples in our [examples](https://github.com/ScenicWeather/pyScenicWeather/blob/master/example) directory.

### API key

As Scenic Weather APIs require a valid API key to allow responses, *pyScenicWeather will not work without one*.
You can get a free API key [on the Scenic website](https://scenicdata.com/register)
Do note that free API subscription plans are subject to requests throttling.

## Documentation

The library software API documentation is available on [Read the Docs](https://api.scenicdata.com/docs).

## Learn More

* [Website](https://www.scenicdata.com/)
* [Android App](https://play.google.com/store/apps/details?id=scenic.weather.v1)

## License

Licensed under the [MIT](https://github.com/ScenicWeather/pyScenicWeather/blob/master/LICENSE) License.