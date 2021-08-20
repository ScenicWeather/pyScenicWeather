""""""
#!/usr/bin/env python
# -*- coding: utf-8 -*-

from datetime import datetime
from traceback import format_exc  # TODO remove once fully stable
from asyncio import run
from json import loads
from requests import get, post
from observation import Observation

BASE_URL = "http://api.scenicdata.com/"

class Scenic:
    """
    Entry point class providing ad-hoc API clients for each Scenic REST API.
    :param api_key: a Scenic REST API key
    :type api_key: str
    """

    def __init__(self, api_key=None):
        """"""
        if api_key is None:
            raise ValueError('A valid Scenic API key must be provided.')
        if api_key == 'your-API-key':
            raise ValueError("'your-API-key' isn't a valid Scenic API key.")

        self.api_key = api_key

    def lat_lon(self, latitude=None, longitude=None, metric_units=True):
        return run(self.__lat_lon(latitude=latitude, longitude=longitude,
                   metric_units=metric_units))

    async def __lat_lon(self, latitude=None, longitude=None, metric_units=True):
        """"""

        headers = {'api_key': self.api_key}
        url = f"{BASE_URL}/weather/{latitude}/{longitude}"
        try:
            response = get(url, headers=headers)
        except Exception:
            print(format_exc())
            return None
        # TODO error catching - eg. network

        if response.status_code == 200:
            json_data = loads(response.content)
            print("current")
            print(json_data['units'])
            print(json_data['forecasts'])
        else:
            print(f"{response.status_code} '{response.reason}'")
            print(response.content)
        end_time = datetime.now()

        return Observation(latitude=latitude, longitude=longitude) # TODO load parameters

    def city(self, city, country, metric_units=True):
        return run(self.__city(city=city, country=country,
                   metric_units=metric_units))

    async def __city(self, city, country, metric_units=True):
        """"""
        url = f"{BASE_URL}/country/{country}/city/{city}"
        headers = {'api_key': self.api_key}
        try:
            response = get(url, headers=headers)
        except Exception:
            # TODO more tailored error catching - eg. network
            print(format_exc())
            return None

        if response.status_code == 200:
            json_data = loads(response.content)
            print("current City data")
            print(json_data['units'])
            print(json_data['forecasts'])
        else:
            print(f"{response.status_code} '{response.reason}'")
            print(response.content)

        return Observation() # TODO load parameters

    def station(self, station_id, metric_units=True):
        return run(self.__city(station_id=station_id,
                   metric_units=metric_units))

    async def __station(self, station_id, metric_units=True):
        """"""
        url = f"{BASE_URL}/station/{station_id}"
        headers = {'api_key': self.api_key}

        try:
            response = get(url, headers=headers)
        except Exception:
            # TODO more tailored error catching - eg. network
            print(format_exc())
            return None

        if response.status_code == 200:
            json_data = loads(response.content)
            print("current City data")
            print(json_data['units'])
            print(json_data['forecasts'])
        else:
            print(f"{response.status_code} '{response.reason}'")
            print(response.content)

        return Observation() # TODO load parameters
