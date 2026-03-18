![CI](https://github.com/Aaronxav99/SDVF/actions/workflows/tests.yml/badge.svg)

# SDVF — Smart Device Validation Framework

Python-based validation framework for Android and wearable devices.
Automates ADB communication, log collection, and device health testing.

## What it does
- Connects to Android devices via ADB
- Runs automated device health tests
- Captures and parses logcat output
- Detects errors and anomalies in logs
- Retry logic for flaky ADB commands
- KPI timing measurement via decorators

## Run it yourself
git clone <your repo url>
cd SDVF
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
pytest tests/ -v

## Tech
Python · pytest · ADB · subprocess · dataclasses · context managers · generators
