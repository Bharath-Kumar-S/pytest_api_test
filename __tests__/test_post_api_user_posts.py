import requests
import json
import pytest
from helper import help
with open("./__tests__/testdata.json") as data:
    data = json.load(data)
request_data = data["user_posts"]["POST"]["request"]
response_data = data["user_posts"]["GET"]["response"]

@pytest.mark.backend
class Test_user_posts_POST_API(object):

    @pytest.fixture(scope='session')
    def response(self):
        client = help(data["user_posts"]["End_point"])
        return client.post(request_data["route"],request_data["body"])

    @pytest.fixture(scope='session')
    def response_body(self, response):
        return response.json()

    def test_post_api_for_posts_check_content_type_equals_json(self, response):
        assert response.headers['Content-Type'] == response_data["content-type"]

    def test_post_api_does_not_return_empty_response(self, response_body):
        assert bool(response_body) != False

    def test_post_api_response_contains_respective_keys(self, response_body):
        keys = response_data["keys"]
        for key in keys:
            assert key in response_body, key + \
                " key does not exist in the response"