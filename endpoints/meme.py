import allure
import requests

from endpoints.base_endpoint import BaseEndpoint


class MemeEndpoint(BaseEndpoint):

    @allure.step('Get meme by id')
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