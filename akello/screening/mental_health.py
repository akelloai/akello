"""
Collection of supported Mental Health screeners
"""
from yaml import CLoader as Loader
from akello.screening.models import Screener
import pathlib
import yaml

CURRENT_PATH = str(pathlib.Path(__file__).parent.resolve())


SCREENER_FILES = {
    'phq9': 'phq9.yaml',
    'gad7': 'gad7.yaml',
}


def load_screener(yaml_file):
    yaml_file = f'{CURRENT_PATH}/../yaml/{yaml_file}'
    with open(yaml_file, 'r', encoding="utf-8") as file:
        screener = yaml.load(file, Loader=Loader)
    return Screener.parse_obj(screener)


class MentalHealth:

    def __init__(self, screener, api):
        self.screener = load_screener(SCREENER_FILES[screener])
        self.api = api

    def add_response(self, question_idx, response):
        self.screener.questions[question_idx].responses.append(response)

    def score_screener(self):
        for idx, question in enumerate(self.screener.questions):
            self.score_question(idx)

    def score_question(self, question_idx):
        resp = self.api.score_screening_question(self.screener.questions[question_idx].dict())
        if 'clarifying_question' in resp and resp['clarifying_question']:
            return resp['clarifying_question']
        self.screener.questions[question_idx]['score'] = question_idx
        self.screener.score += resp['score']