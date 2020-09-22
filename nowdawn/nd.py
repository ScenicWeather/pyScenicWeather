""""""
#!/usr/bin/env python
# -*- coding: utf-8 -*-

from requests import get

class NowDawn:
	"""
    Entry point class providing ad-hoc API clients for each NowDawn web API.
    :param api_key: a NowDawn API key
    :type api_key: str
    """

	def __init__(self, api_key):
		""""""
		assert api_key is not None, 'API Key must be set'
        self.api_key = api_key

    def at_lat_lon(self, lat=None, lon=None, metric_units=True):
    	""""""
    	url = "https://api.nowdawn.com/"
    	response = get(url)
    	print("TODO")

    def at_city(self, city, country, metric_units=True):
    	""""""
    	url = "https://api.nowdawn.com/"
    	response = get(url)
    	print("TODO")
