""""""
#!/usr/bin/env python
# -*- coding: utf-8 -*-

class WeatherAttribute():
    def __init__(self, unit="%"):
        """"""
        self.unit = unit

    def unit(self):
        """"""
        return self.unit

class Humidity(WeatherAttribute):
    """Humidity handling data object"""

    def __init__(self, value=None, unit="%"):
        """"""
        super(self.__class__, self).__init__(unit)
        self.value = value

    def value(self):
        """"""
        return self.value

    def __str__(self):
        """"""
        if self.value is None:
            return "None"

        return f"{self.value}{self.unit}"

    def __repr__(self):
        """"""
        return f"{{Humidity='{self.value}', humidity_unit='{self.unit}'}}"

class Wind(WeatherAttribute):
    """"""
    def __init__(self, speed=None, unit="km/h", gust=None, direction=None):
        """"""
        self.speed = speed
        super(self.__class__, self).__init__(unit)
        self.gust = gust
        self.direction = direction

    def speed(self):
        return self.speed

    def gust(self):
        """"""
        return self.gust

    def direction(self):
        """"""
        # TODO convert angle into string
        return self.direction

    def __str__(self):
        """"""
        if self.speed is None:
            return "None"

        return f"{self.speed} {self.unit}"

    def __repr__(self):
        """"""
        return (f"{{wind_speed='{self.speed}', wind_gust='{self.gust}', "
                f"wind_direction='{self.direction}', wind_unit='{self.unit}'}}")

class Temperature(WeatherAttribute):
    """"""
    def __init__(self, temperature=None, unit="°C", feels_like=None):
        """"""
        super(self.__class__, self).__init__(unit)
        self.value = temperature
        self.feels = feels_like

    def value(self):
        return self.value


    def feels_like(self):
        """"""
        return self.feels

    def __str__(self):
        """"""
        if self.value is None:
            return "None"

        return f"{self.value}{self.unit}"

    def __repr__(self):
        """"""
        return f"{{value='{self.value}', feels='{self.feels}', unit='{self.unit}'}}"

class Precipitation(WeatherAttribute):
    """"""

    def __init__(self, intensity=None, unit="mm", precip_type=None, probability=0.0):
        """"""
        self.intensity = intensity
        super(self.__class__, self).__init__(unit)
        self.precip_type = precip_type
        self.probability = probability

    def intensity(self):
        return self.intensity

    def precip_type(self):
        """"""
        # TODO parse the type values
        return self.precip_type

    def probability(self):
        """"""
        return self.probability

    def __str__(self):
        """"""
        if self.intensity is None:
            return "None"

        return f"{self.intensity} {self.unit}"

    def __repr__(self):
        """"""
        return (f"{{intensity='{self.intensity}', "
                f"precip_type='{self.precip_type}', "
                f"probability='{self.probability}', "
                f"precip_unit='{self.unit}'}}")

class AirQuality:
    """"""
    def __init__(self, aqi=None, pm2_5=None, pm10=None):
        """"""
        self.value = aqi
        self.pm2_5 = pm2_5
        self.pm10 = pm10

    def pm10(self):
        """"""
        return self.pm10

    def pm2_5(self):
        """"""
        return self.pm2_5

    def __str__(self):
        """"""
        if self.value is None:
            return "None"

        return self.value

    def __repr__(self):
        """"""
        return f"{{value='{self.value}', feels='{self.pm2_5}', pm10='{self.pm10}'}}"
