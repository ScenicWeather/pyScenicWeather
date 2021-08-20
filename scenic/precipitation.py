""""""
#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Precipitation:
    """"""

    def __init__(self, intensity=None, unit="C", precip_type=None, probability=0.0):
        """"""
        self.intensity = intensity
        self.unit = unit
        self.precip_type = precip_type
        self.probability = probability

    def unit(self):
        """"""
        return self.unit

    def type(self):
        """"""
        return self.precip_type

    def probability(self):
        """"""
        return self.probability

    def __str__(self):
        """"""
        if self.intensity is None:
            return "None"

        return self.intensity

    def __repr__(self):
        """"""
        return (f"{{intensity='{self.intensity}', "
                f"precip_type='{self.precip_type}', "
                f"probability='{self.probability}', "
                f"precip_unit='{self.unit}'}}")
