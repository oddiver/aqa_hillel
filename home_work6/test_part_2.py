import pytest
import requests


def test_six():
    response = requests.get("https://aqa.science/")
    print(response.status_code)
    print(response.text)


def test_seven():
    response = requests.get("https://aqa.science/users")
    print(response.status_code)
    print(response.text)


def test_eight():
    response = requests.get("https://aqa.science/users", auth=("admin","admin123"))
    print(response.status_code)
    print(response.text)
