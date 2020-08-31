import requests
import json


class help:

    def __init__(self, url):
        self.url = url

    def get(self, route):
        response = requests.get(self.url + route)
        assert response.status_code == 200
        return response

    def post(self, route, data):
        response = requests.post(self.url + route, data=data)
        assert response.status_code == 201 or 200
        return response
