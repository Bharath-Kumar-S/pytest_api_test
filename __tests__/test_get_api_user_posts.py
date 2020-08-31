import requests
import json
import pytest
from helper import help
with open("./__tests__/testdata.json") as data:
    data = json.load(data)
request_data = data["user_posts"]["GET"]["request"]
response_data = data["user_posts"]["GET"]["response"]

@pytest.mark.backend
class Test_Available_posts_GET_API(object):

    @pytest.fixture(scope='session')
    def response(self):
        client = help(data["user_posts"]["End_point"])
        return client.get(request_data["route"])

    @pytest.fixture(scope='session')
    def response_body(self, response):
        return response.json()

    @pytest.fixture(scope='session')
    def first_user_post(self, response_body):
        return response_body[0]

    def test_get_api_for_posts_check_content_type_equals_json(self, response):
        assert response.headers['Content-Type'] == response_data["content-type"]

    def test_get_api_does_not_return_empty_response(self, response_body):
        assert bool(response_body) != False

    def test_get_api_response_contains_respective_keys(self, first_user_post):
        keys = response_data["keys"]
        for key in keys:
            assert key in first_user_post, key + \
                " key does not exist in the response"

    def test_get_api_response_value_datatypes(self, first_user_post):
        keys = first_user_post.keys()
        k = response_data["type"]
        for key in keys:
            assert k[key] in str(type(first_user_post[key]))

    def test_get_api_posts_count(self, response_body):
        assert len(response_body) == 100

    def test_get_api_first_posts_response(self, first_user_post):
        assert first_user_post == response_data["first_post"]