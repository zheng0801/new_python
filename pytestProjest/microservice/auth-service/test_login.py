import pytest
import requests

url = 'https://video.fjjieyu.com:8443/login'

def test_login():
    url = 'https://video.fjjieyu.com:8443/auth-service/auth/login'
    json = {'code': "112233",
            'loginType': "1",
            'password': "Joyusing@2024",
            'username': "admin",
            'uuid': "e03ac699ff7c4b7eb4d07318f44aa5db"
            }
    response = requests.post(url, json)
    assert response.status_code == 200