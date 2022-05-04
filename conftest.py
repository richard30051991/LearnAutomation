import pytest
from selenium import webdriver
import datetime
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="Browser type: chrome or firefox or Opera.")
    parser.addoption("--headless", action="store_true", default=False, help="Headless mode if supplied.")
    parser.addoption("--versions", action="store", default="100.0")
    parser.addoption("--url", action="store", default="https://demo.opencart.com/")


@pytest.fixture(scope="function")
def browser(request):
    """Запуск / выбор и закрытие браузера"""
    current_date = datetime.datetime.now()
    browsers = request.config.getoption("--browser")
    print(f"--browser: {browsers}, {current_date}")
    headless = request.config.getoption("--headless")
    version = request.config.getoption("--version")
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
    driver.get(url)
    yield (driver, url)
    driver.quit()


def test_home_page(browser):
    driver, url = browser
    wait = WebDriverWait(driver, 10)
    assert len(wait.until(EC.presence_of_all_elements_located((
        By.CSS_SELECTOR, '[class="product-thumb transition"]')))) == 4
    assert wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'footer p'))).get_property("textContent") \
           == "Powered By OpenCart Your Store © 2022"
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '[class="btn btn-link dropdown-toggle"]'))).click()
    element = wait.until(EC.presence_of_all_elements_located((
        By.CSS_SELECTOR, '[class="currency-select btn btn-link btn-block"]')))
    assert len(element) == 3
    assert element[0].text == "€ Euro"
    assert wait.until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '[name="search"]'))).get_attribute("placeholder") == "Search"
    assert " item(s) - $" in wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '[id="cart-total"]'))).text


def test_catalog(browser):
    driver, url = browser
    url = url + "index.php?route=product/category&path=20"
    wait = WebDriverWait(driver, 10)
    driver.get(url)
    assert wait.until(EC.presence_of_element_located((
        By.CSS_SELECTOR, '[id="input-limit"] option[selected="selected"] '))).text == "15"
    assert wait.until(EC.presence_of_element_located((
        By.CSS_SELECTOR, '[id="input-sort"] option[selected="selected"] '))).text == "Default"
    assert wait.until(EC.presence_of_element_located((
        By.CSS_SELECTOR, '[id="content"] h2'))).text == "Desktops"
    assert wait.until(EC.presence_of_element_located((
        By.XPATH, "//*[@alt='Apple Cinema 30\"']/../../..//span[@class='price-new']"))).text == "$110.00"
    assert wait.until(EC.presence_of_element_located((
        By.XPATH, "//*[@alt='Apple Cinema 30\"']/../../..//span[@class='price-old']"))).text == "$122.00"


def test_card_apple_cinema(browser):
    driver, url = browser
    url = url + "index.php?route=product/product&product_id=42"
    wait = WebDriverWait(driver, 10)
    driver.get(url)
    assert len(wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, '[class="image-additional"]')))) == 5
    assert wait.until(EC.presence_of_element_located((
        By.XPATH, "//*[(text() = '$122.00')]"))).get_attribute("style") == "text-decoration: line-through;"
    assert wait.until(EC.presence_of_element_located((
        By.CSS_SELECTOR, '[id="product-product"] [class="col-sm-4"] h1'))).text == 'Apple Cinema 30"'
    elements = wait.until(EC.presence_of_all_elements_located((
        By.XPATH, "//*[(text() = 'Related Products')]/../div[@class='row']//h4")))
    assert len(elements) == 2
    assert elements[0].text == "iPhone"
    assert elements[1].text == "iMac"


def test_page_authorization(browser):
    driver, url = browser
    wait = WebDriverWait(driver, 10)
    driver.get(url="http://localhost/admin/")
    assert wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '[class="panel-title"]'))).text == \
           "Please enter your login details."
    element = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "[type='submit']")))
    assert element.text == "Login"
    element.click()
    assert wait.until(EC.presence_of_element_located((
        By.CSS_SELECTOR, '[class="alert alert-danger alert-dismissible"]'))).text == \
           'No match for Username and/or Password.\n×'
    assert wait.until(EC.presence_of_element_located((
        By.CSS_SELECTOR, '[name="username"]'))).get_attribute('placeholder') == "Username"
    assert wait.until(EC.presence_of_element_located((
        By.CSS_SELECTOR, '[name="password"]'))).get_attribute('placeholder') == "Password"


def test_page_registration(browser):
    driver, url = browser
    url = url + "index.php?route=account/register"
    wait = WebDriverWait(driver, 10)
    driver.get(url)
    element = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '[value="Continue"]')))
    element.click()
    assert wait.until(EC.presence_of_element_located((
        By.CSS_SELECTOR, '[class="alert alert-danger alert-dismissible"]'))).text == \
           'Warning: You must agree to the Privacy Policy!'
    assert wait.until(EC.presence_of_all_elements_located((
        By.CSS_SELECTOR, '[class="text-danger"]')))[0].text == "First Name must be between 1 and 32 characters!"
    assert wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '[id="content"] h1'))).text == 'Register Account'
    assert wait.until(EC.presence_of_element_located((
        By.CSS_SELECTOR, '[id="content"] p'))).get_property("textContent") == \
           "If you already have an account with us, please login at the login page."
    assert len(wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, '[class="text-danger"]')))) == 5
