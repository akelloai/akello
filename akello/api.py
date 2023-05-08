"""
API Helper for Akello AI services
"""

import requests


class API():
    """
    API helper for Akello AI services
    """

    def __init__(self, api_token, api_url):
        headers = {'Authorization': 'Token %s' % api_token}
        self.url = api_url
        self.headers = headers
        self.token = api_token

    def post(self, endpoint, params=None, data=None):
        """
        Generic POST method
        """
        resp = requests.post(f'{self.url}/{endpoint}', json=data, params=params, headers=self.headers, timeout=10)
        return resp

    def put(self, endpoint, params=None, data=None):
        """
        Generic PUT method
        """
        resp = requests.put(f'{self.url}/{endpoint}', json=data, params=params, headers=self.headers, timeout=10)
        return resp
