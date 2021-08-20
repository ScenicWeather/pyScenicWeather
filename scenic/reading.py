""""""
#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Reading:
    """"""

    def __init__(self, unit, value=None):
        """"""
        self.value = value
        self.unit = unit

    def unit(self):
        """"""
        return self.unit

    def __str__(self):
        """"""
        return self.value

    def __repr__(self):
        """"""
        return f"{{value='{self.value}', unit='{self.unit}'}}"
