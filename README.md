# akello-gpt

![Alt text](/banner.jpg "akello-gpt")

# Overview
akello-gpt is a SDK for Akello AI's gpt service designed to help developers receive deterministic responses for healthcare applications.


```python
from akellogpt.screening.mental_health import PHQ9
phq9 = PHQ9('<AKELLO_AI_API_TOKEN>')
for question in phq9.questions:
    question.add_response('ok')
phq9.score_screener()
```

# Screening
With akello-gpt, developers can build better patient screening experiences and allow patients to be screened using conversational methods.

Supported screeners:
* **Patient Health Questionnaire-9 (PHQ-9)** 
* **General Anxiety Disorder-7 (GAD7)**
* **Kessler Psychological Distress Scale (K10)**
* **Mood Disorder Questionnaire (MDQ)**
* **The Suicide Behaviors Questionnaire-Revised (SBQ-R)**

# Using akello-gpt for chat-based screening
TBD

# Installation and Setup
TBD

# Interactive Workflows
TBD

# Handling low confidence responses
TBD

# Future work
TBD

# Contributing to akello-gtp

1. Fork it
2. Create your feature branch (git checkout -b my-new-feature).
3 Commit your changes (git commit -am 'Added some feature')
4. Push to the branch (git push origin my-new-feature)
5. Create new Pull Request
6. Tests are in akellogpt/test. To run the tests: python setup.py test
