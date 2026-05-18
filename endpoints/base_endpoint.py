import allure
import os
from dotenv import load_dotenv

load_dotenv()


class BaseEndpoint:
    base_url = os.getenv('BASE_URL')
    response = None
    json = None

    @allure.step('Check that response status is correct')
    def check_status(self, status=200):
        assert self.response.status_code == status

