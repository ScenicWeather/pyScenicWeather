#!/usr/bin/env python
# -*- coding: utf-8 -*-

class NowDawn:
	 """
    Entry point class providing ad-hoc API clients for each NowDawn web API.
    :param api_key: a NowDawn API key
    :type api_key: str
    """
	def __init__(self, api_key):
		assert api_key is not None, 'API Key must be set'
        self.api_key = api_key

    def weather_at(self, city=None, country=None, lat=None, lon=None, metric_units=True):
    	""""""

