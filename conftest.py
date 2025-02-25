# conftest.py
import pytest

def pytest_addoption(parser):
    parser.addoption("--BASE_URL", action="store", default="https://api.example.com", help="Base API URL")
    parser.addoption("--DB_NAME", action="store", default="test_db", help="Database Name")

@pytest.fixture
def base_url(pytestconfig):
    return pytestconfig.getoption("BASE_URL")

@pytest.fixture
def db_name(pytestconfig):
    return pytestconfig.getoption("DB_NAME")
