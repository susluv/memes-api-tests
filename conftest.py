import pytest
from endpoints.authorize import AuthorizeEndpoint


@pytest.fixture()
def authorize():
    return AuthorizeEndpoint()

