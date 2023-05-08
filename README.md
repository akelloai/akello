# akello-gpt
[![PyPI version](https://badge.fury.io/py/akellogpt.svg)](https://badge.fury.io/py/akellogpt)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)


![Alt text](/banner.jpg "akello-gpt")

# Overview
akello-gpt is a service designed to help developers build engaging patient experience to collect screening information. We do this by implementing a deterministic model designed for healthcare applications. 

# Supported screeners
* **Patient Health Questionnaire-9 (PHQ-9)** 
* **General Anxiety Disorder-7 (GAD7)**
* **Kessler Psychological Distress Scale (K10)**
* **Mood Disorder Questionnaire (MDQ)**
* **The Suicide Behaviors Questionnaire-Revised (SBQ-R)**


# Installation and Setup

Install the python package using pip
```bash
pip install akello
```

Setup
```python
from akellog.screening.mental_health import MentalHealth
from akellog.screening.api import ScreeningAPI
api = ScreeningAPI(api_token='<AKELLO_AI_API_TOKEN>')
phq9 = MentalHealth('phq9', api)
```

Add the responses to the screener
```python
# Ask the patient: how often have they been bothered by the following over the past 2 weeks?

# Little interest or pleasure in doing things?
phq9.add_response(0, 'not much anymore') 

# Feeling down, depressed, or hopeless?
phq9.add_response(1, 'yes, most days.')

# Trouble falling or staying asleep, or sleeping too much?
phq9.add_response(2, 'last few nights were rough. not sure why. its been on and off')

# Feeling tired or having little energy?
phq9.add_response(3, 'i take a lot of naps in the afternoon. a few days i have some really good energy') 

# Poor appetite or overeating?
phq9.add_response(4, 'not really. feel like over the last couple of weeks I havent had any issues here')

# Feeling bad about yourself — or that you are a failure or have let yourself or your family down?
phq9.add_response(5, 'no, never')

# Trouble concentrating on things, such as reading the newspaper or watching television?
phq9.add_response(6, 'yes all the time') 

# Moving or speaking so slowly that other people could have noticed? Or so fidgety or restless that you have been moving a lot more than usual?
phq9.add_response(7, 'no never')

# Thoughts that you would be better off dead, or thoughts of hurting yourself in some way?
phq9.add_response(7, 'no never')
```

Score the screener and view the score
```python
phq9.score_screener()
print(phq9.score) 
```

# Future work
We will be expanding akello-gpt to support Workflows

# Contributing to akello-gtp
1. Fork it
2. Create your feature branch (git checkout -b my-new-feature)
3. Commit your changes (git commit -am 'Added some feature')
4. Push to the branch (git push origin my-new-feature)
5. Create new Pull Request
6. Tests are in akellogpt/test. To run the tests: python setup.py test
