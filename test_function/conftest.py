import pytest
import requests


@pytest.fixture
def url(request):
    return request.config.getoption("--url")


@pytest.fixture
def status_code(request):
    return request.config.getoption("--status_code")


def pytest_addoption(parser):
    parser.addoption("--url", default="https://ya.ru", help="Target url")
    parser.addoption("--status_code", default=200, type=int, help="Target status_code")


