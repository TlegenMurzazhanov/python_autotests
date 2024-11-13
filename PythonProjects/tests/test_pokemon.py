import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
HEADER = {'Content-Type': 'application/json', 'trainer_token': '7483e29f4705dfe0d9814bdb287a5908'}
LEVEL = '3'
TRAINER_ID = '8831'

def test_status_code():
    response = requests.get(url = f'{URL}/trainers', params = {'level': LEVEL})
    assert response.status_code == 200

def test_part_of_response():
    response_get = requests.get(url = f'{URL}/trainers', params = {'trainer_id' : TRAINER_ID})
    assert response_get.json()["data"][0]["id"] == '8831'
                            

