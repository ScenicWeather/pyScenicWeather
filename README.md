# pyNowDawn

Open Source Python library for interfacing with the NowDawn API

## What is it?

PyNowDawn is a client Python wrapper library for NowDawn web APIs. It allows quick and easy consumption of NowDawn data by Python applications.

## Get started

### API key

As NowDawns APIs need a valid API key to allow responses, *PyNowDawn will not work without one*.
You can get a free API key [on the NowDawn website](https://nowdawn.com/sign_up)
Do note that free API subscription plans are subject to requests throttling.

### Example

With a free NowDawn API Key:

```python
import nowdawn as NowDawn

NowDawn('your-API-key')  # You MUST provide a valid API key

# Search for current weather in London (Great Britain)
current_weather = NowDawn.weather_at(city='London', country='GB').current()
print(current_weather)  # <Weather - reference time=2013-12-18 09:20, status=Clouds>

# Weather details
current_weather.temperature  # 9
current_weather.humidity     # 87
current_weather.wind_speed   # 4

print(current_weather.__readings__)

# Get the current weather observations at lat=22.57W, lon=43.12S (Rio de Janeiro, BR)
observation = NowDawn.weather_at(lat=-22.57, lon=-43.12, metric_units=True)
print(observation)
```

##  Installation

Install with `pip` for your ease:

```shell
$ pip install pyNowDawn
```

## Documentation

The library software API documentation is available on [Read the Docs](https://pynowdawn.readthedocs.io/en/latest/).


## License
[MIT license](https://github.com/Now-dawn/pyNowDawn/blob/master/LICENSE)