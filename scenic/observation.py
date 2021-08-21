""""""
#!/usr/bin/env python
# -*- coding: utf-8 -*-

from temperature import Temperature
from precipitation import Precipitation
from wind import Wind
from reading import Reading

class Observation:
    """"""
    def __init__(self, latitude=None, longitude=None, altitude=None, temperature=None,
                 precipitation=None, humidity=None, wind=None, downloaded_unix=None):
        """"""
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
        self.humidity = None
        self.summary = None
        self.icon = None
        self.date_time = None
        if precipitation is None:
            self.precipitation = Precipitation()
        else:
            # TODO type check on input
            self.precipitation = precipitation

        # TODO type check on input
        self.humidity = Reading(humidity, "%")
        if wind is None:
            self.wind = Wind()
        else:
            # TODO type check on input
            self.wind = wind

        self.cloud_cover = None
        self.moon_phase = None
        self.uv_index = None
        self.is_daytime = None
        self.alerts = []
        self.unix = None
        self.downloaded_unix=None

    def forecast(self, plus_hour=None):
        # TODO Implement
        raise NotImplementedError("Forecasting not yet implemented")

    def __str__(self):
        """"""
        # TODO replace with parameters list

        if self.date_time is None and self.latitude is None and self.longitude is None:
            return "<Observation @ unknown location and time>"

        if None in (self.latitude, self.longitude):
            return f"<Observation @ unknown location @ {self.date_time}>"

        if self.date_time is None:
            return f"<Observation lat/lon={self.latitude}/{self.longitude} @ unkown time>"

        return f"<Observation lat/lon={self.latitude}/{self.longitude} @ {self.date_time}>"

    def __readings__(self):
        # TODO replace with parameters list
        return self.__str__()

    def __repr__(self):
        """"""
        # TODO more extensive data
        return f"{{is_daytime={self.is_daytime}, precip_intensity={self.precipitation}, temperature={self.temperature}, feels_like={self.temperature.feels_like()}}}"

if __name__ == "__main__":
    obsv = Observation(wind=Wind())
    print(obsv)

    print(obsv.temperature)
    print(obsv.wind)
    print(obsv.wind.gust)
    print(obsv.wind.direction)
