# akello.ai
[![PyPI version](https://badge.fury.io/py/akellogpt.svg)](https://badge.fury.io/py/akellogpt)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)


![Alt text](/banner.jpg "akello-gpt")

# Run Medication Assisted Treatment (MAT) programs on Akello
Akello is a data platform that is designed to support medication assisted treatments for patient populations. One of its key features is its ability to enable developers to integrate natural language queries for patient populations. Moreover, Akello has the capacity to measure patients and streamline screening procedures, which aids in the efficient triage of patients by clinical teams. Additionally, Akello can facilitate the evaluation of treatment efficacy to aid in the determination of their effectiveness.


### Private Beta
We are currently in private beta. To get request access send a message to **vijay@akello.ai**.


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

# Services

## Screening
The screening service helps developers build engaging patient experience to collect screening information. We do this by implementing a deterministic model designed for healthcare applications.

Currently we support the following screeners (more to come soon):
* **Patient Health Questionnaire-9 (PHQ-9)** 
* **General Anxiety Disorder-7 (GAD7)**
* **Kessler Psychological Distress Scale (K10)**
* **Mood Disorder Questionnaire (MDQ)**
* **The Suicide Behaviors Questionnaire-Revised (SBQ-R)**

## Measurements
Our measurement service is our core data ingestor. Data from sensors, screeners and lab data gets collected under measurements. Withing this service you can define rules to call a webhook back to your system to notify teams if an intervention is needed for a patient.

### Webhooks
TBD

## Transportation
TBD

### Uber Health
![Alt text](/uber.jpeg "uber")


### Automated Scheduler
TBD

## Hardware Sensors 
TBD

### Withings
TBD

![Alt text](/scale.png "withings")


## Labs


| Test Description |
|------------------|
| CBC/5Part Diff   |
| Hemoglobin Alc   |
| Metabolic Panel  |
| Liver Profile (AST, ALT, GGT, ALP)  |
| Lipids (Cholesterol, Trigs, HDL-C, LDL calc), Alc  |
| AST (SGOT)  |
| ALT (SGPT)  |
| Alkaline Phosphatase  |
| GGT  |
| Blood Urea Nitrogen (BUN)  |
| Bilirubin, Total  |
| Protein, Total  |
| Albumin  |
| Uric Acid  |
| Cholesterol, Total  |
| Triglycerides  |
| HDL-C  |
| Blood Creatinine  |


## Analytics
TBD

# Future work
We will be expanding akello-gpt to support Workflows

# Contributing to akello-gtp
1. Fork it
2. Create your feature branch (git checkout -b my-new-feature)
3. Commit your changes (git commit -am 'Added some feature')
4. Push to the branch (git push origin my-new-feature)
5. Create new Pull Request
6. To run the tests: python setup.py test
