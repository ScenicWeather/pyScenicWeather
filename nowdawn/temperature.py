""""""
#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Temperature:
    """"""
    
    def __init__(self, temperature=None, unit="C", feels_like=None):
        """"""
        self.value = temperature
        self.unit = unit
        self.feels = feels_like

    def unit(self):
        """"""
        return self.unit

    def feels_like(self):
        """"""
        return self.feels

    def __str__(self):
        """"""
        if self.value is None:
            return "None"

        return self.value

    def __repr__(self):
        """"""
        return str('{value=' + str(self.value) + ', feels=' + str(self.feels) + ', unit=' + str(self.unit) + '}')
