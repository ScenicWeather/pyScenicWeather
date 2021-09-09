""""""
#!/usr/bin/env python
# -*- coding: utf-8 -*-

from .scenic_types import Wind, Precipitation, Temperature, Humidity
from .reading import Reading

class Observation:
    """"""
    def __init__(self, latitude=None, longitude=None, altitude=None, date_time=None,
                 measure_unix=None, summary=None, short_summary=None,
                 icon=None, simple_icon=None, temperature=None,
                 precipitation=None, humidity=None, wind=None, downloaded_unix=None,
                 is_daytime=None, cloud_cover=None, uv_index=None, moon_phase=None,
                 alerts=None):
        """"""
        # TODO handle period vs instant data
        if None in (latitude, longitude):
            raise ValueError('Invalid empty location values')

        self.latitude = latitude  # TODO input validation
        self.longitude = longitude  # TODO input validation
        self.altitude = altitude

        if temperature is None:
            self.temperature = Temperature()
        if isinstance(temperature, Temperature):
            self.temperature = temperature  # Feels like, unit
        else:
            self.temperature = Temperature(temperature)  # Feels like, unit
        self.humidity = humidity  # TODO handle None
        self.summary = summary  # TODO handle None
        self.short_summary = short_summary  # TODO handle None
        self.icon = icon  # TODO handle None
        self.simple_icon = simple_icon
        self.date_time = date_time  # TODO handle None
        if precipitation is None:
            self.precipitation = Precipitation()
        elif isinstance(precipitation, Precipitation):
            self.precipitation = precipitation
        else:
            self.precipitation = Precipitation(precipitation)

        if temperature is None:
            self.humidity = Humidity()
        elif isinstance(humidity, Humidity):
            self.humidity = humidity
        else:
            self.humidity = Humidity(humidity, "%")

        if wind is None:
            self.wind = Wind()
        else:
            # TODO type check on input
            self.wind = wind

        self.cloud_cover = cloud_cover  # TODO handle None
        self.moon_phase = moon_phase  # TODO handle None
        self.uv_index = uv_index  # TODO handle None
        self.is_daytime = is_daytime  # TODO handle None
        if alerts is None:
            self.alerts = []
        else:
            self.alerts = alerts
        self.unix = measure_unix  # TODO handle None
        self.downloaded_unix=downloaded_unix  # TODO handle None

    def forecast(self, plus_hour=None):
        # TODO Forecasting not yet implemented
        return []

    def history(self, date_time):
        # TODO Historical data not yet implemented
        return []

    def __str__(self):
        """"""
        # TODO replace with parameters list

        if self.date_time is None and self.latitude is None and self.longitude is None:
            return "<Observation @ unknown location and time>"

        if None in (self.latitude, self.longitude):
            return f"<Observation @ unknown location @ {self.date_time}>"

        if self.date_time is None:
            return f"<Observation lat/lon={self.latitude}/{self.longitude} @ unknown time>"

        return f"<Observation lat/lon={self.latitude}/{self.longitude} @ {self.date_time}>"

    def __readings__(self):
        # TODO replace with parameters list
        return self.__str__()

    def __repr__(self):
        """"""
        # TODO more extensive data
        #print(self.is_daytime)
        #print(type(self.is_daytime))
        return f"{{is_daytime={self.is_daytime}, precip_intensity={self.precipitation.intensity}, temperature={self.temperature.value}, feels_like={self.temperature.feels_like}}}"

if __name__ == "__main__":
    obsv = Observation()
    print(obsv)

    print(obsv.temperature)
    print(obsv.wind.speed)
    print(obsv.wind.gust)
    print(obsv.wind.direction)
