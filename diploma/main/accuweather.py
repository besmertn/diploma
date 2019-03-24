import requests

from flask import current_app


class AccuWeatherAPI:

    def __init__(self):
        self.api_key = current_app.config['ACCUWEATHER_API_KEY']
        self.language = current_app.config['ACCUWEATHER_LANGUAGE']
        self.basic_url = current_app.config['ACCUWEATHER_BASIC_URL']

    def get_location_key(self, lat, long):
        params = {
            'apikey': self.api_key,
            'q': '%s,%s' % (lat, long),
            'lanuage': self.language,
            'details': 'false',
            'toplevel': 'false'
        }
        response = requests.get(self.basic_url + "locations/v1/cities/geoposition/search", params=params)
        print(response.json())
        return response.json()['Key']

    def get_1hour_forecast(self, lat, long):
        params = {
            'apikey': self.api_key,
            'lanuage': self.language,
            'details': 'false',
            'metric': 'false'
        }
        response = requests.get(self.basic_url + "forecasts/v1/hourly/1hour/%s" % self.get_location_key(lat, long),
                                params=params)
        print(response.json())
        return response.json()

    def get_region_info(self, region_key):
        params = {
            'apikey': self.api_key,
            'lanuage': self.language,
            'details': 'false'
        }
        response = requests.get(self.basic_url + "locations/v1/" + str(region_key), params=params)
        return response.json()

    def get_region_info(self, lat, long):
        params = {
            'apikey': self.api_key,
            'q': '%s,%s' % (lat, long),
            'lanuage': self.language,
            'details': 'false',
            'toplevel': 'false'
        }
        response = requests.get(self.basic_url + "locations/v1/cities/geoposition/search", params=params)
        print(response.json())
        return response.json()
