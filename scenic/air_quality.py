""""""
#!/usr/bin/env python
# -*- coding: utf-8 -*-

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
