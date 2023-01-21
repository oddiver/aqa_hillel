import pytest
import requests


def test_one():
    response = requests.get("https://google.com")
    assert response.status_code == 200
    print(response.status_code)

def test_two():
    response = requests.get("https://google.com")
    assert response.status_code == 200
    print(response.text)

def test_tree():
    response = requests.get("https://google.com")
    response.headers
    assert response.status_code == 200
    print(response.status_code)
    print(response.headers)

def test_four():
    response = requests.get("https://google.com")
    assert response.status_code == 200

def test_five():
    response = requests.get("https://google.com")
    assert response.status_code == 404


