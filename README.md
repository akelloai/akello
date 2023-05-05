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
<TBD>


# Future work
<TBD>
