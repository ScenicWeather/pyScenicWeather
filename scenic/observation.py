""""""
#!/usr/bin/env python
# -*- coding: utf-8 -*-

from temperature import Temperature
from precipitation import Precipitation
from wind import Wind
from reading import Reading

class Observation:
    """"""
    def __init__(self, latitude=None, longitude=None, temperature=None,
                 precipitation=None, humidity=None, wind=None):
        """"""
        if temperature is None:
            self.temperature = Temperature()
        else:
            # TODO type check on input
            self.temperature = temperature # Feels like, unit
        self.humidity = None
        self.summary = None
        self.icon = None
        self.date_time = None
        self.latitude = latitude # TODO input validation
        self.longitude = longitude # TODO input validation
        self.altitude = None
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

    def __str__(self):
        """"""
        # TODO handle empty location / time
        # TODO replace with parameters list
        return "<Observation lat/lon=" + str(self.latitude) + "/" + str(self.longitude) + " @" + str(self.date_time) + ">"

    def __repr__(self):
        """"""
        return '{is_daytime=' + self.is_daytime + ', precip_intensity=' + str(self.precipitation) + ', temperature=' + str(self.temperature) + ', feels_like='+ str(self.temperature.feels_like()) + '}'

if __name__ == "__main__":
    obsv = Observation(wind=Wind())
    print(obsv)

    print(obsv.temperature)
    print(obsv.wind)
    print(obsv.wind.gust)
    print(obsv.wind.direction)
