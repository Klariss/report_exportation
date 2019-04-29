import pytest

from settings import TestConfig
from app import create_app


@pytest.yield_fixture(scope='function')
def app():
    return create_app(TestConfig)


@pytest.yield_fixture(scope='function')
def app():
    return create_app(TestConfig)
