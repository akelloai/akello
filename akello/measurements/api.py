import requests
from akello.api import API
from akello.settings import API_URL

class MeasurementsAPI:
    """
    API for Measurement services
    """

    def __init__(self, api_token, api_url=API_URL):
        self.api = API(api_token=api_token, api_url=api_url)

    def save_measurement_score(self, account_id, user_id, type, data):
        params = {
            'account_id': account_id,
            'user_id': user_id,
            'measurement_type': type,
            'data': data
        }
        resp = self.api.put(endpoint='measurement', params=params)
        return resp