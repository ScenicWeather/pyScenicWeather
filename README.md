# pyScenicWeather

![Windows Build Status](https://github.com/ScenicWeather/pyScenicWeather/workflows/Windows/badge.svg)
![Linux Build Status](https://github.com/ScenicWeather/pyScenicWeather/workflows/Linux/badge.svg)
![MIT License](https://img.shields.io/github/license/ScenicWeather/pyScenicWeather)

## Open Source Python library for interfacing with the Scenic API

## What is it?

PyScenicWeather is a client wrapper Python library for interacting with the Scenic REST API and enables easy access to Scenic Weather data by Python applications.

## Get started

### API key

As Scenic Weather APIs require a valid API key to allow responses, *pyScenicWeather will not work without one*.
You can get a free API key [on the Scenic website](https://scenicdata.com/register)
Do note that free API subscription plans are subject to requests throttling.

### Example

With a free NowDawn API Key:

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

For a demo, please see our [quickstart](https://github.com/ScenicWeather/pyScenicWeather/blob/master/example/example.py).

##  Installation

pyScenicWeather is available on Pypi and can be installed with `pip`:

```shell
$ pip install pyScenicWeather
```

## Documentation

The library software API documentation is available on [Read the Docs](https://api.scenicdata.com/docs).

## Learn More

* [Website](https://www.scenicdata.com/)
* [Android App](https://play.google.com/store/apps/details?id=scenic.weather.v1)

## License

Licensed under the [MIT](https://github.com/ScenicWeather/pyScenicWeather/blob/master/LICENSE) License.