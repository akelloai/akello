import requests


class API():
    """
    API helper for Akello AI services
    """

    def __init__(self, token, api_url, headers=None):
        self.url = api_url
        self.headers = headers

    def post(self, data):
        """
        POST method
        """
        resp = requests.post(self.url, json=data, headers=self.headers)
        assert (resp.status_code == 200)
        return resp

    def score_screening_question(self, screening_question):
        """
        Calls akello-gpt to score a question
        :param screening_question:
        :return:
        """
        resp = self.post(screening_question)
        return resp.json()['score']
