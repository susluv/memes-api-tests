import pytest
from utils.token_generator import fake_token


class TestLogin:
    @pytest.mark.critical
    def test_login_with_valid_name(self, authorize):
        authorize.login("victor")
        authorize.check_status()
        authorize.check_login_response_content_is_correct()

    @pytest.mark.skip("Bug #233")
    @pytest.mark.high
    def test_login_with_empty_name(self, authorize):
        authorize.login("")
        authorize.check_status(400)

    @pytest.mark.low
    def test_login_with_special_characters_name(self, authorize):
        authorize.login("!@#$%^&*()'?.")
        authorize.check_status()


class TestTokenValidation:
    @pytest.mark.high
    def test_valid_token(self, authorize):
        authorize.login("victor")
        authorize.validate_token(authorize.token)
        authorize.check_status()
        authorize.check_validate_token_response_content_is_correct()
        authorize.check_name_in_validate_response_content("victor")

    @pytest.mark.medium
    def test_invalid_token(self, authorize):
        authorize.validate_token(fake_token())
        authorize.check_status(404)

    def test_user_authorized_twice_has_both_tokens_alive_and_different(self, authorize):
        authorize.login("victor")
        first_login_token = authorize.token
        authorize.login("victor")
        second_login_token = authorize.token
        assert first_login_token != second_login_token
        authorize.validate_token(first_login_token)
        authorize.validate_token(second_login_token)



