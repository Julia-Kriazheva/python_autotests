import imp
from urllib import response
import requests
import pytest

def test_status_code():
    response = requests.get("https://petstore.swagger.io/v2/pet/120")
    assert response.status_code == 200

def test_piece_of_body():
    response = requests.get("https://petstore.swagger.io/v2/pet/120")
    assert response.json()['name'] == 'Pie'