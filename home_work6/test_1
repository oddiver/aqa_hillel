import pytest
import requests


def test_one():
    response = requests.get("https://google.com")
    print(response.status_code)

def test_two():
    response = requests.get("https://google.com")
    print(response.text)

def test_tree():
    response = requests.options("https://google.com")
    print(response.headers['Allow'])

def test_four():
    response = requests.get("https://google.com")
    assert response.status_code == 200

def test_five():
    response = requests.get("https://google.com")
    assert response.status_code == 300
