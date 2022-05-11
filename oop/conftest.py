import pytest
from selenium import webdriver
import datetime
from pages.page_autorization import authorization_admin

fixture_authorization = authorization_admin


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="Browser type: chrome or firefox or Opera.")
    parser.addoption("--headless", action="store_true", default=False, help="Headless mode if supplied.")
    parser.addoption("--versions", action="store", default="100.0")
    parser.addoption("--url", action="store", default="http://localhost/")


@pytest.fixture(scope="function")
def browser(request):
    """Запуск / выбор и закрытие браузера"""
    current_date = datetime.datetime.now()
    browsers = request.config.getoption("--browser")
    print(f"--browser: {browsers}, {current_date}")
    headless = request.config.getoption("--headless")
    url = request.config.getoption("--url")
    driver, options = None, None
    if browsers == 'chrome':
        options = webdriver.ChromeOptions()
        driver = webdriver.Chrome(options=options)
    elif browsers == 'firefox':
        options = webdriver.FirefoxOptions()
        driver = webdriver.Firefox()
    elif browsers == 'opera':
        options = webdriver.Opera()
        driver = webdriver.Opera()
    else:
        print("unrecognized --browser: {}".format(browsers))
        yield None
    if headless:
        options.add_argument("--headless")
        options.add_argument("--window-size=1920,1080")
        print("Run test in headless mode: --headless")
    driver.maximize_window()
    driver.set_page_load_timeout(15)
    driver.implicitly_wait(6)
    yield driver
    driver.quit()


@pytest.fixture(scope="function")
def url(request):
    url = request.config.getoption("--url")
    yield url



