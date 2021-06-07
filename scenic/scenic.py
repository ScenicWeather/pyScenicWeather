""""""
#!/usr/bin/env python
# -*- coding: utf-8 -*-

from requests import get, post
from json import loads
from observation import Observation

BASE_URL = "http://api.scenicdata.com/"

class Scenic:
    """
    Entry point class providing ad-hoc API clients for each Scenic REST API.
    :param api_key: a Scenic REST API key
    :type api_key: str
    """

    def __init__(self, api_key):
        """"""
        assert api_key is not None, 'API Key must be set'
        self.api_key = api_key

    def lat_lon(self, lat=None, lon=None, metric_units=True):
        """"""

        headers = {'api_key': self.api_key}
        url = BASE_URL + "/weather/" + str(latitude) + "/" + str(longitude)
        response = get(url, headers=headers)
        # TODO error catching - eg. network

        if r.status_code == 200:
            json_data = loads(r.content)
            print("current")
            print(json_data)
        else:
            print(r.status_code, r.reason)
            print(r.content)
        end_time = datetime.now()

        return Observation(latitude=lat, longitude=lon) # TODO load parameters

    def city(self, city, country, metric_units=True):
        """"""
        url = BASE_URL + "/country/" + str(country) + "/city/" + str(city)
        response = get(url)
        print(r.status_code, r.reason)
        print(r.content)

        # TODO error catching - eg. network
        return Observation() # TODO load parameters

    def station(self, station_id):
        """"""
        url = BASE_URL # TODO
        response = get(url)
        # TODO error catching - eg. network
        return Observation() # TODO load parameters
