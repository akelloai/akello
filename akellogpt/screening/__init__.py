import yaml
from akellogpt.common.api import API
from yaml import CLoader as Loader
import pathlib
from akellogpt.settings import API_URL

current_path = str(pathlib.Path(__file__).parent.resolve())


class Screener(object):

    def __init__(self, akello_api_token, akello_api_url=API_URL):
        self.score = 0
        self.questions = []
        self.api = API(akello_api_token, akello_api_url)
        self.akello_api_token = akello_api_token

        with open(f'{current_path}/yaml/{self.YAML_FILE}', 'r') as file:
            screener = yaml.load(file, Loader=Loader)
            self.load_question_and_options(screener['questions'])

    def add_question(self, key, question):
        question = ScreeningQuestion(key, question)
        self.questions.append(question)
        return question

    def load_question_and_options(self, questions):
        for question in questions:
            screening_question = ScreeningQuestion(question['order'], question['question'], api=self.api)
            for option in question['options']:
                screening_question.add_option(option['name'], option['value'])
            self.questions.append(screening_question)

    def score_screener(self):
        self.score = sum([question.score_question() for question in self.questions])

    def to_json(self):
        return {
            'score': self.score,
            'questions': [question.to_json() for question in self.questions]
        }

class ScreeningQuestion(object):

    def __init__(self, key, question, api=None):
        self.api = api
        self.score = 0
        self.key = key
        self.question = question
        self.options = []
        self.responses = []

    def add_option(self, name, value):
        option = ScreeningQuestion(name, value)
        self.options.append(option)

    def add_response(self, response):
        self.responses.append(response)

    def score_question(self):
        self.score = self.api.score_screening_question(self.to_json())
        return self.score

    def to_json(self):
        return {
            'score': self.score,
            'key': self.key,
            'question': self.question,
            'options': [option.to_json() for option in self.options],
            'responses': self.responses
        }

class ScreeningOption(object):

    def __init__(self, name, value):
        self.name = name
        self.value = value

    def to_json(self):
        return {
            'name': self.name,
            'value': self.value
        }
