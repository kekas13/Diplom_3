import pytest
from selenium import webdriver
from locators.login_page_locators import LoginPageLocators
from data import Data
from urls import Urls


@pytest.fixture(params=['chrome'])
def driver(request):
    if request.param == 'firefox':
        firefox_options = webdriver.FirefoxOptions()
        firefox_options.add_argument('--width=1920')
        firefox_options.add_argument('--height=1080')
        driver = webdriver.Firefox(options=firefox_options)
    if request.param == 'chrome':
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--window-size=1920,1080')
        driver = webdriver.Chrome(options=chrome_options)
    yield driver
    driver.quit()


@pytest.fixture()
def login(driver):
    driver.get(Urls.LOGIN_PAGE)
    driver.find_element(*LoginPageLocators.INPUT_MAIL).send_keys(Data.EMAIL)
    driver.find_element(*LoginPageLocators.INPUT_PASSWORD).send_keys(Data.PASSWORD)
    driver.find_element(*LoginPageLocators.ENTER_BUTTON).click()
    return driver
