import requests

from flask import current_app


class AccuWeatherAPI:

    def __init__(self):
        self.api_key = current_app.config['ACCUWEATHER_API_KEY']
        self.language = current_app.config['ACCUWEATHER_LANGUAGE']

    def get_location_key(self, lat, long):
        params = {'apikey': self.api_key,
                  'q': '49.993500,36.230385',
                  'lanuage': self.language,
                  'details': 'false',
                  'toplevel': 'false'
                  }
        response = requests.get("http://dataservice.accuweather.com/locations/v1/cities/geoposition/search",
                                params=params)
        print(response.json())
