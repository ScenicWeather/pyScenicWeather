""""""
#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Observation:
    """"""
    def __init__(self, temperature):
        """"""
        self.temperature = temperature # Feels like, unit
        self.humidity = None
        self.summary = None
        self.icon = None
        self.date_time = None
        self.latitude = None
        self.longitude = None
        self.altitude = None
        self.precip = None # Intensity, probability, type, unit
        self.humidity = None
        self.wind_speed = None
        self.wind_gust = None
        self.wind_direction = None
        self.cloud_cover = None
        self.moon_phase = None
        self.uv_index = None
        self.is_daytime = None
        self.alerts = []

    def __str__(self):
        """"""
        return self.value

    def __repr__(self):
        """"""
        return '{' + is_daytime + '}'
