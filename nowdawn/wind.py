""""""
#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Wind:
    """"""
    
    def __init__(self, speed=None, unit="km/h", gust=None, direction=None):
        """"""
        self.speed = speed
        self.unit = unit
        self.gust = gust
        self.direction = direction

    def unit(self):
        """"""
        return self.unit

    def gust(self):
        """"""
        return self.gust

    def direction(self):
        """"""
        return self.direction

    def __str__(self):
        """"""
        if self.speed is None:
            return "None"

        return self.speed

    def __repr__(self):
        """"""
        return str('{wind_speed=' + str(self.speed) + ', wind_gust=' + \
            str(self.gust) + ', wind_direction=' + str(self.direction) + \
            ', wind_unit=' + str(self.unit) + '}')
