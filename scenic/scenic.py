""""""
#!/usr/bin/env python
# -*- coding: utf-8 -*-

from datetime import datetime
from traceback import format_exc  # TODO remove once fully stable
from asyncio import run
from json import loads
import urllib3
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
            error_message = ('A non empty Scenic Weather API key must be '
                            'provided. You can register for one at'
                            ' www.scenicdata.com/register')
            exception = ValueError(error_message)
            self.__exit__(ValueError, error_message, exception)
        if api_key == 'your-API-key':
            error_message = ("'your-API-key' isn't a valid Scenic Weather "
                            "API key. You can register for one at"
                            " www.scenicdata.com/register")
            exception = ValueError(error_message)
            self.__exit__(ValueError, error_message, exception)
        self.api_key = api_key

    def __enter__(self):
        try:
            return self
        except ValueError as ex:
            self.__exit__(ex)
            return

    def __exit__(self, type, value, traceback):
        if value is not None:
            print(f"Error: {str(value)}")
        return

    def lat_lon(self, latitude=None, longitude=None, metric_units=True):
        return run(self.__lat_lon(latitude=latitude, longitude=longitude,
                   metric_units=metric_units))

    async def __lat_lon(self, latitude=None, longitude=None, metric_units=True):
        """"""
        headers = {"Accept": "application/json",
                   "Accept": "text/plain",
                   "api_key": self.api_key}
        
        url = f"{BASE_URL}/weather/{latitude}/{longitude}"
        try:
            http = urllib3.PoolManager()
            response = http.request("GET", url, headers)
        except Exception:
            print(format_exc())
            return None
        # TODO error catching - eg. network

        if response.status == 401:
            json_data = loads(response.data)
            raise PermissionError(f"Error: {json_data['error']}")

        if response.status == 200:
            json_data = loads(response.data)
            print("current")
            print(json_data['units'])
            print(json_data['forecasts'])
        else:
            print(f"{response.status} '{response.reason}'")
            print(response.data)
        end_time = datetime.now()

        try:
            return Observation(latitude=latitude, longitude=longitude,
                               downloaded_unix=end_time)  # TODO load parameters
        except ValueError as ex:
            raise ex

    def city(self, city, country, metric_units=True):
        return run(self.__city(city=city, country=country,
                   metric_units=metric_units))

    async def __city(self, city, country, metric_units=True):
        """"""
        url = f"{BASE_URL}/country/{country}/city/{city}"
        headers = {"Accept": "application/json",
                   "Accept": "text/plain",
                   "api_key": self.api_key}

        try:
            http = urllib3.PoolManager()
            response = http.request("GET", url, headers=headers)
        except Exception:
            # TODO more tailored error catching - eg. network
            print(format_exc())
            return None

        if response.status == 401:
            json_data = loads(response.data)
            raise PermissionError(f"Error: {json_data['error']}")

        if response.status == 200:
            json_data = loads(response.data)
            print("current City data")
            print(json_data['units'])
            print(json_data['forecasts'])
        else:
            print(f"{response.status} '{response.reason}'")
            print(response.data)

        try:
            return Observation()  # TODO load parameters
        except ValueError as ex:
            raise ex

    def station(self, station_id, metric_units=True):
        return run(self.__city(station_id=station_id,
                   metric_units=metric_units))

    async def __station(self, station_id, metric_units=True):
        """"""
        url = f"{BASE_URL}/station/{station_id}"
        headers = {"Accept": "application/json",
                   "Accept": "text/plain",
                   "api_key": self.api_key}

        try:
            http = urllib3.PoolManager()
            response = http.request("GET", url, headers=headers)
        except Exception:
            # TODO more tailored error catching - eg. network
            print(format_exc())
            return None

        if response.status == 401:
            json_data = loads(response.data)
            raise PermissionError(f"Error: {json_data['error']}")

        if response.status == 200:
            json_data = loads(response.data)
            print("current City data")
            print(json_data['units'])
            print(json_data['forecasts'])
        else:
            print(f"{response.status} '{response.reason}'")
            print(response.data)

        try:
            return Observation()  # TODO load parameters
        except ValueError as ex:
            raise ex
