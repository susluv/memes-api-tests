import allure
import requests

from endpoints.base_endpoint import BaseEndpoint


class AuthorizeEndpoint(BaseEndpoint):
    token = None
    name = None

    @allure.step('Login with credentials')
    def login(self, name):
        self.response = requests.post(f'{self.base_url}/authorize', json={"name": name})
        if self.response.status_code == 200:
            self.json = self.response.json()
            self.token = self.json["token"]
            self.name = name

    @allure.step('Validate token')
    def validate_token(self, token):
        self.response = requests.get(f'{self.base_url}/authorize/{token}')

    @allure.step('Check that login response content is correct')
    def check_login_response_content_is_correct(self):
        assert self.json['user'] == self.name
        assert len(self.token) > 14

    @allure.step('Check that validate token response content is correct')
    def check_validate_token_response_content_is_correct(self):
        assert 'Token is alive' in self.response.text

    @allure.step('Check that user is correct in validate response content')
    def check_name_in_validate_response_content(self, name):
        assert self.response.text.split('Username is ')[1] == name
