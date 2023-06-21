import pytest
from selenium import  webdriver
@pytest.fixture()
def setup():
    driver=webdriver.Firefox()
    return driver
        # if browser=='firefox':
    # elif browser=='chrome':
    #     driver=webdriver.Chrome()
    # elif browser=='safari':
    #     driver=webdriver.Safari()
    # elif browser=='Ie':
    #     driver=webdriver.ie()
