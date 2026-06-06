from selenium import webdriver
import pytest

from login_pom import LoginPOM

@pytest.fixture
def credentials():
    return "admin", "admin"

@pytest.fixture(scope="session")
def firefox():
    driver = webdriver.Firefox()
    driver.implicitly_wait(5)
    return driver

def test_login_works(credentials, firefox):
    
    # Arrange
    # instance of pom
    login_page = LoginPOM(firefox)

    # Act
    # unpack credentials
    user, password = credentials
    login_page.login(user, password)

    # Assert
    assert login_page.title == "NEO"