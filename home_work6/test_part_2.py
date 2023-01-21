import pytest
import requests


def test_six():
    response = requests.get("https://aqa.science/")
    assert response.status_code == 200
    print(response.status_code)
    print(response.text)


def test_seven():
    response = requests.get("https://aqa.science/users")
    assert response.status_code == 401 or 403
    print(response.status_code)
    print(response.text)


def test_eight():
    response = requests.get("https://aqa.science/users", auth=("admin","admin123"))
    assert response.status_code == 200
    print(response.status_code)
    print(response.text)
