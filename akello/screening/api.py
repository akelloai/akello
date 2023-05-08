"""
API Helper for Akello AI services
"""

import requests
from akello.api import API
from akello.settings import API_URL

class ScreeningAPI:
    """
    API for Screening services
    """

    def __init__(self, api_token, api_url=API_URL):
        self.api = API(api_token=api_token, api_url=api_url)

    def score_screening_question(self, screening_question):
        resp = self.api.post(endpoint='akello-gpt', data=screening_question)
        return resp.json()

